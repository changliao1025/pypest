import sys
import os
import datetime
import calendar
import julian  #to covert datetime to julian date 
import platform #platform independent

import numpy as np
from pathlib import Path
from numpy  import array
from calendar import monthrange #calcuate the number of days in a month



#import the pyes library
sPath_library_python = sWorkspace_code +  slash + 'python' + slash + 'library' + slash + 'pyes_python'
sys.path.append(sPath_library_python)
from toolbox.reader.text_reader_string import text_reader_string

#import swat library
sPath_modflow_python = sWorkspace_code +  slash + 'python' + slash + 'swat' + slash + 'modflow_python'
sys.path.append(sPath_modflow_python)
#from swat.calibration.swat_write_watershed_input_file import swat_write_watershed_input_file
#from swat.calibration.swat_write_subbasin_input_file import swat_write_subbasin_input_file
from swat.calibration.swat_write_hru_input_file import swat_write_hru_input_file

def modflow_prepare_input_from_pest(sFilename_configuration_in, sModel):
    """
    sFilename_configuration_in
    """
    #hru level
    swat_write_hru_input_file(sFilename_configuration_in, sModel)


if __name__ == '__main__':

    sRegion = 'tinpan'
    sModel ='swat'
    sCase = 'test'
    sJob = sCase
    sTask = 'simulation'
    iFlag_simulation = 1
    iFlag_calibration = 0
    if iFlag_calibration == 1:
        sTask = 'calibration'
    sFilename_configuration = sWorkspace_scratch + slash + '03model' + slash \
              + sModel + slash + sRegion + slash \
              + sTask  + slash + sFilename_config
    modflow_prepare_input_from_pest(sFilename_configuration_in, sModel)
   
