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
    sDate_in = None,  sModel_type_in=None,sWorkspace_input_in=None,sWorkspace_output_in=None):

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
    
    
    
    #iYear_start  = int( aConfig['iYear_start'])
    #iMonth_start  = int(  aConfig['iMonth_start'])
    #iDay_start  = int(  aConfig['iDay_start'] )
    #iYear_end  = int( aConfig['iYear_end'])
    #iMonth_end  = int(  aConfig['iMonth_end'])
    #iDay_end  = int(  aConfig['iDay_end'])   

    #by default, this system is used to prepare inputs for modflow simulation.
    #however, it can also be used to prepare gsflow simulation inputs.

    #based on global variable, a few variables are calculate once
    #calculate the modflow simulation period
    #https://docs.python.org/3/library/datetime.html#datetime-objects
    
    
    #dummy1 = datetime.datetime(iYear_start, iMonth_start, iDay_start)
    #dummy2 = datetime.datetime(iYear_end, iMonth_end, iDay_end)
    #julian1 = julian.to_jd(dummy1, fmt='jd')
    #julian2 = julian.to_jd(dummy2, fmt='jd')
    #nstress =int( julian2 - julian1 + 1 )  
    #aConfig['lJulian_start'] =  julian1
    #aConfig['lJulian_end'] =  julian2
    #aConfig['nstress'] =   nstress     
   
    
    #data
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
            sWorkspace_output_in = oPest.sWorkspace_output_model)       
    
        oPest.pSwat = oSwat      
    
    return oPest