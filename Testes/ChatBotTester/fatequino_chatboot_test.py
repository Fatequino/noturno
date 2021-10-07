import unittest
from unittest import result
from FatequinoChatbot import FatequinoChatbot
from datetime import date

 

class TestClass(unittest.TestCase):
      
    def test_mensagemEnviada(self):
        #Aguardando codigo final para cirar testes das funções
        self.assertTrue(FatequinoChatbot.mensagemEnviada(self, "Tem aula hoje?"))
        
        
if __name__ == '__main__':
    unittest.main()