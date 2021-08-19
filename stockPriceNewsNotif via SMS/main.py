import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stockNewsKey = "QPZN0R1IN1SCBBV7"

stockNewsPrameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stockNewsKey
}
# get the API response from alphanvantage API to get stock
stockNewsResponse = requests.get(url="https://www.alphavantage.co/query", params=stockNewsPrameters)
stockNewsResponse.raise_for_status()
stockNewsData = stockNewsResponse.json()


# get the closing stock yesterday and the day before yesterday
stocks = stockNewsData["Time Series (Daily)"]
# stockClosingYesterday1 = stockNewsData["Time Series (Daily)"]["2021-07-21"]
allStocks = [value for key, value in stocks.items()]
stockClosingYesterday = allStocks[0]
stockClosingDayBeforeYesterday = allStocks[1]

# get the closing stock price
stockClosingYesterday1 = float(stockClosingDayBeforeYesterday["4. close"])
stockClosingYesterday = float(stockClosingYesterday["4. close"])

# check if the percentage difference is greater than 5%
percentageDifference = round(((stockClosingYesterday - stockClosingYesterday1) / stockClosingYesterday1) * 100, 2)

increase = "Up by: "
if True:
    if percentageDifference < 0:
        increase = "Down by: "
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    # news API parameters
    newsAPIKey = "a840b6f68eb048ecbce3ccb087c91617"
    newsAPIParameters = {
        "q": COMPANY_NAME,
        "from": "2021-07-21",
        "sortBy": "publishedAt",
        "apiKey": newsAPIKey,
        "pageSize": 3
    }
    newsResponse = requests.get(url="https://newsapi.org/v2/everything", params=newsAPIParameters)
    newsResponse.raise_for_status()
    newsData = newsResponse.json()["articles"]

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    # twilio account sending SMS API

    account_sid = 'AC908d470bc46518b482e838f5314cf40c'
    auth_token = 'e0b3151dce72e0031b2807066c09d304'

    # connect to client of TWILIO
    client = Client(account_sid, auth_token)
    # send 3 news
    for news in newsData:
        headline = news["title"]
        content = news["description"]
        newsMessage = \
        f"""
        Tesla: {increase}{abs(percentageDifference)}%
        Headline: {headline}
        Brief: {content}"""

        message = client.messages.create(body=newsMessage, from_="+14808004636", to="+639989245999")
        print(message.status)
else:
    print('')

#Optional: Format the SMS message like this: 


