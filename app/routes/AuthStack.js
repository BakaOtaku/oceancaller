import React, { useState, useEffect } from 'react';
import { createStackNavigator } from '@react-navigation/stack';
// import AsyncStorage from '@react-native-community/async-storage';
import { AsyncStorage } from 'react-native';
import LoginScreen from '../screens/LoginScreen';
import OnboardingScreen from '../screens/OnboardingScreen';
import Homepage from '../screens/Homepage';

const Stack = createStackNavigator();

function AuthStack({ setUser }) {

  const [isFirstLaunch, setIsFirstLaunch] = useState(null);
  const [isUserSet, setIsUserSet] = useState(null);
  let routeName;

  useEffect(() => {
    AsyncStorage.getItem('alreadyLaunched').then((value) => {
      if (value == null) {
        AsyncStorage.setItem('alreadyLaunched', 'true');
        setIsFirstLaunch(true);
      } else {
        setIsFirstLaunch(false);
      }
    });
    AsyncStorage.getItem('userSet').then((value) => {
      if (value != null) {
        // AsyncStorage.setItem('userSet', 'true');
        setIsUserSet(true);
        console.log(value);
        // setUser(true);
      }
    });
  }, []);

  if (isFirstLaunch === null) {
    return null;
  } else if (isFirstLaunch == true) {
    routeName = 'Onboarding';
  } else if (isFirstLaunch == false && isUserSet == false) {
    routeName = 'Login';
  } else {
    routeName = 'Home';
  }

  return (
    <Stack.Navigator initialRouteName={routeName}>
      <Stack.Screen
        name="Onboarding"
        component={OnboardingScreen}
        options={{ header: () => null }}
      />
      <Stack.Screen
        name="Login"
        component={LoginScreen}
      />
      <Stack.Screen
        name="Home"
        component={Homepage}
      />
    </Stack.Navigator>
  );
};

export default AuthStack;
