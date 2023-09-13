# Booking Lowering Price Script

With this script, you can follow a specific hotel search in booking.com and get an email if the price is decreased.

************************************************************************************************************************************************************************************
booking_selenium is the correct script, it is working with selenium.

booking_network is another script that was working partially, due to lakes with booking.com API (without mail support yet- it is not ready), keeping it in case the API changes. 
************************************************************************************************************************************************************************************


***********************************************************************
How to run:
***********************************************************************

    1) Clone
    2) Edit the searches.json. For each hotel you want to follow, enter the following fields for each search you want to add (use the attached template in searches.json):
            url: go to booking.com, fill in the search details + filters that you want to follow, press search and copy the URL to the JSON.
            current_price: The current\ starting price is in ILS. When the script detects a lower price, it will send you an email.
            my_mail: your email address
            
    3) To run manually just run the booking_selenium script.
        To add scheduled runs follow the following instructions:
        Add a scheduled task in Windows \ crone job in Linux that will run the script once a day. You can do it on your local machine, or on a VM.
            To configure a new scheduled task in Windows that runs this script every day:
                a. Open Task Scheduler
                b. Press under Actions 'Create Task'
                c. In the general tab: 
                            give it a name, and description. choose 'Run whether user is logged on or not'
                d. In the triggers tab:
                            press new and add a trigger (for example Daily) and press ok.
                e. In the Actions tab:
                            press new 
                            - In Action choose: Start a program. 
                            - In Program/script put the absolute path to the python.exe (for example C:\Users\user\AppData\Local\Programs\Python\Python38-32\python.exe)
                            - In Add arguments put the absolute path to the script booking_seleniym.py between "" (for example "c:/Users/user/OneDrive - Microsoft/user/github/bookingLoweringPrice/booking_selenium.py")
                            - In Start in put the absolute path of the project (for example C:\Users\user\OneDrive - Microsoft\user\github\bookingLoweringPrice)
                f. In the Conditions path disable everything
                g. In the settings tab mark 'Run task as soon as possible after a scheduled start is missed'


***************************************************************************
* I suggest triggering it once manually with a high price in the json to verify that the trigger is working and that you seeing the mail (check also spam).

![image](https://github.com/annmoss1/bookingLoweringPrice/assets/122597424/57e33464-e82e-4ca0-bb7e-8452af3044e8)
***************************************************************************
