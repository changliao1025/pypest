#this function is used to copy swat and beopest from linux hpc to calibration folder
import sys
import os, stat
from pyearth.system.define_global_variables import *
    
def pypest_prepare_run_script(oPest_in, oSwat_in):
    """
    prepare the job submission file
    """
    sModel = oSwat_in.sModel
    sFilename_pest_configuration = oPest_in.sFilename_pest_configuration
    sFilename_model_configuration = oSwat_in.sFilename_model_configuration
    
    #strings
    sWorkspace_home= oSwat_in.sWorkspace_home
    sWorkspace_scratch = oSwat_in.sWorkspace_scratch    
    sWorkspace_calibration_case = oSwat_in.sWorkspace_calibration_case   

    sWorkspace_pest_model = sWorkspace_calibration_case
    #replace it with your actual python

    sPython_Path =  oSwat_in.sPython
    sPython = '#!' + sPython_Path + '\n' 

    sFilename_script = sWorkspace_pest_model + slash + 'run_swat_model'
    ifs = open(sFilename_script, 'w')
    
    sLine = '#!/bin/bash\n'
    ifs.write(sLine)

    sLine = 'echo "Started to prepare python scripts"\n'
    ifs.write(sLine)
    #the first one
    sLine = 'cat << EOF > runstep3.py\n'
    ifs.write(sLine)    
    ifs.write(sPython)

    sLine = 'from pyswat.shared.swat import pyswat' +  '\n' 
    ifs.write(sLine)
    sLine = 'from pypest.models.swat.shared.pest import pypest' +  '\n' 
    ifs.write(sLine)
    sLine = 'from pyswat.shared.swat_read_model_configuration_file import *\n'
    ifs.write(sLine)
    sLine = 'from pypest.models.swat.multipletimes.run_step3 import run_step3'  +  '\n' 
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
    sLine = 'run_step3(oPest, oSwat)' + '\n'   
    ifs.write(sLine)
    sLine = 'EOF\n'
    ifs.write(sLine)
    
    #step 5 
    sLine = 'cat << EOF > runstep5.py\n'
    ifs.write(sLine)

    ifs.write(sPython)
    sLine = 'from pyswat.shared.swat import pyswat' +  '\n' 
    ifs.write(sLine)
    sLine = 'from pypest.models.swat.shared.pest import pypest' +  '\n' 
    ifs.write(sLine)
    sLine = 'from pyswat.shared.swat_read_model_configuration_file import *\n'
    ifs.write(sLine)
    sLine = 'from pypest.models.swat.multipletimes.run_step5 import run_step5' + '\n'
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
    
    sLine = 'run_step5(oPest, oSwat)\n'
    ifs.write(sLine)

    sLine = 'EOF\n'
    ifs.write(sLine)
    #end of python

    sLine = 'chmod 755 runstep3.py\n'
    ifs.write(sLine)

    sLine = 'chmod 755 runstep5.py\n'
    ifs.write(sLine)

    sLine = 'echo "Finished preparing python scripts"\n'
    ifs.write(sLine)

    sLine = 'echo "Started to prepare SWAT inputs"\n'
    ifs.write(sLine)
    #step 1: prepare inputs
    sLine = './runstep3.py\n'
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
    sLine = './runstep5.py\n'
    ifs.write(sLine)
    sLine = 'echo "Finished extracting SWAT simulation outputs"\n'
    ifs.write(sLine)
    ifs.close()
    os.chmod(sFilename_script, stat.S_IREAD | stat.S_IWRITE | stat.S_IXUSR)
    print('The pest run model file is prepared successfully!')

