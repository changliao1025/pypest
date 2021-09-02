import sys
import os
import datetime
import calendar
import numpy as np
from numpy  import array



from pyswat.scenarios.swat_write_watershed_input_file import swat_write_watershed_input_file
from pyswat.scenarios.swat_write_subbasin_input_file import swat_write_subbasin_input_file
from pyswat.scenarios.swat_write_hru_input_file import swat_write_hru_input_file

def swat_prepare_input_from_pest(oPest_in, oSwat_in):
    """
    Prepare a swat simulation after PEST generates new parameter files
    """
    swat_write_watershed_input_file(oSwat_in)
    #swat_write_subbasin_input_file(oSwat_in)    
    #swat_write_hru_input_file(oSwat_in)
    print('Finished translating pest parameter to model input')


   
