# Ref: http://chromedriver.chromium.org/getting-started
import time

from selenium import webdriver
import selenium.webdriver.chrome.service as service

service = service.Service('/usr/bin/chromedriver')
service.start()
capabilities = {'chrome.binary': '/opt/google/chrome/chrome'}
driver = webdriver.Remote(service.service_url, capabilities)
driver.get('http://www.google.com/xhtml')
time.sleep(5)
driver.quit()

