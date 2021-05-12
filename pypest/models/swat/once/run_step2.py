#this function is used to copy swat and beopest from linux hpc to calibration folder
import sys
import os, stat
import numpy as np
import datetime
import calendar

import errno
from os.path import isfile, join
from os import listdir

from numpy  import array
from shutil import copyfile, copy2
from pyearth.system.define_global_variables import *

from pyearth.toolbox.reader.text_reader_string import text_reader_string
from pypest.models.swat.once.step2.ppest_prepare_run_script import ppest_prepare_run_script
    
def run_step2(oPest_in, oModel_in):
    ppest_prepare_run_script(oPest_in, oModel_in)
    return


