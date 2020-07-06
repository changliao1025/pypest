#this function is used to copy swat and beopest from linux hpc to calibration folder
import sys, os


sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system.define_global_variables import *

sPath_pypest = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest)

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces

    
def pypest_prepare_pest_command_file(oPest_in, oModel_in):
    """
    prepare the job submission file
    """
    
    
    #strings
    sModel = oPest_in.sModel

    sWorkspace_data_relative = sWorkspace_data
    sWorkspace_project_relative = oPest_in.sWorkspace_project
    sWorkspace_simulation_relative = oPest_in.sWorkspace_simulation
    sWorkspace_calibration_relative = oPest_in.sWorkspace_calibration

    sWorkspace_calibration = sWorkspace_scratch + slash + sWorkspace_calibration_relative

    sWorkspace_pest_model = sWorkspace_calibration + slash + sModel + slash + sRegion
    #create the directory if not available
    if not os.path.exists(sWorkspace_pest_model):
        os.mkdir(sWorkspace_pest_model)
    else:
        pass


    #start writing the script
    sFilename_script = sWorkspace_pest_model + slash + 'run_model'
    ifs = open(sFilename_script, 'w')
    
    sLine = '#!/bin/bash\n'
    ifs.write(sLine)

    sLine = 'echo "Started to write PyPEST scripts"\n'
    ifs.write(sLine)
    #the first one
    sLine = 'cat << EOF > step3.py' + '\n'
    ifs.write(sLine)

    sLine = '#!/share/apps/python/anaconda3.6/bin/python\n'
    ifs.write(sLine)

    sLine = 'from swat_prepare_pest_slave_input_file import *\n'
    ifs.write(sLine)

    sLine = 'sFilename_configuration_in = ' + '"' + sFilename_configuration_in + '"\n'
    ifs.write(sLine)

    sLine = 'sModel = ' + '"' + sModel + '"\n'
    ifs.write(sLine)
    sLine = 'swat_prepare_pest_slave_input_file(sFilename_configuration_in, sModel)\n'
    ifs.write(sLine)

    sLine = 'EOF\n'
    ifs.write(sLine)
    #the second 
    sLine = 'cat << EOF > step4.py' + '"\n'
    ifs.write(sLine)

    sLine = '#!/share/apps/python/anaconda3.6/bin/python\n'
    ifs.write(sLine)

    sLine = 'from swat_prepare_input_from_pest import *\n'
    ifs.write(sLine)

    sLine = 'sFilename_configuration_in = ' + '"' + sFilename_configuration_in + '"\n'
    ifs.write(sLine)

    sLine = 'sModel = ' + '"' + sModel + '\n'
    ifs.write(sLine)
    sLine = 'swat_prepare_input_from_pest(sFilename_configuration_in, sModel)\n'
    ifs.write(sLine)

    sLine = 'EOF\n'
    ifs.write(sLine)
    #the third one
    sLine = 'cat << EOF > step5.py' + '\n'
    ifs.write(sLine)

    sLine = '#!/share/apps/python/anaconda3.6/bin/python\n'
    ifs.write(sLine)

    sLine = 'from swat_extract_output_for_pest import *\n'
    ifs.write(sLine)

    sLine = 'sFilename_configuration_in = ' + '"' + sFilename_configuration_in + '"\n'
    ifs.write(sLine)

    sLine = 'sModel = ' + '"' + sModel + '"\n'
    ifs.write(sLine)
    sLine = 'swat_extract_output_for_pest(sFilename_configuration_in, sModel)\n'
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


if __name__ == '__main__':
    
    sRegion = 'tinpan'
    sModel ='swat'
    sCase = 'test'
    sJob = sCase
    sTask = 'simulation'
    iFlag_simulation = 1
    iFlag_pest = 0
    if iFlag_pest == 1:
        sTask = 'calibration'
    sFilename_configuration = sWorkspace_scratch + slash + '03model' + slash \
              + sModel + slash + sRegion + slash \
              + sTask  + slash + sFilename_config       
    ppest_prepare_run_script(sFilename_configuration, sModel)
