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
    # extract columns
    columns_file = os.path.join(
        DATA_DIR, raw_dir, "CaliforniaHousing", "cal_housing.domain"
    )
    with open(columns_file) as file:
        lines = file.readlines()
    columns = [line.split(":")[0] for line in lines]

    # load DataFrame
    data_file = os.path.join(DATA_DIR, raw_dir, "CaliforniaHousing", "cal_housing.data")
    raw_df = pd.read_csv(data_file, names=columns)

    return raw_df


def get_raw_df():
    """
    Returns the raw data as a DataFrame
    """
    unpack_tar_file()
    return load_raw_data_to_df()
