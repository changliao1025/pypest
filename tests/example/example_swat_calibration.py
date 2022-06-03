import sys, os
import numpy as np
import xml.etree.ElementTree as ET

from pyearth.system.define_global_variables import *

from retired.pypest_read_configuration_file import pypest_read_pest_configuration_file
from swaty.classes.pycase import swatcase
#from pyswat.shared.swat_read_model_configuration_file import swat_read_model_configuration_file

from pypest.classes.pycase import pestcase
#from pypest.models.swat.auxiliary.swat_pypest_prepare_job_file import swat_pypest_prepare_job_file
#from pypest.models.swat.auxiliary.swat_pypest_setup_case import swat_pypest_setup_case

iFlag_use_existing_template = 0

sFilename_pest_configuration= '/global/homes/l/liao313/workspace/python/pypest/tests/configurations/swat/pypest_swat.json'

oPest  = pypest_read_pest_configuration_file(sFilename_pest_configuration)    

oPest.setup()
oPest.prepare_job_file()

