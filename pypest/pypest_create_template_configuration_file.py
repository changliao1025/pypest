import os, sys

from os.path import realpath
from pathlib import Path
import json


from pypest.classes.pycase import pestcase
from swaty.swaty_create_template_configuration_file import swaty_create_template_configuration_file

def pypest_create_template_configuration_file(sFilename_json, sPath_bin,sWorkspace_input, sWorkspace_output, sModel_type, \
    iFlag_parallel_in = None, iCase_index_in = None, \
    sPest_method_in=None, sDate_in = None, aParameter_in = None):
    if iCase_index_in is not None:        
        iCase_index = iCase_index_in
    else:       
        iCase_index = 1
    
    if iFlag_parallel_in is not None:        
        iFlag_parallel = iFlag_parallel_in
    else:       
        iFlag_parallel = 0
    if sPest_method_in is not None:
        sPest_method = sPest_method_in
    else:
        sPest_method = 'pest'

        
    if sDate_in is not None:
        sDate = sDate_in
    else:
        sDate = '20220202'
        pass
    #use a dict to initialize the class
    aConfig = {}
    
    aConfig['iFlag_calibration'] = 1
    aConfig['iFlag_parallel'] = iFlag_parallel

    aConfig['npargp'] = 1 
    aConfig['npar'] = 2
    aConfig['nobsgp'] = 1 
    aConfig['nobs'] = 1 
    aConfig['nprior'] = 0 
    aConfig['ntplfile'] = 1 
    aConfig['ninsfile'] = 1 

    aConfig['sDate']  = sDate
    aConfig['sModel'] = 'pest'
    aConfig['sPest_method'] = sPest_method

    aConfig['sPest_mode']  = 'estimation'
    aConfig['sFilename_pest_configuration'] = ''
    aConfig['sFilename_control'] = 'pest_swat.pst'
    aConfig['sFilename_instruction'] = 'pest_swat.ins'
    aConfig['sPython'] = '/global/homes/l/liao313/.conda/envs/pestenv/bin/python'
    
  

    aConfig['sWorkspace_input'] = sWorkspace_input  
    aConfig['sWorkspace_output'] = sWorkspace_output    

    aConfig['sWorkspace_bin'] = sPath_bin     
    aConfig['sFilename_output'] = 'stream_discharge_monthly.txt'    

    aConfig['iCase_index'] = iCase_index

    
    aConfig['sFilename_pest_configuration'] = sFilename_json

    oPest = pestcase(aConfig)
    oPest.sFilename_pest_configuration = sFilename_json

    oPest.sPest_method = sPest_method
    oPest.sModel_type = sModel_type

    sPath = Path(sFilename_json)
    sFolder_configuration = sPath.parent.absolute()
    if sModel_type == 'swat':
        
        oPest.iModel_type= 1
        sFilename_swat_configuration = os.path.join(sFolder_configuration, 'swat.json')
        if iFlag_parallel ==1:
            pass
        else:
            oSwat = swaty_create_template_configuration_file(sFilename_swat_configuration,sPath_bin, sWorkspace_input,sWorkspace_output,  \
                iFlag_standalone_in=0, iCase_index_in=iCase_index, sDate_in=sDate, aParameter_in=aParameter_in)
            oSwat.sFilename_model_configuration = sFilename_swat_configuration

            oSwat.export_config_to_json(sFilename_swat_configuration)
            oPest.pSwat = oSwat
            oPest.sFilename_model_configuration = sFilename_swat_configuration
    else:
        if sModel_type == 'modflow':
            pass
        else:
            if sModel_type == 'prms':
                pass
            else:
                print('Unsupported model')   
    
    

    oPest.export_config_to_json(sFilename_json)
    return oPest