import sys
import os
import datetime
import calendar
import julian  #to covert datetime to julian date 
import platform #platform independent
import numpy as np
from numpy  import array

from calendar import monthrange #calcuate the number of days in a month



from toolbox.reader.text_reader_string import text_reader_string

sPath_modflow_python = sWorkspace_code +  slash + 'python' + slash + 'modflow' + slash + 'modflow_python'
sys.path.append(sPath_modflow_python)
from swat.postprocess.swat_extract_stream_discharge import swat_extract_stream_discharge


def modflow_extract_output_for_pest(sFilename_configuration_in, sModel):
    """
    sFilename_configuration_in
    """
    #stream discharge
    swat_extract_stream_discharge(sFilename_configuration_in, sModel)


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

    



    modflow_extract_output_for_pest(sFilename_configuration_in, sCase, sJob, sModel)
   
