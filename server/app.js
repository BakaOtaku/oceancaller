const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();
app.use(bodyParser.json());
app.use(cors());


const MongoClient = require('mongodb').MongoClient;
// Connecting to database
let phoneDb = null;
const connectionString = "mongodb+srv://aman:aman@cluster0.btenx.mongodb.net/?retryWrites=true&w=majority";
MongoClient.connect(connectionString, {
  useUnifiedTopology: true
}, (err, client) => {
  if (err) return console.error(err)
  console.log('Connected to Database')
  const db = client.db('off');
  phoneDb = db.collection('phoneList')
})


// Filecoin startup code
const { createPow, powTypes } = require("@textile/powergate-client");
const host = "http://a90b042ed3e9.ngrok.io";
const pow = createPow({ host });
let token = "";
const getToken = async () => {
  console.log("connecting to filecoin")
  try {
    const { user } = await pow.admin.users.create();
    console.log("idhar aa");
    token = user.token;
    pow.setToken(token);
    console.log(JSON.stringify(user));
  } catch (err) {
    console.log(err);
  }
}
// filecoin host setup
app.post('/sethost', async (req, res) => {
  const { url } = req.body;
  host = url;
  getToken();
  res.status(200).send('ok set');
})
// getToken();


// API routes for app
app.post('/fileUpload', async (req, res) => {
  let data = req.body;
  console.log(data);
  // Creating data cid
  buffer = Buffer.from(JSON.stringify(data));
  let cid = await pow.data.stage(buffer);
  console.log(cid);
  res.status(200).send(cid);
});

app.get('/fileDataGet/:cid', async (req, res) => {
  const { cid } = req.params;
  console.log(cid);
  // retrieve data stored in the user by cid
  await pow.storageConfig.apply(cid, { override: true });
  const bytes = await pow.data.get(cid)
  let data = new Buffer.from(bytes).toString();
  res.header("Content-Type", 'application/json');
  res.send(data);
})
app.post('/saveData', async (req, res) => {
  const { phone, did, token, pool } = req.body;
  await phoneDb.insert({ phone: phone, did: did, token: token, pool: pool });
  res.status(200).send('OK');
})

app.get('/fetchThings', async (req, res) => {
  const { phone } = req.body;
  const val = await phoneDb.findOne({ phone: phone });
  console.log(val);
  res.status(200).send(val);
})


// Main Server
app.use('/', (req, res) => {
  console.log('Ocean Protocol node API home');
  res.status(201).send("Main server");
});


app.listen(process.env.PORT || 4000, () => {
  console.log('Listening on 4000');
});