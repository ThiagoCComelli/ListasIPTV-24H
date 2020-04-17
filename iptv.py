from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import random
import time

def pegaSite(siteEmail_):
	
	siteEmail_.get("https://www.fakemail.net/")

	emails = siteEmail_.find_elements_by_class_name('from')

	while len(emails) < 2:
		time.sleep(5)
		emails = siteEmail_.find_elements_by_class_name('from')
		pass

	emails[0].click()

	siteEmail_.switch_to.frame('iframeMail')
	site = siteEmail_.find_element_by_xpath('/html/body/div/div[3]/div/div[1]/center/table/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/p/a').text

	print(site)
	siteEmail_.quit()
	return site

def setup():
	chrome_options = webdriver.ChromeOptions()
	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--no-sandbox")

	siteEmail = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
	# siteFlash = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)

	siteEmail.get("https://www.fakemail.net/")
	# siteFlash.get("https://teste.flashiptv.co/")

	email = siteEmail.find_element_by_xpath('//*[@id="email"]').text

	siteEmail.get("https://teste.flashiptv.co/")

	FlashBotarEmail = siteEmail.find_element_by_xpath('//*[@id="formulario_teste"]/div[2]/input')
	FlashBotaNome = siteEmail.find_element_by_xpath('//*[@id="formulario_teste"]/div[1]/input')
	FlashBotaFone = siteEmail.find_element_by_xpath('//*[@id="phone_number"]')
	FlashBotaPlano = siteEmail.find_element_by_xpath('//*[@id="formulario_teste"]/div[4]/select/option[2]')
	FlashLogin = siteEmail.find_element_by_xpath('//*[@id="gerar_teste"]')
	FlashBotaNome.send_keys("Thiago Comelli")
	FlashBotarEmail.send_keys(email)
	FlashBotaFone.send_keys(str(random.randint(10000000000,99999999999)))
	FlashBotaPlano.click()
	FlashLogin.submit()

	time.sleep(5)

	permissao = siteEmail.find_element_by_xpath('//*[@id="swal2-title"]').text

	if(permissao == "Teste gerado com sucesso"):
		return pegaSite(siteEmail)
	else:
		siteEmail.quit()
		return "Falha para criar a conta IPTV! Tente novamente mais tarde."








