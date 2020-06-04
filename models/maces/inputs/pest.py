from abc import ABCMeta, abstractmethod

class pest(object):
    __metaclass__ = ABCMeta    
    aParameter={}
    pest_mode=0
    npargp=0
    nprior=0
    nobsgp=0
    ntplfile=0
    ninsfile=0
    svd=1

    sWokspace_pest_configuration=''
    sWorkspace_home=''
    sWorkspace_scratch=''
    sWorkspace_data=''
    sWorkspace_project=''
    sWorkspace_simulation=''
    sWorkspace_calibration=''
    sRegion=''
    sModel=''
    
    sWorkspace_pest=''

    def __init__(self, aParameter):
        print('PEST model is being initialized')
        self.aParameter = aParameter

        self.pest_mode             = aParameter[ 'pest_mode']
        self.npargp             = aParameter[ 'npargp']
        self.nprior             = aParameter[ 'nprior']
        self.nobsgp             = aParameter[ 'nobsgp']
        self.ntplfile             = aParameter[ 'ntplfile']
        self.ninsfile             = aParameter[ 'ninsfile']

        self.sWokspace_pest_configuration = aParameter['sWokspace_pest_configuration']
        self.sWorkspace_home       = aParameter[ 'sWorkspace_home' ]
        self.sWorkspace_scratch    = aParameter[ 'sWorkspace_scratch']
        self.sWorkspace_data       = aParameter[ 'sWorkspace_data']
        self.sWorkspace_project    = aParameter[ 'sWorkspace_project']
        self.sWorkspace_simulation = aParameter[ 'sWorkspace_simulation']
        self.sWorkspace_calibration= aParameter[ 'sWorkspace_calibration']
        self.sRegion               = aParameter[ 'sRegion']
        self.sModel               = aParameter[ 'sModel']
        self.sWorkspace_pest       = aParameter[ 'sWorkspace_pest']
        pass

    def read_pest_configuration(self, sInput):

        pass