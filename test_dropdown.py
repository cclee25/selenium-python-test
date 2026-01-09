from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.XPATH, "//div[@id='select-class-example']/fieldset/input[@id='autocomplete']").send_keys("Japan")

time.sleep(3)