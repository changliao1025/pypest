import os, sys
from pathlib import Path
from os.path import realpath
#use this function to generate an initial json file for hexwatershed
import json
#once it's generated, you can modify it and use it for different simulations

from pypest.classes.pycase import pestcase

def pypest_generate_template_configuration_json_file(sFilename_json):
    #use a dict to initialize the class
    aConfig = {}
    
    aConfig['iFlag_calibration'] = 0

    aConfig['npargp'] = 1 
    aConfig['npar'] = 2
    aConfig['nobsgp'] = 1 
    aConfig['nobs'] = 1 
    aConfig['nprior'] = 0 
    aConfig['ntplfile'] = 1 
    aConfig['ninsfile'] = 1 

    aConfig['sDate']  = '20220202'

    aConfig['sPest_mode']  = 'estimation'
    aConfig['sFilename_pest_configuration'] = ''
    aConfig['sFilename_control'] = 'pest_swat.pst'
    aConfig['sFilename_instruction'] = 'pest_swat.pst'
    aConfig['sFilename_control'] = 'pest_swat.ins'

    aConfig['sWorkspace_home'] = '/global/homes/l/liao313'

    aConfig['sWorkspace_bin'] = '/global/homes/l/liao313/bin'
 
    aConfig['sWorkspace_pest'] = ''
    aConfig['sFilename_output'] = 'stream_discharge_monthly.txt'
    

    aConfig['iCase_index'] = 1

    
    

    oModel = pestcase(aConfig)

    

    
    
    

    oModel.export_config_to_json(sFilename_json)
    return oModel