import sys
import os
import numpy as np
import datetime

from numpy  import array

from pyearth.system.define_global_variables import *

from pyearth.toolbox.reader.text_reader_string import text_reader_string




def swat_prepare_pest_instruction_file(oPest_in, oSwat_in):
    """
    prepare pest instruction file
    """
    
    
    
    sWorkspace_scratch=oSwat_in.sWorkspace_scratch 

    sWorkspace_data =  oSwat_in.sWorkspace_data 
    sWorkspace_project =  oSwat_in.sWorkspace_project 
   

    sRegion =  oSwat_in.sRegion 
    sModel =  oSwat_in.sModel 

    
    sWorkspace_data_project = sWorkspace_data + slash + sWorkspace_project

    sWorkspace_calibration_case = oSwat_in.sWorkspace_calibration_case

    sWorkspace_pest_model = sWorkspace_calibration_case 
    sWorkspace_simulation_copy = oSwat_in.sWorkspace_simulation_copy

    iYear_start =  oSwat_in.iYear_start  
    iYear_end  =   oSwat_in.iYear_end  
    #nsegment =  oSwat_in.nsegment  
  
    nstress = oSwat_in.nstress
    nstress_month = oSwat_in.nstress_month

    sFilename_observation = sWorkspace_data_project + slash + 'auxiliary' + slash \
        + 'usgs' + slash + 'discharge' + slash + 'discharge_observation_monthly.txt'
    if os.path.isfile(sFilename_observation):
        pass
    else:
        print(sFilename_observation + ' is missing!')
        return
    aData = text_reader_string(sFilename_observation)
    aDischarge_observation = array( aData ).astype(float) 
    nobs_with_missing_value = len(aDischarge_observation)
    
    aDischarge_observation = np.reshape(aDischarge_observation, nobs_with_missing_value)
    nan_index = np.where(aDischarge_observation == missing_value)

    #write instruction
    sFilename_instruction = sWorkspace_pest_model + slash + oPest_in.sFilename_instruction
    ofs= open(sFilename_instruction,'w')
    ofs.write('pif $\n')

    #we need to consider that there is missing value in the observations

    #changed from daily to monthly
    for i in range(0, nstress_month):
        dDummy = aDischarge_observation[i]
        if( dDummy != missing_value  ):
            sLine = 'l1' + ' !discharge' + "{:04d}".format(i+1) + '!\n'
        else:
            sLine = 'l1' + ' !dum' + '!\n'
        ofs.write(sLine)
            
    ofs.close()
    print('The instruction file is prepared successfully!')