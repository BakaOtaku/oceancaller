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
> https://oceancaller.herokuapp.com/setfilecoin
> ```


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

## or one can use the api and code deployed on our vim 
* http://52.172.192.89:5000/

