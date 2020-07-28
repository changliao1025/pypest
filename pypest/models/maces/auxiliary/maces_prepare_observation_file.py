import sys, os
import numpy as np
import pandas as pd

sSystem_paths = os.environ['PATH'].split(os.pathsep)
sys.path.extend(sSystem_paths)
from pyes.system.define_global_variables import *

sPath_pypest = sWorkspace_code +  slash + 'python' + slash + 'pypest' + slash + 'pypest'
sys.path.append(sPath_pypest)

from pypest.models.maces.shared.pest import pypest
from pypest.models.maces.shared.model import maces

def maces_prepare_minac_observation():

    # read data
    sFilename = r'/people/liao313/data/maces/auxiliary' + slash +'VeniceLagoon/1BF_OBS.xls'
    df = pd.read_excel(sFilename, \
        sheet_name='1BF', \
        header=None, \
            skiprows=range(3), \
            usecols='A,B,F,O,Q')
    df.columns = ['Time','Hmo','Hmax','hw','Turbidity']
    sed_obs_1BF = np.array(df['Turbidity'])[5334:5526]  #mg/l
    nt_obs = np.size(sed_obs_1BF)
    #the orginal data is 15 minutes temporal resolution
    tt_obs = np.arange(nt_obs)/4
    nhour = int(nt_obs/4)
    #reshape 
    sed_obs_1BF1 = np.reshape(sed_obs_1BF, (nhour, 4))
    #get hourly dataset
    sed_obs_1BF2 = np.nanmean(sed_obs_1BF1, axis=1)
    #the temporal resolution is now at hourly
    return sed_obs_1BF2

def maces_prepare_omac_observation():

    # read data
    sFilename = r'/people/liao313/data/maces/auxiliary' + slash +'VeniceLagoon/1BF_OBS.xls'
    df = pd.read_excel(sFilename, \
        sheet_name='1BF', \
        header=None, \
            skiprows=range(3), \
            usecols='A,B,F,O,Q')
    df.columns = ['Time','Hmo','Hmax','hw','Turbidity']
    sed_obs_1BF = np.array(df['Turbidity'])[5334:5526]  #mg/l
    nt_obs = np.size(sed_obs_1BF)
    #the orginal data is 15 minutes temporal resolution
    tt_obs = np.arange(nt_obs)/4
    nhour = int(nt_obs/4)
    #reshape 
    sed_obs_1BF1 = np.reshape(sed_obs_1BF, (nhour, 4))
    #get hourly dataset
    sed_obs_1BF2 = np.nanmean(sed_obs_1BF1, axis=1)
    #the temporal resolution is now at hourly
    return sed_obs_1BF2