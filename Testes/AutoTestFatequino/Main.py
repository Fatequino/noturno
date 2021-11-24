from logging import exception
from time import sleep
from typing import SupportsComplex
from selenium import webdriver
import selenium
#from Utilidades import *
from selenium.webdriver import Firefox, firefox
from selenium.webdriver.common import action_chains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = Firefox()
url = 'http://fatequino.rf.gd/'

#Utilidades

#Localiza e retorna o elemento
def find(by, valor, tempo = 5):
    try:
        WebDriverWait(driver, tempo).until(EC.presence_of_element_located((by, valor)))        
    
        return driver.find_element(by, valor)

    except TimeoutException:
        print("elemento " + str(by) + " não localizado a tempo (" + str(tempo) + "s)")

#Clica no elemento
def click(by, valor, tempo = 5):
    try:        
        WebDriverWait(driver, tempo).until(EC.element_to_be_clickable((by, valor)))
        find(by, valor, tempo).click()
        
    except TimeoutException:
        print("elemento não localizado a tempo (" + str(tempo) + "s)")

#move o cursor do Mouse sobre o elemento
def mover(by, valor, tempo = 5):            
    action_chains.ActionChains(driver).move_to_element(find(by, valor)).perform()
        
#Rola a página até o elemento
def rolar(by, valor):
    driver.execute_script("arguments[0].scrollIntoView(true);", find(by, valor))

#Efeito de rolagem de página de forma lenta
def scrool():
    for i in range(0, driver.execute_script("return document.body.scrollHeight"), 50):
        driver.execute_script('window.scrollTo(0,' + str(i) + ')')
        sleep(0.03)
    driver.execute_script('window.scrollTo(0, 0);')


if __name__ == '__main__':
    
    try:
            
        #driver.maximize_window()
        driver.delete_all_cookies()
        driver.get(url)

        click(By.ID, 'wt-cli-accept-all-btn')

        print("\nIniciando Testes...\n")
        print("\nTestando chatbot\n")
        click(By.CLASS_NAME, 'rsc-float-button')
        sleep(2)

        ######## interação com o chatbot. (desativado) ######## 

        #find(By.CLASS_NAME, 'rsc-input').send_keys('Olá')
        #sleep(0.5)
        #click(By.CLASS_NAME, 'rsc-submit-button')
        #sleep(2)        
        #click(By.CLASS_NAME, 'rsc-input')
        #find(By.CLASS_NAME, 'rsc-input').send_keys('Tudo bem fatequino? Como estão as coisas por aí?')
        #click(By.CLASS_NAME, 'rsc-submit-button')
        #sleep(2)        
        #click(By.CLASS_NAME, 'rsc-input')
        #find(By.CLASS_NAME, 'rsc-input').send_keys('Então tá bom. Só fazendo os testes de rotina aqui')
        #click(By.CLASS_NAME, 'rsc-submit-button')
        
        
        click(By.XPATH, '/html/body/div[12]/div/div/div/div[1]/div[3]')
        sleep(1)

        print("\nTestando Acessibilidades\n")
        click(By.ID, 'real-accessability-btn')
        sleep(1)
        click(By.ID, 'real-accessability-biggerFont')
        sleep(1)
        click(By.ID, 'real-accessability-biggerFont')
        sleep(1)
        click(By.ID, 'real-accessability-smallerFont')
        sleep(1)
        click(By.ID, 'real-accessability-smallerFont')
        sleep(1)
        click(By.LINK_TEXT, 'Preto e branco')
        sleep(1)
        click(By.LINK_TEXT, 'Preto e branco')
        sleep(1)
        click(By.ID, 'real-accessability-invert') 
        sleep(1)
        click(By.ID, 'real-accessability-invert')
        sleep(1)
        click(By.ID, 'real-accessability-linkHighlight') 
        sleep(1)
        click(By.ID, 'real-accessability-linkHighlight')
        sleep(1)
        click(By.ID, 'real-accessability-regularFont') 
        sleep(1)
        click(By.ID, 'real-accessability-regularFont') 
        sleep(1)
        click(By.ID, 'real-accessability-reset') 
        sleep(1)
        click(By.ID, 'real-accessability-btn') 
        sleep(2)
       

        mover(By.ID, 'menu-item-13')  #O projeto Fatequino    
        click(By.ID, 'menu-item-411') #Construção do Fatequino
        WebDriverWait(driver, 60).until(EC.url_to_be('http://fatequino.rf.gd/construcao-do-fatequino/'))
        scrool()

        mover(By.ID, 'menu-item-13')  #O projeto Fatequino  
        click(By.ID, 'menu-item-88')  #controle
        WebDriverWait(driver, 60).until(EC.url_to_be('http://fatequino.rf.gd/construcao-do-fatequino/controle/'))
        scrool()

        mover(By.ID, 'menu-item-13')  #O projeto Fatequino  
        click(By.ID, 'menu-item-86')  #Interacao I
        WebDriverWait(driver, 60).until(EC.url_to_be('http://fatequino.rf.gd/construcao-do-fatequino/interacao/'))
        scrool()
        sleep(3)

        mover(By.ID, 'menu-item-13')  #O projeto Fatequino  
        click(By.ID, 'menu-item-26666')  #Interacao II
        WebDriverWait(driver, 60).until(EC.url_to_be('http://fatequino.rf.gd/interacao-ii/'))
        scrool()
        sleep(3)

        mover(By.ID, 'menu-item-13')  #O projeto Fatequino  
        click(By.ID, 'menu-item-89')  #Mecanica do movimento
        WebDriverWait(driver, 60).until(EC.url_to_be('http://fatequino.rf.gd/construcao-do-fatequino/mecanica/'))
        scrool()
        sleep(3)

        mover(By.ID, 'menu-item-13')  #O projeto Fatequino  
        click(By.ID, 'menu-item-90')  #Presenca na Web
        WebDriverWait(driver, 60).until(EC.url_to_be('http://fatequino.rf.gd/construcao-do-fatequino/web/'))
        scrool()

        
        mover(By.ID, 'menu-item-13')  #O projeto Fatequino  
        click(By.ID, 'menu-item-87')  #Visao
        WebDriverWait(driver, 60).until(EC.url_to_be('http://fatequino.rf.gd/construcao-do-fatequino/visao/'))
        scrool()
            
        mover(By.ID, 'menu-item-13')  #O projeto Fatequino  
        click(By.ID, 'menu-item-26673')  #Testes
        WebDriverWait(driver, 60).until(EC.url_to_be('http://fatequino.rf.gd/construcao-do-fatequino/equipe-de-testes/'))                
        scrool()
        
        
        click(By.ID, 'menu-item-320')  #Minhas fotos
        WebDriverWait(driver, 60).until(EC.url_to_be('http://fatequino.rf.gd/minhas-fotos/'))
        scrool()
            
        click(By.ID, 'menu-item-585')  #Documentos
        WebDriverWait(driver, 60).until(EC.url_to_be('http://fatequino.rf.gd/documentos/'))
        scrool()
            
        #click(By.ID, 'menu-item-460')  #ChatBot antigo
        #WebDriverWait(driver, 60).until(EC.url_to_be(''))
        #scrool()

        click(By.ID, 'menu-item-427')  #Fale Conosco
        WebDriverWait(driver, 60).until(EC.url_to_be('http://fatequino.rf.gd/fale-conosco/'))
        scrool()

        click(By.NAME, 'your-name')
        find(By.NAME, 'your-name').send_keys('Nome Teste')
        sleep(0.5)
        click(By.NAME, 'your-email')
        find(By.NAME, 'your-email').send_keys('email_teste@teste.com')
        sleep(0.5)
        click(By.NAME, 'your-subject')
        find(By.NAME, 'your-subject').send_keys('Assunto Teste')
        sleep(0.5)
        click(By.NAME, 'your-message')
        find(By.NAME, 'your-message').send_keys('Mensagem Teste')
        sleep(2)
        #click(By.CLASS_NAME, 'wpcf7-form-control wpcf7-submit')
        if driver.page_source.__contains__('Um ou mais campos possuem um erro. Verifique e tente novamente.'):
            raise Exception('Não foi possível enviar o e-mail.')

            
        click(By.ID, 'menu-item-304')  #Registro
        WebDriverWait(driver, 60).until(EC.url_to_be('http://fatequino.rf.gd/registro/'))
        scrool()
            
        click(By.LINK_TEXT, 'Termos de uso e Política de privacidade') #Termos de uso
        WebDriverWait(driver, 60).until(EC.url_to_be('http://fatequino.rf.gd/termos-de-uso-e-politica-de-privacidade/'))
        sleep(5)


        driver.close()        

        print("\n\nTeste concluído com sucesso!\n\n")

    except TimeoutException:
        print("Tempo máximo excedido. Teste abortado")

    except Exception as e:
        print(e)