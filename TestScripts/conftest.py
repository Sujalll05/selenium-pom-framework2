from selenium import webdriver
from time import sleep
import pytest
@pytest.fixture
def setup():

    opt= webdriver.ChromeOptions()
    opt.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=opt)
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/login")
    yield driver
    sleep(3)
    driver.quit()

