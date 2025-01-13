from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.irctc.co.in/nget/train-search")
#driver.get("https://www.kickstarter.com/signup")

elem = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//input"))  # This is a dummy element
)

inputs = driver.find_elements(By.XPATH, '//input')
input_items = pd.DataFrame(columns=['item', 'position', 'role', 'label'])

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
    
    input_items.loc[len(input_items)] = [inp, position, inp.get_attribute('role'), label]

# print only the rows that have non empty label or role
print(input_items[(input_items['label'].notna()) | (input_items['role'].notna())])
input_items.to_csv('temp_input_items.csv', index=False)

# for rows that have a role but no label, look for labels in and around a 20px range
# for index, row in input_items.iterrows():
#     if pd.isna(row['label']) and row['role']:
#         x, y = row['position']['x'], row['position']['y']
#         try:
#             label_element = driver.find_element(
#                 By.XPATH, 
#                 f"//label[contains(@style, 'left: {x-20}px') and contains(@style, 'top: {y+20}px')]" +
#                 f" | //label[contains(@style, 'left: {x+20}px') and contains(@style, 'top: {y-20}px')]"
#             )
#             print("Label found: ", input_items.loc[index, 'item'], label_element.text)
#         except Exception as e:
#             print(f"Error occurred for item {input_items.loc[index, 'item']}: {e}")

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

for index, row in input_items.iterrows():
    if pd.isna(row['label']) and row['role']:  # No label and has a role
        x, y = row['position']['x'], row['position']['y']
        
        try:
            # Get all label elements on the page
            labels = driver.find_elements(By.XPATH, "//label")

            # Define the acceptable range for proximity
            proximity_range = 50  # alter as needed

            for label_element in labels:
                # Get the position of the label element
                label_rect = label_element.rect
                label_x, label_y = label_rect['x'], label_rect['y']

                # Check if label is within the proximity range of the input element
                if (abs(label_x - x) <= proximity_range and abs(label_y - y) <= proximity_range):
                    print(f"Label found for item at index {index}: {label_element.text}")
                    break
            else:
                print(f"No label found for item {input_items.loc[index, 'item']}")
        except Exception as e:
            print(f"Error occurred for item {input_items.loc[index, 'item']}: {e}")




# buttons = driver.find_elements(By.XPATH, '//button')
# for btn in buttons:
#     if btn.get_attribute('label') == 'Find Trains':
#         btn.click()

# MGR CHENNAI CTL - MAS (CHENNAI)
# KSR BENGALURU - SBCh
# 2/1/2025