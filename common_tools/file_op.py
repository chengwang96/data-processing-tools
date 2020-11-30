import os
import shutil


def mkdir_if_missing(dir_name):
    if os.path.exists(dir_name):
        if os.path.isdir(dir_name):
            return 0
        else:
            return 2
    else:
        os.makedirs(dir_name)
        return 0


def clean_and_mkdir(dir_name):
    if os.path.exists(dir_name):
        if os.path.isdir(dir_name):
            shutil.rmtree(dir_name)
        else:
            return 2

    os.makedirs(dir_name)
    return 0
