from pyscript import display

Math = {'Manuel', 'Esa', 'Fran', 'Claire'}
Science = {'Dwayne', 'Esa', 'Manuel', 'Martin'}

display('All the students in at least one club are ' + str(Math | Science), target='output') #Union
display('The students in both clubs are ' + str(Math & Science), target='output') #Intersection
display('All Math Club members are ' + str(Math), target='output') 
display('All Science Club members are ' + str(Science), target='output')
display('All sudents in only one club are ' + str(Math ^ Science), target='output') #Symmetric Difference
