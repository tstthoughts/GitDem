

import driver as driver
from selenium import webdriver

#Coding Question: Write a program to
# log on to yahoo.com homepage and list all the web addresses for all the links on the header
driver = webdriver.Chrome("C:\\Users\\sathy\\eclipse-workspace\\chromedriver.exe")

driver.implicitly_wait(2)
driver.maximize_window()
driver.get('https://in.yahoo.com/')
inputElements = driver.find_elements_by_xpath("//*[@id='header-nav-bar']/li/a")
for inputElement in inputElements :
    print(inputElement.get_attribute('href'))
    #.find_element_by_name("q")
driver.quit()

