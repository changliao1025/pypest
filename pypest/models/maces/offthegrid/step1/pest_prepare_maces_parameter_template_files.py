import sys, os
import numpy as np

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from eslib.system import define_global_variables
from eslib.system.define_global_variables import *
from eslib.toolbox.reader.text_reader_string import text_reader_string

#the pypest library
sPath_pypest_python = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest_python'
sys.path.append(sPath_pypest_python)

from pypest.models.maces.inputs.pest import pest
from pypest.models.maces.inputs.template.pest_prepare_maces_hydro_template_file import pest_prepare_maces_hydro_template_file

from pypest.models.maces.inputs.pest_read_configuration_file import pest_read_configuration_file

def pest_prepare_maces_parameter_template_files(oPest_in):
    """
    prepare the pest template file
    """

    pest_prepare_maces_hydro_template_file(oPest_in)
    #other modules


    print('The PEST template file is prepared successfully!')


if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/03configuration/pypest/maces/pest.xml'
    aParameter  = pest_read_configuration_file(sFilename_pest_configuration)
    print(aParameter)    
    oPest = pest(aParameter)
    pest_prepare_maces_parameter_template_files(oPest)