import sys
import os
import numpy as np

import datetime
import calendar
from jdcal import gcal2jd, jd2gcal
from numpy import array

from pyearth.system.define_global_variables import *

from pyearth.toolbox.reader.text_reader_string import text_reader_string



def swat_prepare_observation_discharge_file(oModel_in):
    sModel = oModel_in.sModel
    
    sWorkspace_scratch = oModel_in.sWorkspace_scratch
   
    sWorkspace_data = oModel_in.sWorkspace_data
    

    sFilename_observation_discharge = oModel_in.sFilename_observation_discharge
    iYear_start = oModel_in.iYear_start
    iYear_end  =oModel_in.iYear_end
    iMonth_start = oModel_in.iMonth_start
    iMonth_end  =oModel_in.iMonth_end
    iDay_start = oModel_in.iDay_start
    iDay_end  =oModel_in.iDay_end
   
    sRegion = oModel_in.sRegion

    
    lJulian_start = gcal2jd(iYear_start, iMonth_start, iDay_start)
    nstress = oModel_in.nstress
    
    print(nstress )


    

    sFilename_discharge = sWorkspace_data + slash + sModel + slash \
        + sRegion + slash + 'auxiliary' + slash + sFilename_observation_discharge
    aData_dummy = text_reader_string(sFilename_discharge, cDelimiter_in=',', iSkipline_in=1)
    print(sFilename_discharge)
    aData = array( aData_dummy )
    aMonth =  aData[:,0] 
    aDay =  aData[:,1] 
    aYear =  aData[:,2] 
    aDischarge = aData[:, 3] #unit is cms because it is convected in excel
    nobs = len(aDischarge)
  
    #save a txt file for other purpose
    sPath =  sWorkspace_data + slash + sModel + slash + sRegion + slash \
    + 'auxiliary' + slash + 'usgs' + slash + 'discharge' + slash
    Path(sPath).mkdir(parents=True, exist_ok=True)
    sFilename_observation_discharge_out = sPath + slash + 'discharge_observation.txt' 
    #ofs= open(sFilename_observation_discharge_out, 'w')
    aDischarge_observation = np.full( (nstress), missing_value, dtype=float )
    for i in range(0, nobs):
        iYear = int(aYear[i])
        iMonth = int( aMonth[i])
        iDay = int(aDay[i])
        dDischarge = float(aDischarge[i])
        jd_dummy = gcal2jd(iYear, iMonth, iDay)        
        lIndex = jd_dummy[1] - lJulian_start[1]
        if lIndex >=0 and lIndex < nstress:

            aDischarge_observation[ int(lIndex)] = dDischarge
    #ofs.write(aDischarge_observation)
    #ofs.close()
    np.savetxt(sFilename_observation_discharge_out, aDischarge_observation, delimiter=',', fmt='%0.6f') 
    print('finished')

