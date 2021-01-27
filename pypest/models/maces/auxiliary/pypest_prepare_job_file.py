#this function is used to copy swat and beopest from linux hpc to calibration folder
import sys, os, stat
sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system.define_global_variables import *

    
def pypest_prepare_job_file(oPest_in, oMode_in):
    """
    prepare the job submission file
    """

    #strings
    sModel = oMode_in.sModel
    sWorkspace_pest_case = oMode_in.sWorkspace_calibration_case
    sFilename_control = sWorkspace_pest_case + slash + oPest_in.sFilename_control    
    
    sFilename_job = sWorkspace_pest_case + slash + 'submit.job'
    ifs = open(sFilename_job, 'w')
   
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

    sLine = 'mpirun -np 36 ppest ' + sFilename_control + '  /M slave\n'
    ifs.write(sLine)

    ifs.close()


    print('The pest job file is copied successfully!')


if __name__ == '__main__':
   
    pass
