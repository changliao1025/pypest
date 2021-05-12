import sys
import os
import numpy as np
import datetime

from numpy  import array
from pyearth.system.define_global_variables import *


from pyearth.toolbox.reader.text_reader_string import text_reader_string

from pypest.models.swat.once.step6.swat_prepare_pest_instruction_file import swat_prepare_pest_instruction_file

def run_step6(oPest_in, oModel_in):
    swat_prepare_pest_instruction_file(oPest_in, oModel_in)
    return