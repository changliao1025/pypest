import sys, os

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system.define_global_variables import *
def maces_prepare_job_file(oModel_in):

    iFlag_calibration = oModel_in.iFlag_calibration
    if iFlag_calibration == 1:
        pass
    else:
        sWorkspace_simulation = oModel_in.sWorkspace_simulation
        
        sCase = oModel_in.sCase
        sWorkspace_simulation_case = sWorkspace_simulation + slash + sCase
        if not os.path.exists(sWorkspace_simulation_case):
            os.mkdir(sWorkspace_simulation_case)
        else:
            pass
    sFilename_job = sWorkspace_simulation_case + slash + 'submit_maces.job'
    ofs = open(sFilename_job, 'w')


    sLine = '#!/bin/bash\n'
    ofs.write(sLine)

    sLine = '#SBATCH -A taim\n'
    ofs.write(sLine)

    sLine = '#SBATCH  --job-name=maces' + '\n'
    ofs.write(sLine)

    sLine = '#SBATCH -t 03:00:00' + '\n'
    ofs.write(sLine)

    sLine = '#SBATCH  --nodes=1' + '\n'
    ofs.write(sLine)

    sLine = '#SBATCH  --ntasks-per-node=24' + '\n'
    ofs.write(sLine)

    sLine = '#SBATCH  --partition=short' + '\n'
    ofs.write(sLine)

    sLine = '#SBATCH -o stdout.out\n'
    ofs.write(sLine)

    sLine = '#SBATCH -e stderr.err\n'
    ofs.write(sLine)

    sLine = '#SBATCH --mail-type=ALL\n'
    ofs.write(sLine)

    sLine = '#SBATCH --mail-user=chang.liao@pnnl.gov\n'
    ofs.write(sLine)

    sLine = 'cd $SLURM_SUBMIT_DIR\n'
    ofs.write(sLine)

    sLine = 'module purge\n'
    ofs.write(sLine)

    sLine = 'module load gcc/5.2.0\n'
    ofs.write(sLine)

    sLine = 'module load openmpi/1.8.3' + '\n'
    ofs.write(sLine)

    sLine = 'module load netcdf/4.3.2' + '\n'
    ofs.write(sLine)

    sLine = 'module load python/anaconda3.6' + '\n'
    ofs.write(sLine)

    sLine = 'source /share/apps/python/anaconda3.6/etc/profile.d/conda.sh' + '\n'
    ofs.write(sLine)
    
    
    sLine = 'conda activate mpienv_constance' + '\n'
    ofs.write(sLine)

    sMaces_main = '/people/liao313/workspace/python/maces/MACES/src/MACES_main.py'

    sFilename_namelist_new = sWorkspace_simulation_case + slash + os.path.basename(oModel_in.sFilename_namelist)

    sLine = 'mpiexec -np 1 python ' +  sMaces_main +  ' -f ' + sFilename_namelist_new + ' \n'
    #namelist.maces.xml 
    ofs.write(sLine)   

    sLine = 'conda deactivate' + '\n'
    ofs.write(sLine) 

    ofs.close()

    return