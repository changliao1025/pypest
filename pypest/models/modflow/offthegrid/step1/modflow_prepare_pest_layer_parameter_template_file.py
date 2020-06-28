import sys
import os
import numpy as np
import datetime
import calendar
import julian
import platform 

from pathlib import Path
from numpy  import array

#import the eslib library
sPath_library_python = sWorkspace_code +  slash + 'python' + slash + 'library' + slash + 'eslib_python'

sys.path.append(sPath_library_python)
from toolbox.reader.text_reader_string import text_reader_string

sExtension_envi = '.dat'
sExtension_header = '.hdr'
sExtension_txt = '.txt'

def modflow_prepare_pest_hru_template_file(sFilename_configuration_in, sModel):
    """
    #prepare the pest template file
    """
  
    if sCase_in is not None:
        print(sCase_in)
        sCase = sCase_in
    else:
        #by default, this model will run in steady state
        sCase = 'ss'
    if sJob_in is not None:
        sJob = sJob_in
    else:
        sJob = 'modflow'
    if sModel_in is not None:
        print(sModel_in)
        sModel = sModel_in
    else:
        sModel = 'modflow' #the default mode is modflow

    #strings
    sWorkspace_home = config['sWorkspace_home']
    sWorkspace_scratch=config['sWorkspace_scratch']

    sWorkspace_data_relative = config['sWorkspace_data']
     
    sWorkspace_project_relative = config['sWorkspace_project']
    sWorkspace_simulation_relative = config['sWorkspace_simulation']
    sWorkspace_calibration_relative = config['sWorkspace_calibration']

    pest_mode =  config['pest_mode'] 
    sRegion = config['sRegion']

    sWorkspace_data = sWorkspace_scratch + slash + sWorkspace_data_relative
    sWorkspace_data_project = sWorkspace_data + slash + sWorkspace_project_relative

    sWorkspace_simulation = sWorkspace_scratch +  slash  + sWorkspace_simulation_relative + slash + sCase
    sWorkspace_calibration = sWorkspace_scratch + slash + sWorkspace_calibration_relative + slash + sCase

    #sWorkspace_pest_model = sWorkspace_calibration #+ slash + sModel
    
    sFilename_upw_template = sWorkspace_calibration + slash + 'upw_parameter.tpl'

    sLine = 'ptf $\n'
    ofs.write(sLine)
    #right now we only have one parameter, we can add more later following this format
    #sLine = 'upw, hk, ansi, sy, ss\n'

    ofs = open(sFilename_upw_template, 'w')
    for iLayer in range( 1, nLayer+ 1):
        sLayer = "{:02d}".format( iLayer )

        #read aquifer type 
        sFilename_aquifer_type = sWorkspace_data_project + slash + 'raster' + slash + 'geology' + slash + 'rock_type' + sLayer + sExtension_envi
        ifs = open(sFilename_aquifer_type, 'rb')
        aRock_type = np.fromfile(ifs, '<f4')
        aRock_type.shape = (nrow, ncolumn)
        ifs.close()

        nRock_type = max(aRock_type)


        for iRock_type in range(nRock_type):
            sRock_type = "{:02d}".format( iRock_type + 1)
            sLine = 'hk'+ sLayer + sRock_type + ', ' + '$hk' + sLayer + sRock_type +'$\n'
            ofs.write(sLine)

            sLine = 'anis'+ sLayer + sRock_type + ', ' + '$anis' + sLayer + sRock_type +'$\n'
            ofs.write(sLine)

            sLine = 'sy'+ sLayer + sRock_type + ', ' + '$sy' + sLayer + sRock_type +'$\n'
            ofs.write(sLine)

            sLine = 'ss'+ sLayer + sRock_type + ', ' + '$ss' + sLayer + sRock_type +'$\n'
            ofs.write(sLine)

    ofs.close()
    
    print('layer parameter template is ready!')

    return
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
       
    
    modflow_prepare_pest_hru_template_file(sFilename_configuration_in, sModel)