import pytest
import os
import sys
from selenium import webdriver

from src.common.get_config import r_config,read_config
from src.common.get_log import Log

log_dir = r_config('/Users/ricky/phoenix/src/config/config.txt', "log", "log_path")
geckodriver_path = read_config('/Users/ricky/phoenix/src/config/config.txt', "firefox_driver", "geckodriver_path")
logger = Log(log_dir)

driver = None


@pytest.fixture(scope='session')
def project_session_start():
    logger.info("==========Run testcases of whole project===========")
    global driver
    driver = webdriver.Firefox(executable_path=geckodriver_path)
    driver.set_window_size(1024,768)
    yield driver
    driver.quit()
    logger.info("==========Finish testcases of the project===========")


@pytest.fixture(scope='module')
def project_module_start():
    logger.info("==========Run testcases of specific module===========")
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    logger.info("=========Finish testcases of specific module============")
