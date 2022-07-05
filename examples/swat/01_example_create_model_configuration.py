
import os, sys
from pathlib import Path
from os.path import realpath
import argparse
import logging
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is the time pyhexwatershed simulation started.')
import numpy as np

from swaty.classes.swatpara import swatpara
from pypest.pypest_create_template_configuration_file import pypest_create_template_configuration_file

#example

sModel_type = 'swat'
sPest_method = 'pest'
iCase_index = 1
iFlag_parallel = 0

sDate='20220615'



sPath = str( Path().resolve() )
iFlag_option = 1
sWorkspace_data = realpath( sPath +  '/data/arw' )
sWorkspace_input =  str(Path(sWorkspace_data)  /  'input')
#sWorkspace_output=  str(Path(sWorkspace_data)  /  'output')

sWorkspace_output = '/global/cscratch1/sd/liao313/04model/pest/arw/calibration'

sWorkspace_bin = '/global/homes/l/liao313/bin'

sFilename_configuration_in = sPath +  '/examples/swat/pest_swat.json' 
sWorkspace_data = realpath( sPath +  '/data/arw' )


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

oPest = pypest_create_template_configuration_file(sFilename_configuration_in,sWorkspace_bin, sWorkspace_input, sWorkspace_output, sModel_type,\
    iFlag_parallel_in = iFlag_parallel, iCase_index_in = iCase_index, sDate_in = sDate, sPest_method_in= sPest_method, aParameter_in= aParameter)
print(oPest.tojson())

sFilename_configuration = '/global/homes/l/liao313/workspace/python/pypest/examples/swat/swat_new.json'
oPest.pSwat.export_config_to_json(sFilename_configuration)

oPest.sFilename_model_configuration = sFilename_configuration

sFilename_configuration = '/global/homes/l/liao313/workspace/python/pypest/examples/swat/pest_new.json'
oPest.sFilename_pest_configuration = sFilename_configuration
oPest.export_config_to_json(sFilename_configuration)


logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is the time pyhexwatershed simulation finished.')