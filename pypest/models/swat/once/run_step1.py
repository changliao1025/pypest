import sys
import os
import numpy as np
import datetime
import calendar


from numpy  import array

from pyearth.toolbox.reader.text_reader_string import text_reader_string

from pypest.models.swat.once.step1.swat_prepare_pest_watershed_template_file import swat_prepare_pest_watershed_template_file
from pypest.models.swat.once.step1.swat_prepare_pest_subbasin_template_file import swat_prepare_pest_subbasin_template_file
from pypest.models.swat.once.step1.swat_prepare_pest_hru_template_file import swat_prepare_pest_hru_template_file


def ppest_prepare_template_file(oPest_in, oSwat_in):
    """
    prepare the pest template file
    """

    swat_prepare_pest_watershed_template_file(oPest_in, oSwat_in)
    swat_prepare_pest_subbasin_template_file(oPest_in, oSwat_in)
    swat_prepare_pest_hru_template_file(oPest_in, oSwat_in)

    print('The PEST template file is prepared successfully!')


def run_step1(oPest_in, oSwat_in):
    ppest_prepare_template_file(oPest_in, oSwat_in)
    return


