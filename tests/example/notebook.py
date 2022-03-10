import os
from pathlib import Path
from os.path import realpath
from pypest.classes.pycase import pestcase
from pypest.pypest_generate_template_configuration_json_file import pypest_generate_template_configuration_json_file
from pypest.pypest_read_model_configuration_file import pypest_read_model_configuration_file

iFlag_option = 1
if iFlag_option ==1:
    
    sPath = str(Path(__file__).parent.resolve())
    
    sFilename_configuration_in = realpath( sPath +  '/../configurations//swat/template.json' )
    
    oPest = pypest_generate_template_configuration_json_file(sFilename_configuration_in)
    print(oPest.tojson())
    #now you can customize the model object
    oPest.iCase_index = 1
    print(oPest.tojson())
else: 
    if iFlag_option == 2:
        #an example configuration file is provided with the repository, but you need to update this file based on your own case study
        #linux
        sPath = str(Path(__file__).parent.resolve())
        sFilename_configuration_in = sPath +  '/../tests/configurations/arw.json'
         
        print(sFilename_configuration_in)
        oswaty = pypest_read_model_configuration_file(sFilename_configuration_in)
        #print the case information in details
        print(oswaty.tojson())

   
oPest.setup()
oPest.run()
oPest.evaluate()

print('Finished')