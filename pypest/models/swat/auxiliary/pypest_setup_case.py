import sys, os
import numpy as np
import xml.etree.ElementTree as ET

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system.define_global_variables import *



from pypest.models.swat.shared.pest import pypest
from pypest.models.swat.shared.model import pyswat

from pypest.models.swat.auxiliary.pypest_prepare_job_file import pypest_prepare_job_file

from pypest.models.swat.once.run_step0 import run_step0
from pypest.models.swat.once.run_step1 import run_step1
from pypest.models.swat.once.run_step2 import run_step2
from pypest.models.swat.once.run_step6 import run_step6



#from pest_prepare_swat_run_bash_file import pest_prepare_swat_run_bash_file
from pypest.template.shared.pypest_read_configuration_file import pypest_read_pest_configuration_file, pypest_read_model_configuration_file




def pypest_setup_case(oPest_in, oModel_in):
    
    #call each step
    
    run_step0(oPest_in, oModel_in)
    run_step1(oPest_in, oModel_in)
    run_step2(oPest_in, oModel_in)
    run_step6(oPest_in, oModel_in)

    return


if __name__ == '__main__':


    sFilename_pest_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/swat/config/pypest.xml'
    sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/swat/config/model_calibration.xml'

    aParameter_pest  = pypest_read_pest_configuration_file(sFilename_pest_configuration)    
    aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration
    oPest = pypest(aParameter_pest)



    #sDate = '20210213'
    #iCase_index=1
    aParameter_model = pypest_read_model_configuration_file(sFilename_model_configuration)
    
    aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration
    oswat = swat(aParameter_model)

   
    pypest_setup_case(oPest, oswat)
    pypest_prepare_job_file(oPest, oswat)

    exit

