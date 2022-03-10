
from pyearth.system.define_global_variables import *



from pypest.models.swat.once.run_step0 import run_step0
from pypest.models.swat.once.run_step1 import run_step1
from pypest.models.swat.once.run_step2 import run_step2
from pypest.models.swat.once.run_step6 import run_step6



def swat_pypest_setup_case(oPest_in, oModel_in):
    
    #call each step
    
    run_step0(oPest_in, oModel_in)
    run_step1(oPest_in, oModel_in)
    run_step2(oPest_in, oModel_in)
    run_step6(oPest_in, oModel_in)

    return




