from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import re
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radio_buttons = driver.find_elements(By.CSS_SELECTOR, "input[class='radioButton']")

for rb in radio_buttons:
    if rb.get_attribute("value") == "radio2":
        rb.click()
        assert rb.is_selected()
        break

checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

for checkbox in checkboxes:
    if checkbox.get_attribute("id") == "checkBoxOption2":
        checkbox.click()
        assert checkbox.is_selected()
        break

#Checking if element is displayed or not
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

#Manipulating alert box
name = 'QA Test'
driver.find_element(By.CSS_SELECTOR, "input[name='enter-name']").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
alert = driver.switch_to.alert
assert alert.text == f"Hello {name}, share this practice page and share your knowledge"
alert.accept()

time.sleep(3)