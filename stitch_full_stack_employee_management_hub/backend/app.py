from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
from config import DevelopmentConfig
from models import mysql, Admin, Employee, PasswordReset
import re

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# Initialize MySQL
mysql.init_app(app)

# Enable CORS for frontend integration
CORS(app, resources={r"/api/*": {"origins": "*"}})

# ==================== HELPER FUNCTIONS ====================

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password(password):
    """Validate password strength"""
    return len(password) >= 8

# ==================== ADMIN ROUTES ====================

@app.route('/api/admin/login', methods=['POST'])
def admin_login():
    """Admin login endpoint"""
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'success': False, 'message': 'Missing username or password'}), 400
    
    result = Admin.authenticate_admin_by_email(mysql, data['username'], data['password'])
    
    if result['success']:
        # Don't send password hash to frontend
        admin = result['data']
        return jsonify({
            'success': True,
            'message': 'Login successful',
            'admin': {
                'id': admin['id'],
                'username': admin['username'],
                'email': admin['email']
            }
        }), 200
    else:
        return jsonify(result), 401

@app.route('/api/admin/signup', methods=['POST'])
def admin_signup():
    """Admin signup endpoint"""
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'success': False, 'message': 'Missing required fields'}), 400
    
    if not validate_email(data['email']):
        return jsonify({'success': False, 'message': 'Invalid email format'}), 400
    
    if not validate_password(data['password']):
        return jsonify({'success': False, 'message': 'Password must be at least 8 characters'}), 400
    
    result = Admin.create_admin(mysql, data['username'], data['email'], data['password'])
    
    if result['success']:
        return jsonify(result), 201
    else:
        return jsonify(result), 400

# ==================== EMPLOYEE ROUTES ====================

@app.route('/api/employee/signup', methods=['POST'])
def employee_signup():
    """Employee signup endpoint"""
    data = request.get_json()
    
    required_fields = ['first_name', 'last_name', 'email', 'password', 'department', 'position']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'success': False, 'message': 'Missing required fields'}), 400
    
    if not validate_email(data['email']):
        return jsonify({'success': False, 'message': 'Invalid email format'}), 400
    
    if not validate_password(data['password']):
        return jsonify({'success': False, 'message': 'Password must be at least 8 characters'}), 400
    
    result = Employee.create_employee(
        mysql,
        data['first_name'],
        data['last_name'],
        data['email'],
        data['password'],
        data['department'],
        data['position']
    )
    
    if result['success']:
        return jsonify(result), 201
    else:
        return jsonify(result), 400

@app.route('/api/employee/login', methods=['POST'])
def employee_login():
    """Employee login endpoint"""
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'success': False, 'message': 'Missing email or password'}), 400
    
    result = Employee.authenticate_employee(mysql, data['email'], data['password'])
    
    if result['success']:
        employee = result['data']
        return jsonify({
            'success': True,
            'message': 'Login successful',
            'employee': {
                'id': employee['id'],
                'first_name': employee['first_name'],
                'last_name': employee['last_name'],
                'email': employee['email'],
                'department': employee['department'],
                'position': employee['position']
            }
        }), 200
    else:
        return jsonify(result), 401

@app.route('/api/employee/profile/<int:employee_id>', methods=['GET'])
def get_employee_profile(employee_id):
    """Get employee profile"""
    employee = Employee.get_employee_by_id(mysql, employee_id)
    
    if employee:
        return jsonify({
            'success': True,
            'employee': {
                'id': employee['id'],
                'first_name': employee['first_name'],
                'last_name': employee['last_name'],
                'email': employee['email'],
                'department': employee['department'],
                'position': employee['position'],
                'phone': employee['phone'],
                'address': employee['address'],
                'status': employee['status']
            }
        }), 200
    else:
        return jsonify({'success': False, 'message': 'Employee not found'}), 404

@app.route('/api/employee/profile/<int:employee_id>', methods=['PUT'])
def update_employee_profile(employee_id):
    """Update employee profile"""
    data = request.get_json()
    
    if not data:
        return jsonify({'success': False, 'message': 'No data provided'}), 400
    
    result = Employee.update_employee_profile(
        mysql,
        employee_id,
        data.get('first_name', ''),
        data.get('last_name', ''),
        data.get('department', ''),
        data.get('position', ''),
        data.get('phone', ''),
        data.get('address', '')
    )
    
    if result['success']:
        return jsonify(result), 200
    else:
        return jsonify(result), 400

# ==================== PASSWORD RESET ROUTES ====================

@app.route('/api/password/request-reset', methods=['POST'])
def request_password_reset():
    """Request password reset"""
    data = request.get_json()
    
    if not data or not data.get('email'):
        return jsonify({'success': False, 'message': 'Email is required'}), 400
    
    result = PasswordReset.request_reset(mysql, data['email'])
    return jsonify(result), 200

@app.route('/api/password/reset', methods=['POST'])
def reset_password():
    """Reset password with token"""
    data = request.get_json()
    
    if not data or not data.get('token') or not data.get('new_password'):
        return jsonify({'success': False, 'message': 'Token and new password required'}), 400
    
    if not validate_password(data['new_password']):
        return jsonify({'success': False, 'message': 'Password must be at least 8 characters'}), 400
    
    result = PasswordReset.reset_password(mysql, data['token'], data['new_password'])
    
    if result['success']:
        return jsonify(result), 200
    else:
        return jsonify(result), 400

# ==================== HEALTH CHECK ====================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'success': True, 'message': 'Backend is running'}), 200

# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    return jsonify({'success': False, 'message': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'success': False, 'message': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
