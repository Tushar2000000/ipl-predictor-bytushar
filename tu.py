import streamlit as st
import pandas as pd
import pickle

# Title
st.title('🏏 IPL WINNER PREDICTOR')

# Load trained model
pipe = pickle.load(open('pipe5.pkl', 'rb'))

# Team and city options
Teams = [
    'Chennai Super Kings', 'Delhi Capitals', 'Gujarat Titans', 'Kolkata Knight Riders',
    'Lucknow Super Giants', 'Mumbai Indians', 'Punjab Kings', 'Rajasthan Royals',
    'Royal Challengers Bangalore', 'Sunrisers Hyderabad'
]

City = [
    'Mumbai', 'Pune', 'Raipur', 'Hyderabad', 'Visakhapatnam', 'Durban',
    'Chandigarh', 'Chennai', 'Sharjah', 'Dubai', 'Delhi',
    'Johannesburg', 'East London', 'Bengaluru', 'Bangalore', 'Kolkata',
    'Ahmedabad', 'Jaipur', 'Ranchi', 'Abu Dhabi', 'Lucknow',
    'Navi Mumbai', 'Indore', 'Kimberley', 'Centurion', 'Dharamsala',
    'Cape Town', 'Mohali', 'Rajkot', 'Cuttack', 'Guwahati', 'Kanpur',
    'Bloemfontein', 'Nagpur', 'Port Elizabeth'
]

# UI layout
col1, col2 = st.columns(2)
with col1:
    battingteam = st.selectbox('Select the Batting team', sorted(Teams))
with col2:
    bowlingteam = st.selectbox('Select the Bowling team', sorted(Teams))

city = st.selectbox('Select the City', sorted(City))

target = st.number_input('Target')

col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs Completed')
with col5:
    wickets = st.number_input('Wickets Out')

# Prediction logic
if st.button('Predict Probability'):
    leftrun = target - score
    leftball = 120 - (overs * 6)
    wickets_left = 10 - wickets
    crunrate = score / overs if overs != 0 else 0
    rrunrate = (leftrun * 6) / leftball if leftball != 0 else 0

    # Prepare input for the model
    input_df = pd.DataFrame({
        'batting_team': [battingteam],
        'bowling_team': [bowlingteam],
        'city': [city],
        'left run': [leftrun],
        'left ball': [leftball],
        'wickets': [wickets_left],
        'crunrate': [crunrate],
        'reqrunrate': [rrunrate],
        'total_runs_x': [target]
    })

    # Get probabilities
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]

    # Display result
    st.header(f"{battingteam} - 🟢 {round(win * 100)}% chance to win")
    st.header(f"{bowlingteam} - 🔴 {round(loss * 100)}% chance to win")

import streamlit as st
import base64

import base64
import streamlit as st

import base64
import streamlit as st

def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Replace with your actual file paths
img_base64_1 = get_base64("images/logoipl.png")
img_base64_2 = get_base64("images/ipl.webp")


import streamlit as st
import base64

def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Replace with relative paths if running on Streamlit Cloud
img_base64_logo = get_base64("images/logoipl.png")  
img_base64_ipl = get_base64("images/ipl.webp")  

# Inject logo at top and IPL image at bottom using HTML/CSS
import streamlit as st
import base64

def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load and encode logo
img_base64_logo = get_base64("images/logoipl.png")  # Replace with your image path

import streamlit as st
import base64

def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load and encode both images
img_base64_logo = get_base64("images/logoipl.png")       # top logo
img_base64_bottom = get_base64("images/ipl-bottom.png")  # bottom IPL image

# Inject custom CSS
import streamlit as st
import base64

import streamlit as st
import base64

img_base64_1 = get_base64("images/logoipl.png")  
img_base64_2 = get_base64("images/ipl.webp")

# Background styling with two images
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/webp;base64,{img_base64_1}"), url("data:image/webp;base64,{img_base64_2}");
        background-repeat: no-repeat;
        background-position: top left, bottom right;  /* You can customize positioning */
        background-size: 300px 200px, 400px 300px;  /* Customize size of both images */
    }}
    </style>
    """,
    unsafe_allow_html=True
)




