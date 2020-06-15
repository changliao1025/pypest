slash = '/'
def pest_prepare_maces_parameter_template_file(sFilename_configuration ):

    
    sFilename_parameter_template = sWorkspace_pest_model + slash + 'parameter.tpl'
    ofs = open(sFilename_parameter_template, 'w')
    sLine = 'ptf $\n'
    ofs.write(sLine)
    
    #sLine = 'hru, cn2\n'
    #ofs.write(sLine)
    
    
    sLine = 'hru' + ', ' + '$cn2'  +'$\n'
    ofs.write(sLine)
    ofs.close()
    print('hru template is ready!')
    return
if __name__ == '__main__':
    sFilename_configuration = 
    maces_prepare_parameter_template_file(sFilename_configuration)