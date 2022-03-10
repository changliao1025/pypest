import os, sys
from pyswat.postprocess.extract.swat_extract_stream_discharge import swat_extract_stream_discharge
def run_step5(oPest_in, oSwat_in):
    swat_extract_stream_discharge(oSwat_in)
    return

