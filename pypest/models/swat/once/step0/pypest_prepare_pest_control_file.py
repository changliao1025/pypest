import sys
import os
import numpy as np
import datetime
import calendar


from numpy  import array

from pyearth.system.define_global_variables import *

from pyearth.toolbox.reader.text_reader_string import text_reader_string


def pypest_prepare_pest_control_file(oPest_in, oSwat_in):
    """
    #prepare the pest control file
    """   

    sPest_mode = oPest_in.sPest_mode        
    sRegion = oSwat_in.sRegion
    sModel = oSwat_in.sModel    

    sWorkspace_data= oSwat_in.sWorkspace_data
    sWorkspace_scratch = oSwat_in.sWorkspace_scratch
    
    sWorkspace_project_ralative = oSwat_in.sWorkspace_project
    iFlag_watershed = oSwat_in.iFlag_watershed
    iFlag_subbasin = oSwat_in.iFlag_subbasin
    iFlag_hru = oSwat_in.iFlag_hru

    nsubbasin = oSwat_in.nsubbasin
    
   

    sWorkspace_data_project = sWorkspace_data + slash + sWorkspace_project_ralative

    sFilename_hru_info = sWorkspace_data_project + slash + 'auxiliary' + slash \
      + 'hru' + slash + 'hru_info.txt'
    if os.path.isfile(sFilename_hru_info):
        pass
    else:
        print('The file does not exist: ')
        return
    aHru_info = text_reader_string(sFilename_hru_info)
    aHru_info = np.asarray(aHru_info)
    nhru = len(aHru_info)

    sWorkspace_simulation =  oSwat_in.sWorkspace_simulation
    sWorkspace_calibration = oSwat_in.sWorkspace_calibration   

    #the pest workspace should be the same with the calibration workspace
    sWorkspace_pest_case = oSwat_in.sWorkspace_calibration_case

    sFilename_control = sWorkspace_pest_case + slash + oPest_in.sFilename_control    

    if not os.path.exists(sWorkspace_pest_case):
        os.mkdir(sWorkspace_pest_case)
    else:
        pass
   
  
    sWorkspace_simulation_copy = oSwat_in.sWorkspace_simulation_copy 

    if not os.path.exists(sWorkspace_simulation_copy):
        print("The simulation folder is missing")
        return
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


    
    npar = oSwat_in.nParameter

    sFilename = sWorkspace_data_project + slash + 'auxiliary' + slash \
    + 'usgs'+slash+ 'discharge' + slash + 'stream_discharge_monthly.txt'
    if os.path.isfile(sFilename):
        pass
    else:
        print(sFilename + ' is missing!')
        return
    
    aData_all = text_reader_string(sFilename, cDelimiter_in=',')
    obs= array( aData_all).astype(float)
    good_index = np.where(obs != missing_value)
    nobs_with_missing_value = len(obs)
    nobs = len(good_index[0])

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
    noptmax = 30       #temination criteria
    phiredstp = 0.005
    nphistp = 5
    nphinored = 4
    relparstp = 0.01
    nrelpar = 4
    icov = 1
    icor = 1
    ieig = 1
    derinc = 0.01
    derinclb = 0.01
    derincmul = 1.5
    inctyp = 'relative'
    forcen = 'switch'
    dermthd = 'parabolic'
    partrans ='none'

    
    
    #we need define the input within the configuration file
    sFilename_control= oPest_in.sFilename_control

    sFilename_control = sWorkspace_pest_case + slash +  sFilename_control
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

    if iFlag_watershed ==1:
        sLine =  'para_gp1 ' \
                  + inctyp + ' '\
                  + "{:0.3f}".format(derinc)  + ' ' \
                  +  "{:0.3f}".format(derinclb)  + ' ' \
                  +  forcen  + ' ' \
                  +  "{:0.3f}".format(derincmul)  + ' ' \
                  +  dermthd  + '\n'
        ofs.write(sLine)
        pass
    if iFlag_subbasin ==1:
        sLine =  'para_gp2 ' \
                  + inctyp + ' '\
                  + "{:0.3f}".format(derinc)  + ' ' \
                  +  "{:0.3f}".format(derinclb)  + ' ' \
                  +  forcen  + ' ' \
                  +  "{:0.3f}".format(derincmul)  + ' ' \
                  +  dermthd  + '\n'
        ofs.write(sLine)
        pass
    if iFlag_hru ==1:
        sLine =  'para_gp3 ' \
                  + inctyp + ' '\
                  + "{:0.3f}".format(derinc)  + ' ' \
                  +  "{:0.3f}".format(derinclb)  + ' ' \
                  +  forcen  + ' ' \
                  +  "{:0.3f}".format(derincmul)  + ' ' \
                  +  dermthd  + '\n'
        ofs.write(sLine)

    parchglim = 'relative'
    ofs.write('* parameter data\n')
    if iFlag_watershed ==1:
        nParameter_watershed = oSwat_in.nParameter_watershed
        aParameter_watershed = oSwat_in.aParameter_watershed
        aParameter_value_watershed = oSwat_in.aParameter_value_watershed
        aParameter_value_lower_watershed = oSwat_in.aParameter_value_lower_watershed
        aParameter_value_upper_watershed = oSwat_in.aParameter_value_upper_watershed
        for i in range(nParameter_watershed):
            sParameter = aParameter_watershed[i]

            dVariable_init = aParameter_value_watershed[i]
            dVariable_lower = aParameter_value_lower_watershed[i]
            dVariable_upper = aParameter_value_upper_watershed[i]

            sLine = sParameter  + ' ' \
                  + partrans + ' ' \
                  + parchglim + ' '\
                  + "{:0.3f}".format(dVariable_init) + ' ' \
                  + "{:0.3f}".format(dVariable_lower) + ' ' \
                  +"{:0.3f}".format(dVariable_upper) + ' ' \
                  + ' para_gp1 1.0 0.0 1\n'
            ofs.write(sLine)
        pass

    if iFlag_subbasin ==1:
        nParameter_subbasin = oSwat_in.nParameter_subbasin
        aParameter_subbasin = oSwat_in.aParameter_subbasin
        aParameter_value_subbasin = oSwat_in.aParameter_value_subbasin
        aParameter_value_lower_subbasin = oSwat_in.aParameter_value_lower_subbasin
        aParameter_value_upper_subbasin = oSwat_in.aParameter_value_upper_subbasin
        for i in range(nParameter_subbasin):
            sParameter = aParameter_subbasin[i]
            dVariable_init = aParameter_value_subbasin[i]
            dVariable_lower = aParameter_value_lower_subbasin[i]
            dVariable_upper = aParameter_value_upper_subbasin[i]
            for iSubbasin in range(0, nsubbasin):
                sLine = sParameter + "{:03d}".format(iSubbasin+1) + ' ' \
                  + partrans + ' ' \
                  + parchglim + ' '\
                  + "{:0.3f}".format(dVariable_init) + ' ' \
                  + "{:0.3f}".format(dVariable_lower) + ' ' \
                  +"{:0.3f}".format(dVariable_upper) + ' ' \
                  + ' para_gp2 1.0 0.0 1\n'
                ofs.write(sLine)
            pass

    if iFlag_hru ==1:
        nParameter_hru = oSwat_in.nParameter_hru
        aParameter_hru = oSwat_in.aParameter_hru
        aParameter_value_hru = oSwat_in.aParameter_value_hru
        aParameter_value_lower_hru = oSwat_in.aParameter_value_lower_hru
        aParameter_value_upper_hru = oSwat_in.aParameter_value_upper_hru
        for i in range(nParameter_hru):
            sParameter = aParameter_hru[i]
            dVariable_init = aParameter_value_hru[i]
            dVariable_lower = aParameter_value_lower_hru[i]
            dVariable_upper = aParameter_value_upper_hru[i]
            for ihru_type in range(0, nhru):
                sLine = sParameter + "{:03d}".format(ihru_type+1) + ' ' \
                  + partrans + ' ' \
                  + parchglim + ' '\
                  + "{:0.3f}".format(dVariable_init) + ' ' \
                  + "{:0.3f}".format(dVariable_lower) + ' ' \
                  +"{:0.3f}".format(dVariable_upper) + ' ' \
                  + ' para_gp3 1.0 0.0 1\n'
                ofs.write(sLine)

    ofs.write('* observation groups\n')
    ofs.write( 'discharge\n')
    ofs.write( '* observation data\n')
    
    
    obs = np.reshape(obs, nobs_with_missing_value)
    for i in range(0, nobs_with_missing_value):
        if obs[i] != missing_value:
            sLine = 'discharge' + "{:04d}".format(i+1)   + ' ' \
               + "{:0.4f}".format(obs[i])  + ' 1.0 ' + ' discharge\n'
            ofs.write(sLine)
        else:
            pass

    ofs.write('* model command line\n')

    #run the model
    sLine  = sWorkspace_pest_case + slash + 'run_swat_model\n'
    ofs.write(sLine)

    
    ofs.write('* model input/output\n')

    if iFlag_watershed ==1:
        sLine1 = sWorkspace_pest_case + slash + 'watershed.tpl'    
        sLine2 = 'watershed.para\n'
        sLine = sLine1 + ' ' + sLine2
        ofs.write(sLine)

    if iFlag_subbasin ==1:
        sLine1 = sWorkspace_pest_case + slash + 'subbasin.tpl'    
        sLine2 =  'subbasin.para\n'
        sLine = sLine1 + ' ' + sLine2
        ofs.write(sLine)

    if iFlag_hru ==1:
        sLine1 = sWorkspace_pest_case + slash + 'hru.tpl'    
        sLine2 = 'hru.para\n'
        sLine = sLine1 + ' ' + sLine2
        ofs.write(sLine)

    #result
    sFilename_instruction = oPest_in.sFilename_instruction

    sFilename_instruction = sWorkspace_pest_case + slash + sFilename_instruction
    sFilename_output =  oPest_in.sFilename_output
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


