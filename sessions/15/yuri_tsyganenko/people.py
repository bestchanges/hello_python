#
#  Python-gedcom parser is used - taken from https://github.com/nickreynke/python-gedcom
from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser


# Path to your `.ged` file
file_path = '/media/yuri/SECOND/work/try/grm/parsing_GED/GED_Samples/paf-2.2-first_family.ged'
#   One can download from https://github.com/geni/gedcom/raw/master/samples/paf-2.2-first_family.ged
#    However there are mismatches:
#   *  is a symbol causing troubles, in line    1 NAME Victoria  /Hanèover/
#   *  spaces in the beginning require doing lstrip() for each line (fix in parser.parse_file)

# Initialize the parser
gedcom_parser = Parser()

# Parse your file
gedcom_parser.parse_file(file_path)

root_child_elements = gedcom_parser.get_root_child_elements()

#  Iterate through all root child elements
pple = [element for element in root_child_elements if isinstance(element, IndividualElement)]

# list of dict
# name and birth_date only
ppld = [{"name": e.get_name()[0], "birth_date": e.get_birth_data()[0]} for e in pple]

print(ppld)


#  Sorting by name:
names = sorted([p.get_name()[0] for p in pple])
#sorted_names = names.sort()  #  DOES NOT WORK!!!

print(names)


