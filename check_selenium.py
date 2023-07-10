from selenium import webdriver
from selenium.webdriver import ActionChains , DesiredCapabilities
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation",'enable-logging'])
options.add_experimental_option("detach",True) #fix  Automatically & Immediately After Test Without Calling Quit or Close
# options.add_argument('--allow-running-insecure-content')
# options.add_argument('--ignore-certificate-errors')
# 
# desired_capabilities = DesiredCapabilities().CHROME.copy()
# desired_capabilities['acceptInsureCerts'] = True

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) 
driver.get("https://www.shopee.co.th/")

thai_button = driver.find_element("xpath",'//*[@id="modal"]/div[1]/div[1]/div/div[3]/div[1]/button')
thai_button.click()

# challenge with shadow-root
close_button = driver.execute_script('return document.querySelector("shopee-banner-popup-stateful").shadowRoot.querySelector("div.shopee-popup__close-btn")')
close_button.click()
print(close_button)

# search = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[2]/div/div[1]/div/form/div/input')
search = driver.find_element(By.XPATH,'//*[@id="main"]/div/header/div[2]/div/div[1]/div[1]/div/form/input') #ให้ คัดลอก xpath ไม่ใช่ full xpath
search.send_keys('โต๊ะปรับระดับไฟฟ้า')
print(search)

from selenium.webdriver.common.keys import Keys
search.send_keys(Keys.ENTER)