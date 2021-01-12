<p align="center"><img src="https://user-images.githubusercontent.com/42104907/104137450-be83c680-53c2-11eb-8947-faf4c202e983.png" align="center" width="400"></p>
<h1 align="center">OceanCaller</h1>
<h4 align="center">The first decentralised caller Id app</h4>

## Running the Filecoin server

- download the zip release file from https://github.com/textileio/powergate/releases/download/v1.2.6/powergate-docker-v1.2.6.zip
- unzip the folder and run 
```
make localnet
```
or 
- use the follwing commands
> ```
> wget https://github.com/textileio/powergate/releases/download/v1.2.6/powergate-docker-v1.2.6.zip
> unzip powergate-docker-v1.2.6.zip
> ```
In the powergate folder run the following command on cmd/terminal
```
make localnet
```
To expose port for the application use ngrok https://ngrok.com/
> open cmd/terminal
> ```
> ngrok http 6002
> ```
Now set this URL to our backend by calling this API with a post request
https://oceancaller.herokuapp.com/setfilecoin
params: 
{
  filecoinUrl: `NGROK URL FROM ABOVE`
}

## Running backend server

> if on a Windows based machine
> ```
> python -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt
> python web_app.py
> ```

> if on a Linux based machine
> ```
> python3 -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt
> python web_app.py
> ```

## or one can use the api and code deployed on our server
* http://52.172.192.89:5000/

