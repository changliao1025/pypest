from pest_parse_xml_file import pest_parse_xml_file
def pest_read_configuration_file(sFilename_configuration_in):
    aConfiguration = pest_parse_xml_file(sFilename_configuration_in)
    return aConfiguration
if __name__ == '__main__':

    pest_read_configuration_file(sFilename_configuration_in)