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



def pypest_prepare_maces_hydro_template_file(oPest_in, oModel_in ):

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

