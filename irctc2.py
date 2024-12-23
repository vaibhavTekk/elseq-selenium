from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.irctc.co.in/nget/train-search")

elem = WebDriverWait(driver, 30).until(
EC.presence_of_element_located((By.XPATH, "//input")) #This is a dummy element
)
inputs = driver.find_elements(By.XPATH,'//input')
for inp in inputs:
    parent, gparent = inp.find_element(By.XPATH,'..'), inp.find_element(By.XPATH, '../..')
    if inp.get_attribute('aria-label') == None and gparent.get_attribute('aria-label') == None:
        continue
    else:
        print(inp.aria_role, inp.get_attribute('aria-label') or gparent.get_attribute('aria-label'))
        if (inp.aria_role == 'searchbox'):
            userinp = input()
            inp.send_keys(userinp)
            inp.send_keys(Keys.TAB)
        if (inp.aria_role == 'textbox'):
            userinp = input()            
            inp.send_keys(Keys.CONTROL + 'a')
            inp.send_keys(Keys.BACKSPACE)
            inp.send_keys(userinp)
            inp.send_keys(Keys.TAB)
        if (inp.aria_role == 'checkbox'):
            print(inp.is_selected())
            userinp = input('Y/N:')
            if (userinp == 'Y') and not inp.is_selected():
                parent.click()
            elif userinp == 'N' and inp.is_selected():
                parent.click()
        
# form = driver.find_element(By.XPATH,'//*[@id="divMain"]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form')
# form.submit()

#MGR CHENNAI CTL - MAS (CHENNAI)
#KSR BENGALURU - SBC
#24/12/2024