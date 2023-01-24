import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from features.pageObjectModel.locators.dashboard_Locator import DashboardPage
from features.pageObjectModel.pages.loginPOM import Login_POM
use_step_matcher("re")


@given("Kullanici Tarayiciyi acar")
def step_impl(context):

    options = webdriver.FirefoxOptions()
    context.driver=webdriver.Remote(command_executor="http://localhost:4444/wd/hub",desired_capabilities=DesiredCapabilities.FIREFOX,options=options)

    # context.driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
    # context.driver.implicitly_wait(10)




@when('Kullanici Uygulamanin Url "(.*)" Adresini gider')
def step_impl(context, url):
    Url = Login_POM(context.driver)
    Url.Uygulama_Url_Ac(url)
    time.sleep(1)


@step('Kullanici UserName "(.*)" girer')
def step_impl(context, userName):
    UserName = Login_POM(context.driver)
    UserName.KulaniciAdi_Giris(userName)
    time.sleep(1)


@step('Kullanici Password "(.*)" girer')
def step_impl(context, password):

    Password = Login_POM(context.driver)
    Password.KullaniciSifre_Giris(password)
    time.sleep(1)


@step("Kullanici Giris Yap butonuna tiklar")
def step_impl(context):
    LogiBtn = Login_POM(context.driver)
    LogiBtn.Login_Click_Btn()
    time.sleep(1)


@then("Kullanicinin Uygulamaya giris yaptigi gorulur")
def step_impl(context):
    pass
    BasariliGiris=Login_POM(context.driver)
    BasariliGiris.Basarili_Giris(DashboardPage.BeklenenCvp)
    time.sleep(2)
    context.driver.quit()
