
import os #check existence
import platform #platform independent
import sys #append path
from pathlib import Path


#import the pyearth library
sPath_library_python = sWorkspace_code +  slash + 'python' + slash + 'library' + slash + 'pyearth_python'
sys.path.append(sPath_library_python)
from toolbox.reader.text_reader_string import text_reader_string


#add the package library
sPath_modflow_python = sWorkspace_code +  slash + 'python' + slash + 'modflow' + slash + 'modflow_python'
sys.path.append(sPath_modflow_python)

from modflow.pest.step1.modflow_prepare_pest_layer_parameter_template_file import modflow_prepare_pest_layer_parameter_template_file

#global constant
feet2meter = 0.3048
missing_value = -99.0
def ppest_prepare_template_files(sFilename_configuration_in, sCase_in =None, sJob_in=None, sModel_in = None):
    """
    plot the precipitation data file
    """
    if os.path.isfile(sFilename_configuration_in):
        pass
    else:
        print('The model configuration file does not exist!')
        return
    if sCase_in is not None:
        print(sCase_in)
        sCase = sCase_in
    else:
        #by default, this model will run in steady state
        sCase = 'ss'
    if sJob_in is not None:
        sJob = sJob_in
    else:
        sJob = 'modflow'
    if sModel_in is not None:
        print(sModel_in)
        sModel = sModel_in
    else:
        sModel = 'modflow' #the default mode is modflow
    

    

    modflow_prepare_pest_layer_parameter_template_file(sFilename_configuration_in, sCase, sJob, sModel)

if __name__ == '__main__':

    
    sRegion = 'tinpan'
    sModel ='modflow'
    sCase = 'tr003'
    sJob = sCase
    sTask = 'simulation'
    iFlag_simulation = 1
    iFlag_calibration = 0
    if iFlag_calibration == 1:
        sTask = 'calibration'
    sFilename_configuration = sWorkspace_scratch + slash + '03model' + slash \
              + sModel + slash + sRegion + slash \
              + sTask  + slash + sFilename_config
    ppest_prepare_template_files(sFilename_configuration,sCase, sJob, sModel)