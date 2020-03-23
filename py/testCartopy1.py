#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
testCartopy1

@author: jrminter

see https://scitools.org.uk/cartopy/docs/latest/index.html

Created on Mon Mar 23 15:20:50 2020
"""

import cartopy.crs as ccrs
import matplotlib.pyplot as plt

ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()

# Save the plot by calling plt.savefig() BEFORE plt.show()
plt.savefig('testCartopy1.pdf')
# plt.savefig('testCartopy1.png')

plt.show()