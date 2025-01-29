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
driver.maximize_window()

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


#Next 
elem = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//a'))  # This is a dummy element
)


importelem = driver.find_element(By.XPATH, '//*[@id="uploadlpo"]')

importelem.click()

inputelem = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/table/tbody/tr/td[1]/div[2]')
inputelem.click()
driver.find_element(By.XPATH, '//*[text()="order.phpvt@gmail.com"]').click()

fileelem = driver.find_element(By.XPATH,'//input[@id="folder-select"]')
uploadfile = "D:\\WORK\\ELSEQ\\selenium-test\\elseq\\vaibhav\\"
fileelem.send_keys(uploadfile)

filebutton = driver.find_element(By.XPATH, '//button[@class="buttonmap"]')
filebutton.click()