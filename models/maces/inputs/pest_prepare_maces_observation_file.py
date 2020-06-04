import sys
import os
import numpy as np
import datetime
from numpy  import array
import pandas as pd

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from eslib.system import define_global_variables
from eslib.system.define_global_variables import *
sPath_library_python = sWorkspace_code +  slash + 'python' + slash + 'library' + slash + 'eslib_python'
sys.path.append(sPath_library_python)


from pest import pest
from pest_read_configuration_file import pest_read_configuration_file
def pest_prepare_maces_observation_file(oPest_in):


    # read data
    sFilename = r'/people/liao313/data/maces/auxiliary' + slash +'VeniceLagoon/1BF_OBS.xls'
    df = pd.read_excel(sFilename, sheet_name='1BF', header=None, skiprows=range(3), 
                       usecols='A,B,F,O,Q')
    df.columns = ['Time','Hmo','Hmax','hw','Turbidity']
    sed_obs_1BF = np.array(df['Turbidity'])[5334:5526]  # mg/l
    nt_obs = np.size(sed_obs_1BF)
    tt_obs = np.arange(nt_obs)/4


    #the temporal resolution 
    return sed_obs_1BF


if __name__ == '__main__':
    
    sFilename_pest_configuration = '/qfs/people/liao313/03configuration/pypest/maces/pest.xml'
    aParameter  = pest_read_configuration_file(sFilename_pest_configuration)
    print(aParameter)    
    oPest = pest(aParameter)
    pest_prepare_maces_observation_file(oPest)