import sys
import os
import numpy as np


from pypest.models.swat.once.step1.swat_prepare_pest_watershed_template_file import swat_prepare_pest_watershed_template_file
from pypest.models.swat.once.step1.swat_prepare_pest_subbasin_template_file import swat_prepare_pest_subbasin_template_file
from pypest.models.swat.once.step1.swat_prepare_pest_hru_template_file import swat_prepare_pest_hru_template_file

def run_step1(oPest_in, oSwat_in):
    
    swat_prepare_pest_watershed_template_file(oPest_in, oSwat_in)
    swat_prepare_pest_subbasin_template_file(oPest_in, oSwat_in)
    swat_prepare_pest_hru_template_file(oPest_in, oSwat_in)
    print('The PEST template file is prepared successfully!')
    return


