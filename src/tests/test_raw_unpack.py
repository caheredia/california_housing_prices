from src.data.raw_unpack import get_raw_df
from unittest import TestCase
import pandas as pd


class TestRawUnpack(TestCase):
    def test_raw_unpack(self):
        test_df = get_raw_df()
        self.assertIsInstance(test_df, pd.DataFrame)
