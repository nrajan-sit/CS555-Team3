###############################################################################################

                            #M2.B3: Assignment: Project 2 - GEDCOM data

# Reads each line of a GEDCOM file
# Prints "--> <input line>"
# Prints "<-- <level>|<tag>|<valid?> : Y or N|<arguments>"
# <level> is the level of the input line, e.g. 0, 1, 2
# <tag> is the tag associated with the line, e.g. 'INDI', 'FAM', 'DATE', ...
# <valid?> has the value 'Y' if the tag is one of the supported tags or 'N' otherwise. 
###############################################################################################


# Import gedcom packages
from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser


# Get the ged file
file_path = 'assignment_2.ged'
# file_path = 'original_ged.ged'
# file_path = 'test_ged.ged'

# Initialize the parser
gedcom_parser = Parser()

# Parse your file
gedcom_parser.parse_file(file_path)

#root_child_elements = gedcom_parser.get_root_child_elements()

full_file = gedcom_parser.get_element_list()

valid_tags = ('INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM', 'MARR', 'HUSB', 
              'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE')

valid_ind = 'N'


# --> 0 NOTE dates after now
# <-- 0|NOTE|Y|dates after now

# 0 has 2 version
    # 0 <id> <tag>
        # tag - INDI or FAM
    # 0 <tag> <arguments>
        # tag - HEAD, TLDR or NOTE
    
    

# Iterate through all root child elements
for element in full_file:
    final_output = ''
    print('')
#     print('--> ',element)
#     print('---> level:', element.get_level())
#     print('---> tag:', element.get_tag())
#     print('---> value:', element.get_value())
#     print('---> pointer:' , element.get_pointer())
    
    if element.get_tag() in valid_tags:
        valid_ind = 'Y'
    else:
        valid_ind = 'N'
        
    #print(valid_ind)
    
    # special case for id = 0
    if element.get_level() == 0:
        #version 1 : 0 <id> <tag>
        if (element.get_value() == 'INDI' or element.get_value() == 'FAM'):
            valid_ind = 'Y'
            final_output = '<-- ' + str(element.get_level()) + '|' + element.get_value() + '|' + valid_ind + '|' + element.get_tag()
            
        if (element.get_tag() == 'INDI' or element.get_tag() == 'FAM'):
            valid_ind = 'Y'
            final_output = '<-- ' + str(element.get_level()) + '|' + element.get_tag() + '|' + valid_ind + '|' + element.get_pointer()

        #version 2 : 0 <tag> <arguments>
        if (element.get_tag() == 'HEAD' or element.get_tag() == 'TRLR' or element.get_tag() == 'NOTE'):
            valid_ind = 'Y'
            final_output = '<-- ' + str(element.get_level()) + '|' + element.get_tag() + '|' + valid_ind + '|' + element.get_value()

    else:
        final_output = '<-- ' + str(element.get_level()) + '|' + element.get_tag() + '|' + valid_ind + '|' +element.get_value()

    print('-->' , element)
    print(final_output)


