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

    
    
    ofs = open(sFilename_minac, 'w')
    
    #the first parameter group
    sLine = 'd50' + ', ' + '50'  +'$\n'
    ofs.write(sLine)
    sLine = 'pb' + ', ' + '2000'  +'$\n'
    ofs.write(sLine)
    sLine = 'phi' + ', ' + '0.5'  +'$\n'
    ofs.write(sLine)
    sLine = 'taud' + ', ' + '50'  +'$\n'
    ofs.write(sLine)
    
    sValue =  "{:5.2f}".format( 1.0 )  
    sLine = 'Cz0' + ', ' + sValue  + '\n'
    ofs.write(sLine)
    ofs.close()
    print('hydro F06 file is ready!')
    return

#the model could have more than one parameter file
#the number of parameter file should be same as the template file
def maces_prepare_minac_template_file(oPest_in, oModel_in ):

   
    sWorkspace_calibration_relative = oModel_in.sWorkspace_calibration        
    sWorkspace_calibration = sWorkspace_scratch + slash + sWorkspace_calibration_relative    
    sWorkspace_pest_model = sWorkspace_calibration
    #read obs
    sIndex = "{:02d}".format( 0 )  
    sFilename_hydro_parameter_template = sWorkspace_pest_model + slash + 'pest_template_' + sIndex + '.tpl'
    
    ofs = open(sFilename_hydro_parameter_template, 'w')
    sLine = 'ptf $\n'
    ofs.write(sLine)    
    #the first parameter group
    sLine = 'd50' + ', ' + '$d50'  +'$\n'
    ofs.write(sLine)
    sLine = 'pb' + ', ' + '$pb'  +'$\n'
    ofs.write(sLine)
    sLine = 'phi' + ', ' + '$phi'  +'$\n'
    ofs.write(sLine)
    sLine = 'taud' + ', ' + '$taud'  +'$\n'
    ofs.write(sLine)

    ofs.close()
    print('hydro template file is ready!')

    pypest_prepare_maces_hydro_parameter_file(oPest_in, oModel_in )
    
    return
#major components

def maces_prepare_hydro_template_file(oPest_in, oModel_in ):
    return

def maces_prepare_minac_template_file(oPest_in, oModel_in ):
    
    maces_prepare_minac_f06_parameter_file(oPest_in, oModel_in )
    return
def maces_prepare_omac_template_file(oPest_in, oModel_in ):
    
    return
def maces_prepare_wavero_template_file(oPest_in, oModel_in ):
    
    return
def maces_prepare_landmgr_template_file(oPest_in, oModel_in ):
    
    return
#we need to prepare the template files for all possible parameters
#in general, a model may have more than one parameter file for different components


def pypest_prepare_pest_template_files(oPest_in, oModel_in):
    #maces_prepare_hydro_template_file(oPest_in, oModel_in)
    maces_prepare_minac_template_file(oPest_in, oModel_in )
    #maces_prepare_omac_template_file(oPest_in, oModel_in)
    #maces_prepare_wavero_template_file(oPest_in, oModel_in)
    #maces_prepare_landmgr_template_file(oPest_in, oModel_in)
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
