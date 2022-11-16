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
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar, path="raw")


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
