#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:36:41 2020

@author: jrminter
"""
import os
os.environ['PROJ_LIB'] = '/Users/jrminter/miniconda3/share/proj'
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
# import netCDF4
from netCDF4 import Dataset, date2index

plt.figure()

base_path = '/Users/jrminter/Documents/git/earth-science-maps/data/netcdf/'
fi = "2020032212000.nc"

pth = base_path + fi
print(pth)

dataset = Dataset(base_path)

