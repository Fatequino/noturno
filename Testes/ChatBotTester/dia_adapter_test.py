import unittest
from unittest import result
from DiaAdapter import DiaAdapter
from datetime import date

 

class TestClass(unittest.TestCase):
      
    def test_obter_dia(self):
        self.assertTrue(DiaAdapter.obter_dia(self, "segunda") == "2")
        self.assertTrue(DiaAdapter.obter_dia(self, "terca" or "terça") == "3")
        self.assertTrue(DiaAdapter.obter_dia(self, "quarta") == "4")
        self.assertTrue(DiaAdapter.obter_dia(self, "quinta") == "5")
        self.assertTrue(DiaAdapter.obter_dia(self, "sexta") == "6")
        self.assertTrue(DiaAdapter.obter_dia(self, "sábado" or "sabado") == "7")
        self.assertTrue(DiaAdapter.obter_dia(self, "domingo") == "1")

    def test_obter_dia_false(self):
        self.assertFalse(DiaAdapter.obter_dia(self, "segunda") == "1")
        self.assertFalse(DiaAdapter.obter_dia(self, "terca" or "terça") == "7")
        self.assertFalse(DiaAdapter.obter_dia(self, "quarta") == "2")
        self.assertFalse(DiaAdapter.obter_dia(self, "quinta") == "6")
        self.assertFalse(DiaAdapter.obter_dia(self, "sexta") == "5")
        self.assertFalse(DiaAdapter.obter_dia(self, "sábado" or "sabado") == "3")
        self.assertFalse(DiaAdapter.obter_dia(self, "domingo") == "4")
    

if __name__ == '__main__':
    unittest.main()