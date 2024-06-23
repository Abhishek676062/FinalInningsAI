import streamlit as st 
import pickle
import pandas as pd
import numpy as np

pipe = pickle.load(open('odi_pipe.pkl','rb'))

teams = [
    'Australia',
    'India',
    'Bangladesh',
    'New Zealand',
    'South Africa',
    'England',
    'Netherlands',
    'Afghanistan',
    'West Indies',
    'Pakistan',
    'Sri Lanka'
]

cities = ['Mirpur',
 'London',
 'Colombo',
 'Sydney',
 'Abu Dhabi',
 'Rangiri',
 'Melbourne',
 'Centurion',
 'Adelaide',
 'Dubai',
 'Birmingham',
 'Perth',
 'Auckland',
 'Cardiff',
 'Pallekele',
 'Wellington',
 'Brisbane',
 'Johannesburg',
 'Hamilton',
 'Cape Town',
 'Durban',
 'Nottingham',
 'Manchester',
 'Sharjah',
 'Port Elizabeth',
 'Chandigarh',
 'Southampton',
 'Leeds',
 'Karachi',
 'Napier',
 'Christchurch',
 'Hambantota',
 'Chester-le-Street',
 'Hobart',
 'Mumbai',
 'Lahore',
 'Mount Maunganui',
 'Nagpur',
 'Fatullah',
 'Chittagong',
 'Delhi',
 'Dunedin',
 'Rajkot',
 'Jaipur',
 'Kolkata',
 'Nelson',
 'Ahmedabad',
 'Hyderabad',
 'Bristol',
 'Canberra',
 'Harare',
 'Kanpur',
 'Bloemfontein']

st.title('ScoreVision AI - future of cricket score forecasts ')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team', teams)
with col2:
    bowling_team = st.selectbox('Select bowling team', teams)

city = st.selectbox('Select city', sorted(cities))   

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current score')
with col4:
    overs = st.number_input('Overs done(works for over>5)') 
with col5:
    wickets = st.number_input('Wickets out')  

last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict score'):
    balls_left = 300 - (overs*6)
    wickets_left = 10 - wickets 
    crr = current_score/overs

    input_df = pd.DataFrame(
        {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [city], 'current_score': [current_score], 'overs': [overs], 'wickets': [wickets], 'last_five': [last_five], 'balls_left': [balls_left], 'wickets_left': [wickets_left], 'crr': [crr]})
    result = pipe.predict(input_df)
    st.header('Predicted score: ' + str(int(result[0])))   
    








