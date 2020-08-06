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


#we also need a parameter file for the first run
def maces_prepare_minac_f06_parameter_file(oPest_in, oModel_in ):

    sWorkspace_pest = oPest_in.sWorkspace_pest
    sWorkspace_pest_model = sWorkspace_pest
    #read obs
    iFlag_debug = 1
    if(iFlag_debug == 1 ):
        sPath_current = sWorkspace_pest_model + slash + 'beopest1'
    else:
        sPath_current = os.getcwd()

    
    sFilename = sPath_current + slash + oModel_in.sFilename_parameter_minac 
    ofs = open(sFilename, 'w')
    
    #the first parameter group
    sLine = 'd50' + ', ' + '50'  + '\n'
    ofs.write(sLine)
    sLine = 'rhoSed' + ', ' + '2000'  + '\n'
    ofs.write(sLine)
    sLine = 'porSed' + ', ' + '0.5'  + '\n'
    ofs.write(sLine)
    sLine = 'tauD_cr' + ', ' + '50'  + '\n'
    ofs.write(sLine)
    
    
    ofs.close()
    print('minac F06 parameter file is ready!')
    return

#the model could have more than one parameter file
#the number of parameter file should be same as the template file
def maces_prepare_minac_f06_template_file(oPest_in, oModel_in ):

    sWorkspace_pest = oPest_in.sWorkspace_pest
    sWorkspace_pest_model = sWorkspace_pest
    
    
    sFilename = sWorkspace_pest_model + slash + oModel_in.sFilename_template_minac 
    ofs = open(sFilename, 'w')
    sLine = 'ptf $\n'
    ofs.write(sLine)    
    #the first parameter group
    sLine = 'd50' + ', ' + '$d50'  +'$\n'
    ofs.write(sLine)
    sLine = 'rhoSed' + ', ' + '$rhoSed'  +'$\n'
    ofs.write(sLine)
    sLine = 'porSed' + ', ' + '$porSed'  +'$\n'
    ofs.write(sLine)
    sLine = 'tauD_cr' + ', ' + '$tauD_cr'  +'$\n'
    ofs.write(sLine)

    ofs.close()
    print('minac template file is ready!')

    
    
    
    return
def maces_prepare_minac_template_file(oPest_in, oModel_in ):

    maces_prepare_minac_f06_template_file(oPest_in, oModel_in )
    maces_prepare_minac_f06_parameter_file(oPest_in, oModel_in )
    #if you need to calibrate other submodules, add it here
    return