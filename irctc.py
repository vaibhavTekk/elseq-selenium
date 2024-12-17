from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


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

elements = driver.find_elements("xpath", "//*[contains(@class, 'train-heading')]")
print(elements)
# Loop through and interact with each element
for element in elements:
    print(element.text)
