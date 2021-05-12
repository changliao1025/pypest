import sys, os
import numpy as np
import xml.etree.ElementTree as ET

from pyearth.system.define_global_variables import *

from pyswat.shared.swat import pyswat

from pyswat.shared.swat_read_model_configuration_file import swat_read_model_configuration_file

from pypest.models.swat.shared.pest import pypest

from pypest.models.swat.auxiliary.swat_pypest_prepare_job_file import swat_pypest_prepare_job_file

from pypest.models.swat.once.run_step0 import run_step0
from pypest.models.swat.once.run_step1 import run_step1
from pypest.models.swat.once.run_step2 import run_step2
from pypest.models.swat.once.run_step6 import run_step6

from pypest.template.shared.pypest_read_configuration_file import pypest_read_pest_configuration_file, pypest_read_model_configuration_file

def swat_pypest_setup_case(oPest_in, oModel_in):
    
    #call each step
    
    run_step0(oPest_in, oModel_in)
    run_step1(oPest_in, oModel_in)
    run_step2(oPest_in, oModel_in)
    run_step6(oPest_in, oModel_in)

    return


if __name__ == '__main__':


    sFilename_pest_configuration = '/global/homes/l/liao313/workspace/python/pypest/pypest/models/swat/config/pypest.xml'
    sFilename_model_configuration = '/global/homes/l/liao313/workspace/python/pypest/pypest/models/swat/config/swat_calibration.xml'

    aParameter_pest  = pypest_read_pest_configuration_file(sFilename_pest_configuration)    
    aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration
    oPest = pypest(aParameter_pest)



    #sDate = '20210213'
    #iCase_index=1
    #aParameter_model = pypest_read_model_configuration_file(sFilename_model_configuration)
    aParameter_model =swat_read_model_configuration_file(sFilename_model_configuration)
    
    aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration
    oswat = pyswat(aParameter_model)

   
    swat_pypest_setup_case(oPest, oswat)
    swat_pypest_prepare_job_file(oPest, oswat)

    exit

