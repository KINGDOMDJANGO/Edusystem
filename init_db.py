#!/usr/bin/env python3
"""
Database initialization script for Education System
Run this script to create all database tables
"""

from app import app, db

def init_database():
    """Initialize the database with all tables"""
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("Database tables created successfully!")
        print("You can now access the application.")

if __name__ == "__main__":
    init_database() 