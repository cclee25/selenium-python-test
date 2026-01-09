from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
print(driver.current_url)

# Validating field names
name_label = driver.find_element(By.XPATH, "//label[normalize-space()='Name']" )
assert name_label.text == "Name"

# Interacting with elements
driver.find_element(By.NAME, "name").send_keys("QA Test")
driver.find_element(By.CSS_SELECTOR, "input[name = 'email']").send_keys("qatest123@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
driver.find_element(By.XPATH, "//input[@value='option2']").click()
driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()

time.sleep(10)
