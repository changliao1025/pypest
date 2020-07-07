#this function is used to copy swat and beopest from linux hpc to calibration folder
import sys, os, stat


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
    sModel = oModel_in.sModel
    sRegion= oModel_in.sRegion

    sWorkspace_data_relative = sWorkspace_data
    sWorkspace_project_relative = oModel_in.sWorkspace_project
    sWorkspace_simulation_relative = oModel_in.sWorkspace_simulation
    sWorkspace_calibration_relative = oModel_in.sWorkspace_calibration

    sFilename_pest_configuration = oPest_in.sFilename_pest_configuration
    sFilename_model_configuration = oModel_in.sFilename_model_configuration

    sWorkspace_calibration = sWorkspace_scratch + slash + sWorkspace_calibration_relative

    sWorkspace_pest_model = sWorkspace_calibration #+ slash + sModel + slash + sRegion
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

    sLine = 'sFilename_pest_configuration = ' + '"' + sFilename_pest_configuration + '"\n'
    ifs.write(sLine)

    sLine = 'sFilename_model_configuration = ' + '"' + sFilename_model_configuration + '"\n'
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

    sLine = 'sFilename_pest_configuration = ' + '"' + sFilename_pest_configuration + '"\n'
    ifs.write(sLine)

    sLine = 'sFilename_model_configuration = ' + '"' + sFilename_model_configuration + '"\n'
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

    sLine = 'sFilename_pest_configuration = ' + '"' + sFilename_pest_configuration + '"\n'
    ifs.write(sLine)

    sLine = 'sFilename_model_configuration = ' + '"' + sFilename_model_configuration + '"\n'
    ifs.write(sLine)

    sLine = 'sModel = ' + '"' + sModel + '"\n'
    ifs.write(sLine)
    sLine = 'swat_extract_output_for_pest(sFilename_configuration_in, sModel)\n'
    ifs.write(sLine)

    sLine = 'EOF\n'
    ifs.write(sLine)
    #end of python

    #change permission
    sLine = 'chmod 755 step3.py\n'
    ifs.write(sLine)
    sLine = 'chmod 755 step4.py\n'
    ifs.write(sLine)
    sLine = 'chmod 755 step5.py\n'
    ifs.write(sLine)
    #end of change permission

    
    

    
    #step 3: prepare inputs
    sLine = './step3.py\n'
    ifs.write(sLine)
    
    #step 4: prepare inputs
    sLine = './step4.py\n'
    ifs.write(sLine)       

    #step 5: extract  output
    sLine = './step5.py\n'
    ifs.write(sLine)
    

    ifs.close()

    os.chmod(sFilename_script, stat.S_IREAD | stat.S_IWRITE | stat.S_IXUSR)


    print('The pest run model file is prepared successfully!')


if __name__ == '__main__':
    
    pass
