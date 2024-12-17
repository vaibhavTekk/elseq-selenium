from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://irctc.co.in/nget/train-search")

origin = driver.find_element(By.XPATH,'//*[@id="origin"]/span/input')
origin.send_keys("MGR CHENNAI CTL - MAS (CHENNAI)")


dest = driver.find_element(By.XPATH,'//*[@id="destination"]/span/input')
dest.send_keys("DELHI - DLI (NEW DELHI)")
dest.send_keys(Keys.TAB)

date_field = driver.find_element("xpath", '//*[@id="jDate"]/span/input')
date_field.send_keys("20/12/2024")
dest.send_keys(Keys.TAB)

# dropdown = driver.find_element(By.XPATH,'//*[@id="journeyClass"]/div/div[1]/input')
# dropdown.click()

# option = driver.find_element("xpath", "//li[@class='p-dropdown-item' and text()='AC First Class (1A)']")
# option.click()
# form = driver.find_element(By.XPATH,'//*[@id="divMain"]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form')
# form.submit()
