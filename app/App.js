import React from 'react';
import { NavigationContainer } from '@react-navigation/native'
import { createStackNavigator } from '@react-navigation/stack'
import AppStack from './routes/AppStack';
import AuthStack from './routes/AuthStack';

export default function App() {
  const [user, setUser] = React.useState(false);

  return (
    <NavigationContainer>
      {user ? <AppStack /> : <AuthStack setUser={setUser} />}
    </NavigationContainer>
  );
}

