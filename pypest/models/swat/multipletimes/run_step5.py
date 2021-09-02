import sys
import os
import datetime
import calendar

import numpy as np
from numpy  import array

from calendar import monthrange #calcuate the number of days in a month


from pyswat.postprocess.extract.swat_extract_stream_discharge import swat_extract_stream_discharge


def swat_extract_output_for_pest(oPest_in, oSwat_in):
    """
    Extract river discharge from a SWAT simulation
    """
    #stream discharge
    swat_extract_stream_discharge(oSwat_in)



   
