import sys
import os
import numpy as np
import datetime
from numpy  import array

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from eslib.system import define_global_variables
from eslib.system.define_global_variables import *

sPath_library_python = sWorkspace_code +  slash + 'python' + slash + 'library' + slash + 'eslib_python'
sys.path.append(sPath_library_python)


from pest import pest
from pest_read_configuration_file import pest_read_configuration_file


def pest_prepare_maces_instruction_file(oPest_in):
    """
    prepare pest instruction file
    """
    
    
    
    

    
    #read obs
    aObservation1 = pest_prepare_maces_observation_file(oPest_in)
    nobs_with_missing_value = len(aObservation1)
    nstress = nobs_with_missing_value
    
    aObservation1 = np.reshape(aObservation1, nobs_with_missing_value)
    nan_index = np.where(aObservation1 == missing_value)

    #write instruction
    sFilename_instruction = oPest_in.sFilename_instruction
    ofs= open(sFilename_instruction,'w')
    ofs.write('pif $\n')

    #we need to consider that there is missing value in the observations
    for i in range(0, nstress):
        dDummy = aObservation1[i]
        if( dDummy != missing_value  ):
            sLine = 'l1' + ' !sem' + "{:04d}".format(i+1) + '!\n'
        else:
            sLine = 'l1' + ' !dum' + '!\n'
        ofs.write(sLine)
            
    ofs.close()
    print('The instruction file is prepared successfully!')

if __name__ == '__main__':
    
    sFilename_pest_configuration = '/qfs/people/liao313/03configuration/pypest/maces/pest.xml'
    aParameter  = pest_read_configuration_file(sFilename_pest_configuration)
    print(aParameter)    
    oPest = pest(aParameter)
    pest_prepare_maces_instruction_file(oPest)