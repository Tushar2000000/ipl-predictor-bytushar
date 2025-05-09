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

import streamlit as st
import base64

import streamlit as st
import base64

# Function to convert image to base64
import streamlit as st
import base64

# Function to convert image to base64
import streamlit as st
import base64

# Function to convert image to base64
def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Replace with your image paths
img_base64_logo = get_base64("images/logoipl.png")  
img_base64_ipl = get_base64("images/ipl.webp")  

# Inject logo at top and IPL image at bottom using HTML/CSS
st.markdown(
    f"""
    <style>
    /* Logo at top center with animation */
    .logo-container {{
        display: flex;
        justify-content: center;
        position: fixed;
        top: 5%;  /* Moved logo further down */
        width: 100%;
        z-index: 1000;
        animation: bounce 3s ease infinite;
        padding-left: 10px;  /* Prevent overflow */
        padding-right: 10px;  /* Prevent overflow */
    }}
    .logo-container img {{
        width: 200px;  /* Slightly bigger size for the logo */
        max-width: 100%;
        height: auto;
    }}
    /* Bounce animation */
    @keyframes bounce {{
        0%, 100% {{
            transform: translateY(0);
        }}
        50% {{
            transform: translateY(-20px);
        }}
    }}
    
    /* IPL Image at bottom center, fixed */
    .ipl-footer {{
        position: fixed;
        bottom: 10px;  /* Moved IPL image slightly up */
        width: 100%;
        display: flex;
        justify-content: center;
        pointer-events: none;
        z-index: 500;
    }}
    .ipl-footer img {{
        width: 350px;  /* Bigger size for IPL image */
        height: auto;
        opacity: 0.9;
    }}
    /* Responsive adjustments */
    @media (max-width: 768px) {{
        .logo-container img {{
            width: 180px;  /* Smaller logo for smaller screens */
        }}
        .ipl-footer img {{
            width: 280px;  /* Slightly smaller IPL image for smaller screens */
        }}
    }}
    </style>

    <!-- Logo at the top -->
    <div class="logo-container">
        <img src="data:image/png;base64,{img_base64_logo}" alt="Logo">
    </div>

    <!-- IPL image at the bottom -->
    <div class="ipl-footer">
        <img src="data:image/webp;base64,{img_base64_ipl}" alt="IPL Image">
    </div>
    """,
    unsafe_allow_html=True
)
