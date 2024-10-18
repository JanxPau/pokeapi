import unittest
from unittest.mock import patch
from api import *


class TestAPI(unittest.TestCase):

    @patch('api.requests.get')
    def test_get_pokemon_data_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "name": "pikachu",
            "height": 4,
            "weight": 60
        }

        # Call the function
        pokemon_data = get_pokemon_info('pikachu')

        # Assertions
        self.assertIsNotNone(pokemon_data)
        self.assertEqual(pokemon_data['name'], 'pikachu')
        self.assertEqual(pokemon_data['height'], 4)
        self.assertEqual(pokemon_data['weight'], 60)


if __name__ == '__main__':
    unittest.main()
