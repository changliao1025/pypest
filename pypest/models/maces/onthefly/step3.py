#we will use the existing functions to convert
import sys, os
import numpy as np
from shutil import copy2
sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system.define_global_variables import *

from pyes.toolbox.reader.text_reader_string import text_reader_string

#the pypest library
sPath_pypest = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest)

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces

from pypest.template.shared.pypest_read_configuration_file import pypest_read_configuration_file
from pypest.template.shared.xmlchange import xmlchange

def maces_copy_input_files(oModel_in):

    iFlag_calibration = oModel_in.iFlag_calibration
    if iFlag_calibration == 1:
        #calibration mode
        sWorkspace_calibration_relative = oModel_in.sWorkspace_calibration
        sWorkspace_calibration = sWorkspace_scratch + slash +   sWorkspace_calibration_relative
        sWorkspace_pest_model = sWorkspace_calibration

        iFlag_debug = 1
        if(iFlag_debug == 1 ):
            sPath_current = sWorkspace_pest_model + slash + 'beopest1'
        else:
            sPath_current = os.getcwd()
        pass
    else:
        #simulation mode
        sWorkspace_simulation_relative = oModel_in.sWorkspace_simulation
        sWorkspace_simulation = sWorkspace_scratch +  slash  + sWorkspace_simulation_relative
        if not os.path.exists(sWorkspace_simulation):
            os.mkdir(sWorkspace_simulation)
        else:
            pass
        sCase = oModel_in.sCase
        sWorkspace_simulation_case = sWorkspace_simulation + slash + sCase
        if not os.path.exists(sWorkspace_simulation_case):
            os.mkdir(sWorkspace_simulation_case)
        else:
            pass
        sPath_current = sWorkspace_simulation_case
        pass

    
    #a glimplse of the job file
    #==================================================
    #JOB_DIRECTORY=/people/liao313/workspace/python/maces/MACES/src
    #cd $JOB_DIRECTORY
    #mpiexec -np 1 python MACES_main.py -f namelist.maces.xml 
    #==================================================
    #we will copy the namelist.maces.xml only
    #maybe we also need the MACES_main.py? if this program is at global directory, then we can call it from anywhere

    #the model will have more than one namelist in the future
    sFilename_namelist = oModel_in.sFilename_namelist
    
   
    print('The current child path is: ' + sPath_current)


    sFilename_namelist_new = sPath_current + slash + os.path.basename(oModel_in.sFilename_namelist)
    copy2(sFilename_namelist, sFilename_namelist_new)

    #we will copy all xml files needed

    sFilename_config_hydro   = oModel_in.sFilename_config_hydro
    sFilename_config_minac   = oModel_in.sFilename_config_minac
    sFilename_config_omac    = oModel_in.sFilename_config_omac
    sFilename_config_wavero  = oModel_in.sFilename_config_wavero
    sFilename_config_lndmgr  = oModel_in.sFilename_config_lndmgr

    sFilename_config_hydro_new = sPath_current + slash + os.path.basename(oModel_in.sFilename_config_hydro)
    sFilename_config_minac_new = sPath_current + slash + os.path.basename(oModel_in.sFilename_config_minac)
    sFilename_config_omac_new = sPath_current + slash + os.path.basename(oModel_in.sFilename_config_omac)
    sFilename_config_wavero_new = sPath_current + slash + os.path.basename(oModel_in.sFilename_config_wavero)
    sFilename_config_lndmgr_new = sPath_current + slash + os.path.basename(oModel_in.sFilename_config_lndmgr)

    copy2(sFilename_config_hydro, sFilename_config_hydro_new)
    copy2(sFilename_config_minac, sFilename_config_minac_new)
    copy2(sFilename_config_omac, sFilename_config_omac_new)
    copy2(sFilename_config_wavero, sFilename_config_wavero_new)
    copy2(sFilename_config_lndmgr, sFilename_config_lndmgr_new)


    return
    

#due to the structure of maces, we need to change the path to the calibration folder
def maces_change_file_path(oPest_in, oModel_in):
    iFlag_debug =1
    if iFlag_debug ==1:
        pass
    else:
        pass

    
    #change the namliest file only
    

    return



def pypest_convert_parameter_files(oPest_in, oModel_in):
    sCase = oModel_in.sCase
    sWorkspace_simulation_relative = oModel_in.sWorkspace_simulation
    
    sWorkspace_simulation = sWorkspace_scratch +  slash  + sWorkspace_simulation_relative
    sWorkspace_simulation_case  = sWorkspace_simulation + slash + sCase
    if not os.path.exists(sWorkspace_simulation_case):
        os.mkdir(sWorkspace_simulation_case)
    else:
        pass


    sWorkspace_calibration_relative = oModel_in.sWorkspace_calibration
    sWorkspace_calibration = sWorkspace_scratch + slash + sWorkspace_calibration_relative
    sWorkspace_pest_model = oPest_in.sWorkspace_pest

    #in order to avoid issue, we will copy the input file into the current folder
    maces_copy_input_files(oModel_in)
    maces_change_file_path(oPest_in, oModel_in)

    #next, we need to read the parameter file generated by pest
    maces_convert_minac_parameter_file(oPest_in, oModel_in)
    maces_convert_omac_parameter_file(oPest_in, oModel_in)
    
    print('Finished')

    return

def step3(sFilename_pest_configuration_in, sFilename_model_configuration_in):    
    aParameter_pest  = pypest_read_configuration_file(sFilename_pest_configuration)    
    aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration
    oPest = pypest(aParameter_pest)
    aParameter_model  = pypest_read_configuration_file(sFilename_model_configuration)   
    aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration
    oMaces = maces(aParameter_model)
    pypest_convert_parameter_files(oPest, oMaces)
    return

if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/pypest.xml'
    sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/model.xml'    
    step3(sFilename_pest_configuration, sFilename_model_configuration)
    