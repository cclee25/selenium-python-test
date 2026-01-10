from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("QA Engr A added this print line.")

#Test data json file location
file_loc = r"C:\Selenium_Python\data\shop_data.json"

with open(file_loc) as file:
    testing_data = json.load(file)
    test_data = testing_data["data"]

@pytest.mark.parametrize("test_data", test_data)
def test_e2e(browser_instance, test_data):
    driver = browser_instance
    login_page = LoginPage(driver)
    login_page.login(test_data["username"], test_data["password"])
    time.sleep(3)
    product_selection = ProductSelection(driver, test_data["product_name"])
    product_selection.select_product(test_data["product_name"])
    product_selection.go_to_cart(test_data["product_name"])
    product_checkout = Checkout_Item(driver)
    product_checkout.checkout(test_data["country_string"], test_data["selected_country"])
    product_checkout.validate_purchase()
    print("Edit then commit right in Github")
    print("Added by QA Engr B")
    print("Added by QA Engr A. Created new branch 'develop'")
    print("Added by QA Engr B. Pushed updates to branch 'develop'")
    print("Added by QA Engr A. Pushed updates to branch 'develop' at 19:33")
    time.sleep(5)


@pytest.mark.parametrize("test_data", test_data)
def test_get_title(browser_instance, test_data):
    driver = browser_instance
    login_page = LoginPage(driver)
    assert login_page.get_title() == "LoginPage Practise | Rahul Shetty Academy"
    login_page.login(test_data["username"], test_data["password"])
    time.sleep(3)
    shop_page = ProductSelection(driver, test_data["product_name"])
    assert shop_page.get_title() == "ProtoCommerce"
