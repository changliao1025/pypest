import sys, os
import numpy as np

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system.define_global_variables import *


sPath_pypest = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest)

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces

def maces_extract_omac_output(oPest_in, oModel_in):
    filename = '/Users/tanz151/Python_maces/src/maces_ecogeom_2002-01-01_2004-01-01_466.nc'
    try:
        nc = Dataset(filename,'r')
        x = np.array(nc.variables['x'][:])
        pft = np.array(nc.variables['pft'][:])
        Esed = np.array(nc.variables['Esed'][:])
        Dsed = np.array(nc.variables['Dsed'][:])
        DepOM = np.array(nc.variables['DepOM'][:])
    finally:
        nc.close()
    
    nx = np.size(x)
    dx = np.zeros(nx)
    dx[1:nx-1] = 0.5 * (x[2:nx] - x[0:nx-2])
    dx[0] = 0.5 * (x[0] + x[1])
    dx[nx-1] = 0.5 * (x[nx-2] + x[nx-1])

    nt = np.shape(pft)[0]
    dx = np.tile(dx,(nt,1))

    rhoSed = 2650 # this value from optpar_minac.xml
    porSed = 0.4 # this value from optpar_minac.xml


    # mineral accretion rate (mm/yr)
    wtlnd_x_avg = np.sum(dx[pft==2])/nt
    mineral_accretion = 0.5e3 * (8.64e4*np.sum(Dsed[pft==2]*dx[pft==2])/wtlnd_x_avg - \
        8.64e4*np.sum(Esed[pft==2]*dx[pft==2])/wtlnd_x_avg) / rhoSed / (1.0-porSed)

    # OM accretion rate (gC/m2/yr)
    om_accretion = 0.5e3 * 8.64e4 * np.sum(DepOM[pft==2]*dx[pft==2])/wtlnd_x_avg
    return om_accretion
  