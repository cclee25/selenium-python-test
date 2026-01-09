from argparse import Action
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise")
driver.implicitly_wait(5)

driver.find_element(By.CLASS_NAME, "blinkingText").click()

#Open child window
windows_opened = driver.window_handles
driver.switch_to.window(windows_opened[1])
email = driver.find_element(By.XPATH, "//div[@class='col-md-8']/p[2]/strong/a").text

#Switch to main window
driver.switch_to.window(windows_opened[0])
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys("12345")
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "signInBtn").click()

#Get error notification
wait = WebDriverWait(driver, 10)
error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger.col-md-12")))
print("ERROR_NOTIF:", error.text)

time.sleep(3)   