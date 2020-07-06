from abc import ABCMeta, abstractmethod

class pypest(object):
    __metaclass__ = ABCMeta    
    aParameter={}
    sPest_mode=''
    npar =0
    nobs=0
    npargp=0
    nprior=0
    nobsgp=0
    ntplfile=0
    ninsfile=0
    svd=1

    iCase_index=0

    sWokspace_pest_configuration=''
    sWorkspace_home=''
    sWorkspace_scratch=''
    sWorkspace_data=''
    sWorkspace_project=''
    sWorkspace_simulation=''
    sWorkspace_calibration=''
    sRegion=''
    sModel=''
    sCase=''
    sDate=''
    
    sWorkspace_pest=''
    sFilename_control=''
    sFilename_instruction=''    
    sFilename_template=''
    sFilename_output=''

    def __init__(self, aParameter):
        print('PEST model is being initialized')
        self.aParameter = aParameter

        self.sPest_mode             = aParameter[ 'sPest_mode']
        self.sDate = aParameter[ 'sDate']
        
        self.npargp             = int(aParameter[ 'npargp'])
        self.npar             = int(aParameter[ 'npar'])
        self.nobs             = int(aParameter[ 'nobs'])
        self.nprior             = int(aParameter[ 'nprior'])
        self.nobsgp             = int(aParameter[ 'nobsgp'])
        self.ntplfile             = int(aParameter[ 'ntplfile'])
        self.ninsfile             = int(aParameter[ 'ninsfile'])

        self.sWokspace_pest_configuration = aParameter['sWokspace_pest_configuration']
        self.sWorkspace_home       = aParameter[ 'sWorkspace_home' ]
        self.sWorkspace_scratch    = aParameter[ 'sWorkspace_scratch']
        self.sWorkspace_data       = aParameter[ 'sWorkspace_data']
        self.sWorkspace_project    = aParameter[ 'sWorkspace_project']
        self.sWorkspace_simulation = aParameter[ 'sWorkspace_simulation']
        self.sWorkspace_calibration= aParameter[ 'sWorkspace_calibration']
        self.sRegion               = aParameter[ 'sRegion']
        self.sModel                = aParameter[ 'sModel']
        self.sWorkspace_pest       = aParameter[ 'sWorkspace_pest']
        self.sFilename_control = aParameter['sFilename_control']
        self.sFilename_instruction = aParameter['sFilename_instruction']
        self.sFilename_output = aParameter['sFilename_output']

        sCase_index = "{:03d}".format( int(aParameter['iCase_index']) )
        sCase = self.sModel + self.sDate + sCase_index
        self.sCase = sCase
        pass

    def read_pest_configuration(self, sInput):

        pass