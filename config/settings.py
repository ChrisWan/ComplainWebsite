"""
Configuration settings for the Complaint Management System
"""

import os

class Config:
    """Application configuration"""
    
    # File to store complaints
    COMPLAINTS_FILE = os.path.join('data', 'complaints.json')
    
    # Flask settings
    SECRET_KEY = 'your-secret-key-here'
    DEBUG = True
    
    # Server settings
    HOST = '0.0.0.0'
    PORT = 5000
