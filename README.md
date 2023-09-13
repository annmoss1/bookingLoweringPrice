# Booking Lowering Price Script

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
    3) Add a scheduled task in Windows \ crone job in Linux that will run the script once a day. You can do it on your local machine, or on a VM.
            to configure a new scheduled task in Windows that runs this script every day-
                a. Open Task Scheduler
                b. Press under Actions 'Create Task'
                c. In the general tab: 
                            give it a name, description. choose 'Run whether user is logged on or not'
                d. In the triggers tab:
                    
