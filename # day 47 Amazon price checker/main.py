import requests
import smtplib

MY_EMAIL = "pushpakumarpushpakumar70@gmail.com"
PASSWORD = "thpx ynll qwen mmjx"

from bs4 import BeautifulSoup
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
"User-Agent":"Mozilla/5.0 (Windows N(T 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
"Accept-Language":"en-US,en;q=0.9,ta;q=0.8,zh-CN;q=0.7,zh;q=0.6"
}
response = requests.get(URL, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

price = soup.find(class_="aok-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"{title} \nis now {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="pushpakumar2222000@gmail.com",
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8"))