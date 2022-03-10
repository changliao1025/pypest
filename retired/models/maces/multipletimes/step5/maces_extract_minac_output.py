def maces_extract_minac_output(oPest_in, oModel_in):
    # read simulation outputs
    #example code from maces
    #filename = '/Users/tanz151/Python_maces/src/maces_ecogeom_2002-12-01_2002-12-13_466.nc'
    #try:
    #    nc = Dataset(filename,'r')
    #    x = np.array(nc.variables['x'][:])
    #    zh = np.array(nc.variables['zh'][0,:])
    #finally:
    #    nc.close()

    sFilename = ''
    try:
        nc = Dataset(sFilename,'r')
        x = np.array(nc.variables['x'][:])
        zh = np.array(nc.variables['zh'][0,:])

        #We will match up with the observation data here
        aSem_simulation = x
        #save it to a text file
        sFilename_out = sWorkspace_child + slash + 'sem.txt'

        np.savetxt(sFilename_out, aSem_simulation, delimiter=",")

    finally:
        nc.close()



    return