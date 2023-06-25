# importing the modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.google.com/")
search_bar = driver.find_element("id", "APjFqb")
search_bar.send_keys("kfc")
search_bar.send_keys(Keys.ENTER)
kfc_link = driver.find_element(By.XPATH, "//a[@href='https://www.kfc.co.il/']")
kfc_link.click()
eles = driver.find_element(By.XPATH, "//a[@href='https://www.kfc.co.il/branches/']")
eles.click()
key = driver.find_element(By.CLASS_NAME, "selection")
key.click()
input("Press any key to close...")
driver.close()
