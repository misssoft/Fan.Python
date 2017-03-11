import os
import unittest

def analyze_text(filename):

   lines = 0
   chars = 0
   with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
   return (lines, chars)

class TextAnalysisTests(unittest.TestCase):
    """Test for the ``analyze_test()`` function"""

    def setUp(self):
        self.filename = 'funfile.txt'
        with open(self.filename, 'w') as f:
            f.write('Spring is here. \n'
                    'As the birds sing. \n'
                    'And the flowers and bees. \n'
                    'In such a joy.')

    def tearDown(self):
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        analyze_text(self.filename)

    def test_line_count(self):
        self.assertEqual(analyze_text(self.filename)[0], 4)

    def test_charactor_count(self):
        self.assertEqual(analyze_text(self.filename)[1], 78)

    def test_no_such_file(self):
        with self.assertRaises(IOError):
            analyze_text("foo")

    def test_no_deletion(self):
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

if __name__ == '__main__':
    unittest.main()


