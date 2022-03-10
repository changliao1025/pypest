#this function is used to copy swat and beopest from linux hpc to calibration folder
from pyearth.system.define_global_variables import *

from pypest.models.swat.once.step2.pypest_prepare_run_script import pypest_prepare_run_script
    
def run_step2(oPest_in, oModel_in):
    pypest_prepare_run_script(oPest_in, oModel_in)
    return


