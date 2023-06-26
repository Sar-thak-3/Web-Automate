from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
load_dotenv() 

EMAILFIELD = (By.ID,"i0116")
PASSWORD = (By.ID,"i0118")
NEXTBUTTON = (By.ID,"idSIButton9")
SEARCHBUTTON = (By.XPATH,"/html/body/div/div/main/div[2]/header/div/form/input")
BUTTON = (By.XPATH,"/html/body/div/div/main/div[2]/header/div/form/button")
BUTTON_AFTER_FIRST_SEARCH = (By.XPATH,"/html/body/div/div/main/div[2]/div/div[1]/form/button")
NAME = (By.XPATH,"/html/body/div/div/main/div[2]/div/div[2]/div/div/div[2]/header/div[1]/div[4]")
NAME2 = (By.XPATH,"/html/body/div/div/main/div[2]/div/div[2]/div/div/div[2]/header/div[1]/div[3]")
AFTER_FIRST_SEARCH = (By.XPATH,"/html/body/div/div/main/div[2]/div/div[1]/form/input")
ADDRESS = (By.XPATH,"/html/body/div/div/main/div[2]/div/div[2]/div/div/div[2]/div[2]/a[2]/div/div[2]")

driver = webdriver.Chrome()
driver.get("""https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=code&respone_mode=query&redirect_uri=https%3A%2F%2Fwww.truecaller.com%2Fauth%2Fmicrosoft%2Fcallback&state=asia-south1%7Cin%7Cfalse%7Cweb%7Chttps%3A%2F%2Fwww.truecaller.com&client_id=000000004818BA61&scope=openid+profile+email+User.Read&sso_reload=true""")
# WebDriverWait(driver,10).until(EC.element_to_be_clickable(SIGNINBUTTON)).click()
# WebDriverWait(driver,10).until(EC.element_to_be_clickable(MICROSOFTBUTTON)).click()
WebDriverWait(driver,10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys(os.getenv("MICROSOFT_EMAIL"))
WebDriverWait(driver,10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
WebDriverWait(driver,10).until(EC.element_to_be_clickable(PASSWORD)).send_keys(os.getenv("MICROSOFT_PASSWORD"))
WebDriverWait(driver,10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
WebDriverWait(driver,10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
for i in range(7000000000,7000000002):
    if(i==7000000000):
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(SEARCHBUTTON)).send_keys(i)
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(BUTTON)).click()
        print(WebDriverWait(driver,20).until(EC.visibility_of_element_located(NAME)).text)
        try:
            print(WebDriverWait(driver,10).until(EC.visibility_of_element_located(ADDRESS)).text)
        except:
            pass
    else:
        inp = WebDriverWait(driver,10).until(EC.element_to_be_clickable(AFTER_FIRST_SEARCH))
        inp.click()
        inp.send_keys(Keys.CONTROL + "a")
        inp.send_keys(Keys.DELETE)
        inp.send_keys(i)
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(BUTTON_AFTER_FIRST_SEARCH)).click()
        # print(WebDriverWait(driver,20).until(EC.visibility_of_element_located(NAME)).text) 
        print(WebDriverWait(driver,10).until(EC.visibility_of_element_located(NAME2)).text)
        try:
            print(WebDriverWait(driver,10).until(EC.visibility_of_element_located(ADDRESS)).text)
        except:
            pass