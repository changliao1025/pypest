import sys
import os
import datetime
import calendar
import numpy as np
from numpy  import array



from pyearth.toolbox.reader.text_reader_string import text_reader_string


from swat.calibration.swat_write_hru_input_file import swat_write_hru_input_file

def swat_prepare_input_from_pest(sFilename_configuration_in, sModel):
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
    iFlag_pest = 0
    if iFlag_pest == 1:
        sTask = 'calibration'
    sFilename_configuration = sWorkspace_scratch + slash + '03model' + slash \
              + sModel + slash + sRegion + slash \
              + sTask  + slash + sFilename_config
    swat_prepare_input_from_pest(sFilename_configuration_in, sModel)
   
