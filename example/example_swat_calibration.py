import sys, os
import numpy as np
import xml.etree.ElementTree as ET

from pyearth.system.define_global_variables import *

from pypest.template.shared.pypest_read_configuration_file import pypest_read_pest_configuration_file
from pyswat.shared.swat import pyswat
from pyswat.shared.swat_read_model_configuration_file import swat_read_model_configuration_file

from pypest.models.swat.shared.pest import pypest
from pypest.models.swat.auxiliary.swat_pypest_prepare_job_file import swat_pypest_prepare_job_file
from pypest.models.swat.auxiliary.swat_pypest_setup_case import swat_pypest_setup_case

sFilename_pest_configuration = '/global/homes/l/liao313/workspace/python/pypest/pypest/models/swat/config/pypest.xml'
sFilename_model_configuration = '/global/homes/l/liao313/workspace/python/pypest/pypest/models/swat/config/swat_calibration.xml'
aParameter_pest  = pypest_read_pest_configuration_file(sFilename_pest_configuration)    
aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration   
oPest = pypest(aParameter_pest)
aParameter_watershed = ['SFTMP','SMTMP']
aParameter_subbasin = ['CH_K2','CH_N2']
aParameter_hru = ['CN2']
aParameter = ['SFTMP','SMTMP']
aParameter_value = [1.0,0.5]
aParameter_value_lower = [-5,-5]
aParameter_value_upper = [5.0,5.0]

aParameter_model = swat_read_model_configuration_file(sFilename_model_configuration)

aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration
oSwat = pyswat(aParameter_model)

swat_pypest_setup_case(oPest, oSwat)
swat_pypest_prepare_job_file(oPest, oSwat)

