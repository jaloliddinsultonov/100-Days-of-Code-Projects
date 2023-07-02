import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_KEY_alphavantage = "3GWI5TEXMVNJ2TK1"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# # STEP 1: Use https://newsapi.org/docs/endpoints/everything When STOCK price increase/decreases by 5% between
# yesterday and the day before yesterday then print("Get News"). HINT 1: Get the closing price for yesterday and the
# day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive
# difference is 20. HINT 2: Work out the value of 5% of yerstday's closing stock price.

url_alphavantage = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&interval=60min" \
                   f"&apikey={API_KEY_alphavantage}"
response = requests.get(url_alphavantage)
price_y = float(response.json()['Time Series (Daily)']['2023-06-30']['4. close'])
price_b_y = float(response.json()['Time Series (Daily)']['2023-06-29']['4. close'])

positive_diff = abs(price_y - price_b_y)
positive_diff = round(positive_diff, 2)

if price_y >= price_b_y:
    sticker = "🔺"
else:
    sticker = "🔻"

print(positive_diff)
print(f"2023-06-30 closing price {price_y}")
print(f"2023-06-29 closing price {price_b_y}")

# Percentage of a yesterday's difference
percent = 100 * positive_diff / price_y
percent = round(percent, 2)
print(f"{sticker} {percent}%")

# # STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
# HINT 1: Think about using the Python Slice Operator

url_newsapi = ('https://newsapi.org/v2/everything?'
               'q=Tesla&'
               'from=2023-06-29&'
               'sortBy=popularity&'
               'apiKey=f96ea05f11f14b4eac9f43da9a90c0bf')

response = requests.get(url_newsapi)
data = response.json()['articles']
title = data[2]['title']
info = data[2]['content']
print(data)
print(info)
print(title)

# # STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
# HINT 1: Consider using a List Comprehension.

account_sid = 'AC5180ed732e7cb90ee25b4adda424a3a7'
auth_token = "dbaec1b52eab8c29d6bb6de586a4583a"
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+14847490842',
    body=f"TSLA: {sticker}{percent}%\nHeadline: {title}\nBrief: {info}",
    to='+48733677206'
)

print(message.sid)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
