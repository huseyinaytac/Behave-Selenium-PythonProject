from features.pageObjectModel.domFunctions import DomHelper
from features.pageObjectModel.locators.loginPageLocator import LoginPage
from features.pageObjectModel.locators.dashboard_Locator import DashboardPage




class Login_POM():
    def __init__(self, driver):
        self.driver = driver

    def Uygulama_Url_Ac(self, Url):
        url = DomHelper(self.driver)
        url.open_Page(Url)

    def KulaniciAdi_Giris(self,Username):
        kullaniciAdi=DomHelper(self.driver)
        kullaniciAdi.send_keys_ID(LoginPage.UserName_ID,Username)

    def KullaniciSifre_Giris(self,Password):
        kullaniciSifre=DomHelper(self.driver)
        kullaniciSifre.send_keys_ID(LoginPage.Password_ID,Password)

    def Login_Click_Btn(self):
        loginBtn=DomHelper(self.driver)
        loginBtn.click_button_ID(LoginPage.LoginBtn_ID)

    def Basarili_Giris(self,linkText):
        Anasayfa=DomHelper(self.driver)
        Anasayfa.is_text_equal_XPATH(DashboardPage.Successfully_XPATH,linkText)

