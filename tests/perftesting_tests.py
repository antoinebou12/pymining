import unittest

class TestPerfTesting(unittest.TestCase):

    def test_get_default_transactions(self):
        transactions = perftesting.get_default_transactions()
        self.assertEqual(len(transactions), 10)
        self.assertTrue(('a', 'd') in transactions)

    def test_get_default_transactions_alt(self):
        transactions = perftesting.get_default_transactions_alt()
        self.assertEqual(len(transactions), 10)
        self.assertTrue(('a', 'b') in transactions)

    def test_get_default_sequences(self):
        sequences = get_default_sequences()
        self.assertEqual(len(sequences), 4)
        self.assertTrue('caabc' in sequences)

    def test_perftesting.get_random_transactions(self):
        transactions = perftesting.get_random_transactions(transaction_number=5, max_item_per_transaction=2, universe_size=10)
        self.assertEqual(len(transactions), 5)
        for trans in transactions:
            self.assertTrue(len(trans) <= 2)

    def perftesting.test_sam(self):
        n, report = perftesting.test_sam(ts=[('a', 'b'), ('b', 'c'), ('a', 'c')], support=2)
        self.assertEqual(n, len(report))
        self.assertTrue(frozenset(['a', 'b']) in report or frozenset(['b', 'c']) in report)

    def perftesting.test_relim(self):
        n, report = perftesting.test_relim(ts=[('a', 'b'), ('b', 'c'), ('a', 'c')], support=2)
        self.assertEqual(n, len(report))
        self.assertTrue(frozenset(['a', 'b']) in report or frozenset(['b', 'c']) in report)

    def perftesting.test_fpgrowth(self):
        n, report = perftesting.test_fpgrowth(ts=[('a', 'b'), ('b', 'c'), ('a', 'c')], support=2)
        self.assertEqual(n, len(report))
        self.assertTrue(frozenset(['a', 'b']) in report or frozenset(['b', 'c']) in report)

    def test_perftesting.test_itemset_perf(self):
        # This is more of a performance test, so we might just run it and check it doesn't raise exceptions
        try:
            perftesting.test_itemset_perf(perf_round=1, sparse=True, seed=42)
        except Exception as e:
            self.fail(f"test_itemset_perf raised exception: {e}")

if __name__ == '__main__':
    unittest.main()
