# Find Mr. Ross's Discord
from selenium.webdriver import Keys

rossusername = "grandadmiralcrunch"

from dotenv import load_dotenv
load_dotenv()
import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By

username = os.getenv("username")
vpn = False
password = os.getenv("password")


def clear():
    os.system("clear")
def taskit(task):
    clear()
    print("TASK: "+task)
def timer(thetime, task):
    for i in range(0, thetime):
        taskit(task)
        print("00:"+str(thetime-i)+" Left.")
        time.sleep(1)
        clear()

taskit("Launching a browser: Chrome")

driver = webdriver.Chrome("chromedriver")
if vpn:
    driver.get("https://chrome.google.com/webstore/detail/zenmate-free-vpn%E2%80%93best-vpn/fdcgdnkidjaadafnichfpabhfomcebme?hl=en")
    timer(30, "Please enable a ZenMate VPN. You have 30 seconds.")

timer(2, "Waiting for Discord to load. ")
taskit("Waiting for Discord to load. ")
driver.get("https://discord.com/login")
taskit("Inputing Credentials ")

driver.find_element_by_name("email").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
taskit("Logging In...")
driver.find_element_by_name("email").send_keys(Keys.RETURN)
if vpn:
    timer(60, "Verifying Captcha / Waiting for Discord to Load ")
timer(10, "Final Stretch")

taskit("Sending a Friend Request")
print(driver.find_elements_by_class_name("themed-2-lozF"))
#driver.find_elements_by_class_name("themed-2-lozF")[5].click()
driver.find_elements_by_class_name("themed-2-lozF")[4].click()
timer(5, "Waiting for Discord to load Friend RQ")
names = []
for i in range(1, 9999):
    i = str(i)
    i = (4-len(i))*"0"+i
    # names.append(rossusername+"#"+i)
    #driver.find_element_by_id("uid_16").send_keys(rossusername+"#"+i)
    driver.find_element_by_id("uid_19").send_keys(rossusername+"#"+i)
    timer(1, "Preparing to Click")
    driver.find_elements_by_class_name("button-f2h6uQ")[3].click()
    # if (len(driver.find_element_by_class_name("but ton-f2h6uQ"))>4):
    #     names.append("Failure -> "+rossusername+"#"+i)
    #     driver.find_element_by_class_name("button-f2h6uQ")[4].click()
    # else:
    #     names.append("Pass -> "+rossusername+"#"+i)
    #timer(10, "Waiting for User to Observe")
    try:
        names.append("Failure -> "+rossusername+"#"+i)
    #     driver.find_element_by_class_name("button-f2h6uQ")[4].click()
    except:
        names.append("Pass -> "+rossusername+"#"+i)
for i in names:
    print(i)