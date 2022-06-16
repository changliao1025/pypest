import sys, os
import numpy as np


from pyearth.system.define_global_variables import *

from pypest.pypest_read_model_configuration_file import pypest_read_model_configuration_file


from pypest.classes.pycase import pestcase


iFlag_use_existing_template = 0
iCase_index = 1
sDate = '20220615'
sWorkspace_input = '/global/homes/l/liao313/workspace/python/pypest/data/arw/input'
sWorkspace_output = '/global/cscratch1/sd/liao313/04model/pest/arw/calibration'
sFilename_pest_configuration= '/global/homes/l/liao313/workspace/python/pypest/tests/configurations/swat/pest_new.json'

  
oPest  = pypest_read_model_configuration_file(sFilename_pest_configuration,\
     iCase_index_in=iCase_index,\
        iFlag_read_discretization_in = 0,\
        sDate_in=sDate, \
            sWorkspace_input_in=sWorkspace_input, \
                sWorkspace_output_in=sWorkspace_output)   
#only two steps
oPest.setup()
oPest.prepare_job_file()
#then you are submit the job from your terminal

