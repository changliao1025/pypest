import sys, os
import numpy as np

from pyearth.system import define_global_variables
from pyearth.system.define_global_variables import *


#to be sure we will add the li

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces

from pypest.models.maces.auxiliary.maces_prepare_observation import maces_prepare_omac_observation


def maces_prepare_omac_instruction_file(oPest_in, oModel_in):
    #read obs
    aObservation1 = maces_prepare_omac_observation()
    nobs_with_missing_value = len(aObservation1)
    nstress = nobs_with_missing_value
    
    aObservation1 = np.reshape(aObservation1, nobs_with_missing_value)
    nan_index = np.where(aObservation1 == missing_value)
    aObservation1[nan_index] = missing_value

    #write instruction

    sWorkspace_pest_case =  oModel_in.sWorkspace_calibration_case
  
    
    sFilename_instruction = sWorkspace_pest_case + slash + oModel_in.sFilename_instruction_omac

    ofs= open(sFilename_instruction,'w')
    ofs.write('pif $\n')

    #we need to consider that there is missing value in the observations
    for i in range(1, nstress+1):
        dDummy = aObservation1[i-1]
        if( dDummy != missing_value  ):
            sLine = 'l1' + ' !dOMAC_yr' + '!\n' #+ "{:04d}".format(i) +
        else:
            sLine = 'l1' + ' !dum' + '!\n'
        ofs.write(sLine)
            
    ofs.close()