import React, { useState } from 'react';
import {
  View,
  Text,
  Image,
  StyleSheet,
  ScrollView,
  TextInput,
  TouchableOpacity
} from 'react-native';
import { FontAwesome5 } from '@expo/vector-icons';
import { AsyncStorage } from 'react-native';


const LoginScreen = ({ navigation }) => {

  const [wallet, setWallet] = useState();

  const submitHandler = () => {
    console.log(wallet);
    if (wallet != '') {
      AsyncStorage.setItem('userSet', 'true');
      AsyncStorage.setItem('walletKey', wallet);
    }
    navigation.navigate('Home');
  }

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Image
        source={require('../assets/icon.png')}
        style={styles.logo}
      />
      <Text style={styles.text}>OceanCaller</Text>
      <View style={styles.form}>
        <TextInput
          style={styles.input}
          value={wallet}
          keyboardType={'default'}
          placeholder="Import wallet address"
          numberOfLines={1}
          placeholderTextColor="#666"
          autoCorrect={false}
          onChangeText={wal => setWallet(wal)}
        />
        <TouchableOpacity style={styles.icon} onPress={submitHandler}>
          <FontAwesome5 name="wallet" size={24} color="black" />
        </TouchableOpacity>
      </View>
    </ScrollView>
  );
};

export default LoginScreen;

const styles = StyleSheet.create({
  container: {
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
    paddingTop: 50,
    marginTop: 30
  },
  logo: {
    height: 150,
    width: 150,
    resizeMode: 'cover',
  },
  text: {
    fontSize: 28,
    marginTop: 30,
    color: '#051d5f',
  },
  form: {
    marginTop: 50,
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