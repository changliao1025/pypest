from lib2to3.pgen2.token import OP
import sys, os
import numpy as np
from pyearth.system.define_global_variables import *
from pypest.pypest_read_model_configuration_file import pypest_read_model_configuration_file
from pypest.classes.pycase import pestcase
from swaty.classes.swatpara import swatpara
from swaty.auxiliary.text_reader_string import text_reader_string

iFlag_use_existing_template = 0
iCase_index = 1
sDate = '20220615'
sWorkspace_input = '/global/homes/l/liao313/workspace/python/pypest/data/arw/input'
sWorkspace_output = '/global/cscratch1/sd/liao313/04model/pest/arw/calibration'
sFilename_pest_configuration= '/global/homes/l/liao313/workspace/python/pypest/examples/swat/pest_new.json'

#read default parameter and bounds from here
aParameter=list()
aPara_in=dict()

aParemeter_watershed = np.array(['esco','sftmp','smtmp','smfmx' ,'timp','epco'])
nParameter_watershed = len(aParemeter_watershed)

oPest  = pypest_read_model_configuration_file(sFilename_pest_configuration,\
     iCase_index_in=iCase_index,\
        iFlag_read_discretization_in = 1,\
        sDate_in=sDate, \
            sWorkspace_input_in=sWorkspace_input, \
                sWorkspace_output_in=sWorkspace_output)

oSwat = oPest.pSwat
sWorkspace_simulation_case = oSwat.sWorkspace_output
#read pest default parameter value
sFilename_pest_watershed = os.path.join( sWorkspace_simulation_case, 'watershed_default_parameter.txt' )
aData_dummy1 = text_reader_string(sFilename_pest_watershed, cDelimiter_in=',')
#read the bound        
sFilename_parameter_bounds_watershed = os.path.join(sWorkspace_simulation_case,  'parameter_bounds_watershed.txt' )
aData_dummy2 = text_reader_string(sFilename_parameter_bounds_watershed, cDelimiter_in=',')

for j in np.arange(1, nParameter_watershed+1):
    aPara_in['iParameter_type'] = 1
    aPara_in['lIndex_subbasin'] = 1
    aPara_in['sName']= aData_dummy2[j-1, 0]
    aPara_in['dValue_init']= float(aData_dummy1[1,j])
    aPara_in['dValue_current']= float(aData_dummy1[1,j])
    aPara_in['dValue_lower']=float(aData_dummy2[j-1, 1])
    aPara_in['dValue_upper']=float(aData_dummy2[j-1, 2])
    pParameter = swatpara(aPara_in)
    aParameter.append( pParameter )

aParemeter_subbasin = np.array(['ch_n2','ch_k2','plaps','tlaps'])
nParameter_subbasin = len(aParemeter_subbasin)

sFilename_pest_subbasin = os.path.join( sWorkspace_simulation_case, 'subbasin_default_parameter.txt' )
aData_dummy1 = text_reader_string(sFilename_pest_subbasin, cDelimiter_in=',')
sFilename_parameter_bounds_subbasin = os.path.join(sWorkspace_simulation_case,  'parameter_bounds_subbasin.txt' )
aData_dummy2 = text_reader_string(sFilename_parameter_bounds_subbasin, cDelimiter_in=',')
for j in np.arange(1, nParameter_subbasin+1):
    aPara_in['iParameter_type'] = 2
    aPara_in['lIndex_subbasin'] = 1
    aPara_in['sName']= aData_dummy2[j-1, 0]
    aPara_in['dValue_init']= float(aData_dummy1[1,j])
    aPara_in['dValue_current']= float(aData_dummy1[1,j])
    aPara_in['dValue_lower']=float(aData_dummy2[j-1, 1])
    aPara_in['dValue_upper']=float(aData_dummy2[j-1, 2])
    pParameter = swatpara(aPara_in)
    aParameter.append(pParameter)

aParemeter_hru = np.array(['cn2','rchrg_dp','gwqmn','gw_revap','revapmn','gw_delay','alpha_bf','ov_n'])
nParameter_hru = len(aParemeter_hru)
sFilename_pest_hru = os.path.join( sWorkspace_simulation_case, 'hru_default_parameter.txt' )
aData_dummy1 = text_reader_string(sFilename_pest_hru, cDelimiter_in=',')
sFilename_parameter_bounds_hru = os.path.join(sWorkspace_simulation_case,  'parameter_bounds_hru.txt' )
aData_dummy2 = text_reader_string(sFilename_parameter_bounds_hru, cDelimiter_in=',')
for j in np.arange(1, nParameter_hru+1):
    aPara_in['iParameter_type'] = 3
    aPara_in['lIndex_hru'] = 1
    aPara_in['sName']= aData_dummy2[j-1, 0]
    aPara_in['dValue_init']= float(aData_dummy1[1,j])
    aPara_in['dValue_current']= float(aData_dummy1[1,j])
    aPara_in['dValue_lower']=float(aData_dummy2[j-1, 1])
    aPara_in['dValue_upper']=float(aData_dummy2[j-1, 2])
    pParameter = swatpara(aPara_in)
    aParameter.append(pParameter)

aParemeter_soil = np.array(['sol_k','sol_awc','sol_alb','sol_bd'])
nParameter_soil = len(aParemeter_soil)
sFilename_pest_soil = os.path.join( sWorkspace_simulation_case, 'soiltype01_default_parameter.txt' )
aData_dummy1 = text_reader_string(sFilename_pest_soil, cDelimiter_in=',')
sFilename_parameter_bounds_soil = os.path.join(sWorkspace_simulation_case,  'parameter_bounds_soil.txt' )
aData_dummy2 = text_reader_string(sFilename_parameter_bounds_soil, cDelimiter_in=',')
for j in np.arange(1, nParameter_soil+1):
    aPara_in['iParameter_type'] = 4
    aPara_in['lIndex_hru'] = 1
    aPara_in['lIndex_soil_layer'] = 1
    aPara_in['sName']= aData_dummy2[j-1, 0]
    aPara_in['dValue_init']= float(aData_dummy1[1,j])
    aPara_in['dValue_current']= float(aData_dummy1[1,j])
    aPara_in['dValue_lower']=float(aData_dummy2[j-1, 1])
    aPara_in['dValue_upper']=float(aData_dummy2[j-1, 2])
    pParameter = swatpara(aPara_in)
    aParameter.append(pParameter)
  
oPest  = pypest_read_model_configuration_file(sFilename_pest_configuration,\
     iCase_index_in=iCase_index,\
        iFlag_read_discretization_in = 1,\
        sDate_in=sDate, \
            sWorkspace_input_in=sWorkspace_input, \
                sWorkspace_output_in=sWorkspace_output, aParameter_in= aParameter)   
#only two steps
oPest.setup()
oPest.pypest_prepare_job_file()
#then you are submit the job from your terminal

