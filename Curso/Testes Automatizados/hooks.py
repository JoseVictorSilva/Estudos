"""
    Unittest - Antes e após hooks

- Hooks -> São os testes em si, ou seja a execução deles

- setup() -> é executado antes de cada método de teste. Útil para criar intâncias de objetos e outros dados
- tearDown -> é executado depois de cada método de teste. Útil para excluir ou fechar dados e conexões
"""

import unittest

class ModuloTeste(unittest.TestCase):
    def setUp(self):
        #configurações, roda primeiro
        pass
    def test_primeiro(self):
        pass
    
    def test_segundo(self):
        pass
    
    def test_terceiro(self):
        pass
    def tearDown(self):
        # Tear down roda depois de todos acima
        pass
    