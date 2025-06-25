# Zona de importação

import unittest
from datetime import datetime
from src.models.shows import Show

class TestShow(unittest.TestCase):
    def setUp(self):
        self.show = Show(11, datetime(2025, 6, 26), 'São João na Bahia')

# Testes

    def test_id_is_correctly(self):
        self.assertEqual(self.show.show_id, 11)
    
    def test_date_is_correctly(self):
        self.assertEqual(self.show.date, datetime(2025, 6, 26))

    def test_name_is_correctly(self):
        self.assertEqual(self.show.name, 'São João na Bahia')

    def text_to_dict(self):
        expected = {
            'show_id': 11,
            'date': '2025-06-26',
            'name': 'São João na Bahia'
        }
        self.assertEqual(self.show.to_dict(), expected)

    def test_to_dict_structure(self):
        result = self.show.to_dict()
        print(result)
        self.assertIn('show_id', result)
        self.assertIn('date', result)
        self.assertIn('name', result)