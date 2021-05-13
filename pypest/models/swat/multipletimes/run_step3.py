import sys
import os

import numpy as np
from numpy  import array


from pypest.models.swat.multipletimes.step3.swat_prepare_pest_child_input_file import swat_prepare_pest_child_input_file

def swat_prepare_input_from_pest(oPest_in, sModel_in):
    """
    sFilename_configuration_in
    """
    #hru level
    swat_prepare_pest_child_input_file(sModel_in)
