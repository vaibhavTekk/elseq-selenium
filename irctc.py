from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://irctc.co.in/nget/train-search")
origin = driver.find_element(By.XPATH,'//*[@id="origin"]/span/input')
origin.send_keys("MGR CHENNAI CTL - MAS (CHENNAI)")
origin.send_keys(Keys.TAB)

dest = driver.find_element(By.XPATH,'//*[@id="destination"]/span/input')
dest.send_keys("DELHI - DLI (NEW DELHI)")
dest.send_keys(Keys.TAB)

date_field = driver.find_element(By.XPATH, '//*[@id="jDate"]/span/input')
date_field.clear()
date_field.send_keys(Keys.CONTROL + 'a')
date_field.send_keys(Keys.BACKSPACE)
date_field.send_keys("20/12/2024")
date_field.send_keys(Keys.TAB)
dest.click()

dropdown = driver.find_element(By.XPATH,'//*[@id="journeyClass"]')
dropdown.click()
option = driver.find_element(By.XPATH, '//*[@id="journeyClass"]//p-dropdownitem[.//span[text()=\'All Classes\']]')
option.click()

form = driver.find_element(By.XPATH,'//*[@id="divMain"]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form')
form.submit()
# //*[@id="divMain"]/div/app-train-list//app-train-avl-enq

elem = WebDriverWait(driver, 30).until(
EC.presence_of_element_located((By.XPATH, "//app-train-list//app-train-avl-enq")) #This is a dummy element
)

elements = driver.find_elements(By.XPATH, "//app-train-list//app-train-avl-enq")
# print(elements)
# Loop through and interact with each element
for element in elements:
    el = element.find_elements(By.TAG_NAME, "strong")
    [print(e.text) for e in el]


# QFZrM9t7QUzigWD
# 9174287232
