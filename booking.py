#%%
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Setup webdriver
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

url = "https://www.booking.com/searchresults.en-gb.html?ss=Selina+Ramon%2C+Mitzpe+Ramon%2C+South+District+Israel%2C+Israel&ssne=Mitzpe+Ramon&ssne_untouched=Mitzpe+Ramon&label=en-il-booking-desktop-sD66O*sLIyR37D38rZhp7wS652796016630%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1008001%3Ali%3Adec%3Adm&aid=359627&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=7182588&dest_type=hotel&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=2&search_selected=true&search_pageview_id=ce455e7303b4004b&ac_meta=GhBjZTQ1NWU3MzAzYjQwMDRiIAAoATICZW46CnNlbGluYSByYW1AAEoAUAA%3D&checkin=2023-11-11&checkout=2023-11-12&group_adults=2&no_rooms=1&group_children=0"
driver.get(url)
prices_first_hotel = driver.find_element(By.CSS_SELECTOR, '#search_results_table > div:nth-child(2) > div > div > div.d4924c9e74 > div.c82435a4b8.a178069f51.a6ae3c2b40.a18aeea94d.d794b7a0f7.f53e278e95.da89aeb942.c12ee2f811 > div.d20f4628d0 > div.b978843432 > div > div.d7449d770c.a081c98c6f > div.e41894cca1 > div > div.fd1924b122.d4741ba240 > span').text
prices_first_hotel_splitted = prices_first_hotel.split("₪")
new_price_list = []
for item in prices_first_hotel_splitted:
    new_item = re.sub(r'\D', '', item)
    if new_item != '':
        new_price_list.append(new_item)
min_price = min(new_price_list)

# driver.quit()
# %%
