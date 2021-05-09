#this function is used to copy swat and beopest from linux hpc to calibration folder
import sys
import os
import numpy as np
import datetime
import calendar
import errno
from os.path import isfile, join
from os import listdir

from numpy  import array
from shutil import copyfile, copy2



    
def swat_pypest_prepare_job_file(oPest_in, sModel_in = None):
    """
    prepare the job submission file
    """   
    
    nodes = 1
    ppn = 20
    node_str = "{:0d}".format( nodes )
    ppn_str = "{:0d}".format( ppn )
    tot_p = "{:0d}".format( nodes * ppn )

    #strings
    sModel = 'pypest'
    sWorkspace_pest_case = oMode_in.sWorkspace_calibration_case
    sFilename_control = sWorkspace_pest_case + slash + oPest_in.sFilename_control    

    sFilename_job = sWorkspace_pest_model + slash + 'submit.job'
    ifs = open(sFilename_job, 'w')
  
    #end of example
    sLine = '#!/bin/bash\n'
    ifs.write(sLine)

    sLine = '#SBATCH -A br21_liao313\n'
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

    sLine = 'mpirun -np '+tot_p+' ppest ' + sFilename_control + ' /M child\n'
    ifs.write(sLine)
    
    sLine1= '/share/apps/openmpi/1.8.3/gcc/5.2.0/bin/mpirun --mca btl '+ '^openib'
    sLine = sLine1 +' -np '+tot_p+' ppest ' + sFilename_control + ' /M child\n'
    ifs.write(sLine)

    ifs.close()


    print('The pest job file is copied successfully!')


if __name__ == '__main__':
    sRegion = 'tinpan'
    sModel ='swat'
    sCase = 'test'
    sJob = sCase
    sTask = 'simulation'
    iFlag_simulation = 1
    iFlag_pest = 0
    if iFlag_pest == 1:
        sTask = 'calibration'
    sFilename_configuration = sWorkspace_scratch + slash + '03model' + slash \
              + sModel + slash + sRegion + slash \
              + sTask  + slash + sFilename_config
            
    swat_prepare_calibration_job_file(sFilename_configuration_in, sModel)
