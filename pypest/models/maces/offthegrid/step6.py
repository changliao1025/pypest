import sys, os
import numpy as np

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system import define_global_variables
from pyes.system.define_global_variables import *


#to be sure we will add the libary here similar to other library
sPath_pypest_python = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest_python'
sys.path.append(sPath_pypest_python)

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces

from pypest.template.shared.pypest_read_configuration_file import pypest_read_configuration_file
from pypest.models.maces.auxiliary.maces_prepare_observation_file import maces_prepare_observation_file
def pypest_prepare_minac_type_instruction_files(oPest_in, oModel_in):
    #read obs
    aObservation1 = maces_prepare_observation_file()
    nobs_with_missing_value = len(aObservation1)
    nstress = nobs_with_missing_value
    
    aObservation1 = np.reshape(aObservation1, nobs_with_missing_value)
    nan_index = np.where(aObservation1 == missing_value)
    aObservation1[nan_index] = missing_value

    #write instruction
    sIndex = "{:02d}".format( 0 )  
    sFilename_instruction = sWorkspace_pest_model + slash + 'pest_instruction_' + sIndex + '.ins'

    ofs= open(sFilename_instruction,'w')
    ofs.write('pif $\n')

    #we need to consider that there is missing value in the observations
    for i in range(1, nstress+1):
        dDummy = aObservation1[i-1]
        if( dDummy != missing_value  ):
            sLine = 'l1' + ' !sem' + "{:04d}".format(i) + '!\n'
        else:
            sLine = 'l1' + ' !dum' + '!\n'
        ofs.write(sLine)
            
    ofs.close()

def pypest_prepare_pest_instruction_files(oPest_in, oModel_in):
    """
    prepare pest instruction file
    """
    sWorkspace_calibration_relative = oModel_in.sWorkspace_calibration        

    sWorkspace_calibration = sWorkspace_scratch + slash + sWorkspace_calibration_relative    
    sWorkspace_pest_model = sWorkspace_calibration
    pypest_prepare_minac_type_instruction_files(oPest_in, oModel_in)
    print('The instruction file is prepared successfully!')

def step6(sFilename_pest_configuration_in, sFilename_model_configuration_in):    
    aParameter_pest  = pypest_read_configuration_file(sFilename_pest_configuration)    
    aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration
    oPest = pypest(aParameter_pest)
    aParameter_model  = pypest_read_configuration_file(sFilename_model_configuration)   
    aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration
    oMaces = maces(aParameter_model)

    pypest_prepare_pest_instruction_files(oPest, oMaces)
    return

if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/03configuration/pypest/maces/pest.xml'
    sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/model.xml'    
    step6(sFilename_pest_configuration, sFilename_model_configuration)
    