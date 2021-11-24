import selenium
from selenium.webdriver.firefox import webelement
import Main
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.firefox.webelement import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Firefox, firefox

def find(by, valor, tempo = 5) -> webelement:
    try:
        WebDriverWait(Main.driver, tempo).until(EC.presence_of_element_located((by, valor)))
        
    
        return Main.driver.find_element(by, valor)

    except TimeoutException:
        print("elemento " + str(by) + " não localizado a tempo (" + str(tempo) + "s)")
   
def click(by, valor, tempo = 5):
    try:        
        WebDriverWait(Main.driver, tempo).until(EC.element_to_be_clickable((by, valor)))
        find(by, valor, tempo).click()
        
    except TimeoutException:
        print("elemento não localizado a tempo (" + str(tempo) + "s)")


def mover(by, valor, tempo = 5):            
    action_chains.ActionChains(Main.driver).move_to_element(find(by, valor)).perform()
        
def rolar(by, valor):
    Main.driver.execute_script("arguments[0].scrollIntoView(true);", find(by, valor))


def scrool():
    for i in range(0, Main.driver.execute_script("return document.body.scrollHeight"), 50):
        Main.driver.execute_script('window.scrollTo(0,' + str(i) + ')')
        sleep(0.03)
    Main.driver.execute_script('window.scrollTo(0, 0);')