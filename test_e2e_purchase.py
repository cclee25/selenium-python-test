from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)

#Select a product
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.CSS_SELECTOR, ".col-lg-3.col-md-6.mb-3")
for product in products:
    if product.find_element(By.CSS_SELECTOR, ".card.h-100 .card-body .card-title").text.strip() == "Blackberry":
        product.find_element(By.CSS_SELECTOR, ".btn.btn-info").click()
        break

#Go to cart
driver.find_element(By.XPATH, "//div[@id='navbarResponsive']/ul/li/a").click()
product_name = driver.find_element(By.XPATH, "//div[@class='media-body']/h4[@class='media-heading']/a[normalize-space(text())='Blackberry']")
assert product_name.text == "Blackberry"

#Go to checkout page
driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
driver.find_element(By.ID, "country").send_keys("Un")

wait = WebDriverWait(driver, 10)
countries = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class='suggestions'] ul li")))

for country in countries:
    if country.text.strip() == 'United States of America':
        country.click()
        break

driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()
notif = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text.strip()
assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in notif

time.sleep(5)