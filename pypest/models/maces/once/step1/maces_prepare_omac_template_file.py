import sys, os
import numpy as np
from pathlib import Path
sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system import define_global_variables
from pyes.system.define_global_variables import *

sPath_pypest = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest)

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces


#we also need a parameter file for the first run
def maces_prepare_omac_m12_parameter_file(oPest_in, oModel_in ):

    
    sWorkspace_pest_case = oModel_in.sWorkspace_calibration_case
    #read obs
    iFlag_debug = 0
    if(iFlag_debug == 1 ):
        sPath_current = sWorkspace_pest_case + slash + 'beopest1'
        Path(sPath_current).mkdir(parents=True, exist_ok=True)
    else:
        sPath_current = os.getcwd()

    sPath_current = sWorkspace_pest_case 
    sFilename = sPath_current + slash + oModel_in.sFilename_parameter_omac 
    ofs = open(sFilename, 'w')
    
    #the first parameter group
    sLine = 'aa' + ', ' + '50'  +'\n'
    ofs.write(sLine)
    sLine = 'bb' + ', ' + '-150'  +'\n'
    ofs.write(sLine)
    sLine = 'cc' + ', ' + '-10'  +'\n'
    ofs.write(sLine)
    sLine = 'rhoOM' + ', ' + '500'  +'\n'
    ofs.write(sLine)
    sLine = 'phi' + ', ' + '5.0'  +'\n'
    ofs.write(sLine)
    sLine = 'Kr' + ', ' + '0.1'  +'\n'
    ofs.write(sLine)
    #sLine = 'Tr' + ', ' + '100'  +'\n'
    #ofs.write(sLine)
    
    ofs.close()
    print('omac m12 parameter file is ready!')
    return

#the model could have more than one parameter file
#the number of parameter file should be same as the template file
def maces_prepare_omac_m12_template_file(oPest_in, oModel_in ):

    
    sWorkspace_pest_case = oModel_in.sWorkspace_calibration_case
    
    
    sFilename = sWorkspace_pest_case + slash + oModel_in.sFilename_template_omac 
    ofs = open(sFilename, 'w')
    sLine = 'ptf $\n'
    ofs.write(sLine)    
    #the first parameter group
    sLine = 'aa' + ', ' + '$     aa   '  +'$\n'
    ofs.write(sLine)
    sLine = 'bb' + ', ' + '$     bb   '  +'$\n'
    ofs.write(sLine)
    sLine = 'cc' + ', ' + '$     cc   '  +'$\n'
    ofs.write(sLine)
    sLine = 'rhoOM' + ', ' + '$    rhoOM    '  +'$\n'
    ofs.write(sLine)
    sLine = 'phi' + ', ' + '$   phi    '  +'$\n'
    ofs.write(sLine)
    sLine = 'Kr' + ', ' + '$    Kr    '  +'$\n'
    ofs.write(sLine)
    #sLine = 'Tr' + ', ' + '$Tr'  +'$\n'
    #ofs.write(sLine)

    ofs.close()
    print('omac m12 file is ready!')

    maces_prepare_omac_m12_parameter_file(oPest_in, oModel_in )
    
    
    return

def maces_prepare_omac_template_file(oPest_in, oModel_in ):
    maces_prepare_omac_m12_template_file(oPest_in, oModel_in )
    return
