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
* Follow the steps in the template
    * Eventually replace github.token with secrets.GHCR_TOKEN
    * Add all the necessary environment variables from the .env file to the Azure Web App (Environment variables > New application setting).
    * Replace ${{ env.REPO }}:${{ github.sha }} with ${{ env.REPO }}:latest in the GitHub Actions workflow file.

# IP-Address
* To get the IP address of my local machine: Test-NetConnection -ComputerName yscv.database.windows.net -Port 1433
* Add SourceAddress to firewall rule on Azure.

# TODO
* GE KKG link
* Catchy phrase about the website
* legend von radar plot nach unten
* skills radio buttons nach rechts
* foto von sidebar nach unten