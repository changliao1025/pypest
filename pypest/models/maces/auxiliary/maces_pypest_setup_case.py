import sys, os
import numpy as np
import xml.etree.ElementTree as ET

from pyearth.system.define_global_variables import *

#the pypest library

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces

from pypest.models.maces.auxiliary.pypest_prepare_job_file import pypest_prepare_job_file

from pypest.models.maces.once.run_step0 import run_step0
from pypest.models.maces.once.run_step1 import run_step1
from pypest.models.maces.once.run_step2 import run_step2
from pypest.models.maces.once.run_step6 import run_step6



#from pest_prepare_maces_run_bash_file import pest_prepare_maces_run_bash_file
from pypest.template.shared.pypest_read_configuration_file import pypest_read_pest_configuration_file, pypest_read_model_configuration_file




def pypest_setup_case(oPest_in, oModel_in):
    
    #call each step
    
    run_step0(oPest_in, oModel_in)
    run_step1(oPest_in, oModel_in)
    run_step2(oPest_in, oModel_in)
    run_step6(oPest_in, oModel_in)

    return


if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/pypest.xml'
    sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/model_calibration.xml'

    aParameter_pest  = pypest_read_pest_configuration_file(sFilename_pest_configuration)    
    aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration
    oPest = pypest(aParameter_pest)


    #we need to add the alternative model information into the model
    aMinac_models = ['F06', 'T03', 'KM12', 'M12', 'F07', 'VDK05', 'DA07']
    aOmac_model = models = ['M12', 'DA07', 'KM12', 'K16']

    #sDate = '20210213'
    #iCase_index=1
    aParameter_model = pypest_read_model_configuration_file(sFilename_model_configuration)#, \
     #   sDate_in = sDate, \
      #      iCase_index_in = iCase_index)   
    
    aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration
    oMaces = maces(aParameter_model)

    sOmac_model=aOmac_model[0]
    #oMaces.sModel_minac = 'T03'#sMinac_model
    oMaces.sModel_omac = sOmac_model
    oMaces.sModel_minac = 'Null' #sOmac_model
    pypest_setup_case(oPest, oMaces)
    pypest_prepare_job_file(oPest, oMaces)

    exit

    #use loop to control multiple calibrcation
    #for sMinac_model in aMinac_models:
    #    oMaces.sModel_minac = 'T03'#sMinac_model
    #    for sOmac_model in aOmac_model:
    #        oMaces.sModel_omac = sOmac_model
    #        oMaces.sModel_minac = 'Null' #sOmac_model
    #        pypest_setup_case(oPest, oMaces)
    #        pypest_prepare_job_file(oPest, oMaces)
    #        break
