import os, stat
import numpy as np
from pyearth.system.define_global_variables import *
#this function is used to copy swat and beopest from linux hpc to calibration folder

from swaty.auxiliary.text_reader_string import text_reader_string

from swaty.classes.pycase import swatcase

def pypest_create_swat_pest_template_file(oPest): 
    oSwat= oPest.pSwat
    sFilename_watershed_template = os.path.join( oPest.sWorkspace_output, 'watershed.tpl')
    oSwat.swaty_prepare_watershed_template_file(sFilename_watershed_template)
    sFilename_subbasin_template = os.path.join( oPest.sWorkspace_output, 'subbasin.tpl')
    oSwat.swaty_prepare_subbasin_template_file(sFilename_subbasin_template)
    sFilename_hru_template = os.path.join( oPest.sWorkspace_output, 'hru.tpl')
    oSwat.swaty_prepare_hru_template_file(sFilename_hru_template)
    sFilename_soil_template = os.path.join( oPest.sWorkspace_output, 'soil.tpl')
    oSwat.swaty_prepare_soil_template_file(sFilename_soil_template)

    return
def pypest_create_swat_pest_instruction_file(oPest, sFilename_in): 
    """
    prepare pest instruction file
    """
    
    oSwat= oPest.pSwat
    oSwat.swaty_create_pest_instruction_file(sFilename_in)

    return
def pypest_create_swat_pest_control_file(oPest):
    """
    #prepare the pest control file
    """   
    oSwat=oPest.pSwat
    sPest_mode = oPest.sPest_mode        
    oSwat = oPest.pSwat
    sWorkspace_output= oPest.sWorkspace_output    
    
    iFlag_watershed = oSwat.iFlag_watershed
    iFlag_subbasin = oSwat.iFlag_subbasin
    iFlag_hru = oSwat.iFlag_hru
    iFlag_soil = oSwat.iFlag_soil
    nsubbasin = oSwat.nsubbasin    
    nhru_combination = oSwat.nhru_combination

    sWorkspace_swat = oSwat.sWorkspace_output
    sFilename_hru_info = os.path.join( sWorkspace_swat , 'hru_info.txt')
    if os.path.isfile(sFilename_hru_info):
        pass
    else:
        print('The file does not exist: ')
        return   
   
    sFilename_control = oPest.sFilename_control    
    
     
    #number
    npargp = 0 
    ntplfile = 0
    if iFlag_watershed ==1:
        npargp = npargp + 1
        ntplfile = ntplfile + 1
    if iFlag_subbasin ==1:
        npargp = npargp + 1
        ntplfile = ntplfile + 1
    if iFlag_hru ==1:
        npargp = npargp + 1
        ntplfile = ntplfile + 1
    if iFlag_soil ==1:
        npargp = npargp + 1
        ntplfile = ntplfile + 1

    oPest.npargp = npargp
    oPest.ntplfile = ntplfile
    
    nprior = oPest.nprior
    nobsgp = oPest.nobsgp
    nobs = oPest.nobs
 
    ninsfile = oPest.ninsfile
    npar = oPest.npar
    #npar = oSwat.nParameter_watershed + oSwat.nParameter_subbasin + oSwat.nParameter_hru + oSwat.nParameter_soil
    sFilename = os.path.join( oSwat.sWorkspace_input , 'discharge_observation_monthly.txt')
    if os.path.isfile(sFilename):
        pass
    else:
        print(sFilename + ' is missing!')
        return
    aData_all = text_reader_string(sFilename, cDelimiter_in=',')
    obs= np.array( aData_all).astype(float)
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
    facorig = 0.01
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
    derinclb = 0.1
    derincmul = 1.5
    inctyp = 'relative' #'absolute' #
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

    if iFlag_soil ==1:
        sLine =  'para_gp4 ' \
                  + inctyp + ' '\
                  + "{:0.3f}".format(derinc)  + ' ' \
                  +  "{:0.3f}".format(derinclb)  + ' ' \
                  +  forcen  + ' ' \
                  +  "{:0.3f}".format(derincmul)  + ' ' \
                  +  dermthd  + '\n'
        ofs.write(sLine)
    parchglim = 'relative'
    ofs.write('* parameter data\n')


    iFlag_spatial = 0
    if iFlag_watershed ==1:
        oWatershed = oSwat.pWatershed
        nParameter_watershed = oWatershed.nParameter_watershed
        aParameter_watershed = oWatershed.aParameter_watershed
        
        for i in range(nParameter_watershed):
            sParameter = aParameter_watershed[i].sName
            dVariable_init = aParameter_watershed[i].dValue_current
            dVariable_lower = aParameter_watershed[i].dValue_lower
            dVariable_upper = aParameter_watershed[i].dValue_upper
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
        nsubasin = oSwat.nsubbasin
        if iFlag_spatial == 1:
            for iSubbasin in range(1,nsubasin):                
                pSubbasin  = oSwat.aSubbasin[iSubbasin-1]
                nParameter_subbasin = pSubbasin.nParameter_subbasin
                aParameter_subbasin = pSubbasin.aParameter_subbasin            
                for i in range(nParameter_subbasin):
                    sParameter = aParameter_subbasin[i].sName
                    dVariable_init = aParameter_subbasin[i].dValue_current
                    dVariable_lower = aParameter_subbasin[i].dValue_lower
                    dVariable_upper = aParameter_subbasin[i].dValue_upper                
                    sLine = sParameter + "{:03d}".format(iSubbasin) + ' ' \
                          + partrans + ' ' \
                          + parchglim + ' '\
                          + "{:0.3f}".format(dVariable_init) + ' ' \
                          + "{:0.3f}".format(dVariable_lower) + ' ' \
                          +"{:0.3f}".format(dVariable_upper) + ' ' \
                          + ' para_gp2 1.0 0.0 1\n'
                    ofs.write(sLine)
                    pass
        else:
            pSubbasin  = oSwat.aSubbasin[0]
            nParameter_subbasin = pSubbasin.nParameter_subbasin
            aParameter_subbasin = pSubbasin.aParameter_subbasin            
            for i in range(nParameter_subbasin):
                sParameter = aParameter_subbasin[i].sName
                dVariable_init = aParameter_subbasin[i].dValue_current
                dVariable_lower = aParameter_subbasin[i].dValue_lower
                dVariable_upper = aParameter_subbasin[i].dValue_upper                
                sLine = sParameter +  ' ' \
                      + partrans + ' ' \
                      + parchglim + ' '\
                      + "{:0.3f}".format(dVariable_init) + ' ' \
                      + "{:0.3f}".format(dVariable_lower) + ' ' \
                      +"{:0.3f}".format(dVariable_upper) + ' ' \
                      + ' para_gp2 1.0 0.0 1\n'
                ofs.write(sLine)
                pass
            pass
    
    if iFlag_hru ==1:
        aName_ratio= ['cn2','ov_n']
        nhru_combination = oSwat.nhru_combination
        if iFlag_spatial == 1:
            for iHru_type in range(1,nhru_combination):
                pHru = oSwat.aHru_combination[iHru_type -1]
                aParameter_hru = pHru.aParameter_hru   
                nParameter_hru = oSwat.nParameter_hru      
                for i in range(nParameter_hru):
                    sParameter = aParameter_hru[i].sName
                    dVariable_init = aParameter_hru[i].dValue_current
                    dVariable_lower = aParameter_hru[i].dValue_lower
                    dVariable_upper = aParameter_hru[i].dValue_upper                
                    sLine = sParameter + "{:03d}".format(iHru_type) + ' ' \
                          + partrans + ' ' \
                          + parchglim + ' ' \
                          + "{:0.3f}".format(dVariable_init) + ' ' \
                          + "{:0.3f}".format(dVariable_lower) + ' ' \
                          + "{:0.3f}".format(dVariable_upper) + ' ' \
                          + ' para_gp3 1.0 0.0 1' + '\n'
                    ofs.write(sLine)
            #soil 
            if iFlag_soil ==1:
                nsoil_combination = oSwat.nsoil_combination
                aSoil_combination = oSwat.aSoil_combination            
                for iSoil_type in range(1,nsoil_combination+1): 
                    sSoil_type = "{:03d}".format(iSoil_type)                                   
                    
                    #find the hru that has this soil type
                    
                    nSoillayer = int(aSoil_combination[iSoil_type-1,1])
                    for iSoil_layer in range(1, nSoillayer+1):
                        sSoil_layer = "{:02d}".format(iSoil_layer)
                        for i in range(nParameter_soil):
                            sParameter = aParameter_soil[i].sName
                            dVariable_init = aParameter_soil[i].dValue_current
                            dVariable_lower = aParameter_soil[i].dValue_lower
                            dVariable_upper = aParameter_soil[i].dValue_upper                
                            sLine = sParameter + sSoil_type + sSoil_layer + ' ' \
                                  + partrans + ' ' \
                                  + parchglim + ' '\
                                  + "{:0.3f}".format(dVariable_init) + ' ' \
                                  + "{:0.3f}".format(dVariable_lower) + ' ' \
                                  + "{:0.3f}".format(dVariable_upper) + ' ' \
                                  + ' para_gp4 1.0 0.0 1\n'
                            ofs.write(sLine)
        else:
            pHru = oSwat.aHru_combination[0]
            aParameter_hru = pHru.aParameter_hru   
            nParameter_hru = pHru.nParameter_hru      
            for i in range(nParameter_hru):
                sParameter = aParameter_hru[i].sName
                if sParameter not in aName_ratio:
                    dVariable_init = aParameter_hru[i].dValue_current
                    dVariable_lower = aParameter_hru[i].dValue_lower
                    dVariable_upper = aParameter_hru[i].dValue_upper                
                    sLine = sParameter + ' ' \
                          + partrans + ' ' \
                          + parchglim + ' ' \
                          + "{:0.3f}".format(dVariable_init) + ' ' \
                          + "{:0.3f}".format(dVariable_lower) + ' ' \
                          + "{:0.3f}".format(dVariable_upper) + ' ' \
                          + ' para_gp3 1.0 0.0 1' + '\n'
                    ofs.write(sLine)
                else:
                    dVariable_init = 1.0
                    dVariable_lower = 0.0
                    dVariable_upper = 10.0              
                    sLine = sParameter + ' ' \
                          + partrans + ' ' \
                          + parchglim + ' ' \
                          + "{:0.3f}".format(dVariable_init) + ' ' \
                          + "{:0.3f}".format(dVariable_lower) + ' ' \
                          + "{:0.3f}".format(dVariable_upper) + ' ' \
                          + ' para_gp3 1.0 0.0 1' + '\n'
                    ofs.write(sLine)
            pSoil = oSwat.aHru_combination[0].aSoil[0]     #the first soil layer 
            aParameter_soil = pSoil.aParameter_soil           
            nParameter_soil = len(aParameter_soil) 
            for i in range(nParameter_soil):
                sParameter = aParameter_soil[i].sName
                dVariable_init = aParameter_soil[i].dValue_current
                dVariable_lower = aParameter_soil[i].dValue_lower
                dVariable_upper = aParameter_soil[i].dValue_upper                
                sLine = sParameter + ' ' \
                      + partrans + ' ' \
                      + parchglim + ' '\
                      + "{:0.3f}".format(dVariable_init) + ' ' \
                      + "{:0.3f}".format(dVariable_lower) + ' ' \
                      + "{:0.3f}".format(dVariable_upper) + ' ' \
                      + ' para_gp4 1.0 0.0 1\n'
                ofs.write(sLine)
            pass

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
    sLine  = sWorkspace_output + slash + 'run_swat_model\n'
    ofs.write(sLine)
    ofs.write('* model input/output\n')
    if iFlag_watershed ==1:
        sLine1 = sWorkspace_output + slash + 'watershed.tpl'    
        sLine2 = 'watershed.para\n'
        sLine = sLine1 + ' ' + sLine2
        ofs.write(sLine)
    if iFlag_subbasin ==1:
        sLine1 = sWorkspace_output + slash + 'subbasin.tpl'    
        sLine2 =  'subbasin.para\n'
        sLine = sLine1 + ' ' + sLine2
        ofs.write(sLine)
    if iFlag_hru ==1:
        sLine1 = sWorkspace_output + slash + 'hru.tpl'    
        sLine2 = 'hru.para\n'
        sLine = sLine1 + ' ' + sLine2
        ofs.write(sLine)
    if iFlag_soil ==1:
        sLine1 = sWorkspace_output + slash + 'soil.tpl'    
        sLine2 = 'soil.para\n'
        sLine = sLine1 + ' ' + sLine2
        ofs.write(sLine)
    #result
    sFilename_instruction = oPest.sFilename_instruction    
    sFilename_output =  oPest.sFilename_output
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
    return    


def pypest_create_swat_run_script(oPest_in):
    """
    prepare the job submission file
    """
    oSwat= oPest_in.pSwat
    sModel = oSwat.sModel
    sFilename_pest_configuration = oPest_in.sFilename_pest_configuration
    sFilename_model_configuration = oSwat.sFilename_model_configuration    
    sWorkspace_output = oPest_in.sWorkspace_output

    sWorkspace_output_raw = os.path.dirname(sWorkspace_output)
    sPython_Path =  oPest_in.sPython 
    if oPest_in.iFlag_parallel ==0: 
        #serial       
        #replace it with your actual python        
        sPython = '#!' + sPython_Path + '\n' 
        sFilename_script = sWorkspace_output + slash + 'run_swat_model'
        ifs = open(sFilename_script, 'w')
        sLine = '#!/bin/bash\n'
        ifs.write(sLine)

        sLine = 'echo "Started to prepare python scripts"\n'
        ifs.write(sLine)
        #the first one
        sLine = 'cat << EOF > runstep3.py\n'
        ifs.write(sLine)    
        ifs.write(sPython)        
        
        sLine = 'from pypest.pypest_read_model_configuration_file import pypest_read_model_configuration_file\n'
        ifs.write(sLine)                   
        
        sLine = 'sFilename_pest_configuration = ' + '"' + sFilename_pest_configuration + '"\n'
        ifs.write(sLine)
        

        sLine = 'oPest = pypest_read_model_configuration_file(sFilename_pest_configuration,'  \
            + 'iCase_index_in='+ str(oPest_in.iCase_index) + ',' \
            + 'iFlag_read_discretization_in='+ str(1) + ',' \
            + 'sDate_in="'+ oPest_in.sDate + '",' \
            + 'sWorkspace_input_in="' + oPest_in.sWorkspace_input+ '",' \
            + 'sWorkspace_output_in="' + sWorkspace_output_raw+ '"' \
            + ')'  +   '\n'   
        ifs.write(sLine)

        sLine = "oSwat = oPest.pSwat" + '\n'   
        ifs.write(sLine)

        sFilename_pest_parameter_watershed_in = os.path.join( sWorkspace_output, 'watershed.para' )
        sFilename_watershed_parameter_default_in = os.path.join( sWorkspace_output, 'watershed_parameter_default.txt' )
        sFilename_watershed_parameter_bounds_in = os.path.join( sWorkspace_output, 'watershed_parameter_bounds.txt' )

        sFilename_pest_parameter_subbasin_in= os.path.join( sWorkspace_output, 'subbasin.para' )
        sFilename_subbasin_parameter_default_in = os.path.join( sWorkspace_output, 'subbasin_parameter_default.txt' )
        sFilename_subbasin_parameter_bounds_in = os.path.join( sWorkspace_output, 'subbasin_parameter_bounds.txt' )
        
        sFilename_pest_parameter_hru_in = os.path.join( sWorkspace_output, 'hru.para' )
        sFilename_hru_parameter_default_in = os.path.join( sWorkspace_output, 'hru_parameter_default.txt' )
        sFilename_hru_parameter_bounds_in = os.path.join( sWorkspace_output, 'hru_parameter_bounds.txt' )

        sFilename_pest_parameter_soil_in = os.path.join( sWorkspace_output, 'soil.para' )
        sFilename_soil_parameter_bounds_in = os.path.join( sWorkspace_output, 'soil_parameter_bounds.txt' )
        sWorkspace_soil_parameter_default_in =  sWorkspace_output
        sLine = 'oSwat.convert_pest_parameter_to_model_input(' \
          +  'sFilename_pest_parameter_watershed_in ="' + sFilename_pest_parameter_watershed_in + '",'\
         + 'sFilename_watershed_parameter_default_in ="' +  sFilename_watershed_parameter_default_in + '",' \
         +'sFilename_watershed_parameter_bounds_in ="'+ sFilename_watershed_parameter_bounds_in + '",'\
        +  'sFilename_pest_parameter_subbasin_in ="' + sFilename_pest_parameter_subbasin_in+ '",'\
         +  'sFilename_subbasin_parameter_default_in ="' + sFilename_subbasin_parameter_default_in+ '",'\
         +'sFilename_subbasin_parameter_bounds_in ="' + sFilename_subbasin_parameter_bounds_in + '",' \
        +'sFilename_pest_parameter_hru_in ="' + sFilename_pest_parameter_hru_in+ '",'\
        +'sFilename_hru_parameter_default_in ="' + sFilename_hru_parameter_default_in+ '",' \
        +'sFilename_hru_parameter_bounds_in ="' + sFilename_hru_parameter_bounds_in+ '",' \
        +'sFilename_pest_parameter_soil_in ="' + sFilename_pest_parameter_soil_in+ '",'\
        +'sFilename_soil_parameter_bounds_in ="' + sFilename_soil_parameter_bounds_in+ '",'\
        +'sWorkspace_soil_parameter_default_in ="' + sWorkspace_soil_parameter_default_in \
        + '")' + '\n'   
        ifs.write(sLine)
        
        sLine = 'EOF\n'
        ifs.write(sLine)

        #step 5 
        sLine = 'cat << EOF > runstep5.py\n'
        ifs.write(sLine)

        ifs.write(sPython)
        sLine = 'from pypest.pypest_read_model_configuration_file import pypest_read_model_configuration_file\n'
        ifs.write(sLine)       
        
        sLine = 'sFilename_pest_configuration = ' + '"' + sFilename_pest_configuration + '"\n'
        ifs.write(sLine)
        sLine = 'oPest  = pypest_read_model_configuration_file(sFilename_pest_configuration)'  + '\n'   
        ifs.write(sLine)
        sLine = "oSwat = oPest.pSwat" + '\n'   
        ifs.write(sLine)
        
        sLine = "oSwat.analyze()" + '\n'   
        ifs.write(sLine)

        sLine = 'EOF\n'
        ifs.write(sLine)
        #end of python

        sLine = 'chmod 755 runstep3.py\n'
        ifs.write(sLine)

        sLine = 'chmod 755 runstep5.py\n'
        ifs.write(sLine)

        sLine = 'echo "Finished preparing python scripts"\n'
        ifs.write(sLine)

        sLine = 'echo "Started to prepare SWAT inputs"\n'
        ifs.write(sLine)
        #step 1: prepare inputs
        sLine = './runstep3.py\n'
        ifs.write(sLine)

        sLine = 'echo "Finished preparing SWAT simulation"\n'
        ifs.write(sLine)
        #step 2: run swat model
        sLine = 'echo "Started to run SWAT simulation"\n'
        ifs.write(sLine)
        sLine = './swat\n'
        ifs.write(sLine)
        sLine = 'echo "Finished running SWAT simulation"\n'
        ifs.write(sLine)

        #step 3: extract SWAT output
        sLine = 'echo "Started to extract SWAT simulation outputs"\n'
        ifs.write(sLine)
        sLine = './runstep5.py\n'
        ifs.write(sLine)
        sLine = 'echo "Finished extracting SWAT simulation outputs"\n'
        ifs.write(sLine)
        ifs.close()
        os.chmod(sFilename_script, stat.S_IREAD | stat.S_IWRITE | stat.S_IXUSR)
        print('The pest run model file is prepared successfully!')
        pass
    else:
        #parallel using beopest    
        #replace it with your actual python
        sPython_Path =  oPest_in.sPython
        sPython = '#!' + sPython_Path + '\n' 
        sFilename_script = sWorkspace_output + slash + 'run_swat_model'
        ifs = open(sFilename_script, 'w')
        sLine = '#!/bin/bash\n'
        ifs.write(sLine)

        sLine = 'echo "Started to prepare python scripts"\n'
        ifs.write(sLine)
        #the first one
        sLine = 'cat << EOF > runstep3.py\n'
        ifs.write(sLine)    
        ifs.write(sPython)
        sLine = 'from swaty.shared.swat import swaty' +  '\n' 
        ifs.write(sLine)
        sLine = 'from pypest.models.swat.shared.pest import pypest' +  '\n' 
        ifs.write(sLine)
        sLine = 'from swaty.shared.swat_read_model_configuration_file import *\n'
        ifs.write(sLine)
        sLine = 'from pypest.models.swat.multipletimes.run_step3 import run_step3'  +  '\n' 
        ifs.write(sLine)    
        sLine = 'from pypest.template.shared.pypest_read_configuration_file import *' +  '\n' 
        ifs.write(sLine)  
        sLine = 'sFilename_pest_configuration = ' + '"' + sFilename_pest_configuration + '"\n'
        ifs.write(sLine)
        sLine = 'aParameter_pest  = pypest_read_pest_configuration_file(sFilename_pest_configuration)'  + '\n'   
        ifs.write(sLine)
        sLine = "aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration" + '\n'   
        ifs.write(sLine)
        sLine = 'oPest = pypest(aParameter_pest)' + '\n'   
        ifs.write(sLine)
        sLine = 'sFilename_model_configuration = ' + '"' + sFilename_model_configuration + '"\n'
        ifs.write(sLine)
        sLine = "aParameter_model = swat_read_model_configuration_file(sFilename_model_configuration)" + '\n'   
        ifs.write(sLine)
        sLine = "aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration" + '\n'   
        ifs.write(sLine) 
        sLine = "oSwat = swaty(aParameter_model)" + '\n'   
        ifs.write(sLine)
        sLine = 'run_step3(oPest, oSwat)' + '\n'   
        ifs.write(sLine)
        sLine = 'EOF\n'
        ifs.write(sLine)

        #step 5 
        sLine = 'cat << EOF > runstep5.py\n'
        ifs.write(sLine)

        ifs.write(sPython)
        sLine = 'from swaty.shared.swat import swaty' +  '\n' 
        ifs.write(sLine)
        sLine = 'from pypest.models.swat.shared.pest import pypest' +  '\n' 
        ifs.write(sLine)
        sLine = 'from swaty.shared.swat_read_model_configuration_file import *\n'
        ifs.write(sLine)
        sLine = 'from pypest.models.swat.multipletimes.run_step5 import run_step5' + '\n'
        ifs.write(sLine)
        sLine = 'from pypest.template.shared.pypest_read_configuration_file import *' +  '\n' 
        ifs.write(sLine)
        sLine = 'sFilename_pest_configuration = ' + '"' + sFilename_pest_configuration + '"\n'
        ifs.write(sLine)
        sLine = 'aParameter_pest  = pypest_read_pest_configuration_file(sFilename_pest_configuration)'  + '\n'   
        ifs.write(sLine)
        sLine = "aParameter_pest['sFilename_pest_configuration'] = sFilename_pest_configuration" + '\n'   
        ifs.write(sLine)
        sLine = 'oPest = pypest(aParameter_pest)' + '\n'   
        ifs.write(sLine)
        sLine = 'sFilename_model_configuration = ' + '"' + sFilename_model_configuration + '"\n'
        ifs.write(sLine)
        sLine = "aParameter_model = swat_read_model_configuration_file(sFilename_model_configuration)" + '\n'   
        ifs.write(sLine)
        sLine = "aParameter_model['sFilename_model_configuration'] = sFilename_model_configuration" + '\n'   
        ifs.write(sLine) 
        sLine = "oSwat = swaty(aParameter_model)" + '\n'   
        ifs.write(sLine)

        sLine = 'run_step5(oPest, oSwat)\n'
        ifs.write(sLine)

        sLine = 'EOF\n'
        ifs.write(sLine)
        #end of python

        sLine = 'chmod 755 runstep3.py\n'
        ifs.write(sLine)

        sLine = 'chmod 755 runstep5.py\n'
        ifs.write(sLine)

        sLine = 'echo "Finished preparing python scripts"\n'
        ifs.write(sLine)

        sLine = 'echo "Started to prepare SWAT inputs"\n'
        ifs.write(sLine)
        #step 1: prepare inputs
        sLine = './runstep3.py\n'
        ifs.write(sLine)


        sLine = 'echo "Finished preparing SWAT simulation"\n'
        ifs.write(sLine)
        #step 2: run swat model
        sLine = 'echo "Started to run SWAT simulation"\n'
        ifs.write(sLine)
        sLine = './swat\n'
        ifs.write(sLine)
        sLine = 'echo "Finished running SWAT simulation"\n'
        ifs.write(sLine)

        #step 3: extract SWAT output
        sLine = 'echo "Started to extract SWAT simulation outputs"\n'
        ifs.write(sLine)
        sLine = './runstep5.py\n'
        ifs.write(sLine)
        sLine = 'echo "Finished extracting SWAT simulation outputs"\n'
        ifs.write(sLine)
        ifs.close()
        os.chmod(sFilename_script, stat.S_IREAD | stat.S_IWRITE | stat.S_IXUSR)
        print('The pest run model file is prepared successfully!')


def pypest_update_swat_model(oPest_in):
    if oPest_in.iFlag_parallel ==0:
        
        pass
    else:
        pass
    return

def pypest_extract_swat_output(oPest_in):
    if oPest_in.iFlag_parallel ==0:
        pass
    else:
        pass
    return