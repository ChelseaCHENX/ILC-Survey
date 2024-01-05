import pandas as pd
from pandas.api.types import CategoricalDtype
import numpy as np
from math import *
from collections import Counter

import scanpy as sc
# import scvelo as scv

import os
import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

def run(cmd):
    proc = subprocess.Popen([cmd], shell=True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    return proc.returncode, stdout, stderr

def getarg(argv, index, default=None):
    if len(argv) > index:
        ret = argv[index]
    else:
        ret = default
    return ret

def read_gmt(fpath):
    gdict = {}
    
    with open(fpath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            items = line.strip().rstrip().split('\t')
            gset = items[0].lower()
            genes = items[2:]
            gdict[gset] = genes            
    return gdict

def write_gmt(gdict, fpath):  
    with open(fpath, 'w') as f:
        for key, val in gdict.items():
            val_string = '\t'.join(val)
            f.write('%s\thttp\t%s\n'%(key, val_string))            
    print('finished writing %d gene sets to %s'%(len(gdict), fpath))

    