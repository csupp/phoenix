
from src.common.base_page_objs import BasePageObjs
from src.elements.login_page_element.login_page_element import LoginPageElements as lpe

class  LoginPage(BasePageObjs):
    def login(self,username,password):
        doc='GUI login'
        self.input_element(lpe.username_textbox,username,doc)
        self.input_element(lpe.password_textbox,password,doc)
        self.wait_eleVisible(lpe.login_btn)
        self.click_element(lpe.login_btn,doc)

    def get_login_errMsg(self):
        doc = 'login with error account'
        self.wait_eleVisible(lpe.erro_msg)
        return self.get_element_text(lpe.erro_msg, doc)


