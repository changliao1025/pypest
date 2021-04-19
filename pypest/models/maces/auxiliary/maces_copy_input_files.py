import sys, os
import numpy as np
from shutil import copy2
sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system.define_global_variables import *

def maces_copy_input_files(oModel_in):

    print('Started to copy input files\n')
    

    iFlag_calibration = oModel_in.iFlag_calibration
    if iFlag_calibration == 1:
        #calibration mode
        
        
        sWorkspace_pest_model = oModel_in.sWorkspace_calibration_case

        iFlag_debug = 0
        if(iFlag_debug == 1 ):
            sPath_current = sWorkspace_pest_model + slash + 'child1'
        else:
            sPath_current = os.getcwd()
        pass
    else:
        #simulation mode
        sWorkspace_simulation=oModel_in.sWorkspace_simulation
        
        
        sCase = oModel_in.sCase
        sWorkspace_simulation_case = sWorkspace_simulation + slash + sCase
        
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

    print('Successfully copied input files\n')
    
    return