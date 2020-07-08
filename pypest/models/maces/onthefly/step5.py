import sys, os
import numpy as np

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system.define_global_variables import *


sPath_pypest = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest)

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces


from pypest.template.shared.pypest_read_configuration_file import pypest_read_configuration_file

def maces_extract_hydrodynamic_output(oPest_in, oModel_in):
    # read simulation outputs
    #example code from maces
    #filename = '/Users/tanz151/Python_maces/src/maces_ecogeom_2002-12-01_2002-12-13_466.nc'
    #try:
    #    nc = Dataset(filename,'r')
    #    x = np.array(nc.variables['x'][:])
    #    zh = np.array(nc.variables['zh'][0,:])
    #finally:
    #    nc.close()

    sFilename = ''
    try:
        nc = Dataset(sFilename,'r')
        x = np.array(nc.variables['x'][:])
        zh = np.array(nc.variables['zh'][0,:])

        #We will match up with the observation data here
        aSem_simulation = x
        #save it to a text file
        sFilename_out = sWorkspace_child + slash + 'sem.txt'

        np.savetxt(sFilename_out, aSem_simulation, delimiter=",")

    finally:
        nc.close()



    return

def pypest_extract_model_outputs(oPest_in, oModel_in):
    """
    sFilename_configuration_in
    """
    #stream discharge
    maces_extract_hydrodynamic_output(oPest_in, oModel_in)

def step5(sFilename_pest_configuration_in, sFilename_model_configuration_in):    
    aParameter_pest  = pypest_read_configuration_file(sFilename_pest_configuration)    
    aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration
    oPest = pypest(aParameter_pest)
    aParameter_model  = pypest_read_configuration_file(sFilename_model_configuration)   
    aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration
    oMaces = maces(aParameter_model)
    pypest_extract_model_outputs(oPest, oMaces)
    return
if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/03configuration/pypest/maces/pest.xml'
    sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/model.xml'    
    step5(sFilename_pest_configuration, sFilename_model_configuration)
    
    
    
   
