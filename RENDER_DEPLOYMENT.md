# Deploy Education System on Render

This guide will help you deploy your Education System Flask application on Render.

## Prerequisites

1. A GitHub account with your project pushed to a repository
2. A Render account (free tier available)

## Step-by-Step Deployment

### Method 1: Using render.yaml (Recommended)

1. **Ensure your repository is ready**
   - Your project should be pushed to GitHub
   - All files should be committed and pushed

2. **Connect to Render**
   - Go to [render.com](https://render.com) and sign up/login
   - Click "New +" and select "Blueprint"
   - Connect your GitHub account if not already connected
   - Select your repository: `KINGDOMDJANGO/Edusystem`

3. **Deploy**
   - Render will automatically detect the `render.yaml` file
   - Click "Apply" to start the deployment
   - Wait for the build to complete (usually 2-5 minutes)

### Method 2: Manual Setup

1. **Create a new Web Service**
   - Go to [render.com](https://render.com)
   - Click "New +" and select "Web Service"
   - Connect your GitHub repository

2. **Configure the service**
   - **Name**: `education-system`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free

3. **Environment Variables** (Optional)
   - `FLASK_ENV`: `production`
   - `SECRET_KEY`: Generate a secure random key
   - `DATABASE_URL`: Leave empty for SQLite (default)

4. **Deploy**
   - Click "Create Web Service"
   - Wait for the build to complete

## Post-Deployment

1. **Access your application**
   - Your app will be available at: `https://your-app-name.onrender.com`
   - The URL will be shown in your Render dashboard

2. **Initialize the database**
   - Visit: `https://your-app-name.onrender.com/create-sample-data`
   - This will create sample data for testing

3. **Test the application**
   - Navigate through different sections
   - Add teachers, classes, students, and marks
   - Generate reports

## Troubleshooting

### Common Issues

1. **Build fails**
   - Check that all dependencies are in `requirements.txt`
   - Ensure Python version is compatible (3.7+)

2. **Application crashes**
   - Check the logs in Render dashboard
   - Ensure database initialization is working

3. **Database issues**
   - SQLite database is created automatically
   - For production, consider using PostgreSQL

### Logs and Monitoring

- View logs in the Render dashboard
- Monitor performance and errors
- Set up alerts for downtime

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Flask secret key | Auto-generated |
| `FLASK_ENV` | Environment mode | `production` |
| `DATABASE_URL` | Database connection | SQLite |
| `PORT` | Port number | `5000` |

## Security Notes

1. **Secret Key**: Always use a strong secret key in production
2. **HTTPS**: Render provides SSL certificates automatically
3. **Database**: Consider using PostgreSQL for production data
4. **Authentication**: Add user authentication for production use

## Support

- Render Documentation: [docs.render.com](https://docs.render.com)
- Flask Documentation: [flask.palletsprojects.com](https://flask.palletsprojects.com)
- GitHub Issues: Create an issue in your repository

## Next Steps

1. **Add Authentication**: Implement user login/logout
2. **Database Migration**: Set up PostgreSQL for production
3. **Backup Strategy**: Implement regular database backups
4. **Monitoring**: Add application monitoring and alerts
5. **Custom Domain**: Set up a custom domain name 