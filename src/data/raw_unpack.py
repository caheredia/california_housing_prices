import os
import tarfile
from src.data.helpers import DATA_DIR
import pandas as pd


def unpack_tar_file(file: str = "cal_housing.tgz"):
    """
    Unpack zipped file into present directory.
    """
    file = os.path.join(DATA_DIR, "raw", file)
    with tarfile.open(file) as tar:
        tar.extractall(path="raw")


def load_raw_data_to_df(raw_dir: str = "raw") -> pd.DataFrame:
    """
    Load raw data into pandas DataFrames.
    """
    # load DataFrame
    raw_df = pd.DataFrame(
        os.path.join(DATA_DIR, "CaliforniaHousing", "cal_housing.data")
    )
    # with open("cal_housing.domain") as file:
    #     lines = file.readlines()
    return raw_df


def get_raw_df():
    """
    Returns the raw data as a DataFrame
    """
    unpack_tar_file()
    return load_raw_data_to_df()


# columns = [line.split(":")[0] for line in lines]
