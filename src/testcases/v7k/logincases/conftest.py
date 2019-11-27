import pytest
import os
import sys
from time import sleep
from selenium import webdriver
from src.testdata.logindata import login_data as ldata
from src.pageobjs.v7k.loginPage.login_page import LoginPage
from src.common.base_page_objs import BasePageObjs
from src.common.get_log import Log
from src.common.get_config import r_config

log_dir = r_config(r'/Users/ricky/phoenix/src/config/config.txt', "log", "log_path")
logger = Log(log_dir)

driver = None

@pytest.fixture(scope='class')
def start_session(project_session_start):
    logger.info("==========Start to run testcases===========")
    global driver
    driver = project_session_start
    logger.info("----------------------------------------------------------------------------------" + str(driver))
    driver.get(ldata.web_login_url)
    lg = LoginPage(driver)
    yield (driver, lg)
    logger.info("==========Run testcases done===========")


@pytest.fixture()
def refresh_page():
    yield
    driver.refresh()
    sleep(3)