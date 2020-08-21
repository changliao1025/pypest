#this script is used to set up a model easily so we don't have to copy/paste
import sys, os
import numpy as np
from pathlib import Path
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

from pypest.models.maces.onthefly.step3 import maces_copy_input_files

from pypest.models.maces.auxiliary.maces_prepare_job_file import maces_prepare_job_file

def maces_setup_case(oModel_in):
    #first copy all the needed file
    maces_copy_input_files(oModel_in)
    #then modify the parameters
    
    #get based directory 
    iFlag_calibration = oModel_in.iFlag_calibration
    if iFlag_calibration == 1:
        pass
    else:
        sWorkspace_simulation = oModel_in.sWorkspace_simulation        
        sCase = oModel_in.sCase
        sWorkspace_simulation_case = sWorkspace_simulation + slash + sCase
        if not os.path.exists(sWorkspace_simulation_case):
            os.mkdir(sWorkspace_simulation_case)
        else:
            pass
        
    sFilename_namelist = oModel_in.sFilename_namelist
    sRegion = oModel_in.sRegion

    sFilename_namelist_new = sWorkspace_simulation_case + slash + os.path.basename(oModel_in.sFilename_namelist)

    #change run control
    xmlchange(filename=sFilename_namelist_new,  group='run_control',parameter='RUNROOT',value = sWorkspace_simulation_case)

    #change site file
    if sRegion == 'VeniceLagoon': #first site

        sFilename = '/people/liao313/data/maces/auxiliary/VeniceLagoon/DIVA_maces.xlsx'
        xmlchange(filename=sFilename_namelist_new,  group='run_control',parameter='SITE_FILE',value = sFilename)
        sWorkspace_data_model = '/people/liao313/data/maces/auxiliary/VeniceLagoon'
        xmlchange(filename=sFilename_namelist_new,  group='run_inputs',parameter='DIN_ROOT',value = sWorkspace_data_model)
        #change archive
        sWorkspace_archive = oModel_in.sWorkspace_simulation_case + slash + 'Output'
        Path(sWorkspace_archive).mkdir(parents=True, exist_ok=True)
        xmlchange(filename=sFilename_namelist_new,  group='run_archive',parameter='DOUT_ROOT',value = sWorkspace_archive)

    else:
        if sRegion == 'PlumIsland': #second site
            sFilename = '/people/liao313/data/maces/auxiliary/PlumIsland/DIVA_maces.xlsx'
            xmlchange(filename=sFilename_namelist_new,  group='run_control',parameter='SITE_FILE',value = sFilename)
            #change din 
            sWorkspace_data_model = '/people/liao313/data/maces/auxiliary/PlumIsland'
            xmlchange(filename=sFilename_namelist_new,  group='run_inputs',parameter='DIN_ROOT',value = sWorkspace_data_model)
            #change archive
            sWorkspace_archive = oModel_in.sWorkspace_simulation_case + slash + 'Output'
            Path(sWorkspace_archive).mkdir(parents=True, exist_ok=True)
            xmlchange(filename=sFilename_namelist_new,  group='run_archive',parameter='DOUT_ROOT',value = sWorkspace_archive)
        else: #last site
            sFilename = '/people/liao313/data/maces/auxiliary/HunterEstuary/DIVA_maces.xlsx'
            xmlchange(filename=sFilename_namelist_new,  group='run_control',parameter='SITE_FILE',value = sFilename)
            #change din 
            sWorkspace_data_model = '/people/liao313/data/maces/auxiliary/HunterEstuary'
            xmlchange(filename=sFilename_namelist_new,  group='run_inputs',parameter='DIN_ROOT',value = sWorkspace_data_model)
            #change archive
            sWorkspace_archive = oModel_in.sWorkspace_simulation_case + slash + 'Output'
            Path(sWorkspace_archive).mkdir(parents=True, exist_ok=True)
            xmlchange(filename=sFilename_namelist_new,  group='run_archive',parameter='DOUT_ROOT',value = sWorkspace_archive)
            pass





    
    #generate the job file
    maces_prepare_job_file(oModel_in)

    print('Finished setting up the maces model')
    


    return
if __name__ == '__main__':
    
    sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/model_sim.xml'    

    aParameter_model  = pypest_read_configuration_file(sFilename_model_configuration)   
    oMaces = maces(aParameter_model)
    maces_setup_case(oMaces)