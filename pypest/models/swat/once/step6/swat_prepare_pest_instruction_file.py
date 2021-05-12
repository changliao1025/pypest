import sys
import os
import numpy as np
import datetime

from numpy  import array

from pyearth.system.define_global_variables import *

from pyearth.toolbox.reader.text_reader_string import text_reader_string




def swat_prepare_pest_instruction_file(oPest_in, oModel_in):
    """
    prepare pest instruction file
    """
    
    
    
    sWorkspace_scratch=oModel_in.sWorkspace_scratch 

    sWorkspace_data =  oModel_in.sWorkspace_data 
    sWorkspace_project =  oModel_in.sWorkspace_project 
   

    sRegion =  oModel_in.sRegion 
    sModel =  oModel_in.sModel 

    
    sWorkspace_data_project = sWorkspace_data + slash + sWorkspace_project

    sWorkspace_calibration_case = oModel_in.sWorkspace_calibration_case

    sWorkspace_pest_model = sWorkspace_calibration_case 
    sWorkspace_simulation_copy = oModel_in.sWorkspace_simulation_copy

    iYear_start =  oModel_in.iYear_start  
  
    iYear_end  =   oModel_in.iYear_end  
    #nsegment =  oModel_in.nsegment  
  
    nstress = oModel_in.nstress

    sFilename_observation = sWorkspace_data_project + slash + 'auxiliary' + slash \
        + 'usgs' + slash + 'discharge' + slash + 'discharge_observation.txt'
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
    for i in range(0, nstress):
        dDummy = aDischarge_observation[i]
        if( dDummy != missing_value  ):
            sLine = 'l1' + ' !discharge' + "{:04d}".format(i+1) + '!\n'
        else:
            sLine = 'l1' + ' !dum' + '!\n'
        ofs.write(sLine)
            
    ofs.close()
    print('The instruction file is prepared successfully!')