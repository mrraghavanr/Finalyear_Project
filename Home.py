# ============Importing Necessary Libraries======================================
import streamlit as st
import os
import joblib
import time

col1, col2 = st.columns([3,1])
# ============Creating Main App==================================
def main():
  with col1:
    st.markdown("""
      <style>
      @keyframes blink {
        0% {opacity:1;}
        50% {opacity:0;}
        100% {opacity:1;}
      }
      .blinking-text{
        animation : blink 10s infinite;
        color : #FF4B4B;
        font-size :30px;
        font-family: "Times New Roman", sans-serif;
        font-style: Bold;
      }
      .custom-font{
        font-size :20px;
        font-family: "Times New Roman", sans-serif;
        color:#0C0C0B;
        }
      </style> 
      <p class = "blinking-text"><b>RETAIL PRICE OPTIMIZATION APP</b></p>
      
      <p class = "custom-font">This app predicts the optimal pricing for a retail business for different product categories based on various factors such as lag prices , volume , demand , competitve prices index etc.</p>
    """, unsafe_allow_html= True)

  with col2:
    st.image("images/home_image.png")

  with col2:
    st.image("images/home_image.png")

  st.sidebar.markdown("""
      <style>
      @keyframes blink {
        0% {opacity:1;}
        50% {opacity:0;}
        100% {opacity:1;}
      }
      .blinking-txt{
        animation : blink 10s infinite;
        color : #565353;
        font-size :18px;
        font-family: "Times New Roman", sans-serif;
        font-style: Bold;
        }
      </style>
      <p class = blinking-txt>Which product would you like to optimize it's price?</p>  
        """, unsafe_allow_html= True)

  with col1:
    st.image("EDA/Customer_Segment.png")

  st.markdown(
    """ 
    <style>
    .bottom-text{
      position:fixed;
      bottom:0;
      width:50%;
      background-color:#E2E2EC ;
      color:#565353;               
      text-align:center;
      padding:10px;
      font-size:14px;
      font-family: "Times New Roman", sans-serif;
    }
    </style>
    <div class = bottom-text>
      This App Highlights the Effectiveness of Data-driven 
      Approaches in Informing Retail Pricing Decisions, 
      Providing Actionable Recommendations for Improvement.
    </div>
    
    """
  , unsafe_allow_html= True)

if __name__ == "__main__":
  main()
