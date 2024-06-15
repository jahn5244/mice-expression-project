import pandas as pd
import unittest
from mice_expression import process_dataset

class TestProcessDataset(unittest.TestCase):
    def setUp(self):
        # Create a simple test dataset for testing
        self.test_dataset = pd.read_csv("/Users/johnahnline/Downloads/Data_Cortex_Nuclear.csv", header=None)
        # Remove the unnecessary variables for the analysis.
        self.test_dataset = self.test_dataset.drop([78, 79, 80, 81], axis='columns')

    def test_process_dataset(self):
        # Test with a specific column index, adjust as needed
        
        # Test Case 1
        column_index = 3
        max_val, min_val, top5_ids, bottom5_ids, median_val = process_dataset(self.test_dataset, column_index)

        self.assertEqual(max_val, 0.497159859)
        self.assertEqual(min_val, 0.115181402)
        self.assertEqual(top5_ids, ['3497_1', 'J3295_13', 'J3295_14', 'J3295_12', 'J1291_13'])
        self.assertEqual(bottom5_ids, ['3413_2', '3525_3', '3525_6', '3525_2', '3525_12'])
        self.assertEqual(median_val, 0.328017579)
        
        # Test Case 2
        column_index = 67
        max_val, min_val, top5_ids, bottom5_ids, median_val = process_dataset(self.test_dataset, column_index)

        self.assertEqual(max_val, 1.204598081)
        self.assertEqual(min_val, 0.577396764)
        self.assertEqual(top5_ids, ['3484_3', '3418_9', '50810F_1', '3497_11', '3497_10'])
        self.assertEqual(bottom5_ids, ['3415_13', '3484_3', '3484_2', '3484_6', '3484_1'])
        self.assertEqual(median_val, 0.8663920949999999)
        
        # Test Case 3
        column_index = 35
        max_val, min_val, top5_ids, bottom5_ids, median_val = process_dataset(self.test_dataset, column_index)

        self.assertEqual(max_val, 0.933256284)
        self.assertEqual(min_val, 0.227880387)
        self.assertEqual(top5_ids, ['3418_11', 'J3295_14', 'J3295_13', 'J3295_11', 'J3295_10'])
        self.assertEqual(bottom5_ids, ['3483_3', '3517_13', '3517_14', '3517_10', '3517_11'])
        self.assertEqual(median_val, 0.5017101245)


if __name__ == '__main__':
    unittest.main()
