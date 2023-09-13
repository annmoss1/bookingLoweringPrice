# Booking Lowering Price Script

************************************************************************************************************************************************************************************
booking_selenium is the correct script, working with selenium.

booking_network is the previous script that was working partially, due to lakes with booking.com API (without mail support yet- its not ready), keeping it in case the API changes. 
************************************************************************************************************************************************************************************


***********************************************************************
To run this script, you will need to provide 3 command line arguments:
***********************************************************************
    1) Path - Go to booking.com, search for your hotel with the correct dates and filters, and after pressing 'search' copy the path
    2) Price - the current price\ the price that you want to be notified when it decreased from in ILS
    3) Mail - your Gmail address that you want to be notified


**************
Run example :
**************
& C:/Users/testUser/AppData/Local/Programs/Python/Python38-32/python.exe "C:\github\bookingLoweringPrice\booking_selenium.py" "https://www.booking.com/searchresults.en-gb.html?    ss=Beresheet+by+Isrotel+Exclusive%2C+Mitzpe+Ramon%2C+South+District+Israel%2C+Israel&ssne=Tel+Aviv&ssne_untouched=Tel+Aviv&sid=4f933c37bea46de5efad9cd97701bdaa&aid=2381889&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=289519&dest_type=hotel&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=68ab3845103201c7&ac_meta=GhA2OGFiMzg0NTEwMzIwMWM3IAAoATICZW46BGJlcmVAAEoAUAA%3D&checkin=2023-10-14&checkout=2023-10-15&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure" 5000 example@gmail.com


****************************************
To make the script run automatically:
****************************************
you can set a new scheduled task on your machine - https://www.backup4all.com/how-to-create-a-new-task-using-windows-task-scheduler-kb.html
                                           or create a new Linux VM and set a crone job with the correct parameters.
