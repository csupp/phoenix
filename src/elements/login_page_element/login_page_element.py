from selenium.webdriver.common.by import By

class LoginPageElements:
    username_textbox=(By.XPATH,'//*[@id="dijit_form_ValidationTextBox_0"]')
    password_textbox=(By.XPATH,'//*[@id="dijit_form_ValidationTextBox_1"]')
    login_btn = (By.XPATH,'//*[@id="dijit_form_Button_0"]')
    erro_msg = (By.XPATH,'/html/body/div[2]/div[2]/div[2]/div/div')
