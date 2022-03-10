import os
from pathlib import Path
from os.path import realpath
import argparse
import logging
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is the time swaty simulation started.')

from pypest.classes.pycase import pestcase
from pypest.pypest_generate_template_configuration_file import pypest_generate_template_configuration_file
from pypest.pypest_read_model_configuration_file import pypest_read_model_configuration_file

iFlag_option=1
sPath = str( Path().resolve() )
sWorkspace_data = realpath( sPath +  '/data/arw' )
sWorkspace_input = realpath( sWorkspace_data +  '/input' )
sWorkspace_output = '/global/cscratch1/sd/liao313/04model/pest/arw/simulation'
sPath_bin = realpath( sPath +  '/bin' )
sModel_type ='swat'
sPest_method_in = 'pest'

if iFlag_option ==1:

    sFilename_configuration_in = realpath( sPath +  '/tests/configurations/template.json' ) 
    oPest = pypest_generate_template_configuration_file(sFilename_configuration_in, sWorkspace_input,sWorkspace_output, sPath_bin, sModel_type, iFlag_parallel_in=0, iCase_index_in=1, sPest_method_in= None, sDate_in='20220308')
    print(oPest.tojson())
    #now you can customize the model object
    oPest.iCase_index = 1
    print(oPest.tojson())
else: 
    if iFlag_option == 2:
        #an example configuration file is provided with the repository, but you need to update this file based on your own case study
        #linux     
        sFilename_configuration_in = sPath +  '/tests/configurations/arw.json'
  
        oPest = pypest_read_model_configuration_file(sFilename_configuration_in)
        #print the case information in details
        print(oPest.tojson())

   
oPest.setup()
oPest.pypest_prepare_job_file()
oPest.run()
oPest.analyze()
oPest.evaluate()

print('Finished')