#!/usr/bin/env python
#coding: utf-8

import time, datetime
import numpy as np
import pandas as pd

class Bond() :
	def __init__(self, par, coupon, frequency, maturity) :
		self.par = par
		self.coupon = coupon
		self.frequency = frequency
		self.maturity = maturity

	def get_term_to_maturity(self, unit="y") :
		today = datetime.datetime.now()
		maturity = datetime.datetime.strptime(self.maturity, "%Y-%m-%d")
		ttm = (maturity - today)
		if (unit == "d") :
			ttm = ttm.days
		elif (unit == "m") :
			ttm = round(ttm.days/30)
		elif (unit == "y") :
			ttm = round(ttm.days/360)
		return ttm

	def get_coupon_dates(self) :
		coupon_dates = []
		maturity = datetime.datetime.strptime(self.maturity, "%Y-%m-%d")
		ttm = self.get_term_to_maturity("y")
		for t in range(1, ttm * self.frequency + 1) :
			date = (maturity - datetime.timedelta(days=((365.25 * t) / self.frequency))).strftime("%Y-%m-%d")
			coupon_dates.append(date)
		return coupon_dates

	def get_price(self, ytm) :
		price = 0
		ttm = self.get_term_to_maturity("y")
		cashflow = (self.par * self.coupon) / self.frequency
		ytm /= self.frequency
		for t in range(1, ttm * self.frequency + 1) :
			if (t == ttm * self.frequency) :
				present_value = (self.par + cashflow) / ((1 + ytm) ** t)
			else :
				present_value = cashflow / ((1 + ytm) ** t)
			price += present_value
		return price
		
	def get_cashflows(self, ytm) :
		cf = []
		ttm = self.get_term_to_maturity("y")
		cashflow = (self.par * self.coupon) / self.frequency
		ytm /= self.frequency
		for t in range(1, ttm * self.frequency + 1) :
			if (t == ttm * self.frequency) :
				present_value = (self.par + cashflow) / ((1 + ytm) ** t)
				cashflow = self.par + cashflow
			else :
				present_value = cashflow / ((1 + ytm) ** t)
			cf.append([t, cashflow, present_value])
		ytm *= self.frequency
		df = pd.DataFrame((cf), columns=["T", "CF", "PV"]).set_index("T")
		return df

	def get_current_yield(self, ytm) :
		cashflow = self.par * self.coupon
		price = self.get_price(ytm)
		current_yield = cashflow / price
		return current_yield

def main() :
	pass

if __name__ == "__main__" :
	main()
