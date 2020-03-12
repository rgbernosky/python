from selenium import webdriver
searchItem = input('What do you want to search for?')
def loadTime(secs):
    browser.implicitly_wait(secs) #wait five seconds for pages to load
browser = webdriver.Chrome()
browser.get('https:/duckduckgo.com')

#loadTime(5)

userElem = browser.find_element_by_id('search_form_input_homepage')
userElem.send_keys(searchItem)
userElem.submit()

loadTime(5)
#browser.implicitly_wait(10) #wait 10 seconds for page to load

browser.find_element_by_id('r1-0').click()
