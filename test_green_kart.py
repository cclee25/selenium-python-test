from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

expected_product_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actual_product_list = []

driver = webdriver.Chrome()
#Implicit Wait applies to all lines of code
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, "input[class='search-keyword']").send_keys("ber")
time.sleep(5)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")

for product in products:
    product_name = product.find_element(By.CSS_SELECTOR, ".product-name").text
    actual_product_list.append(product_name)
    product.find_element(By.CSS_SELECTOR, "div button[type='button']").click()
assert expected_product_list == actual_product_list

driver.find_element(By.CSS_SELECTOR, ".cart-icon img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
##Explicit Wait
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
prices = driver.find_elements(By.CSS_SELECTOR, "td:nth-child(5) .amount")
calculated_sum = 0

for price in prices:
    calculated_sum += float(price.text)

total_amount = float(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert calculated_sum == total_amount

discounted_amount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert calculated_sum > discounted_amount

assert driver.find_element(By.CSS_SELECTOR, ".promoInfo").text == "Code applied ..!"

action = ActionChains(driver)

time.sleep(5)

print("QA Engr B made this update.")

