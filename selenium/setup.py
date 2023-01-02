
from selenium import webdriver

chrome_driver_path="/Users/ferdakesik/Desktop/chromedriver"

driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://google.com")