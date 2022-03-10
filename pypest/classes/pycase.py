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

from pyearth.system.define_global_variables import *

class CaseClassEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.float32):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
         
    
       
        if isinstance(obj, list):
            pass  
        return JSONEncoder.default(self, obj)

class pestcase(object):
    __metaclass__ = ABCMeta    
    aConfig_in={}
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

    def __init__(self, aConfig_in):
        print('PEST model is being initialized')
        self.aConfig_in = aConfig_in
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
        if 'sWorkspace_home' in aConfig_in:
            self.sWorkspace_home       = aConfig_in[ 'sWorkspace_home' ]
        if 'sWorkspace_scratch' in aConfig_in:
            self.sWorkspace_scratch    = aConfig_in[ 'sWorkspace_scratch']
        if 'sWorkspace_data' in aConfig_in:
            self.sWorkspace_data       = aConfig_in[ 'sWorkspace_data']
        if 'sWorkspace_project' in aConfig_in:
            self.sWorkspace_project    = aConfig_in[ 'sWorkspace_project']
        if 'sWorkspace_simulation' in aConfig_in:
            self.sWorkspace_simulation = aConfig_in[ 'sWorkspace_simulation']
        if 'sWorkspace_calibration' in aConfig_in:
            self.sWorkspace_calibration= aConfig_in[ 'sWorkspace_calibration']
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
        pass

    def read_pest_configuration(self, sInput):

        pass
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

        
    def pypest_prepare_job_file(self, sFilename_configuration_in, sModel_in = None):
        """
        prepare the job submission file
        """    
        #strings
      
        sWorkspace_scratch=self.sWorkspace_scratch

        
        
        sWorkspace_calibration_relative = self.sWorkspace_calibration



        sRegion = config['sRegion']
  


        sWorkspace_calibration = sWorkspace_scratch + slash + sWorkspace_calibration_relative

        sWorkspace_pest_model = sWorkspace_calibration + slash + sModel

        sFilename_job = sWorkspace_pest_model + slash + 'job.submit'
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

        sLine = '#SBATCH -J ' + sModel + '\n'
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

        sLine = 'mpirun -np 36 ppest ' + sWorkspace_pest_model+slash+sRegion + '_swat /M child\n'
        ifs.write(sLine)

        ifs.close()


        print('The pest job file is copied successfully!')