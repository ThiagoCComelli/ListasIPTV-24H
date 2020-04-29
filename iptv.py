from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import random
import time

def pegaSite(siteEmail_):
	try:
		siteEmail_.get("https://www.fakemail.net/")

		emails = siteEmail_.find_elements_by_class_name('from')

		while len(emails) < 2:
			time.sleep(5)
			emails = siteEmail_.find_elements_by_class_name('from')
			pass

		siteEmail_.get("https://www.fakemail.net/window/id/2")

		siteEmail_.switch_to.frame('iframeMail')
		site = siteEmail_.find_element_by_xpath('/html/body/div/div[3]/div/div[1]/center/table/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/p/a').text

		siteEmail_.quit()
		return site
	except:
		return "Falha para criar ao acessar o email! Tente novamente mais tarde."

def setup():
	chrome_options = webdriver.ChromeOptions()
	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--no-sandbox")

	siteEmail = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
	# siteFlash = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)

	siteEmail.get("https://www.fakemail.net/")

	email = siteEmail.find_element_by_xpath('//*[@id="email"]').text

	siteEmail.get("https://teste.flashiptv.me/")

	FlashBotarEmail = siteEmail.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/input')
	FlashBotaPlano = siteEmail.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/select/option[2]')
	FlashLogin = siteEmail.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/div[2]/button')
	FlashBotarEmail.send_keys(email)
	FlashBotaPlano.click()
	FlashLogin.submit()

	time.sleep(5)

	permissao = siteEmail.find_element_by_xpath('/html/body/div/div/div[2]').text

	if(permissao == "Teste criado com sucesso, verifique seu e-mail!"):
		return pegaSite(siteEmail)
	else:
		siteEmail.quit()
		return "Falha para criar a conta IPTV! Tente novamente mais tarde."








