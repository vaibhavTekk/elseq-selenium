from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.irctc.co.in/nget/train-search")

elem = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//input"))  # This is a dummy element
)

inputs = driver.find_elements(By.XPATH, '//input')
input_items = []

for inp in inputs:
    position = inp.location
    x, y = position['x'], position['y']
    
    # Attempt to find a label element near the input element
    label_element = None
    try:
        label_element = driver.find_element(By.XPATH, f"//label[contains(@style, 'left: {x-10}px') and contains(@style, 'top: {y-10}px')]")
    except:
        pass
    
    label = label_element.text if label_element else inp.get_attribute('aria-label')
    
    input_items.append({
        "item": inp,
        "position": position,
        "role": inp.get_attribute('aria-role'),
        "label": label
    })

for i in input_items:
    print(i)

buttons = driver.find_elements(By.XPATH, '//button')
for btn in buttons:
    if btn.get_attribute('label') == 'Find Trains':
        btn.click()

# MGR CHENNAI CTL - MAS (CHENNAI)
# KSR BENGALURU - SBCh
# 2/1/2025