{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww29200\viewh18460\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import joblib\
import pandas as pd\
\
model = joblib.load('energy_model.pkl')\
\
st.title("\uc0\u9889  WattWise \'97 Household Energy Usage Predictor")\
st.write("Predict tomorrow's household power usage based on recent consumption patterns.")\
\
st.header("Enter Recent Usage Data")\
\
lag_1 = st.number_input("Yesterday's usage (kW)", min_value=0.0, max_value=10.0, value=1.2)\
lag_2 = st.number_input("2 days ago usage (kW)", min_value=0.0, max_value=10.0, value=1.2)\
lag_3 = st.number_input("3 days ago usage (kW)", min_value=0.0, max_value=10.0, value=1.2)\
lag_7 = st.number_input("Same day last week (kW)", min_value=0.0, max_value=10.0, value=1.2)\
rolling_mean_7 = st.number_input("Average usage over past 7 days (kW)", min_value=0.0, max_value=10.0, value=1.2)\
\
month = st.selectbox("Month", list(range(1,13)), index=0)\
day_of_week = st.selectbox("Day of week (0=Mon, 6=Sun)", list(range(0,7)), index=0)\
is_weekend = 1 if day_of_week in [5,6] else 0\
year = st.number_input("Year", min_value=2020, max_value=2030, value=2026)\
\
if st.button("Predict Usage"):\
    input_data = pd.DataFrame([[month, day_of_week, is_weekend, year, \
                                  lag_1, lag_2, lag_3, lag_7, rolling_mean_7]],\
                                columns=['month', 'day_of_week', 'is_weekend', 'year',\
                                         'lag_1', 'lag_2', 'lag_3', 'lag_7', 'rolling_mean_7'])\
    prediction = model.predict(input_data)[0]\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\li1517\fi-1518\pardirnatural\partightenfactor0
\cf0     st.success(f"Predicted power usage: \{prediction:.2f\} kW")}