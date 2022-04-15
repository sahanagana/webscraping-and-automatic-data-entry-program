#import cool selenium stuff
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#setup variables that can be changed in program?
userString = 'user'
passString= 'pass'

link = 'put da link here'

#setup browser
browser = webdriver.Chrome()
browser.get(link)

# fill in username and hit the next button
username = browser.find_element_by_id('Email')
username.send_keys(userString)
nextButton = browser.find_element_by_id('next')
nextButton.click()

# wait for transition then continue to fill items
password = WebDriverWait(browser, 10).until(
EC.presence_of_element_located((By.ID, 'Passwd')))
password.send_keys(passString)
 
signInButton = browser.find_element_by_id('signIn')
signInButton.click()