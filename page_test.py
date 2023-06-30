from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pyautogui
import time
import keyboard
from selenium.webdriver.edge.options import Options
import os
from datetime import datetime

# config
driver = webdriver.Edge()
link_locator = 3
flag = True
locator_flag = True
paper_count = 1
file_count = 1
page_count = 201
directory = "/Users/kaungmyatkyaw/Desktop/downloaded"

# Navigate to a webpage
driver.get("https://www.scopus.com/results/results.uri?sort=cp-f&src=s&st1=Computer+Vision&nlo=&nlr=&nls=&sid=03d8e712505d7771828163aca0d0b5a6&sot=b&sdt=cl&cluster=scopubyr%2c%222023%22%2ct%2c%222022%22%2ct%2c%222021%22%2ct%2bscosubtype%2c%22cp%22%2ct%2bscosubjabbr%2c%22COMP%22%2ct%2bscoexactkeywords%2c%22Computer+Vision%22%2ct%2bscoexactsrctitle%2c%22Proceedings+Of+The+IEEE+Computer+Society+Conference+On+Computer+Vision+And+Pattern+Recognition%22%2ct%2c%22Proceedings+Of+The+IEEE+International+Conference+On+Computer+Vision%22%2ct%2c%22IEEE+Computer+Society+Conference+On+Computer+Vision+And+Pattern+Recognition+Workshops%22%2ct%2c%22Proceedings+IEEE+International+Conference+On+Multimedia+And+Expo%22%2ct%2c%22Proceedings+2023+IEEE+Winter+Conference+On+Applications+Of+Computer+Vision+Wacv+2023%22%2ct&sl=30&s=TITLE-ABS-KEY%28Computer+Vision%29&origin=resultslist&zone=leftSideBar&editSaveSearch=&txGid=8cb2ff633744fa5c778c1f159571807a")
driver.maximize_window()

# closing the popup
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='pendo-close-guide-2e51a252']")))
element = driver.find_element("xpath", "//*[@id='pendo-close-guide-2e51a252']")
element.click()

# setting the offset to 200
element = driver.find_element("xpath", "//*[@id='container']/micro-ui/document-search-results-page/div[1]/section[2]/div/div[2]/div/div[2]/div/els-results-layout/els-paginator/nav/els-select/div/label/select")
element.click()
select_element = Select(driver.find_element("xpath", "//*[@id='container']/micro-ui/document-search-results-page/div[1]/section[2]/div/div[2]/div/div[2]/div/els-results-layout/els-paginator/nav/els-select/div/label/select"))
select_element.select_by_visible_text("200 results")
time.sleep(3)

while (page_count <= 2000):
    driver.get(f"https://www.scopus.com/results/results.uri?sort=plf-f&src=s&st1=computer+vision&nlo=&nlr=&nls=&sid=d3c99617bac5f2fd05366663b18ba5e1&sot=b&sdt=cl&cluster=scoexactsrctitle%2c%22Proceedings+Of+The+IEEE+Computer+Society+Conference+On+Computer+Vision+And+Pattern+Recognition%22%2ct%2c%22Proceedings+Of+The+IEEE+International+Conference+On+Computer+Vision%22%2ct%2c%22IEEE+Computer+Society+Conference+On+Computer+Vision+And+Pattern+Recognition+Workshops%22%2ct%2bscopubyr%2c%222022%22%2ct%2c%222021%22%2ct%2bscosubtype%2c%22cp%22%2ct%2bscosubjabbr%2c%22COMP%22%2ct%2bscolang%2c%22English%22%2ct&sl=30&s=TITLE-ABS-KEY%28computer+vision%29&cl=t&offset={page_count}&origin=resultslist&ss=plf-f&ws=r-f&ps=r-f&cs=r-f&cc=10&txGid=7f8dac5f4b99a6ddde3347e24c937b1a")
    time.sleep(5)
    driver.save_screenshot("screenshot" + str(page_count) + ".png")
    page_count += 200


   