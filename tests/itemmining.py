import unittest

class TestFreqSeqEnum(unittest.TestCase):
    
    def test_freq_seq_enum_empty(self):
        sequences = []
        min_support = 2
        result = freq_seq_enum(sequences, min_support)
        self.assertEqual(result, set())
        
    def test_freq_seq_enum_single_sequence(self):
        sequences = [('a', 'b', 'c')]
        min_support = 1
        result = freq_seq_enum(sequences, min_support)
        self.assertTrue(('a',) in result)
        self.assertTrue(('b',) in result)
        self.assertTrue(('c',) in result)
        self.assertTrue(('a', 'b') in result)
        self.assertTrue(('a', 'c') in result)
        self.assertTrue(('b', 'c') in result)
        self.assertTrue(('a', 'b', 'c') in result)
        
    def test_freq_seq_enum_multiple_sequences(self):
        sequences = [('a', 'b', 'c'), ('a', 'c', 'd'), ('b', 'c', 'e')]
        min_support = 2
        result = freq_seq_enum(sequences, min_support)
        self.assertTrue(('a',) in result)
        self.assertTrue(('b',) in result)
        self.assertTrue(('c',) in result)
        self.assertTrue(('a', 'c') in result)
        self.assertTrue(('b', 'c') in result)
        
    def test_freq_seq_enum_min_support(self):
        sequences = [('a', 'b', 'c'), ('a', 'c', 'd'), ('b', 'c', 'e')]
        min_support = 3
        result = freq_seq_enum(sequences, min_support)
        self.assertTrue(('c',) in result)
        
    def test_freq_seq_enum_no_frequent_sequences(self):
        sequences = [('a', 'b', 'c'), ('d', 'e', 'f')]
        min_support = 2
        result = freq_seq_enum(sequences, min_support)
        self.assertEqual(result, set())

if __name__ == '__main__':
    unittest.main()
