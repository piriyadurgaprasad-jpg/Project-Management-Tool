import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    MYSQL_DATABASE_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_DATABASE_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_DATABASE_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
    MYSQL_DATABASE_DB = os.getenv('MYSQL_DB', 'employee_management')
    MYSQL_DATABASE_PORT = int(os.getenv('MYSQL_PORT', 3306))
    
    # Flask settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    MYSQL_DATABASE_DB = 'employee_management_test'

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
