import sys
import os
import datetime
import calendar
import numpy as np
from numpy  import array




from pyswat.scenarios.swat_write_hru_input_file import swat_write_hru_input_file

def swat_prepare_input_from_pest(oPest_in, oModel_in):
    """
    sFilename_configuration_in
    """
    #hru level
    swat_write_hru_input_file(oModel_in)
    print('Finished translating pest parameter to model input')


   
