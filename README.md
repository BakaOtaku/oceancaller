## Running the filecoin server
> open cmd or terminal depending on the operating system
> ```
> wget https://github.com/textileio/powergate/releases/download/v1.2.6/powergate-docker-v1.2.6.zip
> unzip powergate-docker-v1.2.6.zip
> ```
In the powergate folder run 
```
make localnet
```
To expose port for the application use ngrok
> open cmd/terminal
> ```
> ngrok http 6001
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
```

