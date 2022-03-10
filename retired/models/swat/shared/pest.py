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

    sFilename_pest_configuration='' #the actual full path to the pest configuration
    
    #sWokspace_pest_configuration='' #this is where pest files should be written to
    
    sWorkspace_pest=''
    sFilename_control=''
   

    def __init__(self, aParameter):
        print('PEST model is being initialized')
        self.aParameter = aParameter

        self.sPest_mode             = aParameter[ 'sPest_mode']
  
        
        self.npargp             = int(aParameter[ 'npargp'])
        self.npar             = int(aParameter[ 'npar'])
        self.nobs             = int(aParameter[ 'nobs'])
        self.nprior             = int(aParameter[ 'nprior'])
        self.nobsgp             = int(aParameter[ 'nobsgp'])
        self.ntplfile             = int(aParameter[ 'ntplfile'])
        self.ninsfile             = int(aParameter[ 'ninsfile'])
        self.sFilename_pest_configuration = aParameter['sFilename_pest_configuration']

      
        
        self.sWorkspace_pest   = aParameter[ 'sWorkspace_pest']
        self.sFilename_control = aParameter['sFilename_control']
        self.sWorkspace_home       = aParameter[ 'sWorkspace_home' ]
        self.sWorkspace_scratch    = aParameter[ 'sWorkspace_scratch']
        self.sWorkspace_data       = aParameter[ 'sWorkspace_data']
        
        
        
        self.sWorkspace_pest       = aParameter[ 'sWorkspace_pest']
        self.sFilename_control = aParameter['sFilename_control']
        self.sFilename_instruction = aParameter['sFilename_instruction']
        self.sFilename_output = aParameter['sFilename_output']

        
   
        

        
        pass

    def read_pest_configuration(self, sInput):

        pass