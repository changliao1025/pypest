import os 
import sys #used to add system path

import datetime
import json
import numpy as np
import pyearth.toolbox.date.julian as julian
from pypest.classes.pycase import pestcase
from swaty.classes.pycase import swatcase

from swaty.swaty_read_model_configuration_file import swaty_read_model_configuration_file


pDate = datetime.datetime.today()
sDate_default = "{:04d}".format(pDate.year) + "{:02d}".format(pDate.month) + "{:02d}".format(pDate.day)

def pypest_read_model_configuration_file(sFilename_configuration_in, \
    iCase_index_in = None , \
    iFlag_read_discretization_in =None,\
    sDate_in = None,  sModel_type_in=None,sWorkspace_input_in=None,sWorkspace_output_in=None, aParameter_in = None):

    if not os.path.isfile(sFilename_configuration_in):
        print(sFilename_configuration_in + ' does not exist')
        return
    
    # Opening JSON file
    with open(sFilename_configuration_in) as json_file:
        aConfig = json.load(json_file)   


    if sDate_in is not None:
        sDate = sDate_in
    else:
        sDate = aConfig["sDate"]
        pass
    if sModel_type_in is not None:
        sModel_type = sModel_type_in
    else:
        sModel_type = aConfig["sModel_type"]
        pass

    if iCase_index_in is not None:        
        iCase_index = iCase_index_in
    else:       
        iCase_index = int( aConfig['iCase_index'])
        pass  
    
    if sWorkspace_input_in is not None:
        sWorkspace_input = sWorkspace_input_in
    else:
        sWorkspace_input = aConfig["sWorkspace_input"]
        pass

    if sWorkspace_output_in is not None:
        sWorkspace_output = sWorkspace_output_in
    else:
        sWorkspace_output = aConfig["sWorkspace_output"]
        pass

    aConfig["sDate"] = sDate
    aConfig["sMesh_sModel_typetype"] = sModel_type
    aConfig["iCase_index"] = iCase_index
    aConfig["sWorkspace_input"] = sWorkspace_input
    aConfig["sWorkspace_output"] = sWorkspace_output
    oPest = pestcase(aConfig)
    if oPest.sModel_type == 'swat':

        sFilename_model_configuration = oPest.sFilename_model_configuration
        oSwat = swaty_read_model_configuration_file(sFilename_model_configuration,  \
            iFlag_read_discretization_in = iFlag_read_discretization_in,\
            iFlag_standalone_in = 0,\
            sWorkspace_output_in = oPest.sWorkspace_output_model, aParameter_in=aParameter_in)  

        oSwat.sPython =  oPest.sPython 
    
        oPest.pSwat = oSwat      
    
    return oPest