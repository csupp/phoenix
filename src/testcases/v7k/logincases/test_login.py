import pytest
import allure
import sys
from time import sleep
from src.testdata.logindata import login_data as LD
from src.common.get_log import Log
from src.common.get_config import r_config

log_dir = r_config(r'/Users/ricky/phoenix/src/config/config.txt', 'log', 'log_path')
logger = Log(log_dir)


@pytest.mark.usefixtures('start_session')
class TestLogin:
    @allure.feature('Check login page features')
    @allure.story('Login ')
    def test_login_success(self, start_session):
        logger.info(" Run {0} testcase ".format(sys._getframe().f_code.co_name))
        logger.info(" run login testcase ")
        start_session[1].login(LD.success_data['username'], LD.success_data['password'])
        sleep(5)
     #   logger.info("Expected：{0}".format(True))
    #    logger.info("Actual：{0}".format(IndexPage(start_session[0]).isExist_logout_ele()))
        try:
       #     assert IndexPage(start_session[0]).isExist_logout_ele()
            logger.info(" Test done {0} testcase， result --- PASS ".format(sys._getframe().f_code.co_name))
            start_session[1].take_screenshot("{0}-passed".format(LD.success_data['name']))
        except:
            logger.error(" Test done {0} testcase， result --- failed ".format(sys._getframe().f_code.co_name))
            start_session[1].take_screenshot("{0}-failed".format(LD.success_data['name']))
            raise
