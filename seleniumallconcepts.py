from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.youtube.com/watch?v=Tf2kBtUYemY")
driver.implicitly_wait(30)