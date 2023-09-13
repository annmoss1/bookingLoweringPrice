from email.message import EmailMessage
import re
import sys
from urllib.parse import parse_qs, urlparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import smtplib

if len(sys.argv) < 3:
    print("Please enter the URL of the booking main search screen with your search, current price and your email as arguments")
    sys.exit(1)

if sys.argv[2].isnumeric() == False:
    print("Please enter a valid price")
    sys.exit(1)

current_price = int(sys.argv[2])
url = sys.argv[1]
my_mail = sys.argv[3]

parsed_url = urlparse(url)
query_params = parse_qs(parsed_url.query)

checkin_date = query_params.get('checkin', [''])[0]
checkout_date = query_params.get('checkout', [''])[0]
num_of_adults = int(query_params.get('group_adults', 2)[0])
num_of_rooms = int(query_params.get('no_rooms', 1)[0])
num_of_childrens = int(query_params.get('group_children', 0)[0])

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get(url)
try:
    prices_first_hotel = driver.find_element(By.CSS_SELECTOR, '#search_results_table > div:nth-child(2) > div > div > div.d4924c9e74 > div.c82435a4b8.a178069f51.a6ae3c2b40.a18aeea94d.d794b7a0f7.f53e278e95.da89aeb942.c12ee2f811 > div.d20f4628d0 > div.b978843432 > div > div.d7449d770c.a081c98c6f > div.e41894cca1 > div > div.fd1924b122.d4741ba240 > span').text
except:
    print('No results found')
    sys.exit(1)

name_first_hotel = driver.find_element(By.CSS_SELECTOR, '#search_results_table > div:nth-child(2) > div > div > div.d4924c9e74 > div.c82435a4b8.a178069f51.a6ae3c2b40.a18aeea94d.d794b7a0f7.f53e278e95.da89aeb942.c12ee2f811 > div.d20f4628d0 > div.b978843432 > div > div:nth-child(1) > div > div.aaee4e7cd3.e7a57abb1e > div > div:nth-child(1) > div > h3 > a > div.f6431b446c.a23c043802').text
prices_first_hotel_splitted = prices_first_hotel.split("₪")
new_price_list = []
for item in prices_first_hotel_splitted:
    new_item = re.sub(r'\D', '', item)
    if new_item != '':
        new_price_list.append(new_item)

min_price = min(new_price_list)
driver.quit()

if int(min_price) < current_price:
    text = f'The price was dropped! \n The last price for hotel {name_first_hotel} from {checkin_date} to {checkout_date} for {num_of_adults} adultes and {num_of_childrens} children in {num_of_rooms} rooms was {current_price}₪ and now it is {min_price}₪. To book it, go to: {url}'
    print(text)

    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = f'The price has dropped for {name_first_hotel}!'
    msg['From'] = "booking2811@gmail.com"
    msg['To'] = "annmoss2811@gmail.com"
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("booking2811@gmail.com", "ipwh bogl twpd rvtd")
            server.send_message(msg)
            print("Email sent successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")