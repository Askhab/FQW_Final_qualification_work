import xmlschema

schema = xmlschema.XMLSchema('input_files/TP_v06_R04/TP_v06.xsd')
print(schema.is_valid('input_files/TP_v06_R04/TP_v06.xml'))