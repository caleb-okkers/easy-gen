EasyGen AI – Backend, Containerization & Deployment

This project focused on designing and deploying an AI‑powered backend capable of generating customized text using OpenAI models. Our team built a FastAPI backend, containerized it with Docker, and prepared it for deployment through Kubernetes and GitHub Container Registry (GHCR). We also integrated a CI/CD workflow using GitHub Actions to automate image building and pushing.

✔️ Architecture Overview
FastAPI backend providing endpoints for text generation.
OpenAI API integration for AI responses.
Docker container packaging the entire backend environment.
GitHub Container Registry (GHCR) used for image hosting.
Kubernetes manifests prepared for scalable deployment (deployment + secrets + service).

✔️ Containerization & Deployment Workflow
Created a Dockerfile for backend app.
Built and ran the container locally (docker build, docker run).
Tagged and pushed the production image to GHCR.
Implemented Kubernetes configs:
Deployment
Service
Secret (API key + image pull credentials)
Debugged login, PAT, registry auth, and image pull issues.
Successfully pulled the image on teammate’s machine and tested deployment logic.

✔️ CI/CD Setup (GitHub Actions)
A GitHub Actions workflow was created to:
Automatically build Docker images on every push.
Push the updated image to GHCR using a secure PAT.
Ensure consistent, reproducible deployments across environments.
This automation removes manual build/push steps and enforces a reliable, repeatable process.

✔️ AI Components
The backend uses:
OpenAI text generation models
Custom parameters such as temperature, max tokens, system instructions
A well‑structured API endpoint that the frontend or external apps can call
The AI layer is clean, modular, and easy to integrate with other services.

⭐ What Went Well
Here are the strongest success points to highlight:
1. Full Backend Containerization
The backend app ran flawlessly inside Docker, proving the environment was stable and production-ready.
2. Successful Image Publication to GHCR
You resolved:
PAT permissions
Username mismatch
Registry authentication failures
… and ultimately pushed your image successfully — a key milestone for Kubernetes deployment.
3. Team Collaboration
GHCR access was set up so your teammate could:
Log in
Pull the same image
Deploy it in their Kubernetes cluster
This shows excellent teamwork and DevOps workflow planning.
4. GitHub Actions CI/CD
Automating Docker builds through CI/CD was a major achievement.
It removes human error and supports scalable development.
5. Clear Architectural Design
The system is modular:
Backend
Containerization
Registry
Deployment layer
Each piece is separable and upgradable.


Although not every component reached full production deployment, the project successfully demonstrated containerization, registry-based distribution, CI/CD automation, and AI integration — all of which aligned with the capstone goals.
