import sys
import os
import numpy as np
import datetime
import calendar
from numpy  import array
from pyearth.system.define_global_variables import *

from pyearth.toolbox.reader.text_reader_string import text_reader_string
def swat_prepare_pest_watershed_template_file(oPest_in, oSwat_in):
    """
    #prepare the pest template file
    """
    

    #strings    
    sWorkspace_data=oSwat_in.sWorkspace_data
    sWorkspace_scratch = oSwat_in.sWorkspace_scratch
    sWorkspace_project = oSwat_in.sWorkspace_project
    

    sWorkspace_data_project = sWorkspace_data + slash + sWorkspace_project

    sWorkspace_calibration_case = oSwat_in.sWorkspace_calibration_case

    sWorkspace_pest_model = sWorkspace_calibration_case 
    iFlag_watershed = oSwat_in.iFlag_watershed

    aParameter_watershed = oSwat_in.aParameter_watershed
    nvariable = aParameter_watershed.size

    if iFlag_watershed ==1:

        sFilename_watershed_template = sWorkspace_pest_model + slash + 'watershed.tpl'
        ofs = open(sFilename_watershed_template, 'w')
        sLine = 'ptf $\n'
        ofs.write(sLine)
        #right now we only have one parameter, we can add more later following this format
        sLine = 'watershed'
        for iVariable in range(nvariable):
            sVariable = aParameter_watershed[iVariable]
            sLine = sLine + ',' + sVariable
        sLine = sLine + '\n'        
        ofs.write(sLine)
        
        
        sLine = 'watershed'
        for iVariable in range(nvariable):
            sVariable = aParameter_watershed[iVariable]
            sLine = sLine + ', $' +  sVariable         
            
        sLine = sLine + '\n'
        
        
        ofs.write(sLine)
        ofs.close()
        print('hru template is ready!')
    else:
        pass

    return