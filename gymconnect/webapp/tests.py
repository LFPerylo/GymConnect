from django.test import TestCase, LiveServerTestCase
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Chrome()

driver.get("https://www.google.com")
pesquisa = driver

time.sleep(5)


