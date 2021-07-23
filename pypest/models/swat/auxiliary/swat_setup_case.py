#this script is used to set up a model easily so we don't have to copy/paste
import sys, os
import numpy as np
from pathlib import Path
from shutil import copy2

from pyearth.system.define_global_variables import *

from pyearth.toolbox.reader.text_reader_string import text_reader_string
from pyswat.shared.swat import pyswat
from pypest.models.swat.shared.pest import pypest


from pypest.template.shared.pypest_read_configuration_file import pypest_read_model_configuration_file
from pypest.template.shared.xmlchange import xmlchange



def swat_setup_case(oSwat_in):
    print('Started to setup case in child node\n')
    
    #first copy all the needed file
    swat_copy_input_files(oSwat_in)
    #then modify the parameters
    
    #get based directory 
    iFlag_calibration = oSwat_in.iFlag_calibration
    if iFlag_calibration == 1:
        iFlag_debug =0
        if iFlag_debug ==1:
            sPath_current= oSwat_in.sWorkspace_calibration_case + slash + 'child1'  
        else:
        #current path
            sPath_current = os.getcwd()
        
        pass
    else:
        sPath_current = oSwat_in.sWorkspace_simulation_case  
         
        
    print('The current workspace is: ' + sPath_current)  
    print('Started to change namelist parameter\n')    
    sFilename_namelist = oSwat_in.sFilename_namelist
    sRegion = oSwat_in.sRegion

    sFilename_namelist_new = sPath_current + slash + os.path.basename(oSwat_in.sFilename_namelist)

    #change run control
    xmlchange(filename=sFilename_namelist_new,  group='run_control',parameter='RUNROOT',value = sPath_current)

    #change site file
    if sRegion == 'VeniceLagoon': #first site
        xmlchange(filename=sFilename_namelist_new,  group='run_desc',parameter='RUN_STARTDATE',value = oSwat_in.sDate_start)
        xmlchange(filename=sFilename_namelist_new,  group='run_desc',parameter='RUN_STOPDATE',value = oSwat_in.sDate_end)

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
        maces_prepare_job_file(oSwat_in)

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