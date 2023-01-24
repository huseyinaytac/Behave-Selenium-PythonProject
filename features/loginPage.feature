Feature: Login Ekranindan Kullanici uygulamaya giris saglayabilmelidir.

  Scenario: Kullanici Login Ekranindan Uygulamya giris yapabiliyor mu?

    Given Kullanici Tarayiciyi acar
    When Kullanici Uygulamanin Url "https://practicetestautomation.com/practice-test-login" Adresini gider
    And Kullanici UserName "student" girer
    And Kullanici Password "Password123" girer
    And Kullanici Giris Yap butonuna tiklar
    Then Kullanicinin Uygulamaya giris yaptigi gorulur

