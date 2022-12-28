import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
from PIL import Image

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)
url = "https://inspirobot.me/"
driver.get(url)

for i in range(1):
    button = driver.find_element(By.CLASS_NAME, "btn-text")
    button.click()
    time.sleep(2)
    image = driver.find_element(By.CLASS_NAME, "generated-image").get_attribute("src")
    img = Image.open(requests.get(image, stream=True).raw)
    img.save('photos/AIquote1-'+ str(i) +'.png')
    time.sleep(1)


