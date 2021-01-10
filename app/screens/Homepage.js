import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TextInput,
  TouchableOpacity
} from 'react-native';
import { AntDesign } from '@expo/vector-icons';
import axios from 'axios';

import * as Contacts from 'expo-contacts';


const Homepage = () => {
  const [contacts, setContacts] = React.useState([]);
  const [phone, setPhone] = React.useState('');
  const [isPublished, setIsPublished] = React.useState(false);
  const [isPublishLoading, setIsPublishLoading] = React.useState(false);
  const [isFinding, setIsFinding] = React.useState(false);
  const [resultJson, setResultJson] = React.useState(null);

  const handleSearch = async () => {
    console.log(phone);
    /*  buy
        privatekey, did, token, pool add -> 200 ok
        /download
        privatekey, did -> zip file
        privatekey, did, [numbers] -> json (name - number)
    */
    try {
      setResultJson(null);
      setIsFinding(true);
      const res = await axios.get('http://192.168.0.106:4000/fetchThings', {
        phone: phone
      });
      console.log(res.data);
      const phone_num = res.data.phone;
      const did = res.data.did;
      const token = res.data.token;
      const pool = res.data.pool;
      console.log(phone_num);

      await axios.post('http://52.172.192.89:5000/buy', {
        privatekey: "22421ce8bbd0c2876547a61519001decac4471c1437cd88ec96d74f61d0be0b8",
        did: did,
        token: token,
        pool_address: pool
      })

      const res2 = await axios.post('http://52.172.192.89:5000/download', {
        privatekey: "22421ce8bbd0c2876547a61519001decac4471c1437cd88ec96d74f61d0be0b8",
        did: did,
        numbers: [phone]
      })

      const json_obj = res2.data;
      console.log(json_obj);
      setIsFinding(false);
      
    } catch (err) {
      console.log(err)
    }
  }

  const handlePublish = async () => {
    console.log("Publish");
    setIsPublishLoading(true);
    const data = {
      "contacts": {
        [contacts[2].firstName + ' ' + contacts[2].lastName]: contacts[2].phoneNumbers[0].number,
        [contacts[3].firstName + ' ' + contacts[3].lastName]: contacts[3].phoneNumbers[0].number,
        [contacts[4].firstName + ' ' + contacts[4].lastName]: contacts[4].phoneNumbers[0].number,
        [contacts[5].firstName + ' ' + contacts[5].lastName]: contacts[5].phoneNumbers[0].number,
        [contacts[7].firstName + ' ' + contacts[7].lastName]: contacts[7].phoneNumbers[0].number,
      }
    }
    console.log(data);

    try {
      // upload to filecoin and get cid
      const res1 = await axios.post('http://192.168.0.106:4000/fileUpload', data);
      const { cid } = res1.data;
      console.log(cid);

      // get datatoken
      const res2 = await axios.post('http://52.172.192.89:5000/datatoken', {
        privatekey: "22421ce8bbd0c2876547a61519001decac4471c1437cd88ec96d74f61d0be0b8"
      })
      const { token } = res2.data;
      console.log(token);

      await new Promise(resolve => setTimeout(resolve, 20000));

      console.log("here")
      // publish data
      const res3 = await axios.post('http://52.172.192.89:5000/publish', {
        privatekey: "22421ce8bbd0c2876547a61519001decac4471c1437cd88ec96d74f61d0be0b8",
        token: token,
        url: "http://f9e4f42dbb40.ngrok.io/fileDataGet/QmZQxq4p6Zh4wpEZDKX5eumZbgNSxo8TBFEHfpi2FFg8aZ"
      });
      const { did, dataset_name } = res3.data;
      console.log(did, dataset_name);

      await new Promise(resolve => setTimeout(resolve, 20000));

      // pool published data 
      const res4 = await axios.post('http://52.172.192.89:5000/pool', {
        privatekey: "22421ce8bbd0c2876547a61519001decac4471c1437cd88ec96d74f61d0be0b8",
        token: token
      })
      const { pool_address } = res4.data;
      console.log(pool_address);


      // save did, token and pool address
      const res = axios.post('http://192.168.0.106:4000/saveData', {
        "token": "0x3Bd38C3D5472525f02e1D8e6f77922F97888b09c",
        "phone": contacts[2].phoneNumbers[0].number,
        "did": "did:op:3Bd38C3D5472525f02e1D8e6f77922F97888b09c",
        "pool": "0x9048a01bC5652A0cCf1A1dD43c0006F9a1DaB61a"
      });

      setIsPublishLoading(false);
      setIsPublished(true);
    } catch (err) {
      console.log(err);
    }

  }

  React.useEffect(() => {
    (async () => {
      const { status } = await Contacts.requestPermissionsAsync();
      if (status === 'granted') {
        const { data } = await Contacts.getContactsAsync({
          fields: [Contacts.Fields.PhoneNumbers],
        });
        if (data.length > 0) {
          setContacts(data);
        }
      }
    })();
  }, []);

  return (
    <ScrollView contentContainerStyle={styles.container}>

      <Text style={styles.publishText}>Publish your contacts</Text>

      {
        isPublishLoading ?
          <Text style={styles.loadingText}>⌛ Please wait... ⌛</Text>
          : null
      }
      {
        isPublished ?
          <Text style={styles.pushedText}>🎉 Data pushed</Text>
          : <TouchableOpacity style={styles.buttonContainer} onPress={handlePublish}>
            <Text style={styles.buttonText}>Publish</Text>
          </TouchableOpacity>
      }
      {
        isPublished && <Text style={styles.jsontext}>dataset_name: mobile1497797240801</Text>
      }


      <Text style={styles.text}>Find contacts on ocean protocol</Text>
      <View style={styles.form}>
        <TextInput
          style={styles.input}
          keyboardType={'numeric'}
          placeholder="Enter phone number"
          autoCorrect={false}
          value={phone}
          onChangeText={phone => setPhone(phone)}
        />
        <TouchableOpacity style={styles.icon} onPress={handleSearch}>
          <AntDesign name="search1" size={24} color="black" />
        </TouchableOpacity>
      </View>

      {
        isFinding ?
          <Text style={styles.loadingText}>⌛ Finding... ⌛</Text>
          : null
      }
      {
        resultJson &&
        <Text style={styles.pushedText}>🎉 Data Fetched successfully</Text>
      }
      {
        resultJson &&
        <Text style={styles.jsontext}>{resultJson}</Text>
      }
    </ScrollView>
  );
}

export default Homepage;


const styles = StyleSheet.create({
  container: {
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
    paddingTop: 50,
    marginTop: 30
  },
  centerView: {
    textAlign: 'center'
  },
  logo: {
    height: 150,
    width: 150,
    resizeMode: 'cover',
  },
  loadingText: {
    fontSize: 18,
    marginTop: 20,
    marginBottom: 20,
    color: '#ff8e71',
  },
  jsontext: {
    fontSize: 12,
    marginTop: 20,
    color: '#051d5f',
  },
  pushedText: {
    fontSize: 20,
    marginTop: 20,
    color: '#16c79a',
  },
  publishText: {
    fontSize: 26,
    marginTop: 30,
    color: '#051d5f',
  },
  buttonContainer: {
    marginTop: 10,
    width: '40%',
    height: 40,
    backgroundColor: '#2e64e5',
    padding: 10,
    alignItems: 'center',
    justifyContent: 'center',
    borderRadius: 50,
  },
  buttonText: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#ffffff',
  },
  text: {
    fontSize: 26,
    marginTop: 100,
    color: '#051d5f',
  },
  form: {
    marginTop: 20,
    flexDirection: 'row',
    borderRadius: 50,
    overflow: 'hidden',
    alignItems: 'center',
    backgroundColor: 'rgba(234, 234, 234, 0.9)',
    marginHorizontal: 30
  },
  input: {
    flexGrow: 1,
    marginHorizontal: 30
  },
  icon: {
    width: 50,
    height: 50,
    backgroundColor: 'rgba(5, 29, 95, 0.1)',
    justifyContent: 'center',
    alignItems: 'center',
    marginHorizontal: 0,
    borderRadius: 50,
  },
});
