"""
Tests that FASTA files can be loaded.
"""
import os
import unittest

import deepchem as dc


class TestFASTALoader(unittest.TestCase):
  """
  Test FASTALoader
  """

  def setUp(self):
    super(TestFASTALoader, self).setUp()
    self.current_dir = os.path.dirname(os.path.abspath(__file__))

  def test_fasta_load(self):
    legacy = False # Whether to assume legacy one hot encoding shape from FASTA loader.

    input_file = os.path.join(self.current_dir,
                              "../../data/tests/example.fasta")
    loader = dc.data.FASTALoader()
    sequences = loader.create_dataset(input_file)

    # example.fasta contains 3 sequences each of length 58.
    # The one-hot encoding turns base-pairs into vectors of length 5 (ATCGN).
    # There is one "image channel".
    if (legacy == True):
      assert sequences.X.shape == (3, 5, 58, 1)
    else:
      assert sequences.X.shape == (3, 58, 6)
