
import sys
from pathlib import Path
from os.path import realpath
import argparse
import logging
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is the time pyhexwatershed simulation started.')

from pypest.pypest_create_template_configuration_file import pypest_create_template_configuration_file

#example

sModel_type = 'swat'
sPest_method = 'pest'
iCase_index = 1
iFlag_parallel = 0

sDate='20220604'



sPath = str( Path().resolve() )
iFlag_option = 1
sWorkspace_data = realpath( sPath +  '/data/arw' )
sWorkspace_input =  str(Path(sWorkspace_data)  /  'input')
sWorkspace_output=  str(Path(sWorkspace_data)  /  'output')

sWorkspace_bin = realpath( sPath +  '/bin' )

sFilename_configuration_in = sPath +  '/tests/configurations/swat/pypest_swat.json' 
sWorkspace_data = realpath( sPath +  '/data/arw' )
oPest = pypest_create_template_configuration_file(sFilename_configuration_in,sWorkspace_bin, sWorkspace_input, sWorkspace_output, sModel_type,\
    iFlag_parallel_in = iFlag_parallel, iCase_index_in = iCase_index, sDate_in = sDate, sPest_method_in= sPest_method)
print(oPest.tojson())


logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is the time pyhexwatershed simulation finished.')