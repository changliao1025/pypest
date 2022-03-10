def pypest_prepare_pest_instruction_file():
    sWorkspace_scratch = oPest_in.sWorkspace_scratch
    sWorkspace_calibration_relative = oPest_in.sWorkspace_calibration        
    sWorkspace_calibration = sWorkspace_scratch + slash + sWorkspace_calibration_relative    
    sWorkspace_pest_model = sWorkspace_calibration
    #read obs
    aObservation1 = pest_prepare_maces_observation_file(oPest_in)
    nobs_with_missing_value = len(aObservation1)
    nstress = nobs_with_missing_value
    
    aObservation1 = np.reshape(aObservation1, nobs_with_missing_value)
    nan_index = np.where(aObservation1 == missing_value)
    aObservation1[nan_index] = missing_value

    #write instruction
    sFilename_instruction =  sWorkspace_pest_model + slash + oPest_in.sFilename_instruction
    ofs= open(sFilename_instruction,'w')
    ofs.write('pif $\n')

    #we need to consider that there is missing value in the observations
    for i in range(1, nstress+1):
        dDummy = aObservation1[i-1]
        if( dDummy != missing_value  ):
            sLine = 'l1' + ' !sem' + "{:04d}".format(i) + '!\n'
        else:
            sLine = 'l1' + ' !dum' + '!\n'
        ofs.write(sLine)
            
    ofs.close()
    print('The instruction file is prepared successfully!')
    return