#this script is used to set up a model easily so we don't have to copy/paste
import sys, os
import numpy as np
from pathlib import Path
from shutil import copy2
sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyearth.system.define_global_variables import *

from pyearth.toolbox.reader.text_reader_string import text_reader_string

#the pypest library
sPath_pypest = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest)

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces

from pypest.template.shared.pypest_read_configuration_file import pypest_read_model_configuration_file
from pypest.template.shared.xmlchange import xmlchange

from pypest.models.maces.auxiliary.maces_copy_input_files import maces_copy_input_files

from pypest.models.maces.auxiliary.maces_prepare_job_file import maces_prepare_job_file

def maces_setup_case(oModel_in):
    print('Started to setup case in child node\n')
    
    #first copy all the needed file
    maces_copy_input_files(oModel_in)
    #then modify the parameters
    
    #get based directory 
    iFlag_calibration = oModel_in.iFlag_calibration
    if iFlag_calibration == 1:
        iFlag_debug =0
        if iFlag_debug ==1:
            sPath_current= oModel_in.sWorkspace_calibration_case + slash + 'child1'  
        else:
        #current path
            sPath_current = os.getcwd()
        
        pass
    else:
        sPath_current = oModel_in.sWorkspace_simulation_case  
         
        
    print('The current workspace is: ' + sPath_current)  
    print('Started to change namelist parameter\n')    
    sFilename_namelist = oModel_in.sFilename_namelist
    sRegion = oModel_in.sRegion

    sFilename_namelist_new = sPath_current + slash + os.path.basename(oModel_in.sFilename_namelist)

    #change run control
    xmlchange(filename=sFilename_namelist_new,  group='run_control',parameter='RUNROOT',value = sPath_current)

    #change site file
    if sRegion == 'VeniceLagoon': #first site
        xmlchange(filename=sFilename_namelist_new,  group='run_desc',parameter='RUN_STARTDATE',value = oModel_in.sDate_start)
        xmlchange(filename=sFilename_namelist_new,  group='run_desc',parameter='RUN_STOPDATE',value = oModel_in.sDate_end)

        #sFilename = '/qfs/projects/taim/TAIMOD/Data/VeniceLagoon/DIVA_maces.xlsx'
        sFilename = '/qfs/people/liao313/data/maces/VeniceLagoon/auxiliary/DIVA_maces.xlsx'

        xmlchange(filename=sFilename_namelist_new,  group='run_control',parameter='SITE_FILE',value = sFilename)
        xmlchange(filename=sFilename_namelist_new,  group='run_control',parameter='CELL_RES',value = "10")
        #sWorkspace_data_model = '/qfs/projects/taim/TAIMOD/Data/VeniceLagoon'
        sWorkspace_data_model = '/qfs/people/liao313/data/maces/VeniceLagoon/auxiliary/'
        xmlchange(filename=sFilename_namelist_new,  group='run_inputs',parameter='DIN_ROOT',value = sWorkspace_data_model)
        xmlchange(filename=sFilename_namelist_new,  group='run_inputs',parameter='h_TSTEP',value = "10")

        xmlchange(filename=sFilename_namelist_new,  group='run_inputs',parameter='FILE_SSC',value = "")
        


        #change archive
        sWorkspace_archive = sPath_current + slash + 'output'
        Path(sWorkspace_archive).mkdir(parents=True, exist_ok=True)
        xmlchange(filename=sFilename_namelist_new,  group='run_archive',parameter='DOUT_ROOT',value = sWorkspace_archive)

    else:
        if sRegion == 'PlumIsland': #second site
            xmlchange(filename=sFilename_namelist_new,  group='run_desc',parameter='RUN_STARTDATE',value = "2017-07-17")
            xmlchange(filename=sFilename_namelist_new,  group='run_desc',parameter='RUN_STOPDATE',value = "2017-08-01")
            #sFilename = '/qfs/projects/taim/TAIMOD/Data/PlumIsland/DIVA_maces.xlsx'
            sFilename = '/qfs/people/liao313/data/maces/PlumIsland/auxiliary/DIVA_maces.xlsx'
            xmlchange(filename=sFilename_namelist_new,  group='run_control',parameter='SITE_FILE',value = sFilename)
            xmlchange(filename=sFilename_namelist_new,  group='run_control',parameter='CELL_RES',value = "50")
            #change din 
            #sWorkspace_data_model = '/qfs/projects/taim/TAIMOD/Data/PlumIsland'
            sWorkspace_data_model = '/qfs/people/liao313/data/maces/PlumIsland/auxiliary/'
            xmlchange(filename=sFilename_namelist_new,  group='run_inputs',parameter='DIN_ROOT',value = sWorkspace_data_model)
            xmlchange(filename=sFilename_namelist_new,  group='run_inputs',parameter='FILE_SSC',value = "")

            xmlchange(filename=sFilename_namelist_new,  group='run_inputs',parameter='h_TSTEP',value = "15")

            #change archive
            sWorkspace_archive = sPath_current + slash + 'output'
            Path(sWorkspace_archive).mkdir(parents=True, exist_ok=True)
            xmlchange(filename=sFilename_namelist_new,  group='run_archive',parameter='DOUT_ROOT',value = sWorkspace_archive)
        else: #last site HunterEstuary
            xmlchange(filename=sFilename_namelist_new,  group='run_desc',parameter='RUN_STARTDATE',value = "2004-09-25")
            xmlchange(filename=sFilename_namelist_new,  group='run_desc',parameter='RUN_STOPDATE',value = "2004-10-06")
            #sFilename = '/qfs/projects/taim/TAIMOD/Data/HunterEstuary/DIVA_maces.xlsx'
            sFilename = '/qfs/people/liao313/data/maces/HunterEstuary/auxiliary/DIVA_maces.xlsx'
            xmlchange(filename=sFilename_namelist_new,  group='run_control',parameter='SITE_FILE',value = sFilename)
            xmlchange(filename=sFilename_namelist_new,  group='run_control',parameter='CELL_RES',value = "2")

            xmlchange(filename=sFilename_namelist_new,  group='run_inputs',parameter='h_TSTEP',value = "15")
            #change din 
            #sWorkspace_data_model = '/qfs/projects/taim/TAIMOD/Data/HunterEstuary'
            sWorkspace_data_model = '/qfs/people/liao313/data/maces/HunterEstuary/auxiliary/'
            xmlchange(filename=sFilename_namelist_new,  group='run_inputs',parameter='DIN_ROOT',value = sWorkspace_data_model)
            #change archive
            sWorkspace_archive = sPath_current + slash + 'output'
            Path(sWorkspace_archive).mkdir(parents=True, exist_ok=True)
            xmlchange(filename=sFilename_namelist_new,  group='run_archive',parameter='DOUT_ROOT',value = sWorkspace_archive)
            pass



    print('Finished changing namelist parameter\n') 


    
    #generate the job file
    if iFlag_calibration ==1:
        pass
    else:
        maces_prepare_job_file(oModel_in)

    print('Finished setting up the maces case')
    


    return
if __name__ == '__main__':
    iFlag_calibration =1
    if iFlag_calibration ==1:

        sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/model_calibration.xml'    
    else:
        sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/model_simulation.xml'    

   
    aParameter_model = pypest_read_model_configuration_file(sFilename_model_configuration)   
    oMaces = maces(aParameter_model)
    maces_setup_case(oMaces)