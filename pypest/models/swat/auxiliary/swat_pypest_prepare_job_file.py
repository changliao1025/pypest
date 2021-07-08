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



from pyearth.system.define_global_variables import *
    
def swat_pypest_prepare_job_file(oPest_in, oModel_in):
    """
    prepare the job submission file
    """   
    
    nodes = 1
    ppn = 10
    node_str = "{:0d}".format( nodes )
    ppn_str = "{:0d}".format( ppn )
    tot_p = "{:0d}".format( nodes * ppn )

    #strings
    sModel = 'pypest'
    sWorkspace_pest_case = oModel_in.sWorkspace_calibration_case
    sFilename_control = sWorkspace_pest_case + slash + oPest_in.sFilename_control    

    sFilename_job = sWorkspace_pest_case + slash + 'submit.job'
    ifs = open(sFilename_job, 'w')
  
    #end of example
    sLine = '#!/bin/bash' + '\n'
    ifs.write(sLine)

    sLine = '#SBATCH -A m1800' + '\n'
    ifs.write(sLine)

    sLine = '#SBATCH -q debug' + '' + '\n'
    sLine = '#SBATCH -q regular' + '' + '\n'
    ifs.write(sLine)

    sLine = '#SBATCH -t 00:30:00' + '\n'
    sLine = '#SBATCH -t 05:00:00' + '\n'
    ifs.write(sLine)

    sLine = '#SBATCH -N 1' + '\n'
    ifs.write(sLine)

    sLine = '#SBATCH -n ' +ppn_str+ '\n'
    ifs.write(sLine)

    sLine = '#SBATCH -J ' + sModel  + '\n'
    ifs.write(sLine)

    sLine = '#SBATCH -C haswell'  + '\n'
    ifs.write(sLine)
    sLine = '#SBATCH -L SCRATCH'  + '\n'
    ifs.write(sLine)

    sLine = '#SBATCH -o out.out' + '\n'
    ifs.write(sLine)

    sLine = '#SBATCH -e err.err' + '\n'
    ifs.write(sLine)

    sLine = '#SBATCH --mail-type=ALL' + '\n'
    ifs.write(sLine)

    sLine = '#SBATCH --mail-user=chang.liao@pnnl.gov' + '\n'
    ifs.write(sLine)

    sLine = 'cd $SLURM_SUBMIT_DIR' + '\n'
    ifs.write(sLine)

    sLine = 'module purge' + '\n'
    ifs.write(sLine)

    #python/3.7-anaconda-2019.10 
    sLine = 'module load python/3.7-anaconda-2019.10 '  + '\n'  
    ifs.write(sLine)

    sLine = 'module load gcc/6.1.0' +  '\n'
    ifs.write(sLine)

    sLine = 'module load openmpi/3.1.3' + '\n'
    ifs.write(sLine)

    #sLine = 'mpirun -np '+tot_p+' ppest ' + sFilename_control + ' /M child' + '\n'
    #ifs.write(sLine)

    #/global/common/software/m3169/cori/openmpi/3.1.3/intel/bin/mpirun
    
    #sLine1= '/global/common/software/m3169/cori/openmpi/3.1.3/intel/bin/mpirun --mca btl '+ '^openib'
    sLine1= '/global/common/software/m3169/cori/openmpi/3.1.3/gnu/bin/mpirun '
    sLine = sLine1 +' -np '+tot_p+' ppest ' + sFilename_control + ' /M child' + '\n'
    ifs.write(sLine)

    ifs.close()


    print('The pest job file is copied successfully!')


