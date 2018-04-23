from pyautocad import Autocad, APoint
import math

PI=math.pi

acad=Autocad('Test.dwg')

for dim in acad.iter_objects('Dimension'):
	print(dim.EntityName, dim.EntityType)
	print(dim.GetTypeInfo)
	print(dim.Handle.title())
	print(dim.TextPosition)
	if dim.EntityType == 10:
		print(round(dim.Measurement*180/PI,3))
	else:
		print (dim.Measurement)
	print ('==============================\n')
