import sys, os

from pyearth.system.define_global_variables import *


from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces
from pypest.template.shared.pypest_read_configuration_file import pypest_read_pest_configuration_file, pypest_read_model_configuration_file

def maces_pypest_run_model(oPest_in, oMaces_in):

    #is it possible to call the maces python script from here?
    #a glimplse of the job file
    #==================================================
    #JOB_DIRECTORY=/people/liao313/workspace/python/maces/MACES/src
    #cd $JOB_DIRECTORY
    #mpiexec -np 1 python MACES_main.py -f namelist.maces.xml 
    #==================================================

    #if not, we can just place the command within the run command
    #we will use the second option here because it does not require python to call mpi
    #the way to do it is explained in step 2

    return

def run_step4(oPest_in, oModel_in):
    pypest_run_model(oPest_in, oModel_in)
    return
def step4(sFilename_pest_configuration_in, sFilename_model_configuration_in):    
    aParameter_pest  = pypest_read_pest_configuration_file(sFilename_pest_configuration_in)    
    aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration_in
    oPest = pypest(aParameter_pest)
    aParameter_model  = pypest_read_model_configuration_file(sFilename_model_configuration_in)   
    aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration_in
    oMaces = maces(aParameter_model)
    maces_pypest_run_model(oPest, oMaces)

    return
def pypest_run_model_simulation():
    sFilename_pest_configuration = '/qfs/people/liao313/03configuration/pypest/maces/pest.xml'
    sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/model.xml'    
    step4(sFilename_pest_configuration, sFilename_model_configuration)