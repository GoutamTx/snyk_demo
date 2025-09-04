# Sample application with intentional security issues for testing
import sqlite3
import hashlib
import os

# Weak cryptography - should trigger AI scanner
def weak_hash(data):
    return hashlib.md5(data.encode()).hexdigest()  # Weak hash algorithm

# SQL Injection vulnerability
def get_user_data(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Vulnerable SQL query - should trigger scanner
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    
    return cursor.fetchall()

# Hardcoded secret - should trigger scanner
API_KEY = "sk-1234567890abcdef"  # Hardcoded API key

# Insecure random number generation
def generate_token():
    import random
    return str(random.random())  # Weak random generation

if __name__ == "__main__":
    print("Sample app with security issues for testing")

# Test change for security scan
