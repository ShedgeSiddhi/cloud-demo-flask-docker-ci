<<<<<<< HEAD

# 🚀 Cloud Demo Flask App (Docker + GitHub Actions)

A simple Flask API packaged in Docker with a CI pipeline that builds and pushes the image to Docker Hub.

## Run locally (without Docker)
```bash
pip install -r requirements.txt
python app.py
# http://localhost:5000
```

## Run with Docker
```bash
docker build -t cloud-demo-flask:local .
docker run -p 8080:5000 cloud-demo-flask:local
# http://localhost:8080
```

## Run with docker-compose
```bash
docker compose up --build
# http://localhost:8080
```

## GitHub Actions CI
- Add `DOCKER_USERNAME` and `DOCKER_PASSWORD` as repo secrets
- Update IMAGE_NAME in workflow with your Docker Hub username
- On each push to main, image will be built and pushed to Docker Hub

## API Endpoints
- GET `/` – Welcome page
- GET `/health` – Health check
- GET `/students` – List students
- POST `/students` – Add student (`{"name":"Priya"}`)
=======
# cloud-demo-flask-docker-ci
Devops Project
>>>>>>> 1542be349122b8832efeaa435b532f8b9fb586ff
