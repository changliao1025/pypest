import sys, os
import numpy as np
import xml.etree.ElementTree as ET

from pyearth.system.define_global_variables import *

from pypest.pypest_read_model_configuration_file import pypest_read_model_configuration_file


from pypest.classes.pycase import pestcase


iFlag_use_existing_template = 0

sFilename_pest_configuration= '/global/homes/l/liao313/workspace/python/pypest/tests/configurations/swat/pypest_swat.json'

oPest  = pypest_read_model_configuration_file(sFilename_pest_configuration)    

#only two steps
oPest.setup()
oPest.prepare_job_file()
#then you are submit the job from your terminal

