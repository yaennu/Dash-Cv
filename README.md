# README

* In project folder: docker build -t "ge-dashboard" .
* Do not miss the dot at the end of the line above...
* For a complete fresh image build: docker build --no-cache -t "ge-dashboard" .
* docker run -d -p 8050:8050 ge-dashboard
    * -d: detach mode
    * -p: publish
    * bind the localhost port to the same port number for your machine
* export a image (e.g. for NAS transit): docker save --output ge-dashboard.tar ge-dashboard
* If you want to run the app locally you have to change the HOST variable in the .env file: 
    * Locally: HOST=127.0.0.1
    * In dockerized status: HOST=0.0.0.0