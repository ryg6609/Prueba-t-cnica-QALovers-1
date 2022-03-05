import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class test_campos_vacios(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_campos_vacios(self):
		driver = self.driver
		actions = ActionChains(driver)
		driver.maximize_window()
		driver.get("https://www.qalovers.com/") 
		self.assertIn("QALovers", driver.title) #validar el titulo de la pestaña web
		cookie = driver.find_element_by_xpath("//*[@id='hs-eu-confirmation-button']").click() #aceptar cookies
		enviar = driver.find_element_by_xpath("//*[@id='ContactForm1_contact-form-submit']").click() # pulsar en el botón enviar
		time.sleep(3)
		respuesta = driver.find_element_by_xpath("//*[@id='ContactForm1_contact-form-error-message']").text #Recoger respuesta 
		self.assertEqual(respuesta, "Tienes que escribir una dirección de correo electrónico válida.")
		
class test_campos_completados(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_campos_completados(self):
		driver = self.driver
		actions = ActionChains(driver)
		driver.maximize_window()
		driver.get("https://www.qalovers.com/")
		cookie = driver.find_element_by_xpath("//*[@id='hs-eu-confirmation-button']").click()
		nombre = driver.find_element_by_name("name").send_keys("Nombre")
		email = driver.find_element_by_name("email").send_keys("prueba@prueba.com")
		mensaje = driver.find_element_by_name("email-message").send_keys("Esto es un mensaje de prueba, disculpa las molestias")
		time.sleep(3)
		enviar = driver.find_element_by_xpath("//*[@id='ContactForm1_contact-form-submit']").click()
		time.sleep(2)
		success = driver.find_element_by_xpath("//*[@id='ContactForm1_contact-form-success-message']").text
		time.sleep(2)
		self.assertEqual(success, "Se ha enviado tu mensaje.")
		time.sleep(3)




def tearDown(self):
	self.driver.close()
		
if __name__ == '__main__':
	unittest.main()