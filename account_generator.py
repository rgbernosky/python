from selenium import webdriver
import random

# from https://pythonspot.com/selenium-click-button/
'''options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"'''
browser = webdriver.Chrome()
# End of copy from pythonspot

browser.get('https://jsouapphub.azurewebsites.net/users/jcloudlogin')

def loadTime(secs):
    browser.implicitly_wait(secs) #wait five seconds for pages to load

loadTime(10)

#Create new account button
browser.find_element_by_xpath('/html/body/main/div[1]/div/form/div/div/div/div/div[3]/a').click()




# Field Inputs for Account Creation
# Username (id = unameNew) 
newPw = browser.find_element_by_id('unameNew')
newPw.send_keys('sitec')

#First Name (id = fName)
newPw = browser.find_element_by_id('fName')
newPw.send_keys('sitec')

#Last Name (id = lName)
newPw = browser.find_element_by_id('lName')
newPw.send_keys('sitec')

#Enter Password (id = pwdNew)
newPw = browser.find_element_by_id('pwdNew')
newPw.send_keys('sitec')

#Confirm Password Entry (id = confirmPwd)
newPwC = browser.find_element_by_id('confirmPwd')
newPwC.send_keys('sitec')



# Submit information for account creation
#submit_button = browser.find_elements_by_xpath('//*[@id="NewAccountModal"]/div/div/div[3]/button')
#submit_button.click()