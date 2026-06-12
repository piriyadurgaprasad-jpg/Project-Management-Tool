from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import MySQLdb.cursors
from datetime import datetime

mysql = MySQL()

class Admin:
    @staticmethod
    def create_admin(mysql, username, email, password):
        """Create a new admin account"""
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        hashed_password = generate_password_hash(password)
        
        try:
            cursor.execute(
                'INSERT INTO admins (username, email, password, created_at) VALUES (%s, %s, %s, %s)',
                (username, email, hashed_password, datetime.now())
            )
            mysql.connection.commit()
            return {'success': True, 'message': 'Admin created successfully'}
        except MySQLdb.Error as e:
            mysql.connection.rollback()
            if 'Duplicate entry' in str(e):
                return {'success': False, 'message': 'Username or email already exists'}
            return {'success': False, 'message': str(e)}
        finally:
            cursor.close()

    @staticmethod
    def authenticate_admin(mysql, username, password):
        """Authenticate admin user by username"""
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        try:
            cursor.execute('SELECT * FROM admins WHERE username = %s', (username,))
            admin = cursor.fetchone()
            
            if admin and check_password_hash(admin['password'], password):
                return {'success': True, 'data': admin}
            else:
                return {'success': False, 'message': 'Invalid username or password'}
        finally:
            cursor.close()

    @staticmethod
    def authenticate_admin_by_email(mysql, email, password):
        """Authenticate admin user by email"""
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        try:
            cursor.execute('SELECT * FROM admins WHERE email = %s', (email,))
            admin = cursor.fetchone()
            
            if admin and check_password_hash(admin['password'], password):
                return {'success': True, 'data': admin}
            else:
                return {'success': False, 'message': 'Invalid email or password'}
        finally:
            cursor.close()

class Employee:
    @staticmethod
    def create_employee(mysql, first_name, last_name, email, password, department, position):
        """Create a new employee account"""
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        hashed_password = generate_password_hash(password)
        
        try:
            cursor.execute(
                '''INSERT INTO employees (first_name, last_name, email, password, department, position, status, created_at) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',
                (first_name, last_name, email, hashed_password, department, position, 'pending', datetime.now())
            )
            mysql.connection.commit()
            return {'success': True, 'message': 'Employee registered successfully. Awaiting admin approval.'}
        except MySQLdb.Error as e:
            mysql.connection.rollback()
            if 'Duplicate entry' in str(e):
                return {'success': False, 'message': 'Email already registered'}
            return {'success': False, 'message': str(e)}
        finally:
            cursor.close()

    @staticmethod
    def authenticate_employee(mysql, email, password):
        """Authenticate employee user"""
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        try:
            cursor.execute('SELECT * FROM employees WHERE email = %s', (email,))
            employee = cursor.fetchone()
            
            if employee and check_password_hash(employee['password'], password):
                if employee['status'] != 'approved':
                    return {'success': False, 'message': 'Your account is pending admin approval'}
                return {'success': True, 'data': employee}
            else:
                return {'success': False, 'message': 'Invalid email or password'}
        finally:
            cursor.close()

    @staticmethod
    def get_employee_by_id(mysql, employee_id):
        """Get employee profile by ID"""
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        try:
            cursor.execute('SELECT * FROM employees WHERE id = %s', (employee_id,))
            employee = cursor.fetchone()
            return employee
        finally:
            cursor.close()

    @staticmethod
    def update_employee_profile(mysql, employee_id, first_name, last_name, department, position, phone, address):
        """Update employee profile"""
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        try:
            cursor.execute(
                '''UPDATE employees SET first_name = %s, last_name = %s, department = %s, position = %s, phone = %s, address = %s 
                   WHERE id = %s''',
                (first_name, last_name, department, position, phone, address, employee_id)
            )
            mysql.connection.commit()
            return {'success': True, 'message': 'Profile updated successfully'}
        except MySQLdb.Error as e:
            mysql.connection.rollback()
            return {'success': False, 'message': str(e)}
        finally:
            cursor.close()

class PasswordReset:
    @staticmethod
    def request_reset(mysql, email):
        """Request password reset"""
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        import secrets
        
        try:
            # Check if email exists
            cursor.execute('SELECT id FROM employees WHERE email = %s', (email,))
            employee = cursor.fetchone()
            
            if not employee:
                # Don't reveal if email exists for security
                return {'success': True, 'message': 'If email exists, reset link will be sent'}
            
            # Generate reset token
            reset_token = secrets.token_urlsafe(32)
            
            cursor.execute(
                'INSERT INTO password_resets (employee_id, token, expires_at) VALUES (%s, %s, DATE_ADD(NOW(), INTERVAL 1 HOUR))',
                (employee['id'], reset_token)
            )
            mysql.connection.commit()
            
            return {'success': True, 'message': 'Reset link sent', 'token': reset_token}
        except MySQLdb.Error as e:
            mysql.connection.rollback()
            return {'success': False, 'message': str(e)}
        finally:
            cursor.close()

    @staticmethod
    def reset_password(mysql, token, new_password):
        """Reset password with valid token"""
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        hashed_password = generate_password_hash(new_password)
        
        try:
            # Verify token
            cursor.execute(
                'SELECT employee_id FROM password_resets WHERE token = %s AND expires_at > NOW()',
                (token,)
            )
            reset_record = cursor.fetchone()
            
            if not reset_record:
                return {'success': False, 'message': 'Invalid or expired reset link'}
            
            # Update password
            employee_id = reset_record['employee_id']
            cursor.execute(
                'UPDATE employees SET password = %s WHERE id = %s',
                (hashed_password, employee_id)
            )
            
            # Delete used token
            cursor.execute('DELETE FROM password_resets WHERE token = %s', (token,))
            mysql.connection.commit()
            
            return {'success': True, 'message': 'Password reset successfully'}
        except MySQLdb.Error as e:
            mysql.connection.rollback()
            return {'success': False, 'message': str(e)}
        finally:
            cursor.close()
