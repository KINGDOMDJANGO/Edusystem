#!/usr/bin/env python3
"""
Education System - Startup Script
Run this script to start the education management system.
"""

import os
import sys

def main():
    print("=" * 50)
    print("Education System - Starting up...")
    print("=" * 50)
    
    # Check if required packages are installed
    try:
        import flask
        import flask_sqlalchemy
        print("✓ Required packages are installed")
    except ImportError as e:
        print(f"✗ Missing required package: {e}")
        print("Please install requirements using: pip install -r requirements.txt")
        sys.exit(1)
    
    # Import and run the Flask app
    try:
        from app import app, db
        
        # Create database tables
        with app.app_context():
            db.create_all()
            print("✓ Database initialized")
        
        print("✓ Application ready!")
        print("\nAccess the application at: http://localhost:5000")
        print("Press Ctrl+C to stop the server")
        print("-" * 50)
        
        # Run the Flask development server
        app.run(debug=True, host='0.0.0.0', port=5000)
        
    except Exception as e:
        print(f"✗ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 