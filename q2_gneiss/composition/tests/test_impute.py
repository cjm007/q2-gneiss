# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest
import numpy as np
from q2_composition import add_pseudocount
from biom import Table


class TestAdd_Pseudocount(unittest.TestCase):

    def test_add_pseudocount(self):
        t = Table(np.array([[0, 1, 3], [1, 1, 2]]),
                  ['O1', 'O2'],
                  ['S1', 'S2', 'S3'])
        obs = add_pseudocount(t)
        exp = Table(np.array([[1, 2, 4], [2, 2, 3]]),
                    ['O1', 'O2'],
                    ['S1', 'S2', 'S3'])
        self.assertEqual(obs, exp)

    def test_add_pseudocount2(self):
        t = Table(np.array([[0, 1, 3], [1, 1, 2]]),
                  ['O1', 'O2'],
                  ['S1', 'S2', 'S3'])
        obs = add_pseudocount(t, 2)
        exp = Table(np.array([[2, 3, 5], [3, 3, 4]]),
                    ['O1', 'O2'],
                    ['S1', 'S2', 'S3'])
        self.assertEqual(obs, exp)

    def test_add_pseudocount3(self):
        t = Table(np.array([[0, 1, 3], [1, 1, 2]]),
                  ['O1', 'O2'],
                  ['S1', 'S2', 'S3'])
        obs = add_pseudocount(t, 0.1, True)

        exp = Table(np.array([[0.1, 0.5, 0.6],
                              [0.9, 0.5, 0.4]]),
                    ['O1', 'O2'],
                    ['S1', 'S2', 'S3'])
        self.assertEqual(obs, exp)


if __name__ == '__main__':
    unittest.main()
# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest

from q2_composition import Composition, Balance
from qiime2.plugin.testing import TestPluginBase


class TestTypes(TestPluginBase):
    package = "q2_composition.tests"

    def test_composition_semantic_type_registration(self):
        self.assertRegisteredSemanticType(Composition)

    def test_balance_semantic_type_registration(self):
        self.assertRegisteredSemanticType(Balance)


if __name__ == '__main__':
    unittest.main()
