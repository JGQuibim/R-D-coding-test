import dicomhandling as dh
from dicomhandling import DcmFilter
from dicomhandling import DcmRotate

path1 = (r"C:\Users\Quibim\PycharmProjects\pythonProject\T1_3D_TFE-301/IM-0001-0035-0001.dcm")
path2 = (r"C:\Users\Quibim\PycharmProjects\pythonProject\T1_3D_TFE-301/IM-0001-0086-0001.dcm")

#Prueba1
sigma = 5
prueba1 = DcmFilter(path1, sigma)
print(prueba1.ipp)

#Prueba2
angle=270
prueba2 = DcmRotate(path2, angle)
print(prueba2.rotated)

#Prueba3
dh.check_ipp(prueba1, prueba2)

#Prueba4
dh.main()


