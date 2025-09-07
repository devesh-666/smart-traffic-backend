# Smart Traffic Backend

This is a simple Flask backend for the Smart Traffic project.

## Endpoints
- `/traffic` → Returns JSON data about traffic at junctions.

## Deployment on Render
1. Push this code to a GitHub repo.
2. Create a new **Web Service** on [Render](https://render.com/).
3. Select Python environment and set the Start Command as:
   ```
   gunicorn app:app
   ```
4. After deployment, your API will be available at:
   ```
   https://your-app-name.onrender.com/traffic
   ```

