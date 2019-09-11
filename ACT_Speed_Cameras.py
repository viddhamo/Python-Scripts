## Script to read ACT Speed Cameras data set and project them on maps
## Author : Vid Dhamodaran
## Initial Version : 13/06/2019

#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import gmaps

#Configure Gmaps
gmaps.configure(api_key='AIzaSyDOEsV16WxZkLwFj_Ysh2FyXNO2aYutnys')

new_york_coordinates = (40.75, -74.00)
gmaps.figure(center=new_york_coordinates, zoom_level=12)



