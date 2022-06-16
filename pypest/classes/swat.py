import os, stat
import numpy as np
from pyearth.system.define_global_variables import *
#this function is used to copy swat and beopest from linux hpc to calibration folder



from swaty.classes.pycase import swatcase

def pypest_create_swat_pest_template_file(oPest): 
    oSwat= oPest.pSwat
    oSwat.swaty_prepare_watershed_template_file()
    oSwat.swaty_prepare_subbasin_template_file()
    oSwat.swaty_prepare_hru_template_file()
    oSwat.swaty_prepare_soil_template_file()

    return
def pypest_create_swat_pest_instruction_file(oPest): 
    """
    prepare pest instruction file
    """
    
    oSwat= oPest.pSwat
    oSwat.swaty_create_pest_instruction_file(oPest.sFilename_instruction)

    return
def pypest_create_swat_pest_control_file(oPest):
    """
    #prepare the pest control file
    """   
    oSwat=oPest.pSwat
    sPest_mode = oPest.sPest_mode        
    sRegion = oPest.pSwat.sRegion
    sModel = oPest.pSwat.sModel    
    
    iFlag_watershed = oPest.pSwat.iFlag_watershed
    iFlag_subbasin = oPest.pSwat.iFlag_subbasin
    iFlag_hru = oPest.pSwat.iFlag_hru

    nsubbasin = oPest.pSwat.nsubbasin    
    sFilename_hru_info = oSwat.sFilename_hru_info
    if os.path.isfile(sFilename_hru_info):
        pass
    else:
        print('The file does not exist: ')
        return
      
    #the pest workspace should be the same with the calibration workspace
    sWorkspace_output = oPest.sWorkspace_output
    sFilename_control = sWorkspace_pest_case + slash + self.sFilename_control    
    if not os.path.exists(sWorkspace_pest_case):
        os.mkdir(sWorkspace_pest_case)
    else:
        pass
    
    
    sWorkspace_simulation_copy = oPest.pSwat.sWorkspace_simulation_copy 
    if not os.path.exists(sWorkspace_simulation_copy):
        print("The simulation folder is missing")
        return
    else:
        pass
    
    #number
    npargp = self.npargp
    npar = self.npar
    nprior = self.nprior
    nobsgp = self.nobsgp
    nobs = self.nobs
    ntplfile = self.ntplfile
    ninsfile = self.ninsfile
    npar = oPest.pSwat.nParameter
    sFilename = sWorkspace_data_project + slash + 'auxiliary' + slash \
    + 'usgs'+slash+ 'discharge' + slash + 'stream_discharge_monthly.txt'
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
    sFilename_control= self.sFilename_control
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
        nParameter_watershed = oPest.pSwat.nParameter_watershed
        aParameter_watershed = oPest.pSwat.aParameter_watershed
        aParameter_value_watershed = oPest.pSwat.aParameter_value_watershed
        aParameter_value_lower_watershed = oPest.pSwat.aParameter_value_lower_watershed
        aParameter_value_upper_watershed = oPest.pSwat.aParameter_value_upper_watershed
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
        nParameter_subbasin = oPest.pSwat.nParameter_subbasin
        aParameter_subbasin = oPest.pSwat.aParameter_subbasin
        aParameter_value_subbasin = oPest.pSwat.aParameter_value_subbasin
        aParameter_value_lower_subbasin = oPest.pSwat.aParameter_value_lower_subbasin
        aParameter_value_upper_subbasin = oPest.pSwat.aParameter_value_upper_subbasin
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
        nParameter_hru = oPest.pSwat.nParameter_hru
        aParameter_hru = oPest.pSwat.aParameter_hru
        aParameter_value_hru = oPest.pSwat.aParameter_value_hru
        aParameter_value_lower_hru = oPest.pSwat.aParameter_value_lower_hru
        aParameter_value_upper_hru = oPest.pSwat.aParameter_value_upper_hru
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
    sFilename_instruction = self.sFilename_instruction
    sFilename_instruction = sWorkspace_pest_case + slash + sFilename_instruction
    sFilename_output =  self.sFilename_output
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
    
    #strings
    sWorkspace_home= oSwat.sWorkspace_home
    sWorkspace_scratch = oSwat.sWorkspace_scratch    
    sWorkspace_calibration_case = oSwat.sWorkspace_calibration_case   
    sWorkspace_pest_model = sWorkspace_calibration_case
    if oPest_in.iFlag_parallel ==0: 
        #serial
        pass
    else:
        #parallel using beopest    
        #replace it with your actual python
        sPython_Path =  oSwat.sPython
        sPython = '#!' + sPython_Path + '\n' 
        sFilename_script = sWorkspace_pest_model + slash + 'run_swat_model'
        ifs = open(sFilename_script, 'w')
        sLine = '#!/bin/bash\n'
        ifs.write(sLine)

        sLine = 'echo "Started to prepare python scripts"\n'
        ifs.write(sLine)
        #the first one
        sLine = 'cat << EOF > runstep3.py\n'
        ifs.write(sLine)    
        ifs.write(sPython)

        sLine = 'from pyswat.shared.swat import pyswat' +  '\n' 
        ifs.write(sLine)
        sLine = 'from pypest.models.swat.shared.pest import pypest' +  '\n' 
        ifs.write(sLine)
        sLine = 'from pyswat.shared.swat_read_model_configuration_file import *\n'
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
        sLine = "oSwat = pyswat(aParameter_model)" + '\n'   
        ifs.write(sLine)
        sLine = 'run_step3(oPest, oSwat)' + '\n'   
        ifs.write(sLine)
        sLine = 'EOF\n'
        ifs.write(sLine)

        #step 5 
        sLine = 'cat << EOF > runstep5.py\n'
        ifs.write(sLine)

        ifs.write(sPython)
        sLine = 'from pyswat.shared.swat import pyswat' +  '\n' 
        ifs.write(sLine)
        sLine = 'from pypest.models.swat.shared.pest import pypest' +  '\n' 
        ifs.write(sLine)
        sLine = 'from pyswat.shared.swat_read_model_configuration_file import *\n'
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
        sLine = "oSwat = pyswat(aParameter_model)" + '\n'   
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
def pypest_run_swat_model(oPest_in):
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