import sys
import os
import numpy as np


from calendar import monthrange #calcuate the number of days in a month

from pyswat.postprocess.extract.swat_extract_stream_discharge import swat_extract_stream_discharge


def swat_extract_output_for_pest(oPest_in, oSwat_in):
    """
    Extract river discharge from a SWAT simulation
    """
    #stream discharge
    swat_extract_stream_discharge(oSwat_in)




    


   
