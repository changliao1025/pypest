import sys
import os
import numpy as np
import datetime
import calendar


import os, errno
from os.path import isfile, join
from os import listdir

from numpy  import array

from pypest.models.swat.multipletimes.step3.swat_child_copy_swat_executable_file import swat_child_copy_swat_executable_file
from pypest.models.swat.multipletimes.step3.swat_child_link_swat_permanent_file import swat_child_link_swat_permanent_file
 
def swat_prepare_pest_child_input_file(oPest_in, oModel_in):
    """
    prepare the input files for the child simulation
    """

    sWorkspace_calibration_case = oModel_in.sWorkspace_calibration_case
   
    sWorkspace_pest_model = sWorkspace_calibration_case
    
    #get current directory
    sPath_current = os.getcwd()

    if (os.path.normpath(sPath_current)  == os.path.normpath(sWorkspace_pest_model)):
        print('This is the master directory, no need to copy anything')
    else:
        swat_child_copy_swat_executable_file(oPest_in, oModel_in)
        swat_child_link_swat_permanent_file(oPest_in, oModel_in)
        print('The swat child files are prepared successfully!')


