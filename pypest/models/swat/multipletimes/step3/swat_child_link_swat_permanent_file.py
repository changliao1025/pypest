import sys
import os
import numpy as np
import datetime
import calendar

import glob
import errno
from os.path import isfile, join
from os import listdir

from numpy  import array



from pyearth.system.define_global_variables import *


def create_symlink(source, target_link):
    """
    """
    try:
        os.symlink(source, target_link)
    except OSError as e:
        if e.errno == errno.EEXIST:
            pass
            os.remove(target_link)
            os.symlink(source, target_link)
        else:
            raise e


def swat_child_link_swat_permanent_file(oPest_in, oSwat_in):
    """
    create sym limk of swat files
    """
    
    #strings
    sWorkspace_calibration = oSwat_in.sWorkspace_calibration
    sWorkspace_calibration_case = oSwat_in.sWorkspace_calibration_case
   
    sWorkspace_pest_model = sWorkspace_calibration + slash + 'TxtInOut'

    
    sPath_current = os.getcwd()
    
    sWorkspace_child = sPath_current

    #we will use a tuple
    aExtension = ('.pnd','.rte','.sub','.swq','.wgn','.wus',\
            '.chm','.gw','.hru','.mgt','sdr','.sep',\
             '.sol','ATM','bsn','wwq','deg','.cst',\
             'dat','fig','cio','fin','dat','.pcp','.tmp'  )
            
    for sExtension in aExtension:
        sRegax = sWorkspace_pest_model + slash + '*' + sExtension
        for sFilename in glob.glob(sRegax):
            sBasename_with_extension = os.path.basename(sFilename)
            sLink = sWorkspace_child + slash + sBasename_with_extension
            create_symlink(sFilename, sLink)   

    print('The swat permanent files are prepared successfully!')



