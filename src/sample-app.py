#!/usr/bin/env python3
"""
Deliberately vulnerable application for testing security scanners
"""
import sqlite3
import subprocess
import os
import hashlib
from flask import Flask, request

app = Flask(__name__)

# High-severity issues that should trigger Snyk Code
SECRET_KEY = "sk-1234567890abcdef"  # Hardcoded API key
DATABASE_PASSWORD = "admin123"      # Hardcoded password
JWT_SECRET = "my-secret-jwt-key"    # Hardcoded JWT secret

@app.route('/user/<user_id>')
def get_user(user_id):
    """SQL Injection vulnerability"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Direct SQL injection - should definitely trigger
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    cursor.execute(query)
    
    return cursor.fetchall()

@app.route('/execute')
def execute_command():
    """Command Injection vulnerability"""
    cmd = request.args.get('cmd', 'ls')
    
    # Command injection - critical vulnerability
    result = subprocess.run(cmd, shell=True, capture_output=True)
    return result.stdout

@app.route('/file')
def read_file():
    """Path Traversal vulnerability"""
    filename = request.args.get('file', 'default.txt')
    
    # Path traversal - should trigger
    with open('/app/files/' + filename, 'r') as f:
        return f.read()

def weak_crypto_hash(password):
    """Weak cryptography"""
    # MD5 is cryptographically broken
    return hashlib.md5(password.encode()).hexdigest()

def insecure_random():
    """Weak random number generation"""
    import random
    # Using predictable random
    return str(random.random())

# Exposed debug mode
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Should trigger security warning

