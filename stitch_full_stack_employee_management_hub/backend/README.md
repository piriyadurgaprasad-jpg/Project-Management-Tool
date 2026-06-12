# Employee Management Backend

Python/Flask backend for the Employee Management System using MySQL database.

## Setup Instructions

### 1. Install Python Requirements
```bash
pip install -r requirements.txt
```

### 2. Create MySQL Database
```bash
mysql -u root -p < init_db.sql
```

Or manually in MySQL:
```sql
mysql> source init_db.sql
```

### 3. Configure Environment Variables
Update `.env` file with your MySQL credentials:
```
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=employee_management
MYSQL_PORT=3306
```

### 4. Run the Backend
```bash
python app.py
```

The backend will run on `http://localhost:5000`

## API Endpoints

### Admin Endpoints
- `POST /api/admin/signup` - Create admin account
- `POST /api/admin/login` - Admin login

### Employee Endpoints
- `POST /api/employee/signup` - Employee registration
- `POST /api/employee/login` - Employee login
- `GET /api/employee/profile/<id>` - Get employee profile
- `PUT /api/employee/profile/<id>` - Update employee profile

### Password Reset Endpoints
- `POST /api/password/request-reset` - Request password reset
- `POST /api/password/reset` - Reset password with token

### Health Check
- `GET /api/health` - Check if backend is running

## Frontend Integration

The frontend HTML files should send requests to:
- Base URL: `http://localhost:5000`
- All requests use JSON format
- CORS is enabled for local development

## Database Schema

### Admins Table
- id (INT, PRIMARY KEY)
- username (VARCHAR, UNIQUE)
- email (VARCHAR, UNIQUE)
- password (VARCHAR, hashed)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)

### Employees Table
- id (INT, PRIMARY KEY)
- first_name (VARCHAR)
- last_name (VARCHAR)
- email (VARCHAR, UNIQUE)
- password (VARCHAR, hashed)
- department (VARCHAR)
- position (VARCHAR)
- phone (VARCHAR)
- address (VARCHAR)
- status (ENUM: pending, approved, rejected, inactive)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)

### Password Resets Table
- id (INT, PRIMARY KEY)
- employee_id (INT, FOREIGN KEY)
- token (VARCHAR, UNIQUE)
- expires_at (DATETIME)
- created_at (TIMESTAMP)
