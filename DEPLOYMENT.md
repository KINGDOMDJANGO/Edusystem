# Education System - Deployment Guide

## Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/KINGDOMDJANGO/Edusystem.git
   cd Edusystem
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```
   or
   ```bash
   python run.py
   ```

4. **Access the application**
   Open your browser and go to: `http://127.0.0.1:5000`

## Production Deployment

### Using Gunicorn (Recommended)

1. **Install Gunicorn**
   ```bash
   pip install gunicorn
   ```

2. **Run with Gunicorn**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

### Using Docker

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 5000
   CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
   ```

2. **Build and run**
   ```bash
   docker build -t education-system .
   docker run -p 5000:5000 education-system
   ```

### Environment Variables

You can configure the following environment variables:

- `FLASK_ENV`: Set to `production` for production mode
- `SECRET_KEY`: Set a secure secret key
- `DATABASE_URL`: Set custom database URL

## Database Management

### SQLite (Default)
- Database file: `education_system.db`
- Automatically created on first run
- No additional setup required

### PostgreSQL
1. Install PostgreSQL adapter:
   ```bash
   pip install psycopg2-binary
   ```

2. Update database URL in `app.py`:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/education_db'
   ```

## Security Considerations

1. **Change the secret key** in `app.py`
2. **Use HTTPS** in production
3. **Set up proper authentication** (not included in current version)
4. **Regular database backups**
5. **Keep dependencies updated**

## Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   lsof -ti:5000 | xargs kill -9
   ```

2. **Database errors**
   ```bash
   rm education_system.db
   python app.py
   ```

3. **Permission errors**
   ```bash
   chmod +x run.py
   ```

### Logs
- Check console output for error messages
- Flask debug mode provides detailed error information

## Support

For issues and questions:
- Create an issue on GitHub
- Check the README.md for detailed documentation 