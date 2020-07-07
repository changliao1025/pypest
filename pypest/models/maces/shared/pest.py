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

    sFilename_pest_configuration=''
    sWokspace_pest_configuration=''

    

    
    
    
    sWorkspace_pest=''
    sFilename_control=''
    #sFilename_instruction=''
    #sFilename_hydro_template=''
    #sFilename_hydro_parameter=''
    #sFilename_template=''
    #sFilename_output=''

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
        self.sWokspace_pest_configuration = aParameter['sWokspace_pest_configuration']

        #system wide variable will not be used
       

        
        self.sWorkspace_pest       = aParameter[ 'sWorkspace_pest']
        self.sFilename_control = aParameter['sFilename_control']
        #self.sFilename_instruction = aParameter['sFilename_instruction']
        #self.sFilename_hydro_template = aParameter['sFilename_hydro_template']
        #self.sFilename_hydro_parameter = aParameter['sFilename_hydro_parameter']
        #self.sFilename_output = aParameter['sFilename_output']

        
        pass

    def read_pest_configuration(self, sInput):

        pass