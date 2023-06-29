from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import keyboard
from selenium.webdriver.edge.options import Options
import os
from datetime import datetime

edge_options = Options()
edge_options.add_argument("--disable-notifications")  # Optional: Disable notifications

prefs = {
    "download.default_directory": "/Users/kaungmyatkyaw/Desktop/downloaded",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
}

directory = "/Users/kaungmyatkyaw/Desktop/downloaded"

edge_options.add_experimental_option("prefs", prefs)

driver = webdriver.Edge(options=edge_options)

# Navigate to a webpage
driver.get("https://www.scopus.com/results/results.uri?sort=cp-f&src=s&st1=Computer+Vision&nlo=&nlr=&nls=&sid=03d8e712505d7771828163aca0d0b5a6&sot=b&sdt=cl&cluster=scopubyr%2c%222023%22%2ct%2c%222022%22%2ct%2c%222021%22%2ct%2bscosubtype%2c%22cp%22%2ct%2bscosubjabbr%2c%22COMP%22%2ct%2bscoexactkeywords%2c%22Computer+Vision%22%2ct%2bscoexactsrctitle%2c%22Proceedings+Of+The+IEEE+Computer+Society+Conference+On+Computer+Vision+And+Pattern+Recognition%22%2ct%2c%22Proceedings+Of+The+IEEE+International+Conference+On+Computer+Vision%22%2ct%2c%22IEEE+Computer+Society+Conference+On+Computer+Vision+And+Pattern+Recognition+Workshops%22%2ct%2c%22Proceedings+IEEE+International+Conference+On+Multimedia+And+Expo%22%2ct%2c%22Proceedings+2023+IEEE+Winter+Conference+On+Applications+Of+Computer+Vision+Wacv+2023%22%2ct&sl=30&s=TITLE-ABS-KEY%28Computer+Vision%29&origin=resultslist&zone=leftSideBar&editSaveSearch=&txGid=8cb2ff633744fa5c778c1f159571807a")
temp = 3
i = 0

driver.maximize_window()
while True: 

    if(i == 10):
        time.sleep(10)
        # Get the list of files in the directory
        files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

        # Sort the files based on their creation time
        files.sort(key=lambda x: os.path.getctime(x))
        # Iterate over the files and assign an index
        for index, filepath in enumerate(files, start=0):
            # Get the filename from the file path
            filename = os.path.basename(filepath)

            # Get the timestamp of the file's creation
            timestamp = os.path.getctime(filepath)

            # Convert the timestamp to a datetime object
            dt = datetime.fromtimestamp(timestamp)

            # Format the datetime as desired for the new filename
            new_filename = f"{index}.pdf"

            # Rename the file
            new_filepath = os.path.join(directory, new_filename)
            os.rename(filepath, new_filepath)
        file_path = "/Users/kaungmyatkyaw/Desktop/downloaded/0.pdf"
        os.remove(file_path)
        i = 0

    # Find the element
    if(temp == 33):
        temp = 32
    if(temp == 3):
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='pendo-close-guide-2e51a252']")))
        element = driver.find_element("xpath", "//*[@id='pendo-close-guide-2e51a252']")
        element.click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, f"//*[@id='container']/micro-ui/document-search-results-page/div[1]/section[2]/div/div[2]/div/div[2]/div/els-results-layout/div[1]/table/tbody/tr[{temp}]/td[2]/els-collapsible-panel-v2/div/div/div/div/a/span[1]")))
    element = driver.find_element("xpath", f"//*[@id='container']/micro-ui/document-search-results-page/div[1]/section[2]/div/div[2]/div/div[2]/div/els-results-layout/div[1]/table/tbody/tr[{temp}]/td[2]/els-collapsible-panel-v2/div/div/div/div/a/span[1]")
    element.click()

    # Switch to the newly opened tab
    driver.switch_to.window(driver.window_handles[-1])

    # Wait until the website isc completely loaded
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "PDF")))
    element = driver.find_element(By.LINK_TEXT, "PDF")
    element.click()

    # download
    time.sleep(2)

    pyautogui.moveTo(50, 300)
    # Perform the right-click action
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(3)
    if(temp == 3):
        time.sleep(10)
    pyautogui.press('enter')
    
    # close the tab
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print(temp)
    temp += 3
    i += 1
   