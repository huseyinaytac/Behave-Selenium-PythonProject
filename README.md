1.Behave Selenium Projesini çalıştırmak için Terminal üzerinde "C:\Users\huseyin.aytac\PycharmProjects\Behave-Selenium-PythonProject>"
dizinine gelerek "behave -f allure_behave.formatter:AllureFormatter -o features/target/allure-results" komutunu çalıştırıyoruz.

2.İşlem tamamlandıktan sonra çıkan test sonucunun çıktısını target/allure-results klasörü içerisindeki json formatlı dosyanın içeriğini Html tipinde görüntülemek için 
"C:\Users\huseyin.aytac\PycharmProjects\Behave-Selenium-PythonProject>" dizininde "allure serve features/target/allure-results/" komutunu çalıştırıyoruz.