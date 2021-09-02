file = open('group2.docx', 'a')

file.write('''
	Accepting File Submissions with Flask
For regular forms, Flask provides access to submitted form fields in the request.form dictionary. File fields, however, are included in the request.files dictionary. The request.form and request.files dictionaries are really "multi-dicts", a specialized dictionary implementation that supports duplicate keys. This is necessary because forms can include multiple fields with the same name, as is often the case with groups of check boxes. This also happens with file fields that allow multiple files.

Ignoring important aspects such as validation and security for the moment, the short Flask application shown below accepts a file uploaded with the form shown in the previous section, and writes the submitted file to the current directory:
	''')

# for x in file:
# 	print(x)

# print(file.readlines(23))

# file.write('\nI am a good programmer')

file.close()