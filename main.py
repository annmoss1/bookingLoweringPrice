import requests
import sys
from urllib.parse import urlparse, parse_qs
from pprint import pprint

if len(sys.argv) < 3:
    print("Please enter the URL of the booking main search screen with your search (go to booking.com, enter the "
          "parameters for your search starting after"
          "https://www.booking.com/searchresults.en-gb.html?), current price and your email as arguments")
    sys.exit(1)

current_price = int(sys.argv[2])
url = f'https://www.booking.com/dml/graphql?{sys.argv[1]}'

parsed_url = urlparse(url)
query_params = parse_qs(parsed_url.query)

checkin_date = query_params.get('checkin', [''])[0]
checkout_date = query_params.get('checkout', [''])[0]
num_of_adults = int(query_params.get('group_adults', [''])[0])
num_of_rooms = int(query_params.get('no_rooms', [''])[0])
num_of_childrens = int(query_params.get('group_children', [''])[0])
dest_type = query_params.get('dest_type', [''])[0].upper()
dest_id = int(query_params.get('dest_id', [''])[0])
aid = query_params.get('aid', [''])[0]
selectedFilters = query_params.get('nflt', [''])[0]
acidCarouselId = 6

cookies = {
    'bkng': '11UmFuZG9tSVYkc2RlIyh9Yaa29%2F3xUOLbwcLxQQ4VaCqc9oIsRnN8ekA9pET0BBgaIy1ydAu4N5q1c1IqrlWzHEKSFUBGsyRFN0AgoF730ZjwUE0XMSF1%2FycWlUZBSq0XmcUHXrLiM0Lz%2F9ekg8v%2BusgrhbShw6TYAlSzE%2Bk4ZhINvAAVGOvFA1HUGwZ8%2F%2BdPIh%2FL53b29mY%3D',
}

headers = {
    'authority': 'www.booking.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,he;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://www.booking.com',
    'pragma': 'no-cache',
    'referer': url,
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-booking-context-action-name': 'searchresults_irene',
    'x-booking-context-aid': aid,
    'x-booking-site-type-id': '1',
    'x-booking-topic': 'capla_browser_b-search-web-searchresults',
}

json_data = {
    'operationName': 'AcidCarouselSearch',
    'variables': {
        'input': {
            'basicSearchInput': {
                'pagination': {
                    'rowsPerPage': 25,
                    'offset': 0,
                },
                'nbRooms': num_of_rooms,
                'nbAdults': num_of_adults,
                'nbChildren': num_of_childrens,
                'childrenAges': [],
                'travelPurpose': 2,
                'dates': {
                    'checkin': checkin_date,
                    'checkout': checkout_date,
                },
                'location': {
                    'destType': dest_type,
                    'destId': dest_id,
                },
                'filters': {
                    'selectedFilters': selectedFilters,
                },
                'optionalFeatures': {
                    'forceArpExperiments': True,
                    'testProperties': False,
                },
            },
            'acidCarouselContext': {
                'acidCarouselId': acidCarouselId,
                'seedHotelId': None,
            },
            'filterAggregates': None,
        },
    },
    'extensions': {},
    'query': 'query AcidCarouselSearch($input: AcidCarouselInput!) {\n  searchQueries {\n    searchAcidCarousel(input: $input) {\n      acidCarouselId\n      title\n      subtitle\n      trackOnView {\n        experimentHash\n        type\n        experimentTag\n        value\n        __typename\n      }\n      acidCards {\n        sustainability {\n          isSustainable\n          __typename\n        }\n        basicPropertyData {\n          propertyId: id\n          name\n          accommodationTypeName\n          pageName\n          location {\n            countryCode\n            __typename\n          }\n          photos {\n            main {\n              lowResJpegUrl {\n                relativeUrl\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          starRating {\n            value\n            symbol\n            showAdditionalInfoIcon\n            __typename\n          }\n          reviewScore: reviews {\n            score: totalScore\n            totalScoreTextTag {\n              translation\n              __typename\n            }\n            showScore\n            __typename\n          }\n          __typename\n        }\n        priceDisplayInfo {\n          displayPrice {\n            amountPerStay {\n              amountRounded\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        localizedDistanceToCityCenter\n        lastViewDateTime\n        lastBookDateTime\n        __typename\n      }\n      canShowMoreProperties\n      hasAvailability\n      landingOptions {\n        ...LandingOptions\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment LandingOptions on LandingOptions {\n  page\n  selectedFilters\n  destId\n  destType\n  checkin\n  checkout\n  nbAdults\n  nbChildren\n  childrenAges\n  nbRooms\n  sorter\n  travelPurpose\n  __typename\n}\n',
}

response = requests.post(
    url,
    cookies=cookies,
    headers=headers,
    json=json_data,
)

response_as_json = response.json()
optional_price = \
    response_as_json["data"]["searchQueries"]["searchAcidCarousel"]["acidCards"][0]["priceDisplayInfo"]["displayPrice"][
        "amountPerStay"]["amountRounded"]
optional_price_as_number = int(''.join(filter(str.isdigit, optional_price)))
if optional_price_as_number < current_price:
    print(f"found a better price! you are paying {current_price} while today its {optional_price_as_number}")
    pprint(response_as_json)
