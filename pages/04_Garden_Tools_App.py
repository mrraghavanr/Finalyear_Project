# ============Importing Necessary Libraries======================================
import streamlit as st
import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# ============Loading dataset and pre-trained model================================
X_data = pd.read_csv("data/garden_tools_Data.csv")
y_data = pd.read_csv("target/y_garden_tools.csv")
model = RandomForestRegressor(n_jobs = -1, random_state = 42)

# =========================splitting the dataset================================
X_garden_tools = X_data.drop(columns = ["unit_price"], axis = 1)

X_train, X_test, y_train, y_test = train_test_split(X_garden_tools, y_data, test_size=0.2,random_state=250)

# =========================training the model================================
model.fit(X_train,y_train)

# =========================Making predictions on the test data=======================
y_pred = model.predict(X_test)

# =========================metrics for model performance============================
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test,y_pred)

# =========================Defining a function to get user inputs====================
def user_input_features():
  qty = st.number_input("Monthly Sales", value=0.0)
  product_photos_qty = st.number_input("Product Photos Quantity", value=0.0)
  customers = st.number_input("Monthly Demand", value=0.0)
  
  # creating dictionary to map month name to their corresponding numeric value
  month_mapping ={
    "January":1,"Febuary":2,"March":3,"April":4,"May":5,"June":6,"July":7,
    "August":8,"September":9,"October":10,"November":11,"December":12 
  }
  # creating a selectbox for month selection
  
  selected_month = st.selectbox("Select a Month", list(month_mapping.keys()))
  volume = st.number_input("Volume", value=0.0)
  lag_price = st.number_input("Lag Price (Previous Month)", value=0.0)
  weekend_ratio = st.number_input("Weekend Ratio", value=0.0)
  competive_price_index = st.number_input("Competitive Price Index", value=0.0)
  freight_ratio = st.number_input("Freight Ratio", value=0.0)
  ratings_ratio = st.number_input("Ratings Ratio", value=0.0)
  competive_weight_index = st.number_input("Competitive Weight Index", value=0.0)
  competive_namelenght_index = st.number_input("Competitive Name Lenght Index", value=0.0)
  competive_descriptionlenght_index = st.number_input("Competitive Description Lenght Index", value=0.0)
  
  # creating dictionary to map holiday month name to their corresponding numeric value
  holiday_mapping ={"Yes":1,"No":0}
  # creating a selectbox for holiday month selection
  selected_holiday = st.selectbox("Holiday Month?", list(holiday_mapping.keys()))
  
  # Storing the input features in a dictionary(input_data)
  input_data = {
    "qty":qty,
    "product_photos_qty":product_photos_qty,
    "customers":customers,
    "month":month_mapping[selected_month],
    "volume":volume,
    "lag_price":lag_price,
    "weekend_ratio":weekend_ratio,
    "competitive_price_index":competive_price_index,
    "freight_ratio":freight_ratio,
    "ratings_ratio":ratings_ratio,
    "competitive_weight_index":competive_weight_index,
    "competitive_Namelenght_index":competive_namelenght_index,
    "competitive_Descriptionlenght_index":competive_descriptionlenght_index,
    "holiday_month":holiday_mapping[selected_holiday],
  }
  # Converting the dictionary(input_data) to a DataFrame
  features = pd.DataFrame(input_data, index=[0])
  return features
#FF4B4B 
def garden_tool():
  st.sidebar.image("images/price_image5.webp")
  st.markdown("""
           <style>
           .text-header{
            color :#22521E;
            font-size :30px;
            font-family: "Times New Roman", sans-serif;
            font-style: Bold;
           }
           </style>
           <p class = text-header >Garden Tools Price Optimization App</p>
           """, unsafe_allow_html= True)

garden_tool()

# Getting user input
input = user_input_features()

# Making predictions based on the input data
if st.button('Optimize'):
    prediction = model.predict(input)
    
    # Display the prediction
    st.success(f"Unit Price : {prediction[0]:.2f}")