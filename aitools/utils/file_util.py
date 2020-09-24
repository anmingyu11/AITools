import pathlib
from pathlib import Path
import shutil
import os

from utils import logger

from tqdm import tqdm

import pandas as pd


def mkdir(path):
    if not exists(path):
        try:
            pathlib.Path(path).mkdir(parents=False, exist_ok=False)
        except Exception as e:
            print(e)
    else:
        logger.error(' File {} has exists '.format(path))


def exists(path):
    return pathlib.Path(path).exists()


def search(root, pattern):
    p = Path(root)
    return list(p.rglob(pattern))


def rename(target, new_target):
    p_old = Path(target)
    p_new = Path(new_target)
    p_old.rename(p_new)


def cp_file(source, target):
    p_source = Path(source)
    p_target = Path(target)
    shutil.copy(str(p_source.absolute()), str(p_target.absolute()))


def cp_dir(source, target):
    mkdir(target)
    p_source = Path(source)
    p_target = Path(target)
    fl = os.listdir(p_source.absolute())
    for f in fl:
        f_source = str(p_source.absolute()) + '/' + f
        f_target = str(p_target.absolute()) + '/' + f
        cp_file(f_source, f_target)
    pass

def combine_csv(csv_files):
    path_list = csv_files
    dfs = []
    pbar = tqdm(path_list)
    for raw_path in path_list:
        pbar.update(1)
        df = pd.read_csv(raw_path)
        dfs.append(df)
    pbar.close()
    dfs = pd.concat(dfs)
    dfs = dfs.reset_index(drop = True)
    return dfs

def remove(path):
    os.remove(path)
