#this script is used to set up a model easily so we don't have to copy/paste
import sys, os
from pathlib import Path
sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyearth.system.define_global_variables import *
from abc import ABCMeta, abstractmethod
import datetime

pDate = datetime.datetime.today()
sDate_default = "{:04d}".format(pDate.year) + "{:02d}".format(pDate.month) + "{:02d}".format(pDate.day)

class maces(object):
    __metaclass__ = ABCMeta
    iCase_index=0
    iSiteID=0
    iFlag_calibration=0

    sFilename_model_configuration=''
    sWorkspace_project=''
    sWorkspace_simulation=''
    sWorkspace_simulation_case=''
    sWorkspace_calibration=''
    sWorkspace_calibration_case=''
    sRegion=''
    sModel=''
    sCase=''
    sDate=''
    sSiteID=''
    sDate_start =''
    sDate_end=''
    sFilename_namelist=''

    #sub module
    sModel_minac=''
    sModel_omac=''
    #config
    sFilename_config_hydro=''
    sFilename_config_minac=''
    sFilename_config_omac=''
    sFilename_config_wavero=''
    sFilename_config_lndmgr=''

    #parameter
    sFilename_parameter_hydro=''
    sFilename_parameter_minac=''
    sFilename_parameter_omac=''
    sFilename_parameter_wavero=''
    sFilename_parameter_lndmgr=''
    #template
    sFilename_template_hydro=''
    sFilename_template_minac=''
    sFilename_template_omac=''
    sFilename_template_wavero=''
    sFilename_template_lndmgr=''

    #instruction 
    sFilename_instruction_hydro=''
    sFilename_instruction_minac=''
    sFilename_instruction_omac=''
    sFilename_instruction_wavero=''
    sFilename_instruction_lndmgr=''

    #output
    sFilename_output_hydro=''
    sFilename_output_minac=''
    sFilename_output_omac=''
    sFilename_output_wavero=''
    sFilename_output_lndmgr=''

    def __init__(self, aParameter):
        self.sFilename_model_configuration    = aParameter[ 'sFilename_model_configuration']
        self.sFilename_namelist    = aParameter[ 'sFilename_namelist']
        #self.sWorkspace_project    = aParameter[ 'sWorkspace_project']
        self.sRegion               = aParameter[ 'sRegion']
        self.sModel                = aParameter[ 'sModel']
        self.sDate_start              = aParameter[ 'sDate_start']
        self.sDate_end                = aParameter[ 'sDate_end']

        self.sWorkspace_simulation = sWorkspace_scratch + slash + '04model' + slash \
            + self.sModel + slash + self.sRegion +  slash + 'simulation'
        sPath = self.sWorkspace_simulation
        Path(sPath).mkdir(parents=True, exist_ok=True)

        self.sWorkspace_calibration = sWorkspace_scratch + slash + '04model' + slash  \
            + self.sModel + slash + self.sRegion +  slash + 'calibration'
        sPath = self.sWorkspace_calibration
        Path(sPath).mkdir(parents=True, exist_ok=True)


        sCase_index = "{:03d}".format( int(aParameter['iCase_index']) )
        sDate                = aParameter[ 'sDate']
        if sDate is not None:
            self.sDate= sDate
        else:
            self.sDate = sDate_default
            
        sCase = self.sModel + self.sDate + sCase_index
        self.sCase = sCase
        self.iSiteID                = int(aParameter[ 'iSiteID'])
        self.sSiteID = "{:03d}".format(self.iSiteID)

        self.sWorkspace_simulation_case = self.sWorkspace_simulation + slash + sCase
        sPath = self.sWorkspace_simulation_case
        Path(sPath).mkdir(parents=True, exist_ok=True)

        self.sWorkspace_calibration_case = self.sWorkspace_calibration + slash + sCase
        sPath = self.sWorkspace_calibration_case
        Path(sPath).mkdir(parents=True, exist_ok=True)

        self.iFlag_calibration =  int(aParameter['iFlag_calibration']) 

        #config
        self.sFilename_config_hydro =      aParameter[ 'sFilename_config_hydro']
        self.sFilename_config_minac =      aParameter[ 'sFilename_config_minac']
        self.sFilename_config_omac =       aParameter[ 'sFilename_config_omac']
        self.sFilename_config_wavero =     aParameter[ 'sFilename_config_wavero']
        self.sFilename_config_lndmgr =    aParameter[ 'sFilename_config_lndmgr']

        #parameter
        self.sFilename_parameter_hydro = aParameter[ 'sFilename_parameter_hydro']
        self.sFilename_parameter_minac = aParameter[ 'sFilename_parameter_minac']
        self.sFilename_parameter_omac = aParameter[ 'sFilename_parameter_omac']
        self.sFilename_parameter_wavero = aParameter[ 'sFilename_parameter_wavero']
        self.sFilename_parameter_lndmgr = aParameter[ 'sFilename_parameter_lndmgr']
        #template
        self.sFilename_template_hydro = aParameter[ 'sFilename_template_hydro']
        self.sFilename_template_minac = aParameter[ 'sFilename_template_minac']
        self.sFilename_template_omac = aParameter[ 'sFilename_template_omac']
        self.sFilename_template_wavero = aParameter[ 'sFilename_template_wavero']
        self.sFilename_template_lndmgr = aParameter[ 'sFilename_template_lndmgr']

        self.sFilename_instruction_hydro =      aParameter[ 'sFilename_instruction_hydro']
        self.sFilename_instruction_minac =      aParameter[ 'sFilename_instruction_minac']
        self.sFilename_instruction_omac =       aParameter[ 'sFilename_instruction_omac']
        self.sFilename_instruction_wavero =     aParameter[ 'sFilename_instruction_wavero']
        self.sFilename_instruction_lndmgr =    aParameter[ 'sFilename_instruction_lndmgr']

        self.sFilename_output_hydro =   aParameter[ 'sFilename_output_hydro']
        self.sFilename_output_minac =   aParameter[ 'sFilename_output_minac']
        self.sFilename_output_omac =    aParameter[ 'sFilename_output_omac']
        self.sFilename_output_wavero =  aParameter[ 'sFilename_output_wavero']
        self.sFilename_output_lndmgr = aParameter[ 'sFilename_output_lndmgr']
        return
        