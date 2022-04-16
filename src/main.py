# Find Mr. Ross's Discord

rossusername = "grandadmiralcrunch"

from dotenv import load_dotenv
load_dotenv()
import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By

username = os.getenv("username")
password = os.getenv("password")



driver = webdriver.Chrome("chromedriver")
print("Add the ZenMate extension and turn it on. You have 120 seconds")
driver.get("https://chrome.google.com/webstore/detail/zenmate-free-vpn%E2%80%93best-vpn/fdcgdnkidjaadafnichfpabhfomcebme?hl=en")
for i in range(0, 60):
    print(str(60-i)+" seconds left.")
    time.sleep(1)
# try:
#     #d#river.close()
# except:
#     print("closing failed :/")
driver.get("https://discord.com/login")

time.sleep(60)

driver.find_element_by_name("email").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
names = []
for i in range(1, 9999):
    i = str(i)
    i = (4-len(i))*"0"+i
    names.append(rossusername+"#"+i)
for i in names:
    print(i)