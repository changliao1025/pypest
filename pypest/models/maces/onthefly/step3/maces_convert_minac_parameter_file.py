import sys, os
import numpy as np
from shutil import copy2
sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system.define_global_variables import *

from pyes.toolbox.reader.text_reader_string import text_reader_string

#the pypest library
sPath_pypest = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest)

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces
from pypest.template.shared.xmlchange import xmlchange

def maces_convert_minac_parameter_file(oPest_in, oModel_in):
    sWorkspace_pest_model = oPest_in.sWorkspace_pest

    iFlag_debug = 1
    if(iFlag_debug == 1 ):
        sPath_current = sWorkspace_pest_model + slash + 'beopest1'
    else:
        sPath_current = os.getcwd()
    sWorkspace_child = sPath_current    
    sFilename_parameter = sWorkspace_child + slash + oModel_in.sFilename_parameter_minac
    sFilename_config =  sWorkspace_child + slash + os.path.basename(oModel_in.sFilename_config_minac)
    if os.path.isfile(sFilename_parameter):
        pass
    else:
        print('The file does not exist!')
        return
        
    aData_all = text_reader_string(sFilename_parameter, cDelimiter_in = ',')
    aDummy = aData_all[:,0]
    nParameter = len(aDummy) 
    aParameter_list = aDummy

    ngrid = 1 
    #aParameter_value = (aData_all[1:ngrid+1,1: nParameter+1]).astype(float)
    aParameter_value = (aData_all[:, 1]).astype(float)
    aParameter_value = np.asarray(aParameter_value)
    
    #second we will call the existing python function to convert
    #construct the command string
    #./xmlchange.py -f optpar_minac.xml -g M12MOD -p rhoSed -v 2650.0

    for p in range(0, nParameter):    
        sValue =  "{:16.2f}".format( aParameter_value[p] )
        #sCommand = '-f' + sFilename + ' -g M12MOD -p rhoSed -v '  + sValue
        xmlchange(filename=sFilename_config, group='F06MOD', parameter=aParameter_list[p],value=sValue.strip())

    return