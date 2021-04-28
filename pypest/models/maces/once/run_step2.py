#this function is used to copy swat and beopest from linux hpc to calibration folder
import sys, os, stat


sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyearth.system.define_global_variables import *

sPath_pypest = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest)

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces
from pypest.template.shared.pypest_read_configuration_file import pypest_read_model_configuration_file
    
def pypest_prepare_pest_command_file(oPest_in, oModel_in):
    """
    prepare the job submission file
    """

    #strings
    sModel = oModel_in.sModel
    sRegion= oModel_in.sRegion

 
   

    sFilename_pest_configuration = oPest_in.sFilename_pest_configuration
    sFilename_model_configuration = oModel_in.sFilename_model_configuration

    
    
    sWorkspace_pest_case = oModel_in.sWorkspace_calibration_case
    #create the directory if not available
    if not os.path.exists(sWorkspace_pest_case):
        os.mkdir(sWorkspace_pest_case)
    else:
        pass


    #start writing the script
    sFilename_script = sWorkspace_pest_case + slash + 'run_model'
    ifs = open(sFilename_script, 'w')
    
    sLine = '#!/bin/bash\n'
    ifs.write(sLine)

    sLine = 'echo "Started to prepare scripts in child node"\n'
    ifs.write(sLine)
    #the first one
    sLine = 'cat << EOF > step3.py' + '\n'
    ifs.write(sLine)

    sLine = '#!/share/apps/python/anaconda3.6/bin/python\n'
    ifs.write(sLine)

    sLine = 'import sys, os, stat\n'
    ifs.write(sLine)

    sLine = 'sSystem_paths = os.environ['+"'PATH'"+'].split(os.pathsep)\n'
    ifs.write(sLine)

    sLine = 'sys.path.extend(sSystem_paths)\n'
    ifs.write(sLine)    


    sLine = 'from pypest.models.maces.multipletimes.run_step3 import step3\n'
    ifs.write(sLine)

    sLine = 'sFilename_pest_configuration = ' + '"' + sFilename_pest_configuration + '"\n'
    ifs.write(sLine)

    sLine = 'sFilename_model_configuration = ' + '"' + sFilename_model_configuration + '"\n'
    ifs.write(sLine)
    sLine = 'step3(sFilename_pest_configuration, sFilename_model_configuration)\n'
    ifs.write(sLine)

    sLine = 'EOF\n'
    ifs.write(sLine)


    #the second 
    sLine = 'cat << EOF > step4.py' + '\n'
    ifs.write(sLine)

    sLine = '#!/share/apps/python/anaconda3.6/bin/python\n'
    ifs.write(sLine)
    sLine = 'import sys, os, stat\n'
    ifs.write(sLine)
    sLine = 'sSystem_paths = os.environ['+"'PATH'"+'].split(os.pathsep)\n'
    ifs.write(sLine)

    sLine = 'sys.path.extend(sSystem_paths)\n'
    ifs.write(sLine)    

    sLine = 'from pypest.models.maces.multipletimes.run_step4 import step4\n'
    ifs.write(sLine)

    sLine = 'sFilename_pest_configuration = ' + '"' + sFilename_pest_configuration + '"\n'
    ifs.write(sLine)

    sLine = 'sFilename_model_configuration = ' + '"' + sFilename_model_configuration + '"\n'
    ifs.write(sLine)

    sLine = 'step4(sFilename_pest_configuration, sFilename_model_configuration)\n'
    ifs.write(sLine)

    sLine = 'EOF\n'
    ifs.write(sLine)
    #the third one
    sLine = 'cat << EOF > step5.py' + '\n'
    ifs.write(sLine)

    sLine = '#!/share/apps/python/anaconda3.6/bin/python\n'
    ifs.write(sLine)
    sLine = 'import sys, os, stat\n'
    ifs.write(sLine)
    sLine = 'sSystem_paths = os.environ['+"'PATH'"+'].split(os.pathsep)\n'
    ifs.write(sLine)

    sLine = 'sys.path.extend(sSystem_paths)\n'
    ifs.write(sLine)    

    sLine = 'from pypest.models.maces.multipletimes.run_step5 import step5\n'
    ifs.write(sLine)

    sLine = 'sFilename_pest_configuration = ' + '"' + sFilename_pest_configuration + '"\n'
    ifs.write(sLine)

    sLine = 'sFilename_model_configuration = ' + '"' + sFilename_model_configuration + '"\n'
    ifs.write(sLine)

    sLine = 'step5(sFilename_pest_configuration, sFilename_model_configuration)\n'
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
    
    #step 4: run model is replace by the command line directly
    #sLine = './step4.py\n'
    #ifs.write(sLine)       
    iFlag_debug = 0
    if(iFlag_debug == 1 ):
        sPath_current = sWorkspace_pest_case + slash + 'beopest1'
    else:
        sPath_current = os.getcwd()
        
    sMaces_main = '/people/liao313/workspace/python/maces/MACES/src/MACES_main.py'

    sFilename_namelist_new =  os.path.basename(oModel_in.sFilename_namelist)


    #sLine = 'mpiexec -np 1 python ' +  sMaces_main +  ' -f ' + sFilename_namelist_new + ' \n'
    sLine = 'python ' +  sMaces_main +  ' -f ' + sFilename_namelist_new + ' \n'
    #namelist.maces.xml 
    ifs.write(sLine)     


    #step 5: extract  output
    sLine = './step5.py\n'
    ifs.write(sLine)
    

    ifs.close()

    os.chmod(sFilename_script, stat.S_IREAD | stat.S_IWRITE | stat.S_IXUSR)


    print('The pest run model file is prepared successfully!')

def run_step2(oPest_in, oModel_in):
    pypest_prepare_pest_command_file(oPest_in, oModel_in)
    return

def step2(sFilename_pest_configuration_in, sFilename_model_configuration_in):    
    aParameter_pest  = pypest_read_configuration_file(sFilename_pest_configuration)    
    aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration
    oPest = pypest(aParameter_pest)
    aParameter_model  = pypest_read_configuration_file(sFilename_model_configuration)   
    aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration
    oMaces = maces(aParameter_model)

    pypest_prepare_pest_command_file(oPest, oMaces)

    return
if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/pypest.xml'
    sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/model.xml'    
    step2(sFilename_pest_configuration, sFilename_model_configuration)
