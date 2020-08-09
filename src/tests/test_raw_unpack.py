from src.data.raw_unpack import get_raw_df
from unittest import TestCase
import pandas as pd


class TestRawUnpack(TestCase):
    def test_raw_unpack(self):
        test_df = get_raw_df()
        # test instance
        self.assertIsInstance(test_df, pd.DataFrame)

        # test columns
        columns = [
            "housingMedianAge",
            "medianIncome",
            "latitude",
            "totalBedrooms",
            "households",
            "medianHouseValue",
            "totalRooms",
            "population",
            "longitude",
        ]
        self.assertSetEqual(set(test_df.columns), set(columns))

        # test type
        self.assertEqual(test_df["longitude"].dtype.name, "float64")
