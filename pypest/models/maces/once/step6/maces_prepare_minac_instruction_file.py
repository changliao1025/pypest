import sys, os
import numpy as np

from pyearth.system import define_global_variables
from pyearth.system.define_global_variables import *



from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces


from pypest.models.maces.auxiliary.maces_prepare_observation import maces_prepare_minac_observation


def maces_prepare_minac_instruction_file(oPest_in, oModel_in):
    #read obs
    aObservation1 = maces_prepare_minac_observation_file()
    nobs_with_missing_value = len(aObservation1)
    nstress = nobs_with_missing_value
    
    aObservation1 = np.reshape(aObservation1, nobs_with_missing_value)
    nan_index = np.where(aObservation1 == missing_value)
    aObservation1[nan_index] = missing_value

    #write instruction
    
    sFilename_instruction = sWorkspace_pest_model + slash + oModel_in.sFilename_instruction_minac

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