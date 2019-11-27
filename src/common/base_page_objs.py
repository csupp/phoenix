import time,datetime,os,sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.common.get_log import Log
from src.common.get_config import r_config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
#BASE_DIR = os.path.split(os.path.realpath(__file__))[0]

if sys.platform == "win32":
    conf_dir = os.path.join(BASE_DIR, 'src/config/config.txt').replace('/', '\\')
else:
    conf_dir = os.path.join(BASE_DIR, 'src/config/config.txt')
log_dir = r_config(conf_dir, "log", "log_path")
screenshots_dir = r_config(conf_dir, "screenshot", "screenshot_path")
logger = Log(log_dir)

# logger, common fuction methods
class BasePageObjs:

    def __init__(self, driver):
        self.driver = driver

    # Take screenshot
    def take_screenshot(self, doc):
        filePath = screenshots_dir + '{0}_{1}.png'.format(doc, time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime()))
        try:
            self.driver.save_screenshot(filePath)
            logger.info('{0} take screenshot done，file path: {0}'.format(doc, filePath))
        except:
            logger.info('{0} take screenshot failed'.format(doc))

    # Waiting element visible
    def wait_eleVisible(self, locator, doc=''):
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout=20, poll_frequency=0.5).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_time = (end - start).seconds
            logger.info('{0},waiting element:{1}:，cost time {2}s '.format(doc, locator, wait_time))
        except:
            logger.info('{0},waiting element:{1} failed！！！'.format(doc, locator))
            self.take_screenshot(doc)

    #
    def wait_elePresence(self):
        pass

    # Search web element
    def get_element(self, locator, doc=''):
        print(locator)
        logger.info('{0},search web element:{1}'.format(doc, locator))
        try:
            self.wait_eleVisible(locator, doc)
            return self.driver.find_element(*locator)
        except:
            logger.info('{0},search web element:{1} failed！！！'.format(doc, locator))
            raise

    # click web element
    def click_element(self, locator, doc=''):
        logger.info('{0},click web element:{1}'.format(doc, locator))
        try:
            self.get_element(locator, doc).click()
        except:
            logger.info('click web element:{0},failed！！！'.format(locator))
            raise

    # input variable
    def input_element(self, locator, key, doc=''):
        logger.info('{0},web element:{1} value {2}'.format(doc, locator, key))
        try:
            self.wait_eleVisible(locator, doc)
            self.get_element(locator, doc).send_keys(key)
        except:
            logger.info('{0},set value failed！！！'.format(doc))
            raise

    # Get text
    def get_element_text(self, locator, doc=''):
        logger.info('{0},get web element:{1}'.format(doc, locator))
        try:
            self.wait_eleVisible(locator, doc)
            return self.get_element(locator, doc).text
        except:
            logger.info('{0},get web element failed！！！'.format(doc))
            raise

    # Get web element attribute
    def get_element_attribute(self, attr, locator, doc=''):
        logger.info('{0},get web element attribute:{1}'.format(doc, locator))
        try:
            self.wait_eleVisible(locator, doc)
            return self.get_element(locator, doc).get_attribute(attr)
        except:
            logger.info('{0},get web element attribute failed！！！'.format(doc))
            raise

    # alter
    def alter_action(self):
        pass

    # iframe
    def switch_iframe(self):
        pass

    # windows
    def switch_window(self):
        pass

    # upload file
    def upload_file(self):
        pass

    # scroll bar
    def scroll_window(self):
        pass

