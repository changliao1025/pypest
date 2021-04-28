import sys, os
import numpy as np
from netCDF4 import Dataset

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyearth.system.define_global_variables import *


sPath_pypest = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest)

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces
from pypest.template.shared.pypest_parse_xml_file import pypest_parse_xml_file

def maces_extract_omac_output(oPest_in, oModel_in):
    #filename = '/Users/tanz151/Python_maces/src/maces_ecogeom_2002-01-01_2004-01-01_466.nc'
    iFlag_calibration = oModel_in.iFlag_calibration
    if iFlag_calibration == 1:
        #calibration mode
        sWorkspace_calibration_relative = oModel_in.sWorkspace_calibration
        sWorkspace_calibration = sWorkspace_scratch + slash +   sWorkspace_calibration_relative
        sWorkspace_pest_model = sWorkspace_calibration

        iFlag_debug = 0
        if(iFlag_debug == 1 ):
            sPath_current = sWorkspace_pest_model + slash + 'beopest1'
        else:
            sPath_current = os.getcwd()
        pass
    else:
        #simulation mode
        sWorkspace_simulation=oModel_in.sWorkspace_simulation
        
        
        sCase = oModel_in.sCase
        sWorkspace_simulation_case = sWorkspace_simulation + slash + sCase
        if not os.path.exists(sWorkspace_simulation_case):
            os.mkdir(sWorkspace_simulation_case)
        else:
            pass
        sPath_current = sWorkspace_simulation_case
        pass

    sFilename = sPath_current + slash \
        + 'output' + slash + 'maces_ecogeom_' + oModel_in.sDate_start + '_' + oModel_in.sDate_end \
            + '_' + oModel_in.sSiteID + sExtension_netcdf 

    if os.path.isfile(sFilename):
        nc = Dataset(sFilename,'r')
        x = np.array(nc.variables['x'][:])
        pft = np.array(nc.variables['pft'][:])
        Esed = np.array(nc.variables['Esed'][:])
        Dsed = np.array(nc.variables['Dsed'][:])
        DepOM = np.array(nc.variables['DepOM'][:])
        nc.close()
    else:
        print('Output file does not exist!')
        return
    
    
    nx = np.size(x)
    dx = np.zeros(nx)
    dx[1:nx-1] = 0.5 * (x[2:nx] - x[0:nx-2])
    dx[0] = 0.5 * (x[0] + x[1])
    dx[nx-1] = 0.5 * (x[nx-2] + x[nx-1])

    nt = np.shape(pft)[0]
    dx = np.tile(dx,(nt,1))

    #rhoSed = 2650 # this value from optpar_minac.xml
    #porSed = 0.4 # this value from optpar_minac.xml

    sFilename = sPath_current + slash + os.path.basename(oModel_in.sFilename_config_minac)

    print(sFilename)
    aParameter = pypest_parse_xml_file(sFilename)
    rhoSed = float( aParameter['rhoSed'] )
    porSed = float( aParameter['porSed'] )


    # mineral accretion rate (mm/yr)
    wtlnd_x_avg = np.sum(dx[pft==2])/nt
    mineral_accretion = 0.5e3 * (8.64e4*np.sum(Dsed[pft==2]*dx[pft==2])/wtlnd_x_avg - \
        8.64e4*np.sum(Esed[pft==2]*dx[pft==2])/wtlnd_x_avg) / rhoSed / (1.0-porSed)

    # OM accretion rate (gC/m2/yr)
    om_accretion = 0.5e3 * 8.64e4 * np.sum(DepOM[pft==2]*dx[pft==2])/wtlnd_x_avg
    print(om_accretion)

    #save as text file

    sFilename_out = sPath_current + slash + 'output_omac.out'
    ifs = open(sFilename_out, 'w')
    sLine =  "{:0.1f}".format( om_accretion )
    ifs.write(sLine)
    ifs.close()



    return om_accretion
  