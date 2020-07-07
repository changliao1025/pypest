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
from pypest.template.shared.pypest_read_configuration_file import pypest_read_configuration_file

def pypest_prepare_maces_hydro_template_file(oPest_in, oModel_in ):

   
    sWorkspace_calibration_relative = oModel_in.sWorkspace_calibration        
    sWorkspace_calibration = sWorkspace_scratch + slash + sWorkspace_calibration_relative    
    sWorkspace_pest_model = sWorkspace_calibration
    #read obs
    sIndex = "{:02d}".format( 0 )  
    sFilename_hydro_parameter_template = sWorkspace_pest_model + slash + 'pest_parameter_' + sIndex + '.tpl'
    
    ofs = open(sFilename_hydro_parameter_template, 'w')
    sLine = 'ptf $\n'
    ofs.write(sLine)    
    #the first parameter group
    sLine = 'Cz0' + ', ' + '$Cz0'  +'$\n'
    ofs.write(sLine)
    ofs.close()
    print('hydro template file is ready!')
    return

#we need to prepare the template files for all possible parameters
#in general, a model may have more than one parameter file for different components

def pypest_prepare_pest_template_files(oPest_in, oModel_in):
    pypest_prepare_maces_hydro_template_file(oPest_in, oModel_in)
    return 


def step1(sFilename_pest_configuration_in, sFilename_model_configuration_in):    
    aParameter_pest  = pypest_read_configuration_file(sFilename_pest_configuration)    
    aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration
    oPest = pypest(aParameter_pest)
    aParameter_model  = pypest_read_configuration_file(sFilename_model_configuration)   
    aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration
    oMaces = maces(aParameter_model)

    pypest_prepare_pest_template_files(oPest, oMaces)
    return
if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/03configuration/pypest/maces/pest.xml'
    sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/model.xml'    
    step1(sFilename_pest_configuration, sFilename_model_configuration)
