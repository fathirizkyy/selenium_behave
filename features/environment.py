from selenium import webdriver
import time


def before_scenario(context,driver):
    context.driver=webdriver.Firefox()
    time.sleep(2)
    
    
def after_scenario(context,driver):
    context.driver.quit()