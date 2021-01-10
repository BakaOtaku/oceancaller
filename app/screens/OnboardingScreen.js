import React from 'react';
import { View, Text, Image, TouchableOpacity } from 'react-native';

import Onboarding from 'react-native-onboarding-swiper';

const Dots = ({ selected }) => {
  let backgroundColor = selected ? 'rgba(0, 0, 0, 0.8)' : 'rgba(0, 0, 0, 0.3)';
  return (
    <View
      style={{
        width: 6,
        height: 6,
        marginHorizontal: 3,
        backgroundColor
      }}
    />
  );
}

const Skip = ({ ...props }) => (
  <TouchableOpacity
    style={{ marginHorizontal: 10 }}
    {...props}
  >
    <Text style={{ fontSize: 16 }}>Skip</Text>
  </TouchableOpacity>
);

const Next = ({ ...props }) => (
  <TouchableOpacity
    style={{ marginHorizontal: 10 }}
    {...props}
  >
    <Text style={{ fontSize: 16 }}>Next</Text>
  </TouchableOpacity>
);

const Done = ({ ...props }) => (
  <TouchableOpacity
    style={{ marginHorizontal: 10 }}
    {...props}
  >
    <Text style={{ fontSize: 16 }}>Lets Go</Text>
  </TouchableOpacity>
);

const OnboardingScreen = ({ navigation }) => {
  return (
    <Onboarding
      SkipButtonComponent={Skip}
      NextButtonComponent={Next}
      DoneButtonComponent={Done}
      DotComponent={Dots}
      onSkip={() => navigation.replace("Login")}
      onDone={() => navigation.navigate("Login")}
      pages={[
        {
          backgroundColor: '#a6e4d0',
          image: <Image source={require('../assets/favicon.png')} />,
          title: "The world's first decentralised Caller ID",
          subtitle: 'A New Way To Connect With The World',
        },
        {
          backgroundColor: '#fdeb93',
          image: <Image source={require('../assets/favicon.png')} />,
          title: 'Identify unknown numbers, spam or companies calling before',
          subtitle: 'See the true identity of each incoming call anywhere in the world',
        },
        {
          backgroundColor: '#e9bcbe',
          image: <Image source={require('../assets/favicon.png')} />,
          title: 'Share data to compute',
          subtitle: "Always call the right people",
        },
      ]}
    />
  );
};

export default OnboardingScreen;
