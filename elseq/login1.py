from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

start = time.time()
driver.get("http://ec2-52-32-108-4.us-west-2.compute.amazonaws.com:8082/")
stop = time.time()

print(f"Page load time: {stop-start}")
elem = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//input"))  # This is a dummy element
)

inputs = driver.find_elements(By.XPATH,'//input')
for inp in inputs:
    if inp.get_attribute("id") == "email":
        inp.send_keys("tekkalurvaibhav@gmail.com")
    elif inp.get_attribute("id") == "password":
        inp.send_keys("vaibhav123")

buttons = driver.find_elements(By.XPATH, '//button')
for btn in buttons:
    if btn.get_attribute("type") == "submit":
        btn.click()

start = time.time()
elem = WebDriverWait(driver, 30).until(
EC.presence_of_element_located((By.XPATH, '//*[@id="BasicNavDropdown"]')) #This is a dummy element
)
stop = time.time()

print(f"Login time: {stop-start}")
elem = driver.find_element(By.XPATH, '//*[@id="BasicNavDropdown"]')
if elem.text == "tekkalurvaibhav@gmail.com":
    print("Login successful")

# Next 
elements_dict = {}
interactive_elements = driver.find_elements(By.XPATH, '//a | //button | //input | //select | //textarea')
for index, element in enumerate(interactive_elements):
    # print(f"Tag: {element.tag_name}, Text: {element.text}, Attributes: {element.get_attribute('outerHTML')}")
    elements_dict[index] = {
            "tag": element.tag_name,
            "text": element.text,
            "attributes": element.get_attribute('outerHTML')
        }

for key, value in elements_dict.items():
    print(f"Element {key}: {value['text']}")