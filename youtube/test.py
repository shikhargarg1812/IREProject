import unittest
import json
import search

class TestSearch(unittest.TestCase):

    def test_key(self):
        path = '../creds.json'
        
        with open(path,'r') as f:
            key = json.load(f)
        
        self.assertEqual(search.get_key(path),key)

    def search(self):
        path = '../creds.json'
        search.search(path,'test')

if __name__ == '__main__':
    unittest.main()