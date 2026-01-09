from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

expected_product_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actual_product_list = []

driver = webdriver.Chrome()
#Implicit Wait applies to all lines of code
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, "input[class='search-keyword']").send_keys("ber")
time.sleep(5)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div[@class='product']")

for product in products:
    actual_product_list.append(product.find_element(By.CSS_SELECTOR, "h4[class='product-name']").text)
    product.find_element(By.CSS_SELECTOR, "div[class='product-action'] button").click()

assert expected_product_list == actual_product_list

item_count = driver.find_element(By.CSS_SELECTOR, "div[class='cart-info'] table tbody tr td:nth-child(3)").text
assert int(item_count) == len(products)

driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()
button_name = driver.find_element(By.CSS_SELECTOR, "div[class='action-block'] button").text
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

product_prices = driver.find_elements(By.CSS_SELECTOR, "#productCartTables tbody tr td:nth-child(5)")
total_amount = 0

for price in product_prices:
    total_amount += int(price.text)

assert total_amount == int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
driver.find_element(By.CSS_SELECTOR, "input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, "button[class='promoBtn']").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[class='promoInfo']")))

discounted_amount = float(driver.find_element(By.CSS_SELECTOR, "span[class='discountAmt']").text)
assert total_amount > discounted_amount

time.sleep(5)