# README

# Docker
* In project folder: docker build -t "cv" .
* Do not miss the dot at the end of the line above...
* For a complete fresh image build: docker build --no-cache -t "cv" .
* docker run --env-file .env -p 8047:8047 cv
* Export a image (e.g. for NAS transit): docker save --output cv.tar cv
* If you want to run the app locally you have to change the RUN_LOCATION variable.

# Deployment
* In Azure create a new Web App for Containers and go through the steps.
* Choose a template (Deploy a container to an Azure Web App) in GitHub Actions and create a new workflow.
* Follow the steps in the template and ev. replace github.token with secrets.GHCR_TOKEN.