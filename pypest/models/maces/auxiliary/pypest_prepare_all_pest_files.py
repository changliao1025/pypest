import sys, os
import numpy as np
import xml.etree.ElementTree as ET

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system.define_global_variables import *

#the pypest library
sPath_pypest = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest)

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces

from pypest.models.maces.offthegrid.run_step0 import run_step0
from pypest.models.maces.offthegrid.run_step1 import run_step1
from pypest.models.maces.offthegrid.run_step2 import run_step2
from pypest.models.maces.offthegrid.run_step6 import run_step6

#from pest_prepare_maces_run_bash_file import pest_prepare_maces_run_bash_file
from pypest.template.shared.pypest_read_configuration_file import pypest_read_configuration_file


def pypest_prepare_all_pest_files(oPest_in, oModel_in):
    
    #call each step
    
    run_step0(oPest_in, oModel_in)
    run_step1(oPest_in, oModel_in)
    run_step2(oPest_in, oModel_in)
    run_step6(oPest_in, oModel_in)

    return


if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/pypest.xml'
    sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/model_calibration.xml'

    aParameter_pest  = pypest_read_configuration_file(sFilename_pest_configuration)    
    aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration
    oPest = pypest(aParameter_pest)


    #we need to add the alternative model information into the model
    aMinac_models = ['F06', 'T03', 'KM12', 'M12', 'F07', 'VDK05', 'DA07']
    aOmac_model = models = ['M12', 'DA07', 'KM12', 'K16']

    aParameter_model  = pypest_read_configuration_file(sFilename_model_configuration)   
    aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration
    oMaces = maces(aParameter_model)

    #use loop to control multiple calication
    for sMinac_model in aMinac_models:
        oMaces.sModel_minac = 'T03'#sMinac_model
        for sOmac_model in aOmac_model:
            oMaces.sModel_omac = sOmac_model
            oMaces.sModel_minac = 'Null' #sOmac_model
            pypest_prepare_all_pest_files(oPest, oMaces)
            break
