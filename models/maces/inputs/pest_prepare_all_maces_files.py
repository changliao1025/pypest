import numpy as np
import xml.etree.ElementTree as ET
from pest import pest

from pest_prepare_maces_control_file import pest_prepare_maces_control_file
#from pest_prepare_maces_instruction_file import pest_prepare_maces_instruction_file
#from pest_prepare_maces_parameter_template_file import pest_prepare_maces_parameter_template_file
#from pest_prepare_maces_run_bash_file import pest_prepare_maces_run_bash_file
from pest_read_configuration_file import pest_read_configuration_file


def pest_prepare_all_maces_files(sFilename_pest_configuration):


    aParameter  = pest_read_configuration_file(sFilename_pest_configuration)
    print(aParameter)    
    oPest = pest(aParameter)
    #call each step
    pest_prepare_maces_control_file(oPest)
    #pest_prepare_maces_instruction_file()
    #pest_prepare_maces_parameter_template_file()
    #pest_prepare_maces_run_bash_file()


    return

if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/03configuration/maces/calibration/pest.xml'
    pest_prepare_all_maces_files(sFilename_pest_configuration)
