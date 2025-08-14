# Cloud Deployment Guide

This guide explains how to deploy the Assistant Magistère application to various cloud platforms.

## Environment Variables Required

Before deploying, ensure you have these environment variables configured:

### Required Variables
- `OPENAI_API_KEY` - Your OpenAI API key (required)
- `FLASK_APP` - Set to `app.py`
- `FLASK_ENV` - Set to `production`

### Optional Variables (with defaults)
- `OPENAI_MODEL` - Default: `gpt-4o-mini`
- `OPENAI_MAX_TOKENS` - Default: `1000`
- `OPENAI_TEMPERATURE` - Default: `0.7`

## Render.com Deployment

### 1. Connect Your Repository
1. Go to [Render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub/GitLab repository
4. Select the repository containing this project

### 2. Configure the Service
- **Name**: `assistant-magistere` (or your preferred name)
- **Environment**: `Docker`
- **Region**: Choose closest to your users
- **Branch**: `main` (or your default branch)
- **Root Directory**: `app_form` (if your code is in a subdirectory)

### 3. Set Environment Variables
In the Environment section, add:

```env
OPENAI_API_KEY=sk-your-actual-openai-api-key-here
OPENAI_MODEL=gpt-4o-mini
OPENAI_MAX_TOKENS=1000
OPENAI_TEMPERATURE=0.7
FLASK_APP=app.py
FLASK_ENV=production
```

### 4. Build Configuration
- **Build Command**: Leave empty (Docker will handle this)
- **Start Command**: Leave empty (Dockerfile CMD will handle this)

### 5. Deploy
Click "Create Web Service" and wait for the build to complete.

## Railway.app Deployment

### 1. Connect Repository
1. Go to [Railway.app](https://railway.app)
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository

### 2. Configure Environment Variables
In the Variables tab, add the same environment variables as above.

### 3. Deploy
Railway will automatically detect the Dockerfile and deploy.

## Heroku Deployment

### 1. Create Heroku App
```bash
heroku create your-app-name
```

### 2. Set Environment Variables
```bash
heroku config:set OPENAI_API_KEY=sk-your-actual-openai-api-key-here
heroku config:set OPENAI_MODEL=gpt-4o-mini
heroku config:set OPENAI_MAX_TOKENS=1000
heroku config:set OPENAI_TEMPERATURE=0.7
heroku config:set FLASK_APP=app.py
heroku config:set FLASK_ENV=production
```

### 3. Deploy
```bash
git push heroku main
```

## DigitalOcean App Platform

### 1. Create App
1. Go to DigitalOcean App Platform
2. Click "Create App" → "Source: GitHub"
3. Select your repository

### 2. Configure Environment
- **Source Directory**: `app_form`
- **Environment**: `Docker`

### 3. Set Environment Variables
Add the required environment variables in the App Spec.

### 4. Deploy
Click "Create Resources" to deploy.

## Troubleshooting

### Common Issues

#### 1. "OPENAI_API_KEY is missing"
**Solution**: Ensure the environment variable is set in your cloud platform's dashboard.

#### 2. Build fails
**Solution**: Check that your Dockerfile is in the correct directory and all files are committed.

#### 3. Application crashes on startup
**Solution**: Check the logs for specific error messages and ensure all required environment variables are set.

### Health Check
The application includes a health check endpoint at `/`. You can test it with:
```bash
curl https://your-app-url.com/
```

### Logs
Check your cloud platform's logs section for detailed error messages and debugging information.

## Security Notes

1. **Never commit your `.env` file** to version control
2. **Use environment variables** for all sensitive configuration
3. **Rotate API keys** regularly
4. **Monitor usage** to avoid unexpected costs

## Cost Optimization

1. **Use appropriate instance sizes** for your traffic
2. **Monitor OpenAI API usage** and set up alerts
3. **Consider using a CDN** for static assets
4. **Enable auto-scaling** if your platform supports it
