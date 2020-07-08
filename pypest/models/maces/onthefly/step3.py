#we will use the existing functions to convert
import sys, os
import numpy as np
from shutil import copy2
sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system.define_global_variables import *

from pyes.toolbox.reader.text_reader_string import text_reader_string

#the pypest library
sPath_pypest = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest)

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces

from pypest.template.shared.pypest_read_configuration_file import pypest_read_configuration_file
from pypest.template.shared.xmlchange import xmlchange

def maces_copy_input_files(oPest_in, oModel_in):

    
    sWorkspace_calibration_relative = oModel_in.sWorkspace_calibration
    sWorkspace_calibration = sWorkspace_scratch + slash + sWorkspace_calibration_relative
    sWorkspace_pest_model = sWorkspace_calibration #+ slash + sModel + slash + sRegion
    #a glimplse of the job file
    #==================================================
    #JOB_DIRECTORY=/people/liao313/workspace/python/maces/MACES/src
    #cd $JOB_DIRECTORY
    #mpiexec -np 1 python MACES_main.py -f namelist.maces.xml 
    #==================================================
    #we will copy the namelist.maces.xml only
    #maybe we also need the MACES_main.py? if this program is at global directory, then we can call it from anywhere

    #the model will have more than one namelist in the future
    sFilename_namelist = oModel_in.sFilename_namelist
    iFlag_debug = 1
    if(iFlag_debug == 1 ):
        sPath_current = sWorkspace_pest_model + slash + 'beopest1'
    else:
        sPath_current = os.getcwd()
    print('The current child path is: ' + sPath_current)
    sWorkspace_child = sPath_current

    sFilename_new = sPath_current + slash + 'namelist.maces.xml'
    copy2(sFilename_namelist, sFilename_new)
    return

def pypest_convert_parameter_files(oPest_in, oModel_in):
    sWorkspace_simulation_relative = oModel_in.sWorkspace_simulation
    sCase = oModel_in.sCase
    sWorkspace_simulation = sWorkspace_scratch +  slash  + sWorkspace_simulation_relative
    sWorkspace_simulation_case  = sWorkspace_simulation + slash + sCase

    sWorkspace_calibration_relative = oModel_in.sWorkspace_calibration
    sWorkspace_calibration = sWorkspace_scratch + slash + sWorkspace_calibration_relative
    sWorkspace_pest_model = sWorkspace_calibration

    #in order to avoid issue, we will copy the input file into the current folder
    maces_copy_input_files(oPest_in, oModel_in)

    #next, we need to read the parameter file generated by pest
    #read hydro parameter
    #the multiple parameter index starts with 0
    sIndex = "{:02d}".format( 0 )  


    iFlag_debug = 1
    if(iFlag_debug == 1 ):
        sPath_current = sWorkspace_pest_model + slash + 'beopest1'
    else:
        sPath_current = os.getcwd()
    sWorkspace_child = sPath_current    
    sFilename_parameter = sWorkspace_child + slash + 'pest_template_' + sIndex + '.para'

    if os.path.isfile(sFilename_parameter):
        pass
    else:
        print('The file does not exist!')
        return
        
    aData_all = text_reader_string(sFilename_parameter, cDelimiter_in = ',')
    aDummy = aData_all[0,:]
    nParameter = len(aDummy) - 1
    aParameter_list = aDummy[1: nParameter+1]

    ngrid = 1 
    aParameter_value = (aData_all[1:ngrid+1,1: nParameter+1]).astype(float)
    aParameter_value = np.asarray(aParameter_value)
    
    #second we will call the existing python function to convert

    #construct the command string
    #./xmlchange.py -f optpar_minac.xml -g M12MOD -p rhoSed -v 2650.0

    #for p in range(0, nParameter):
    sFilename  = sWorkspace_simulation_case + slash + 'optpar_minac.xml'
    sValue =  "{:16.2f}".format( aParameter_value[0] )
    #sCommand = '-f' + sFilename + ' -g M12MOD -p rhoSed -v '  + sValue
    xmlchange(filename=sFilename, group='M12MOD', parameter='Cz0',value=sValue)
    print('Finished')


    
    return

def step3(sFilename_pest_configuration_in, sFilename_model_configuration_in):    
    aParameter_pest  = pypest_read_configuration_file(sFilename_pest_configuration)    
    aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration
    oPest = pypest(aParameter_pest)
    aParameter_model  = pypest_read_configuration_file(sFilename_model_configuration)   
    aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration
    oMaces = maces(aParameter_model)
    pypest_convert_parameter_files(oPest, oMaces)
    return


if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/03configuration/pypest/maces/pest.xml'
    sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/model.xml'    
    step3(sFilename_pest_configuration, sFilename_model_configuration)
    