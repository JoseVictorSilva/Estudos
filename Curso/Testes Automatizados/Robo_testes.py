import unittest
from robo import Robo

class RoboTestes(unittest.TestCase):

    def setUp(self):
        self.megaman = Robo('Megaman', bateria = 50)
        print('setUp() sendo executado...')

    def test_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria,100)
    
    def teste_dizer_nome(self):
        self.assertEqual(self.megaman.dizer_nome(),'BEEP BOOP BEEP. EU SOU MEGAMAN')
        self.assertEqual(self.megaman.bateria, 49, 'A bateria deveria estar em 49')
    
    def tearDown(self):
        print('tearDown() sendo executado...')

if __name__ == '__main__':
     unittest.main()