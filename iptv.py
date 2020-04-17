from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

def pegaSite(siteEmail_):
	try:
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
	except:
		return "Falha para acessar o email! Tente novamente mais tarde."

def setup():
	siteEmail = webdriver.Firefox(executable_path='geckodriver')
	siteFlash = webdriver.Firefox(executable_path='geckodriver')

	siteEmail.get("https://www.fakemail.net/")
	siteFlash.get("https://teste.flashiptv.co/")

	email = siteEmail.find_element_by_xpath('//*[@id="email"]').text
	FlashBotarEmail = siteFlash.find_element_by_xpath('//*[@id="formulario_teste"]/div[2]/input')
	FlashBotaNome = siteFlash.find_element_by_xpath('//*[@id="formulario_teste"]/div[1]/input')
	FlashBotaFone = siteFlash.find_element_by_xpath('//*[@id="phone_number"]')
	FlashBotaPlano = siteFlash.find_element_by_xpath('//*[@id="formulario_teste"]/div[4]/select/option[2]')
	FlashLogin = siteFlash.find_element_by_xpath('//*[@id="gerar_teste"]')
	FlashBotaNome.send_keys("Thiago Comelli")
	FlashBotarEmail.send_keys(email)
	FlashBotaFone.send_keys(str(random.randint(10000000000,99999999999)))
	FlashBotaPlano.click()
	FlashLogin.submit()

	time.sleep(5)

	permissao = siteFlash.find_element_by_xpath('//*[@id="swal2-title"]').text

	if(permissao == "Teste gerado com sucesso"):
		siteFlash.quit()
		return pegaSite(siteEmail)
	else:
		siteFlash.quit()
		siteEmail.quit()
		return "Falha para criar a conta IPTV! Tente novamente mais tarde."








