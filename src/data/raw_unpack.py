import tarfile
import os


def unpack_tar_file(file: str = "cal_housing.tgz"):
    """
    Unpack zipped file into present directory.
    """
    with tarfile.open(file) as tar:
        tar.extractall()

    # with open("cal_housing.domain") as file:
    #     lines = file.readlines()

