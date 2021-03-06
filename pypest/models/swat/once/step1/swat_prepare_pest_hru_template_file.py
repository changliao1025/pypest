import sys
import os
import numpy as np
import datetime
import calendar
from numpy  import array
from pyearth.system.define_global_variables import *

from pyearth.toolbox.reader.text_reader_string import text_reader_string

def swat_prepare_pest_hru_template_file(oPest_in, oModel_in):
    """
    #prepare the pest template file
    """
    

    #strings    
    sWorkspace_data=oModel_in.sWorkspace_data
    sWorkspace_scratch = oModel_in.sWorkspace_scratch


     
    sWorkspace_project = oModel_in.sWorkspace_project
    

    sWorkspace_data_project = sWorkspace_data + slash + sWorkspace_project

    sWorkspace_calibration_case = oModel_in.sWorkspace_calibration_case

    sWorkspace_pest_model = sWorkspace_calibration_case 
    
    
    #read hru type
    sFilename_hru_combination = sWorkspace_data_project + slash + 'auxiliary' + slash\
     + 'hru' +slash  + 'hru_combination.txt'
    aData_all = text_reader_string(sFilename_hru_combination)
    nhru_type = len(aData_all)


    sFilename_hru_template = sWorkspace_pest_model + slash + 'hru.tpl'
    ofs = open(sFilename_hru_template, 'w')
    sLine = 'ptf $\n'
    ofs.write(sLine)
    #right now we only have one parameter, we can add more later following this format
    sLine = 'hru, cn2\n'
    ofs.write(sLine)
    for iHru_type in range(0, nhru_type):
        sHru_type = "{:03d}".format( iHru_type + 1)
        sLine = 'hru'+ sHru_type + ', ' + '$cn2' + sHru_type +'$\n'
        ofs.write(sLine)
    ofs.close()
    print('hru template is ready!')

    return


  

