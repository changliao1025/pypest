import os,stat
import sys
import glob
import numpy as np
from pathlib import Path
from shutil import copyfile
from abc import ABCMeta, abstractmethod
import datetime
from shutil import copy2
import json
from json import JSONEncoder

from swaty.classes.pycase import swatcase

class CaseClassEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.float32):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
         
        if isinstance(obj, swatcase):
            return json.loads(obj.tojson())
       
        if isinstance(obj, list):
            pass  
        return JSONEncoder.default(self, obj)

class pestcase(object):
    __metaclass__ = ABCMeta    
    
    sPest_mode=''
    npar =0
    nobs=0
    npargp=0
    nprior=0
    nobsgp=0
    ntplfile=0
    ninsfile=0
    svd=1

    iFlag_parallel=0

    #iCase_index=0

    sWokspace_pest_configuration=''
    
  
    sRegion=''
    sModel='pest'
    sModel_type='swat'
    iModel_type=1
    sPest_method='pest' #can be other
    
    sCase=''
    sDate=''
    
    sWorkspace_pest=''
    sFilename_control=''
    sFilename_instruction=''    
    sFilename_template=''
    sFilename_output=''
    pSwat=None

    def __init__(self, aConfig_in):
        print('PEST model is being initialized')
        #self.aConfig_in = aConfig_in
        if 'sPest_mode' in aConfig_in:
            self.sPest_mode             = aConfig_in[ 'sPest_mode']
        
        if 'sDate' in aConfig_in:
            self.sDate = aConfig_in[ 'sDate']
        if 'iFlag_parallel' in aConfig_in:
            self.iFlag_parallel             = int(aConfig_in[ 'iFlag_parallel'])
        
        if 'iCase_index' in aConfig_in:
            self.iCase_index             = int(aConfig_in[ 'iCase_index'])
        if 'npargp' in aConfig_in:
            self.npargp             = int(aConfig_in[ 'npargp'])
        if 'npar' in aConfig_in:
            self.npar             = int(aConfig_in[ 'npar'])
        if 'nobs' in aConfig_in:
            self.nobs             = int(aConfig_in[ 'nobs'])
        if 'nprior' in aConfig_in:
            self.nprior             = int(aConfig_in[ 'nprior'])
        if 'nobsgp' in aConfig_in:
            self.nobsgp             = int(aConfig_in[ 'nobsgp'])
        if 'ntplfile' in aConfig_in:
            self.ntplfile             = int(aConfig_in[ 'ntplfile'])
        if 'ninsfile' in aConfig_in:
            self.ninsfile             = int(aConfig_in[ 'ninsfile'])
        if 'sWokspace_pest_configuration' in aConfig_in:
            self.sWokspace_pest_configuration = aConfig_in['sWokspace_pest_configuration']
        
        
        if 'sWorkspace_input' in aConfig_in:
            self.sWorkspace_input = aConfig_in[ 'sWorkspace_input']
        if 'sWorkspace_output' in aConfig_in:
            self.sWorkspace_output= aConfig_in[ 'sWorkspace_output']
        if 'sRegion' in aConfig_in:
            self.sRegion               = aConfig_in[ 'sRegion']
        if 'sModel' in aConfig_in:
            self.sModel                = aConfig_in[ 'sModel']
        if 'sWorkspace_pest' in aConfig_in:
            self.sWorkspace_pest       = aConfig_in[ 'sWorkspace_pest']
        if 'sFilename_control' in aConfig_in:
            self.sFilename_control = aConfig_in['sFilename_control']
        if 'sFilename_instruction' in aConfig_in:
            self.sFilename_instruction = aConfig_in['sFilename_instruction']
        if 'sFilename_output' in aConfig_in:
            self.sFilename_output = aConfig_in['sFilename_output']

        sCase_index = "{:03d}".format( self.iCase_index )
        sCase = self.sModel + self.sDate + sCase_index
        self.sCase = sCase
        sPath = str(Path(self.sWorkspace_output)  /  sCase)
        self.sWorkspace_output_case = sPath
        Path(sPath).mkdir(parents=True, exist_ok=True)

        pass

    def read_pest_configuration(self, sInput):

        pass
    def setup(self):

        if self.sModel_type == 'swat':
            self.pSwat.setup_pest_calibration()
            #set up pest file
            
            self.pypest_create_pest_template_file()
            self.pypest_create_pest_instruction_file()
            self.pypest_create_pest_control_file()
        else:
            pass
        
        return
    def run(self):
        return
    def analyze(self):
        return
    def export(self):
        return    
    def export_config_to_json(self, sFilename_output):
        with open(sFilename_output, 'w', encoding='utf-8') as f:
            json.dump(self.__dict__, f,sort_keys=True, \
                ensure_ascii=False, \
                indent=4, cls=CaseClassEncoder)
        return

    def tojson(self):
        aSkip = []      

        obj = self.__dict__.copy()
        for sKey in aSkip:
            obj.pop(sKey, None)
        sJson = json.dumps(obj,\
            sort_keys=True, \
                indent = 4, \
                    ensure_ascii=True, \
                        cls=CaseClassEncoder)
        return sJson

    
    def pypest_create_pest_template_file(self):
        return
    def pypest_create_pest_instruction_file(self):
        return
    def pypest_create_pest_control_file(self):
        return    
    def pypest_prepare_job_file(self):
        """
        prepare the job submission file
        """    
       
        sWorkspace_pest_model = self.sWorkspace_output_case
        sFilename_job = os.path.join(sWorkspace_pest_model , 'job.submit')     
        iFlag_parallel = self.iFlag_parallel
        sPest_method = self.sPest_method

        if iFlag_parallel == 1: #parallel, only beopest is supported right now
            ifs = open(sFilename_job, 'w')    
            sLine = '#!/bin/bash\n'
            ifs.write(sLine)
            sLine = '#SBATCH -A inversion\n'
            ifs.write(sLine)
            sLine = '#SBATCH -t 100:00:00\n'
            ifs.write(sLine)
            sLine = '#SBATCH -N 3\n'
            ifs.write(sLine)
            sLine = '#SBATCH -n 36\n'
            ifs.write(sLine)
            sLine = '#SBATCH -J ' + self.sModel_type + '\n'
            ifs.write(sLine)
            sLine = '#SBATCH -o out.out\n'
            ifs.write(sLine)
            sLine = '#SBATCH -e err.err\n'
            ifs.write(sLine)
            sLine = '#SBATCH --mail-type=ALL\n'
            ifs.write(sLine)
            sLine = '#SBATCH --mail-user=chang.liao@pnnl.gov\n'
            ifs.write(sLine)
            sLine = 'cd $SLURM_SUBMIT_DIR\n'
            ifs.write(sLine)
            sLine = 'module purge\n'
            ifs.write(sLine)
            sLine = 'module load python/anaconda3.6\n'
            ifs.write(sLine)
            sLine = 'module load gcc/5.2.0\n'
            ifs.write(sLine)
            sLine = 'module load openmpi/1.8.3\n'
            ifs.write(sLine)
            sLine = 'mpirun -np 36 ppest ' + sWorkspace_pest_model + '_swat /M child\n'
            ifs.write(sLine)
            ifs.close()
        else:
            #serial calibration
            if sPest_method == 'pest':
                ifs = open(sFilename_job, 'w')    
                sLine = '#!/bin/bash\n'
                ifs.write(sLine)
                sLine = '#SBATCH -A inversion\n'
                ifs.write(sLine)
                sLine = '#SBATCH -t 100:00:00\n'
                ifs.write(sLine)
                sLine = '#SBATCH -N 1\n'
                ifs.write(sLine)
                sLine = '#SBATCH -n 10\n'
                ifs.write(sLine)
                sLine = '#SBATCH -J ' + self.sModel_type + '\n'
                ifs.write(sLine)
                sLine = '#SBATCH -o out.out\n'
                ifs.write(sLine)
                sLine = '#SBATCH -e err.err\n'
                ifs.write(sLine)
                sLine = '#SBATCH --mail-type=ALL\n'
                ifs.write(sLine)
                sLine = '#SBATCH --mail-user=chang.liao@pnnl.gov\n'
                ifs.write(sLine)
                sLine = 'cd $SLURM_SUBMIT_DIR\n'
                ifs.write(sLine)
                sLine = 'module purge\n'
                ifs.write(sLine)
                sLine = 'module load python/anaconda3.6\n'
                ifs.write(sLine)
                sLine = 'module load gcc/5.2.0\n'
                ifs.write(sLine)                
                sLine = 'pest ' + sWorkspace_pest_model + '_swat /M child\n'
                ifs.write(sLine)
                ifs.close()
            else:
                if sPest_method =='sceua':
                    pass


        print('The pest job file is copied successfully!')