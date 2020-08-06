#!/usr/bin/env python
#coding: utf-8

import datetime
import bond
import pandas as pd
import streamlit as st

def user_input_features() :
    st.sidebar.header("Bond")
    par = st.sidebar.number_input("Par", 0.00, 100000000000.00, 1000000.00, step=500.00)
    coupon = st.sidebar.number_input("Annual Coupon (%)", 0.00, 100.00, 1.50, step=0.05)
    frequency = st.sidebar.selectbox("Frequency", [1, 2, 4, 12], 3)
    maturity = st.sidebar.date_input("Maturity", datetime.date(2030, 12, 31))
    
    st.sidebar.header("Market")
    rate = st.sidebar.number_input("Market Rate (%)", 0.00, 100.00, 1.00, step=0.05)

    data = {
        "par" : par,
        "coupon" : coupon,
        "frequency" : frequency,
        "maturity" : maturity.strftime("%Y-%m-%d"),
        "rate" : rate
    }
    features = pd.DataFrame(data, index=[0])
    return features

st.subheader("User Input Parameters")    
features = user_input_features()
st.write(features)

bond = bond.Bond(
    par=features['par'][0],
    coupon=features['coupon'][0]/100,
    frequency=features['frequency'][0],
    maturity=features['maturity'][0]
)

rate = features['rate'][0]/100

st.subheader("Output")
price = round(bond.get_price(rate), 2)
st.write("Price", price)

current_yield = round(bond.get_current_yield(rate), 6)
st.write("Current Yield", current_yield*100, "%")
