import sys, os
import numpy as np
import xml.etree.ElementTree as ET

from pyearth.system.define_global_variables import *

from pyswat.shared.swat import pyswat

from pyswat.shared.swat_read_model_configuration_file import swat_read_model_configuration_file

from pypest.models.swat.shared.pest import pypest

from pypest.models.swat.auxiliary.swat_pypest_prepare_job_file import swat_pypest_prepare_job_file

from pypest.models.swat.once.run_step0 import run_step0
from pypest.models.swat.once.run_step1 import run_step1
from pypest.models.swat.once.run_step2 import run_step2
from pypest.models.swat.once.run_step6 import run_step6

from pypest.template.shared.pypest_read_configuration_file import pypest_read_pest_configuration_file

def swat_pypest_setup_case(oPest_in, oModel_in):
    
    #call each step
    
    run_step0(oPest_in, oModel_in)
    run_step1(oPest_in, oModel_in)
    run_step2(oPest_in, oModel_in)
    run_step6(oPest_in, oModel_in)

    return




