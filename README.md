<p align="center"><img src="https://user-images.githubusercontent.com/42104907/104137450-be83c680-53c2-11eb-8947-faf4c202e983.png" align="center" width="400"></p>
<h1 align="center">OceanCaller</h1>
<h6 align="center">The first decentralised Caller Id app.</h6>
<h6 align="center">Identify unknown numbers, spam, or companies calling numbers.</h6>

Centralized apps like truecaller help us get the owner of unknown mobile numbers. They do it by collecting contacts of people who have there apps installed, and then the apps serves the information to the one who requires this information

But in this case the data published gets no benifit as well as the collected data gets shared with everyone hence hampering privacy.

[Prdouct Demo Video](https://www.youtube.com/watch?v=A4_vXOVZmGA)

### Our mobile app

Welcome screens

<p float="left">
  <img src="https://user-images.githubusercontent.com/42104907/104363954-eea2a500-553b-11eb-996e-0600feab8eeb.png" width="200" height="433.3">
  <img src="https://user-images.githubusercontent.com/42104907/104364031-0aa64680-553c-11eb-92c7-36e3d807d097.png" width="200" height="433.3">
  <img src="https://user-images.githubusercontent.com/42104907/104364074-198cf900-553c-11eb-81af-08bf6746d619.png" width="200" height="433.3">
  <img src="https://user-images.githubusercontent.com/42104907/104364117-27427e80-553c-11eb-8c05-b909317bfe87.png" width="200" height="433.3">
</p>

User can import his wallet with his private key

<img src="https://user-images.githubusercontent.com/42104907/104364154-36c1c780-553c-11eb-8008-ad712d708ba9.png" width="200" height="433.3">

<br />

App will read all his contacts and create a data set from it to publish on ocean marketplace. If another user buys his dataset then publisher will be rewarded.

<p float="left">
  <img src="https://user-images.githubusercontent.com/42104907/104364192-46411080-553c-11eb-8362-c604f34f53be.png" width="200" height="433.3">
  <img src="https://user-images.githubusercontent.com/42104907/104364227-548f2c80-553c-11eb-9ae7-3f8f756af2b3.png" width="200" height="433.3">
  <img src="https://user-images.githubusercontent.com/42104907/104364261-6375df00-553c-11eb-8291-fb3a35e59af6.png" width="200" height="433.3">
  <img src="https://user-images.githubusercontent.com/42104907/104364313-71c3fb00-553c-11eb-9e42-81d8a31b05a6.png" width="200" height="433.3">
</p>

Now if someone wants to search for unknown spam calls, he can search the phone number in dataset.

<p float="left">
  <img src="https://user-images.githubusercontent.com/42104907/104364376-843e3480-553c-11eb-9974-ba7f4dabe61b.png" width="200" height="433.3">
  <img src="https://user-images.githubusercontent.com/42104907/104364415-9029f680-553c-11eb-9f26-94e005176ad9.png" width="200" height="433.3">
</p>

In future We will also be adding a `Mark as Spam` option for spammers on the mobile app and when the user has got a significantly collected data then he can publish this dataset too for others to buy and improve their experience with spam calls by purchasing these datasets to oceancaller.

### Running the project on your machine

#### For mobile app

Run these commands on your machine

```bash
cd app
yarn install
yarn start
```

Now you can see the app in your ios or android device.

#### API server with filecoin integration

Steps to run locally

```bash
wget https://github.com/textileio/powergate/releases/download/v1.2.6/powergate-docker-v1.2.6.zip
unzip powergate-docker-v1.2.6.zip
cd powergate-docker-v1.2.6
make localnet
```

To expose port for the app use ngrok https://ngrok.com/
In termical `ngrok http 6002`

Now set this URL to our backend by calling this API with a post request
https://oceancaller.herokuapp.com/setfilecoin
with params: `{ filecoinUrl: "NGROK URL FROM ABOVE" }`

#### Running backend ocean integrated server

If on a Windows based machine

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python web_app.py
```

On a Linux based machine

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python web_app.py
```

OR one can use the api and code deployed on our vm server
http://52.172.192.89:5000/
