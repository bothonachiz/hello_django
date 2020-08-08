import unittest

from unittest.mock import patch

from my_app import Random

class TestRandom(unittest.TestCase):
    @patch('my_app.random.randint')
    def test_it_should_call_randint_with_1_and_10(self, mock):
        Random.get_random_number_plus_one()
        # assert here
        mock.assert_called_once_with(1,10)

    #@patch('__main__.random.randint')
    @patch('my_app.random.randint')
    def test_it_should_get_4_when_random_get_3(self, mock): #mock1, mock2
        # stubs mock https://docs.python.org/3/library/unittest.mock.html
        mock.return_value = 3
        result = Random.get_random_number_plus_one()
        self.assertEqual(result, 4)
        
    def test_it_should_get_3(self):
        while True:
            result = Random.get_random_number_plus_one()
            if result == 3:
                break    
        self.assertEqual(result, 3)  

unittest.main()