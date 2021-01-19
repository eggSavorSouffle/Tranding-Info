
# Xavier Souffront
# 1/18/2020 
# Tranding Info

import yfinance as yf 

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup


#Procedure to search and retrive stock data

contd = "y"

while contd == "y":
    print("Search For Stock Data\nEnter The Ticker")
    x = input()
    tickerData = yf.Ticker(x)
    tickerDf = tickerData.history(period= '1d', start= '2010-1-1', end= '2020-1-25')
    print(tickerDf)
    print("Would like to make another search? ")
    contd = input()

#CAP M Formula (Ra = Rf + B(Rm - Rf))
#Default Variables
Ra = 0
Rf = 0
B = 0
Rm = 0

print("Would you like to find the CAP M? \n")
y = input()
while y == "y":
    print("What is the Beta of your Stock? \n")
    beta = input()
    B = beta

    print("What kind of T-Note would you like to see? \n")
    tNote = input()
    Rf = tNote

    print("What is the last closing price of the S&P 500? \n")
    indexPrice = input()
    print("Now what was the price of it a year ago? \n")
    oldIndexPrice = input()
    Rm = ((indexPrice - oldIndexPrice)/oldIndexPrice)#I got an error here. Cant do arithmetic on strings 

    Ra = Rf+B(Rm-Rf)

    print("The CAP M for this stock is "+ Ra +"%")
