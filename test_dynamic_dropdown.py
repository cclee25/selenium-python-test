from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise")

#Clicking on a dynamic dropdown menu
driver.find_element(By.ID, "autosuggest").send_keys("Ja")
time.sleep(3)
countries = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item a")
for country in countries:
    if country.text == "Japan":
        country.click()
        break

#Check for selected option
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "Japan"

time.sleep(3)