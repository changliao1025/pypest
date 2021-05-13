import sys
import os
import datetime
import calendar

import numpy as np
from numpy  import array

from calendar import monthrange #calcuate the number of days in a month


from swat.postprocess.swat_extract_stream_discharge import swat_extract_stream_discharge


def swat_extract_output_for_pest(oPest_in, sModel):
    """
    sFilename_configuration_in
    """
    #stream discharge
    swat_extract_stream_discharge(sModel)



   
