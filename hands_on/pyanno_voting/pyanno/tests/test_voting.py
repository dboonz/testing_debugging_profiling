import unittest
import numpy as np
from numpy.testing import assert_array_equal
from numpy.testing import assert_array_almost_equal

from pyanno import voting
from pyanno.voting import MISSING_VALUE as MV


class TestVoting(unittest.TestCase):

    def test_labels_count(self):
        annotations = [
            [1,  2, MV, MV],
            [MV, MV,  3,  3],
            [MV,  1,  3,  1],
            [MV, MV, MV, MV],
        ]
        nclasses = 5
        expected = [0, 3, 1, 3, 0]
        result = voting.labels_count(annotations, nclasses)
        self.assertEqual(result, expected)

    def test_majority_vote(self):
        annotations = [
            [1, 2, 2, MV],
            [2, 2, 2, 2],
            [1, 1, 3, 3],
            [1, 3, 3, 2],
            [MV, 2, 3, 1],
            [MV, MV, MV, 3],
        ]
        expected = [2, 2, 1, 3, 1, 3]
        result = voting.majority_vote(annotations)
        self.assertEqual(expected, result)

    def test_majority_vote_empty_item(self):
        # Bug: majority vote with row of invalid annotations fails
        annotations = np.array(
            [[1, 2, 3],
             [MV, MV, MV],
             [1, 2, 2]]
        )
        expected = [1, MV, 2]
        result = voting.majority_vote(annotations)
        self.assertEqual(expected, result)

    def test_dummy(self):
        """Test that one plus two equals three """
        expected = 3
        result = 1+2
        self.assertEqual(expected, result)

    def test_decimals(self):
        """Test that 1.1 plus 2.2 equals 3.3."""
        expected = 3.3
        result = 1.1 + 2.2
        self.assertAlmostEqual(expected,result)

    def test_label_frequency(self):
        expected = np.array([ 0. ,  0.6,  0.4,  0. ])
        annotations = [[1, 1, 2], [-1, 1, 2]]
        n_classes = 4
        result = voting.labels_frequency(annotations, n_classes)
        assert_array_almost_equal(expected,result)

    def test_sum_arrays(self):
        """ Test that [1,1] + [2,2] == [3,3]"""
        x = np.array([1,1])
        y = np.array([2,2])
        z = np.array([3,3], dtype=np.complex64)
        assert_array_equal(x+y, z)



if __name__ == '__main__':
    unittest.main()
