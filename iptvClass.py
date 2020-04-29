from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import random
import time

class Iptv():
    def __init__(self):
        self.siteEmail = webdriver.Firefox()


    def pegaSite(self):
        try:
            print(0)
            self.siteEmail.get("https://www.fakemail.net/")
            print(1)

            self.emails = self.siteEmail.find_elements_by_class_name('from')
            print(2)

            while len(self.emails) < 2:
                print(3)
                time.sleep(5)
                self.emails = self.siteEmail.find_elements_by_class_name('from')
                print(4)
                pass
            
            print(5)
            self.siteEmail.get("https://www.fakemail.net/window/id/2")
            print(6)
            self.siteEmail.switch_to.frame('iframeMail')
            print(7)
            self.site = self.siteEmail.find_element_by_xpath('/html/body/div/div[3]/div/div[1]/center/table/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/p/a').text
            print(8)
            self.siteEmail.quit()
            return self.site
        except:
            return "Falha para acessar o email! Tente novamente mais tarde."

    def setup(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--no-sandbox")

        
        # siteFlash = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)

        self.siteEmail.get("https://www.fakemail.net/")
        # siteFlash.get("https://teste.flashiptv.co/")

        self.email = self.siteEmail.find_element_by_xpath('//*[@id="email"]').text

        self.siteEmail.get("https://teste.flashiptv.co/")

        self.FlashBotarEmail = self.siteEmail.find_element_by_xpath('//*[@id="formulario_teste"]/div[2]/input')
        self.FlashBotaNome = self.siteEmail.find_element_by_xpath('//*[@id="formulario_teste"]/div[1]/input')
        self.FlashBotaFone = self.siteEmail.find_element_by_xpath('//*[@id="phone_number"]')
        self.FlashBotaPlano = self.siteEmail.find_element_by_xpath('//*[@id="formulario_teste"]/div[4]/select/option[2]')
        self.FlashLogin = self.siteEmail.find_element_by_xpath('//*[@id="gerar_teste"]')
        self.FlashBotaNome.send_keys("Joao Paulo")
        self.FlashBotarEmail.send_keys(self.email)
        self.FlashBotaFone.send_keys(str(random.randint(10000000000,99999999999)))
        self.FlashBotaPlano.click()
        self.FlashLogin.submit()

        time.sleep(5)

        self.permissao = self.siteEmail.find_element_by_xpath('//*[@id="swal2-title"]').text

        if(self.permissao == "Teste gerado com sucesso"):
            return self.pegaSite()
        else:
            self.siteEmail.quit()
            return "Falha para criar a conta IPTV! Tente novamente mais tarde."
