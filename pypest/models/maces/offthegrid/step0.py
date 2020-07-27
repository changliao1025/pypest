#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = "Chang Liao"
__copyright__ = "Copyright 2020, Pacific Northwest National Labortory"
__credits__ = ["Chang Liao", "Teklu Tesfa"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Chang Liao"
__email__ = "chang.liao@pnnl.gov"
__status__ = "Production"
"""
import sys, os
#third party package
import numpy as np

#dependency package
sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system.define_global_variables import *

#the pypest library
sPath_pypest = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest)
from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces
from pypest.template.shared.pypest_read_configuration_file import pypest_read_configuration_file

from pypest.models.maces.auxiliary.maces_prepare_observation_file import maces_prepare_minac_observation_file

def pypest_prepare_pest_control_file(oPest_in, oModel_in):
    """
    #prepare the pest control file
    """
    
    #strings
    sPest_mode = oPest_in.sPest_mode        

    sWorkspace_project_ralative = oModel_in.sWorkspace_project
    sWorkspace_simulation_relative = oModel_in.sWorkspace_simulation
    sWorkspace_calibration_relative = oModel_in.sWorkspace_calibration   
    
    sRegion = oModel_in.sRegion
    sModel = oModel_in.sModel    

    sWorkspace_data_project = sWorkspace_data + slash + sWorkspace_project_ralative

    sWorkspace_simulation = sWorkspace_scratch +  slash  + sWorkspace_simulation_relative
    sWorkspace_calibration = sWorkspace_scratch + slash + sWorkspace_calibration_relative    

    #the pest workspace should be the same with the calibration workspace
    sWorkspace_pest = oPest_in.sWorkspace_pest
    sWorkspace_pest_model = sWorkspace_pest

    sFilename_control = sWorkspace_pest_model + slash + oPest_in.sFilename_control    

    if not os.path.exists(sWorkspace_pest_model):
        os.mkdir(sWorkspace_pest_model)
    else:
        pass
    
    #number   
  
    npargp = oPest_in.npargp
    npar = oPest_in.npar
    nprior = oPest_in.nprior
    nobsgp = oPest_in.nobsgp
    nobs = oPest_in.nobs
    ntplfile = oPest_in.ntplfile
    ninsfile = oPest_in.ninsfile

    svd = 1
    if svd == 1:
        rlambda1 = 10
        numlam = 9
    else:
        rlambda1 = 0
        numlam = 1
    rlamfac = 3.0 #the rlambda1 change factor
    phiratsuf = 0.3  #the iteration criteria
    phiredlam = 0.01
    relparmax = 3
    facparmax = 3
    facorig = 0.0001
    phiredswh = 0.1
    noptmax = 20       #temination criteria
    phiredstp = 0.005
    nphistp = 5
    nphinored = 4
    relparstp = 0.01
    nrelpar = 4
    icov = 1
    icor = 1
    ieig = 1
    derinc = 0.01
    derinclb = 0.1
    derincmul = 1.5
    inctyp = 'relative'
    forcen = 'switch'
    dermthd = 'parabolic'
    partrans ='none'

   
    #we need define the input within the configuration file

    ofs = open(sFilename_control, 'w')
    ofs.write('pcf\n')
    ofs.write('* control data\n')
    ofs.write('restart ' + sPest_mode  + '\n' ) 
    #third line
    sLine = "{:0d}".format(npar)  + ' ' \
     +  "{:0d}".format(nobs)  + ' ' \
     +  "{:0d}".format(npargp)  + ' ' \
     +  "{:0d}".format(nprior)  + ' ' \
     +  "{:0d}".format(nobsgp)  + '\n'
    ofs.write(sLine) 
    #fourth line
    sLine = "{:0d}".format(ntplfile)  + ' ' \
     +  "{:0d}".format(ninsfile)  +  ' '\
     + ' double point ' \
     + '1 0 0 \n'
    ofs.write(sLine) 
    #fifth line
    sLine = "{:0.3f}".format(rlambda1)  + ' ' \
     +  "{:0.3f}".format(rlamfac)  + ' ' \
     +  "{:0.3f}".format(phiratsuf)  + ' ' \
     +  "{:0.3f}".format(phiredlam)  + ' ' \
     +  "{:0d}".format(numlam)  + '\n'
    ofs.write(sLine)
    #sixth line
    sLine = "{:0d}".format(relparmax)  + ' ' \
     +  "{:0d}".format(facparmax)  + ' ' \
     +  "{:0.4f}".format(facorig)  + '\n'
    ofs.write(sLine)
    #seventh line
    sLine = "{:0.3f}".format(phiredswh) + '\n'
    ofs.write(sLine)

    sLine = "{:02d}".format(noptmax)  + ' ' \
     +  "{:0.3f}".format(phiredstp)  + ' ' \
     +  "{:0d}".format(nphistp)  + ' ' \
     +  "{:0d}".format(nphinored)  + ' ' \
      +  "{:0.3f}".format(relparstp)  + ' ' \
     +  "{:0d}".format(nrelpar)  + '\n'
    ofs.write(sLine)

    sLine = "{:0d}".format(icov)  + ' ' \
     +  "{:0d}".format(icor)  + ' ' \
     +  "{:0d}".format(ieig)  + '\n'
    ofs.write(sLine)

    ofs.write('* singular value decomposition\n')
    ofs.write('1\n')
    sLine = "{:0d}".format(npar)  + ' ' \
       +  "{:0.4f}".format(1E-4)  + '\n'
    ofs.write(sLine)
    ofs.write('1\n')
    ofs.write( '* parameter groups\n'  )   

    sLine =  'para_gp1 ' \
              + inctyp + ' '\
              + "{:0.3f}".format(derinc)  + ' ' \
              +  "{:0.3f}".format(derinclb)  + ' ' \
              +  forcen  + ' ' \
              +  "{:0.3f}".format(derincmul)  + ' ' \
              +  dermthd  + '\n'
    ofs.write(sLine)

    parchglim = 'relative'
    ofs.write('* parameter data\n')
   
    

    ofs.write('* observation groups\n')
    
    ofs.write( '* observation data\n')
    #add the observation here
    #tsm_obs = maces_prepare_minac_observation_file()
    #omac obervation
    

    ofs.write('* model command line\n')

    #run the model
    sLine  = sWorkspace_pest_model + slash + 'run_model\n'
    ofs.write(sLine)

    
    ofs.write('* model input/output\n')

    #this part is model dependent

    
    #input template files
    sLine1 = sWorkspace_pest_model + slash + oModel_in.sFilename_template_omac 
    sLine2 = oModel_in.sFilename_parameter_omac  + '\n'
    sLine = sLine1 + ' ' + sLine2
    ofs.write(sLine)

    #output instruction files
     
    sFilename_instruction = sWorkspace_pest_model + slash + oModel_in.sFilename_instruction_omac 
    
    sFilename_output =  oModel_in.sFilename_output_omac  
    sLine = sFilename_instruction + ' '  + sFilename_output + '\n'
    ofs.write(sLine)

    phimlim = 1.0
    phimaccept = 1.05 * phimlim
    wfinit = 0.5
    wfmin = 0.1
    wfmax = 10
    wffac = 1.5
    wftol = 0.1
    iregadj = 0


    if sPest_mode  == 'estimation' :
        pass
    else:
        ofs.write(' * regularisation\n')
        sLine = "{:0.3f}".format(phimlim) + ' '  \
          + "{:0.3f}".format(phimaccept) + ' '   + '\n'
        ofs.write(sLine)    

        sLine = "{:0.3f}".format(wfinit) + ' '  \
             + "{:0.3f}".format(wfmin) + ' '  \
              + "{:0.3f}".format(wfmax) + ' '  + '\n'
        ofs.write(sLine)    
    
        sLine = "{:0.3f}".format(wffac) + ' '  \
            + "{:0.3f}".format(wftol) + ' ' \
             + "{:0.3f}".format(iregadj) + ' '   + '\n'
        ofs.write(sLine)
        pass


    ofs.close()

    print('The PEST control file is prepared successfully at: ' + sFilename_control)

def step0(sFilename_pest_configuration_in, sFilename_model_configuration_in):    
    aParameter_pest  = pypest_read_configuration_file(sFilename_pest_configuration)    
    aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration
    oPest = pypest(aParameter_pest)
    aParameter_model  = pypest_read_configuration_file(sFilename_model_configuration)   
    aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration
    oMaces = maces(aParameter_model)

    pypest_prepare_pest_control_file(oPest, oMaces )
    return
if __name__ == '__main__':
    sFilename_pest_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/pypest.xml'
    sFilename_model_configuration = '/qfs/people/liao313/workspace/python/pypest/pypest/pypest/models/maces/config/model.xml'    
    step0(sFilename_pest_configuration, sFilename_model_configuration)
    
