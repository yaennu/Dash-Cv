# README

* In project folder: docker build -t "cv" .
* Do not miss the dot at the end of the line above...
* For a complete fresh image build: docker build --no-cache -t "cv" .
* docker run --env-file .env -p 8047:8047 cv
    * -d: detach mode
    * -p: publish
    * bind the localhost port to the same port number for your machine
    * --env-file ensures that the .env file is used for credentials
* Export a image (e.g. for NAS transit): docker save --output cv.tar cv
* If you want to run the app locally you have to change the HOST variable in the .env file: 
    * Locally: HOST=127.0.0.1
    * In dockerized status: HOST=0.0.0.0