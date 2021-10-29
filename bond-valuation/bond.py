#!/usr/bin/env python
#coding: utf-8

import time, datetime
import numpy as np
import pandas as pd
import streamlit as st

class Bond():
    def __init__(self, par, coupon, frequency, maturity):
        self.par = par
        self.coupon = coupon
        self.frequency = frequency
        self.maturity = maturity

    def get_term_to_maturity(self, unit="y"):
        today = datetime.datetime.now()
        maturity = datetime.datetime.strptime(self.maturity, "%Y-%m-%d")
        ttm = (maturity - today)
        if (unit == "d"):
            ttm = ttm.days
        elif (unit == "m"):
            ttm = round(ttm.days / 30)
        elif (unit == "y"):
            ttm = round(ttm.days / 360)
        return ttm

    def get_coupon_dates(self):
        coupon_dates = []
        maturity = datetime.datetime.strptime(self.maturity, "%Y-%m-%d")
        ttm = self.get_term_to_maturity("y")
        for t in range(1, ttm * self.frequency + 1):
            date = (maturity - datetime.timedelta(days=((365.25 * t) / self.frequency))).strftime("%Y-%m-%d")
            coupon_dates.append(date)
        return coupon_dates

    def get_price(self, ytm):
        price = 0
        ttm = self.get_term_to_maturity("y")
        cashflow = (self.par * self.coupon) / self.frequency
        ytm /= self.frequency
        for t in range(1, ttm * self.frequency + 1):
            if (t == ttm * self.frequency):
                present_value = (self.par + cashflow) / ((1 + ytm) ** t)
            else:
                present_value = cashflow / ((1 + ytm) ** t)
            price += present_value
        return price

    def get_cashflows(self, ytm):
        cf = []
        ttm = self.get_term_to_maturity("y")
        cashflow = (self.par * self.coupon) / self.frequency
        ytm /= self.frequency
        for t in range(1, ttm * self.frequency + 1):
            if (t == ttm * self.frequency):
                present_value = (self.par + cashflow) / ((1 + ytm) ** t)
                cashflow = self.par + cashflow
            else:
                present_value = cashflow / ((1 + ytm) ** t)
            cf.append([t, cashflow, present_value])
        ytm *= self.frequency
        df = pd.DataFrame((cf), columns=["T", "CF", "PV"])
        df['date'] = self.get_coupon_dates()[::-1]
        df = df[["T", "date", "CF", "PV"]].set_index("T")
        return df

    def get_current_yield(self, ytm):
        cashflow = self.par * self.coupon
        price = self.get_price(ytm)
        current_yield = cashflow / price
        return current_yield

def user_input_features():
    st.sidebar.header("Bond")
    par = st.sidebar.number_input(label="Par", min_value=0.00, value=1000000.00, step=500.00)
    coupon = st.sidebar.number_input(label="Annual Coupon (%)", min_value=0.00, max_value=100.00, value=1.50, step=0.05)
    frequency = st.sidebar.selectbox(label="Frequency", options=[1, 2, 4, 12], index=3)
    maturity = st.sidebar.date_input(label="Maturity", value=datetime.date(2030, 12, 31))

    st.sidebar.header("Market")
    rate = st.sidebar.number_input(label="Market Rate (%)", min_value=0.00, max_value=100.00, value=1.00, step=0.05)

    data = {
        "par": par,
        "coupon": coupon,
        "frequency": frequency,
        "maturity": maturity.strftime("%Y-%m-%d"),
        "rate": rate
    }
    features = pd.DataFrame(data, index=[0])
    return features

st.header("User Input Parameters")
features = user_input_features()
st.subheader("Bond")
st.write(features[['par', 'coupon', 'frequency', 'maturity']])
st.subheader("Market")
st.write(features[['rate']])

bond = Bond(
    par=features['par'][0],
    coupon=features['coupon'][0] / 100,
    frequency=features['frequency'][0],
    maturity=features['maturity'][0]
)

rate = features['rate'][0] / 100

st.header("Output")
price = round(bond.get_price(rate), 2)
st.write("Price", price)

current_yield = round(bond.get_current_yield(rate), 6)
st.write("Current Yield", current_yield * 100, "%")

def main():
    pass

if __name__ == "__main__":
    main()
