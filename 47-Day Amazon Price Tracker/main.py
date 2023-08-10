import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
import os

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-PL,en;q=0.9,ru-PL;q=0.8,ru;q=0.7,en-GB;q=0.6,en-US;q=0.5,pl;q=0.4,uz;q=0.3"
}

email = os.environ.get("YOUR_EMAIL")
password = os.environ.get("YOUR_PASSWORD")

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
response = requests.get(url=URL, headers=header)
soup = BeautifulSoup(response.text, "lxml")

price_whole = soup.find(name="span", class_='a-price-whole').getText()  # shows the integer part of the price
price_fraction = soup.find(name="span", class_="a-price-fraction").getText()  # shows the fractional price
price = float(price_whole + price_fraction)

product_name = soup.find(name="span", id="productTitle").getText().strip()  # gets the product's name


if price < 100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)

        subject = "Amazon Price Alert!"
        product_name_encoded = product_name.encode("utf-8")  # Encode the product name
        message = f"Subject: {subject}\n{product_name_encoded.decode()} is now ${price}\n{URL}"

        # Convert the message to bytes using UTF-8 encoding
        message_bytes = message.encode("utf-8")

        connection.sendmail(
            from_addr=email,
            to_addrs="sultonovjaloliddin07@gmail.com",
            msg=message_bytes
        )