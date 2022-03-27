import unittest

from atividadesUnit import *

# coloca a classe que ta testando+Testes
class atividadesUnitTestes(unittest.TestCase):
    # coloca test_funcao
    def test_comer(self):
        """Testando o retorno comida saudavel. """ #-> Se usar python nomeDoArquivo -v vai aparecer as docstrings falando sobre o teste com no final ... .ok
        self.assertEqual(
            comer('quiabo',True),
            'Estou comendo quiabo porque quero manter a forma'
        )
    def test_comer_besteira(self):
        """Testando o retorno comida gostosa. """
        self.assertEqual(
            comer(comida = 'pizza',saudavel = False),
            'Estou comendo pizza porque só vivemos uma vez'
        )
    def test_dormir_pouco(self):
        """Testando o retorno dormir pouco. """
        self.assertEqual(
            dormir(10),
            'Estou atrasado pro trabalho'
        )
    def test_dormir_muito(self):
        """Testando o retorno dormir muito. """
        self.assertEqual(
            dormir(4),
            'Estou cansado pro trabalho :('
        )
if __name__ == '__main__':
     unittest.main()