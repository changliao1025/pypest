import sys
import os


from pypest.models.swat.multipletimes.step3.swat_prepare_pest_child_input_file import swat_prepare_pest_child_input_file
from pypest.models.swat.multipletimes.step3.swat_prepare_input_from_pest import swat_prepare_input_from_pest


def run_step3(oPest_in, oSwat_in):

    swat_prepare_pest_child_input_file(oPest_in, oSwat_in)
    swat_prepare_input_from_pest(oSwat_in)

    return
