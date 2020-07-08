from abc import ABCMeta, abstractmethod

class maces(object):
    __metaclass__ = ABCMeta
    iCase_index=0

    sFilename_model_configuration=''
    sWorkspace_project=''
    sWorkspace_simulation=''
    sWorkspace_calibration=''
    sRegion=''
    sModel=''
    sCase=''
    sDate=''
    sFilename_namelist=''
    sFilename_parameter=''
    def __init__(self, aParameter):
        self.sFilename_model_configuration    = aParameter[ 'sFilename_model_configuration']
        self.sFilename_namelist    = aParameter[ 'sFilename_namelist']
        self.sFilename_parameter    = aParameter[ 'sFilename_parameter']
        self.sWorkspace_project    = aParameter[ 'sWorkspace_project']
        self.sWorkspace_simulation = aParameter[ 'sWorkspace_simulation']
        self.sWorkspace_calibration= aParameter[ 'sWorkspace_calibration']
        self.sRegion               = aParameter[ 'sRegion']
        self.sModel                = aParameter[ 'sModel']
        sCase_index = "{:03d}".format( int(aParameter['iCase_index']) )
        sCase = self.sModel + self.sDate + sCase_index
        self.sCase = sCase
        return
        