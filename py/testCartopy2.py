#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
testCartopy2

@author: jrminter

see https://scitools.org.uk/cartopy/docs/latest/index.html

Created on Mon Mar 23 15:25:50 2020
"""

# testCartopy2.py

import cartopy.crs as ccrs
import matplotlib.pyplot as plt

ax = plt.axes(projection=ccrs.Mollweide())
ax.stock_img()
plt.savefig('testCartopy2.pdf')
# plt.savefig('testCartopy2.png')
plt.show()