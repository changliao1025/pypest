#this function is used to copy the swat from calibration folder to the current slave folder
import sys
import os
import datetime
import calendar

import glob

import numpy as np
from numpy  import array
from shutil import copyfile, copy2



from pyearth.system.define_global_variables import *

from pyswat.simulation.swat_copy_executable_file import swat_copy_executable_file


def swat_child_copy_swat_executable_file(oPest_in, oModel_in):
    """
    copy swat to local slave directory
    """
    

    

    swat_copy_executable_file(oModel_in)
    
    
    
    print('Finished copying swat in slave directory')


