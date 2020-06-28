import sys, os
import numpy as np

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from eslib.system import define_global_variables
from eslib.system.define_global_variables import *

sPath_pypest_python = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest_python'
sys.path.append(sPath_pypest_python)

from pypest.models.maces.inputs.pest import pest
from pypest.models.maces.inputs.pest_read_configuration_file import pest_read_configuration_file

def pest_prepare_maces_hydro_template_file(oPest_in ):

    sWorkspace_scratch = oPest_in.sWorkspace_scratch
    sWorkspace_calibration_relative = oPest_in.sWorkspace_calibration        
    sWorkspace_calibration = sWorkspace_scratch + slash + sWorkspace_calibration_relative    
    sWorkspace_pest_model = sWorkspace_calibration
    #read obs
    
    sFilename_hydro_parameter_template = sWorkspace_pest_model + slash + oPest_in.sFilename_hydro_template
    ofs = open(sFilename_hydro_parameter_template, 'w')
    sLine = 'ptf $\n'
    ofs.write(sLine)    
    #the first parameter group
    sLine = 'Cz0' + ', ' + '$Cz0'  +'$\n'
    ofs.write(sLine)
    ofs.close()
    print('hru template is ready!')
    return
if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/03configuration/pypest/maces/pest.xml'
    aParameter  = pest_read_configuration_file(sFilename_pest_configuration)
    print(aParameter)    
    oPest = pest(aParameter)
    pest_prepare_maces_hydro_template_file(oPest)
