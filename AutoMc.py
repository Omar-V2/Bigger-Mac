from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def click_next(): # helper function to click the next button on the webpage
    driver.find_element_by_id("NextButton").click()

initial_button_xpath = "/html/body/div[1]/div[3]/div[2]/form/div/div[1]/div[2]/div[1]/span/span"

driver = webdriver.Chrome()
driver.get("https://mcdfoodforthoughts.com/")
click_next()
driver.find_element_by_xpath(initial_button_xpath).click() # Do you have your receipt available


# McDonalds site is poorly designed, a loophole is to continually press the next button 
# until we reach a page with no next button which is the page which contains the code
while True:
    try:
        click_next()
    except NoSuchElementException:
        break

# Parse the HTML containing the code and print as an integer
code = driver.find_element_by_class_name("ValCode")
code = code.get_attribute('innerHTML')
code = code.split(" ")
code = int(code[-1])
print(code)


