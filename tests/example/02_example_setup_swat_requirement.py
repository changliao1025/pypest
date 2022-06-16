#this function will be used to setup some basic swat information

#this should be done after you edited the configuration files

#please refer to the swaty package 
import sys, os
import numpy as np
import xml.etree.ElementTree as ET

from pyearth.system.define_global_variables import *

from pypest.pypest_read_model_configuration_file import pypest_read_model_configuration_file


from pypest.classes.pycase import pestcase
from swaty.classes.swatpara import swatpara

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


oSwat = oPest.pSwat

oSwat.swaty_generate_model_structure_files()

oPest  = pypest_read_model_configuration_file(sFilename_pest_configuration,\
     iCase_index_in=iCase_index,\
        iFlag_read_discretization_in = 1,\
        sDate_in=sDate, \
            sWorkspace_input_in=sWorkspace_input, \
                sWorkspace_output_in=sWorkspace_output)   

oSwat = oPest.pSwat
aParameter=list()
aPara_in=dict()

aParemeter_watershed = np.array(['esco','ai0', 'sftmp','smtmp','timp','epco'])
nParameter_watershed = len(aParemeter_watershed)


for j in np.arange(1, nParameter_watershed+1):
    aPara_in['iParameter_type'] = 1
    aPara_in['iIndex_subbasin'] = j
    aPara_in['sName']= aParemeter_watershed[j-1]
    aPara_in['dValue_init']=0.0
    aPara_in['dValue_current']=0.01* j +0.01
    aPara_in['dValue_lower']=-1
    aPara_in['dValue_upper']=5
    pParameter = swatpara(aPara_in)
    aParameter.append(    pParameter )


aParemeter_subbasin = np.array(['ch_n2','ch_k2','plaps','tlaps'])
nParameter_subbasin = len(aParemeter_subbasin)
for j in np.arange(1, nParameter_subbasin+1):
    aPara_in['iParameter_type'] = 2
    aPara_in['iIndex_subbasin'] = j
    aPara_in['sName']= aParemeter_subbasin[j-1]
    aPara_in['dValue_init']=0.0
    aPara_in['dValue_current']=0.01* j +0.01
    aPara_in['dValue_lower']=-1
    aPara_in['dValue_upper']=5
    pParameter = swatpara(aPara_in)
    aParameter.append(pParameter)

aParemeter_hru = np.array(['cn2','rchrg_dp','gwqmn','gw_revap','revapmn','gw_delay','alpha_bf','ov_n'])
nParameter_hru = len(aParemeter_hru)
for j in np.arange(1, nParameter_hru+1):
    aPara_in['iParameter_type'] = 3
    aPara_in['iIndex_hru'] = j
    aPara_in['sName']= aParemeter_hru[j-1]
    aPara_in['dValue_init']=0.0
    aPara_in['dValue_current']=0.01* j +0.01
    aPara_in['dValue_lower']=-1
    aPara_in['dValue_upper']=5
    pParameter = swatpara(aPara_in)
    aParameter.append(pParameter)



aParemeter_soil = np.array(['sol_k','sol_awc','sol_alb','sol_bd'])
nParameter_soil = len(aParemeter_soil)
for j in np.arange(1, nParameter_soil+1):
    aPara_in['iParameter_type'] = 4
    aPara_in['lIndex_soil_layer'] = j
    aPara_in['sName']= aParemeter_soil[j-1]
    aPara_in['dValue_init']=0.0
    aPara_in['dValue_current']=0.01* j +0.01
    aPara_in['dValue_lower']=-1
    aPara_in['dValue_upper']=5
    pParameter = swatpara(aPara_in)
    aParameter.append(pParameter)

oSwat.extract_default_parameter_value(aParameter)

oSwat.generate_parameter_bounds()

sFilename_configuration = os.path.join(oSwat.sWorkspace_output , 'swat.json')
sFilename_configuration = '/global/homes/l/liao313/workspace/python/pypest/tests/configurations/swat/swat_new.json'

oSwat.export_config_to_json(sFilename_configuration)

