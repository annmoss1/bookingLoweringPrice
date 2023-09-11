import requests

cookies = {
    'FPLC': 'Xsc%2BN%2FAqlMeMIZUdl19znRqp%2Bm4KJgWCDJliCgoOhpA7xl9wrw5mnVK3dgBFTgtG2208IrX5xfEFPoSWPqf4veAV%2FhP3KSamwyMEjSV%2Bdpx3IKlx3ALjFql3zlEy2Q%3D%3D',
    'FPID': 'FPID2.2.5qeJqMh3anOoyQH%2BQqRaicMTEm8C3PFA7976XwaA%2Fyw%3D.1691235292',
    'cors_js': '1',
    'BJS': '-',
    'bkng_sso_session': 'e30',
    'OptanonConsent': 'implicitConsentCountry=nonGDPR&implicitConsentDate=1694429179369',
    'pxcts': '70ec6807-5090-11ee-9fdf-65ce91af9140',
    '_pxvid': '70ec55a6-5090-11ee-9fdf-2201b3b6c2a5',
    'bkng_sso_ses': 'eyJib29raW5nX2dsb2JhbCI6W3siaCI6Ik5KOHJMeUhQdEwxZW1CcmhXaHhVaTc4Q1MyRnhHMFpBVGxMbFE1OXU1MmciLCJhIjoxfV19',
    'pcm_consent': 'consentedAt%3D2023-09-11T10%3A46%3A19.768Z%26countryCode%3DIL%26expiresAt%3D2024-03-09T10%3A46%3A19.768Z%26implicit%3Dfalse%26regionCode%3DTA%26regulation%3Dnone%26legacyRegulation%3Dnone%26consentId%3Dab370efe-6dc5-44f9-aca8-78dc9e71092f%26analytical%3Dtrue%26marketing%3Dtrue',
    'bkng_sso_auth': 'CAIQsOnuTRqEAX6qRfR1BNaVI+Q6rVsjbg0QnoSS11e3dQJ8Xpbh2mV0teIO1OgD2PuVI9Rhy4wfFA3Q2IeWpjXEoQQpZtCPFZoPO7r883WdFXQCKMjqrPNUq2emSLty3Na+LYjvuIt84fXcgT7Yyt0GwrrefYaCjGJOdP8tZMvdGRzgyD0TQcYi3GGQCQ==',
    '_pxhd': '2TG7-SvZXmpslYTmP46QX288-oniva5M9iaIaPDpBNS5H0ROebDqtputvJWqigii%252F5bldnTwD0E2dPkp4A-%252FPg%253D%253D%253ALYz6Noopix51bGSBEVMfw-FAEYr8zSQ2QUw90IOX1TrHmJzJAGja5NXSB-TGcv9WJIhNzapdBhimlH1Cpr6LPvOvOY8qb9EqMUtOaTCGtIs%253D',
    'bkng_prue': '1',
    '_gcl_au': '1.1.1919996597.1694429182',
    '_ga': 'GA1.1.679704450.1694429182',
    '_scid': 'c3931429-79a8-4ec9-9ad2-14b48e5a65c8',
    '_pin_unauth': 'dWlkPVpqTTVOV05qWVdVdE5qUTNPQzAwT1RnM0xUZ3pObUl0T1dRNU5tVTRNVGRqTURNNA',
    '_sctr': '1%7C1694379600000',
    'b': '%7B%22countLang%22%3A4%7D',
    '_ga_4GY873RFCC': 'GS1.1.1694429442.2.0.1694429442.0.0.0',
    'px_init': '0',
    '_gcl_aw': 'GCL.1694433845.EAIaIQobChMI46Tg98GigQMVtkFBAh3vrwKuEAAYASAAEgJfr_D_BwE',
    'reese84': '3:wd3q/ALuBKSAVUfUjTqzWA==:CeAYf/d83ADcoVq3QAkxQLYWlVBptkf0+EDZbEXpRXc1lktcXmWbs6cvPngt8r/+6uYWDR0aZND97ODew6St8dPrcLOVu3tZSXF9zR0D8ECoFKK38TOCk/ORV+0xBdl+wJe2PUj/WMU/eGMa89UDbxJMdFwyZ9KWc7OE1dYovyjxuG2A0txt9VgvRkXb66QH2O2xqHxxZ6oZwJrNkjP4RVXhctxvUgfhgk4vmBPz5/3z2dqmbGpPK6r9stjKgNRa090mjCQxmgV12eGwJMPkR68BXFv6t2esZL24t8bKuKLMJqNqrh1VgTg2to1ntPNE/71r2NCPfZO/ZTWiG8O4jdort34vvEahhMXbKQe3DzoARBb1FjimI8tIcNvA0AG+V168afF+uWgQ1udZS53GFZrBIMayQyIcEzo0rN3JzGkhWurCaQSgvdqqfkW6YMY83vhMLudYwKJL46yuyFJ+SA==:3DrOp+Zx7O7HdyvpKtOBZbKPod1S8AHZhjMM8Uv7SYM=',
    '_pxff_cfp': '1',
    '_pxff_ddtc': '1',
    '_scid_r': 'c3931429-79a8-4ec9-9ad2-14b48e5a65c8',
    '_uetsid': '5802fe60507911eea36c1132d84f2c6a',
    '_uetvid': 'a79d17d02b0d11ed881f9f08fe65ae24',
    '_px3': '3b01d663bd287be955b986ca74d076a24c3bd08c7500f0bf71288a22c7e00f2a:OjC40VhUrabjZUEPE+xupmE1jUC+XeYvqt+2NXHII6kl/YHVAqh2EatgczgJMTIaICV5UkUZcq1Y235vBi++Lw==:1000:8cKi0a8Gu1AjFn92gf7qvV4O3PvRTtLy7iBhKGLhcRXRUYl3fHoVZbLvrLoUqo6i3HcGADA6r1ahJoRGAA1KVDcKVZt74m6aF/quouPYCnoEoJKMUT7m4kz+IEDH4Mrll1TQmLCQtPfb0a9ou9gwaElwbO8O5NtfrBnbMxTjBsQkLqU4wgDnWTH0Xio1jDj801x1lQ8JMPvvMqOt/Oyb+w==',
    '_pxde': '79dbd4f2e0d2d1a58bf2a852103a35adc9bc4d80b2c054030672d9383aeb5f32:eyJ0aW1lc3RhbXAiOjE2OTQ0Mzg0NjcxMzAsImZfa2IiOjAsImlwY19pZCI6W119',
    '_ga_FPD6YLJCJ7': 'GS1.1.1694437463.3.1.1694438489.28.0.0',
    '_ga_A12345': 'GS1.1.1694437463.8.1.1694438490.0.0.0',
    'lastSeen': '1694438490066',
    'bkng': '11UmFuZG9tSVYkc2RlIyh9Yaa29%2F3xUOLbca8KLfxLPeftaKMkl4GFNeoP5yG1wYavAuAZAunsf2zkWAVNmYrg4atuwhF%2F%2BgyS1scRaIBrjSTLH8HP4Stduyxgrxfnqr7goOWRoG8M1JBOv4rfANesg%2FMIukwN9j7MoHTMVjlNciODvigE21RkME9n5%2BczuK7eWsIwGkctbG08YpRCFwd11g%3D%3D',
}

headers = {
    'authority': 'www.booking.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,he;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': 'FPLC=Xsc%2BN%2FAqlMeMIZUdl19znRqp%2Bm4KJgWCDJliCgoOhpA7xl9wrw5mnVK3dgBFTgtG2208IrX5xfEFPoSWPqf4veAV%2FhP3KSamwyMEjSV%2Bdpx3IKlx3ALjFql3zlEy2Q%3D%3D; FPID=FPID2.2.5qeJqMh3anOoyQH%2BQqRaicMTEm8C3PFA7976XwaA%2Fyw%3D.1691235292; cors_js=1; BJS=-; bkng_sso_session=e30; OptanonConsent=implicitConsentCountry=nonGDPR&implicitConsentDate=1694429179369; pxcts=70ec6807-5090-11ee-9fdf-65ce91af9140; _pxvid=70ec55a6-5090-11ee-9fdf-2201b3b6c2a5; bkng_sso_ses=eyJib29raW5nX2dsb2JhbCI6W3siaCI6Ik5KOHJMeUhQdEwxZW1CcmhXaHhVaTc4Q1MyRnhHMFpBVGxMbFE1OXU1MmciLCJhIjoxfV19; pcm_consent=consentedAt%3D2023-09-11T10%3A46%3A19.768Z%26countryCode%3DIL%26expiresAt%3D2024-03-09T10%3A46%3A19.768Z%26implicit%3Dfalse%26regionCode%3DTA%26regulation%3Dnone%26legacyRegulation%3Dnone%26consentId%3Dab370efe-6dc5-44f9-aca8-78dc9e71092f%26analytical%3Dtrue%26marketing%3Dtrue; bkng_sso_auth=CAIQsOnuTRqEAX6qRfR1BNaVI+Q6rVsjbg0QnoSS11e3dQJ8Xpbh2mV0teIO1OgD2PuVI9Rhy4wfFA3Q2IeWpjXEoQQpZtCPFZoPO7r883WdFXQCKMjqrPNUq2emSLty3Na+LYjvuIt84fXcgT7Yyt0GwrrefYaCjGJOdP8tZMvdGRzgyD0TQcYi3GGQCQ==; _pxhd=2TG7-SvZXmpslYTmP46QX288-oniva5M9iaIaPDpBNS5H0ROebDqtputvJWqigii%252F5bldnTwD0E2dPkp4A-%252FPg%253D%253D%253ALYz6Noopix51bGSBEVMfw-FAEYr8zSQ2QUw90IOX1TrHmJzJAGja5NXSB-TGcv9WJIhNzapdBhimlH1Cpr6LPvOvOY8qb9EqMUtOaTCGtIs%253D; bkng_prue=1; _gcl_au=1.1.1919996597.1694429182; _ga=GA1.1.679704450.1694429182; _scid=c3931429-79a8-4ec9-9ad2-14b48e5a65c8; _pin_unauth=dWlkPVpqTTVOV05qWVdVdE5qUTNPQzAwT1RnM0xUZ3pObUl0T1dRNU5tVTRNVGRqTURNNA; _sctr=1%7C1694379600000; b=%7B%22countLang%22%3A4%7D; _ga_4GY873RFCC=GS1.1.1694429442.2.0.1694429442.0.0.0; px_init=0; _gcl_aw=GCL.1694433845.EAIaIQobChMI46Tg98GigQMVtkFBAh3vrwKuEAAYASAAEgJfr_D_BwE; reese84=3:wd3q/ALuBKSAVUfUjTqzWA==:CeAYf/d83ADcoVq3QAkxQLYWlVBptkf0+EDZbEXpRXc1lktcXmWbs6cvPngt8r/+6uYWDR0aZND97ODew6St8dPrcLOVu3tZSXF9zR0D8ECoFKK38TOCk/ORV+0xBdl+wJe2PUj/WMU/eGMa89UDbxJMdFwyZ9KWc7OE1dYovyjxuG2A0txt9VgvRkXb66QH2O2xqHxxZ6oZwJrNkjP4RVXhctxvUgfhgk4vmBPz5/3z2dqmbGpPK6r9stjKgNRa090mjCQxmgV12eGwJMPkR68BXFv6t2esZL24t8bKuKLMJqNqrh1VgTg2to1ntPNE/71r2NCPfZO/ZTWiG8O4jdort34vvEahhMXbKQe3DzoARBb1FjimI8tIcNvA0AG+V168afF+uWgQ1udZS53GFZrBIMayQyIcEzo0rN3JzGkhWurCaQSgvdqqfkW6YMY83vhMLudYwKJL46yuyFJ+SA==:3DrOp+Zx7O7HdyvpKtOBZbKPod1S8AHZhjMM8Uv7SYM=; _pxff_cfp=1; _pxff_ddtc=1; _scid_r=c3931429-79a8-4ec9-9ad2-14b48e5a65c8; _uetsid=5802fe60507911eea36c1132d84f2c6a; _uetvid=a79d17d02b0d11ed881f9f08fe65ae24; _px3=3b01d663bd287be955b986ca74d076a24c3bd08c7500f0bf71288a22c7e00f2a:OjC40VhUrabjZUEPE+xupmE1jUC+XeYvqt+2NXHII6kl/YHVAqh2EatgczgJMTIaICV5UkUZcq1Y235vBi++Lw==:1000:8cKi0a8Gu1AjFn92gf7qvV4O3PvRTtLy7iBhKGLhcRXRUYl3fHoVZbLvrLoUqo6i3HcGADA6r1ahJoRGAA1KVDcKVZt74m6aF/quouPYCnoEoJKMUT7m4kz+IEDH4Mrll1TQmLCQtPfb0a9ou9gwaElwbO8O5NtfrBnbMxTjBsQkLqU4wgDnWTH0Xio1jDj801x1lQ8JMPvvMqOt/Oyb+w==; _pxde=79dbd4f2e0d2d1a58bf2a852103a35adc9bc4d80b2c054030672d9383aeb5f32:eyJ0aW1lc3RhbXAiOjE2OTQ0Mzg0NjcxMzAsImZfa2IiOjAsImlwY19pZCI6W119; _ga_FPD6YLJCJ7=GS1.1.1694437463.3.1.1694438489.28.0.0; _ga_A12345=GS1.1.1694437463.8.1.1694438490.0.0.0; lastSeen=1694438490066; bkng=11UmFuZG9tSVYkc2RlIyh9Yaa29%2F3xUOLbca8KLfxLPeftaKMkl4GFNeoP5yG1wYavAuAZAunsf2zkWAVNmYrg4atuwhF%2F%2BgyS1scRaIBrjSTLH8HP4Stduyxgrxfnqr7goOWRoG8M1JBOv4rfANesg%2FMIukwN9j7MoHTMVjlNciODvigE21RkME9n5%2BczuK7eWsIwGkctbG08YpRCFwd11g%3D%3D',
    'origin': 'https://www.booking.com',
    'pragma': 'no-cache',
    'referer': 'https://www.booking.com/searchresults.en-gb.html?ss=Beresheet+by+Isrotel+Exclusive%2C+Mitzpe+Ramon%2C+South+District+Israel%2C+Israel&ssne=Mitzpe+Ramon&ssne_untouched=Mitzpe+Ramon&efdco=1&label=en-il-booking-desktop-sD66O*sLIyR37D38rZhp7wS652796016630%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1008001%3Ali%3Adec%3Adm&sid=4f933c37bea46de5efad9cd97701bdaa&aid=2311236&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=289519&dest_type=hotel&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=03575de0818b026e&ac_meta=GhAwMzU3NWRlMDgxOGIwMjZlIAAoATICZW46BmJlcmVzaEAASgBQAA%3D%3D&checkin=2023-11-11&checkout=2023-11-12&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-booking-context-action-name': 'searchresults_irene',
    'x-booking-context-aid': '2311236',
    'x-booking-csrf-token': 'eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJjb250ZXh0LWVucmljaG1lbnQtYXBpIiwic3ViIjoiY3NyZi10b2tlbiIsImlhdCI6MTY5NDQzODQ4OSwiZXhwIjoxNjk0NTI0ODg5fQ.WsIy6H25P2FTbctoA5LnNyRcOBbYkP5807JXOPJfFzUduyYRCnNYr1TsC5mKPgcAgpwdVOdlQ2udHDK8c9LY1A',
    'x-booking-et-serialized-state': 'EPFalX7N1WP-azanmy5yu-5v3MHYk0oiIpBMY3yG6B7MaUajzV2GOeOwwyDIw7wAxmBV83BD4WC0',
    'x-booking-pageview-id': '08195dec20a8007a',
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
                'nbRooms': 1,
                'nbAdults': 2,
                'nbChildren': 0,
                'childrenAges': [],
                'travelPurpose': 2,
                'dates': {
                    'checkin': '2023-11-11',
                    'checkout': '2023-11-12',
                },
                'location': {
                    'destType': 'CITY',
                    'destId': 900040703,
                },
                'filters': {},
                'optionalFeatures': {
                    'forceArpExperiments': True,
                    'testProperties': False,
                },
            },
            'acidCarouselContext': {
                'acidCarouselId': 6,
                'seedHotelId': None,
            },
            'filterAggregates': None,
        },
    },
    'extensions': {},
    'query': 'query AcidCarouselSearch($input: AcidCarouselInput!) {\n  searchQueries {\n    searchAcidCarousel(input: $input) {\n      acidCarouselId\n      title\n      subtitle\n      trackOnView {\n        experimentHash\n        type\n        experimentTag\n        value\n        __typename\n      }\n      acidCards {\n        sustainability {\n          isSustainable\n          __typename\n        }\n        basicPropertyData {\n          propertyId: id\n          name\n          accommodationTypeName\n          pageName\n          location {\n            countryCode\n            __typename\n          }\n          photos {\n            main {\n              lowResJpegUrl {\n                relativeUrl\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          starRating {\n            value\n            symbol\n            showAdditionalInfoIcon\n            __typename\n          }\n          reviewScore: reviews {\n            score: totalScore\n            totalScoreTextTag {\n              translation\n              __typename\n            }\n            showScore\n            __typename\n          }\n          __typename\n        }\n        priceDisplayInfo {\n          displayPrice {\n            amountPerStay {\n              amountRounded\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        localizedDistanceToCityCenter\n        lastViewDateTime\n        lastBookDateTime\n        __typename\n      }\n      canShowMoreProperties\n      hasAvailability\n      landingOptions {\n        ...LandingOptions\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment LandingOptions on LandingOptions {\n  page\n  selectedFilters\n  destId\n  destType\n  checkin\n  checkout\n  nbAdults\n  nbChildren\n  childrenAges\n  nbRooms\n  sorter\n  travelPurpose\n  __typename\n}\n',
}

response = requests.post(
    'https://www.booking.com/dml/graphql?ss=Beresheet+by+Isrotel+Exclusive%2C+Mitzpe+Ramon%2C+South+District+Israel%2C+Israel&ssne=Mitzpe+Ramon&ssne_untouched=Mitzpe+Ramon&efdco=1&label=en-il-booking-desktop-sD66O*sLIyR37D38rZhp7wS652796016630%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1008001%3Ali%3Adec%3Adm&sid=4f933c37bea46de5efad9cd97701bdaa&aid=2311236&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=289519&dest_type=hotel&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=03575de0818b026e&ac_meta=GhAwMzU3NWRlMDgxOGIwMjZlIAAoATICZW46BmJlcmVzaEAASgBQAA%3D%3D&checkin=2023-11-11&checkout=2023-11-12&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure',
    cookies=cookies,
    headers=headers,
    json=json_data,
)


response_as_json = response.json()
optional_price = response_as_json["data"]["searchQueries"]["searchAcidCarousel"]["acidCards"][0]["priceDisplayInfo"]["displayPrice"]["amountPerStay"]["amountRounded"]
optional_price_as_number = ''.join(filter(str.isdigit, optional_price))
if optional_price_as_number < current_price:
    print("found a better price! you are paying {current} while today its {optional}".format(current=current_price, optional=optional_price_as_number))
print(response.json())
