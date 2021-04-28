import sys, os
import numpy as np
from shutil import copy2
sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyearth.system.define_global_variables import *

from pyearth.toolbox.reader.text_reader_string import text_reader_string

#the pypest library
sPath_pypest = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest)

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces
from pypest.template.shared.xmlchange import xmlchange

def maces_convert_omac_parameter_file(oPest_in, oModel_in):
    sWorkspace_pest_model = oPest_in.sWorkspace_pest
    sWorkspace_calibration_case = oModel_in.sWorkspace_calibration_case
    iFlag_debug = 0
    if(iFlag_debug == 1 ):
        sPath_current = sWorkspace_calibration_case + slash + 'child1'
    else:
        sPath_current = os.getcwd()


    sFilename_parameter = sPath_current + slash + oModel_in.sFilename_parameter_omac
    sFilename_config = sPath_current + slash + os.path.basename(oModel_in.sFilename_config_omac)

    if os.path.isfile(sFilename_parameter):
        pass
    else:
        print('The file does not exist!'+ sFilename_parameter)
        return
        
    aData_all = text_reader_string(sFilename_parameter, cDelimiter_in = ',')
    aDummy = aData_all[:,0]
    nParameter = len(aDummy) 
    aParameter_list = aDummy

    ngrid = 1 
    aParameter_value = (aData_all[:, 1]).astype(float)
    aParameter_value = np.asarray(aParameter_value)
    
    #second we will call the existing python function to convert
    #construct the command string
    #./xmlchange.py -f optpar_minac.xml -g M12MOD -p rhoSed -v 2650.0

    #aParameter = ['d50']

    for p in range(0, nParameter):    
        sValue =  "{:16.2f}".format( aParameter_value[p] )
        #sCommand = '-f' + sFilename + ' -g M12MOD -p rhoSed -v '  + sValue
        xmlchange(filename=sFilename_config,  group='M12MOD',parameter=aParameter_list[p],value=sValue.strip())

    return