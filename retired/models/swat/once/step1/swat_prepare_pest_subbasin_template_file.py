import os
import numpy as np
import datetime
import calendar
from numpy  import array
from pyearth.system.define_global_variables import *

from pyearth.toolbox.reader.text_reader_string import text_reader_string

def swat_prepare_pest_subbasin_template_file(oPest_in, oSwat_in):
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
    iFlag_subbasin = oSwat_in.iFlag_subbasin
   
    nsubbasin = oSwat_in.nsubbasin
    aParameter_subbasin = oSwat_in.aParameter_subbasin
    nvariable = aParameter_subbasin.size
    

    if iFlag_subbasin ==1:

        sFilename_subbasin_template = sWorkspace_pest_model + slash + 'subbasin.tpl'
        ofs = open(sFilename_subbasin_template, 'w')
        sLine = 'ptf $\n'
        ofs.write(sLine)
        #right now we only have one parameter, we can add more later following this format
        sLine = 'subbasin'
        for iVariable in range(nvariable):
            sVariable = aParameter_subbasin[iVariable]
            sLine = sLine + ',' + sVariable
        sLine = sLine + '\n' 

        ofs.write(sLine)

        for iSubbasin in range(0, nsubbasin):
            sSubbasin = "{:03d}".format( iSubbasin + 1)
            sLine = 'subbasin'+ sSubbasin 
            for iVariable in range(nvariable):
                sVariable = aParameter_subbasin[iVariable]
                sValue = ' $' +  sVariable +  sSubbasin  +'$'       
                sLine = sLine + ', ' + sValue 

            sLine = sLine +'\n'
            ofs.write(sLine)
        ofs.close()
        print('subbasin template is ready!')
    else:
        pass
    return