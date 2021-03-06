#this function is used to copy swat and beopest from linux hpc to calibration folder
import sys
import os, stat
import numpy as np
import datetime
import calendar
import errno
from os.path import isfile, join
from os import listdir

from numpy  import array
from shutil import copyfile, copy2
from pyearth.system.define_global_variables import *
from pyearth.toolbox.reader.text_reader_string import text_reader_string

    
def ppest_prepare_run_script(oPest_in, oModel_in):
    """
    prepare the job submission file
    """
    sModel = oModel_in.sModel
    sFilename_pest_configuration = oPest_in.sFilename_pest_configuration
    sFilename_model_configuration = oModel_in.sFilename_model_configuration
    
    #strings
    sWorkspace_home= oModel_in.sWorkspace_home
    sWorkspace_scratch = oModel_in.sWorkspace_scratch    
    sWorkspace_calibration_case = oModel_in.sWorkspace_calibration_case   

    sWorkspace_pest_model = sWorkspace_calibration_case
    #replace it with your actual python

    sPython_Path =  oModel_in.sPython
    sPython = '#!' + sPython_Path + '\n' 

    sFilename_script = sWorkspace_pest_model + slash + 'run_swat_model'
    ifs = open(sFilename_script, 'w')
    
    sLine = '#!/bin/bash\n'
    ifs.write(sLine)

    sLine = 'echo "Started to prepare python scripts"\n'
    ifs.write(sLine)
    #the first one
    sLine = 'cat << EOF > pyscript1.py\n'
    ifs.write(sLine)    
    ifs.write(sPython)

    sLine = 'from pyswat.shared.swat import pyswat' +  '\n' 
    ifs.write(sLine)
    sLine = 'from pypest.models.swat.shared.pest import pypest' +  '\n' 
    ifs.write(sLine)
    sLine = 'from pyswat.shared.swat_read_model_configuration_file import *\n'
    ifs.write(sLine)
    sLine = 'from pypest.models.swat.multipletimes.step3.swat_prepare_pest_child_input_file import *\n'
    ifs.write(sLine)    
    sLine = 'from pypest.template.shared.pypest_read_configuration_file import *' +  '\n' 
    ifs.write(sLine)  
    sLine = 'sFilename_pest_configuration = ' + '"' + sFilename_pest_configuration + '"\n'
    ifs.write(sLine)
    sLine = 'aParameter_pest  = pypest_read_pest_configuration_file(sFilename_pest_configuration)'  + '\n'   
    ifs.write(sLine)
    sLine = "aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration" + '\n'   
    ifs.write(sLine)
    sLine = 'oPest = pypest(aParameter_pest)' + '\n'   
    ifs.write(sLine)
    sLine = 'sFilename_model_configuration = ' + '"' + sFilename_model_configuration + '"\n'
    ifs.write(sLine)
    sLine = "aParameter_model = swat_read_model_configuration_file(sFilename_model_configuration)" + '\n'   
    ifs.write(sLine)
    sLine = "aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration" + '\n'   
    ifs.write(sLine) 
    sLine = "oSwat = pyswat(aParameter_model)" + '\n'   
    ifs.write(sLine)
    sLine = 'swat_prepare_pest_child_input_file(oPest, oSwat)' + '\n'   
    ifs.write(sLine)
    sLine = 'EOF\n'
    ifs.write(sLine)
    #the second 
    sLine = 'cat << EOF > pyscript2.py\n'
    ifs.write(sLine)
    
    ifs.write(sPython)
    sLine = 'from pyswat.shared.swat import pyswat' +  '\n' 
    ifs.write(sLine)
    sLine = 'from pypest.models.swat.shared.pest import pypest' +  '\n' 
    ifs.write(sLine)
    sLine = 'from pyswat.shared.swat_read_model_configuration_file import *\n'
    ifs.write(sLine)
    sLine = 'from pypest.models.swat.multipletimes.step3.swat_prepare_input_from_pest import *\n'
    ifs.write(sLine)
    sLine = 'from pypest.template.shared.pypest_read_configuration_file import *' +  '\n' 
    ifs.write(sLine)
    sLine = 'sFilename_pest_configuration = ' + '"' + sFilename_pest_configuration + '"\n'
    ifs.write(sLine)
    sLine = 'aParameter_pest  = pypest_read_pest_configuration_file(sFilename_pest_configuration)'  + '\n'   
    ifs.write(sLine)
    sLine = "aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration" + '\n'   
    ifs.write(sLine)
    sLine = 'oPest = pypest(aParameter_pest)' + '\n'   
    ifs.write(sLine)
    sLine = 'sFilename_model_configuration = ' + '"' + sFilename_model_configuration + '"\n'
    ifs.write(sLine)
    sLine = "aParameter_model = swat_read_model_configuration_file(sFilename_model_configuration)" + '\n'   
    ifs.write(sLine)
    sLine = "aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration" + '\n'   
    ifs.write(sLine) 
    sLine = "oSwat = pyswat(aParameter_model)" + '\n'   
    ifs.write(sLine)

    sLine = 'swat_prepare_input_from_pest(oPest, oSwat)\n'
    ifs.write(sLine)

    sLine = 'EOF\n'
    ifs.write(sLine)


    #the third one
    sLine = 'cat << EOF > pyscript3.py\n'
    ifs.write(sLine)

    
    ifs.write(sPython)
    sLine = 'from pyswat.shared.swat import pyswat' +  '\n' 
    ifs.write(sLine)
    sLine = 'from pypest.models.swat.shared.pest import pypest' +  '\n' 
    ifs.write(sLine)
    sLine = 'from pyswat.shared.swat_read_model_configuration_file import *\n'
    ifs.write(sLine)
    sLine = 'from pypest.models.swat.multipletimes.step5.swat_extract_output_for_pest import *\n'
    ifs.write(sLine)
    sLine = 'from pypest.template.shared.pypest_read_configuration_file import *' +  '\n' 
    ifs.write(sLine)
    sLine = 'sFilename_pest_configuration = ' + '"' + sFilename_pest_configuration + '"\n'
    ifs.write(sLine)
    sLine = 'aParameter_pest  = pypest_read_pest_configuration_file(sFilename_pest_configuration)'  + '\n'   
    ifs.write(sLine)
    sLine = "aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration" + '\n'   
    ifs.write(sLine)
    sLine = 'oPest = pypest(aParameter_pest)' + '\n'   
    ifs.write(sLine)
    sLine = 'sFilename_model_configuration = ' + '"' + sFilename_model_configuration + '"\n'
    ifs.write(sLine)
    sLine = "aParameter_model = swat_read_model_configuration_file(sFilename_model_configuration)" + '\n'   
    ifs.write(sLine)
    sLine = "aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration" + '\n'   
    ifs.write(sLine) 
    sLine = "oSwat = pyswat(aParameter_model)" + '\n'   
    ifs.write(sLine)
    
    sLine = 'swat_extract_output_for_pest(oPest, oSwat)\n'
    ifs.write(sLine)

    sLine = 'EOF\n'
    ifs.write(sLine)
    #end of python

    sLine = 'chmod 755 pyscript1.py\n'
    ifs.write(sLine)

    sLine = 'chmod 755 pyscript2.py\n'
    ifs.write(sLine)

    sLine = 'chmod 755 pyscript3.py\n'
    ifs.write(sLine)

    sLine = 'echo "Finished preparing python scripts"\n'
    ifs.write(sLine)

    sLine = 'echo "Started to prepare SWAT inputs"\n'
    ifs.write(sLine)
    #step 1: prepare inputs
    sLine = './pyscript1.py\n'
    ifs.write(sLine)
    
    sLine = './pyscript2.py\n'
    ifs.write(sLine)

    sLine = 'echo "Finished preparing SWAT simulation"\n'
    ifs.write(sLine)
    #step 2: run swat model
    sLine = 'echo "Started to run SWAT simulation"\n'
    ifs.write(sLine)
    sLine = './swat\n'
    ifs.write(sLine)
    sLine = 'echo "Finished running SWAT simulation"\n'
    ifs.write(sLine)

    #step 3: extract SWAT output
    sLine = 'echo "Started to extract SWAT simulation outputs"\n'
    ifs.write(sLine)
    sLine = './pyscript3.py\n'
    ifs.write(sLine)
    sLine = 'echo "Finished extracting SWAT simulation outputs"\n'
    ifs.write(sLine)


    ifs.close()

    os.chmod(sFilename_script, stat.S_IREAD | stat.S_IWRITE | stat.S_IXUSR)


    print('The pest run model file is prepared successfully!')

