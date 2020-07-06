import sys, os
import numpy as np

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system import define_global_variables
from pyes.system.define_global_variables import *

sPath_pypest = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest)

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces



from pypest.models.maces.offthegrid.step1.pypest_prepare_maces_hydro_template_file import pypest_prepare_maces_hydro_template_file



def pypest_prepare_pest_template_files(oPest_in, oModel_in):
    pypest_prepare_maces_hydro_template_files(oPest_in, oModel_in)
    return 

if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest_python/pypest/models/maces/config/pypest.xml'
    aParameter  = pest_read_configuration_file(sFilename_pest_configuration)
    print(aParameter)    
    oPest = pypest(aParameter)


    sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest_python/pypest/models/maces/config/model.xml'
    aParameter  = pest_read_configuration_file(sFilename_model_configuration)
    print(aParameter)    
    oMaces = pest(aParameter)
    pypest_prepare_pest_template_files(oPest, oMaces)
