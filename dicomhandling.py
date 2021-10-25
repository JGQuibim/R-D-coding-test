import numpy as np
import os
from pydicom import dcmread
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt

class DcmFilter:
    def __init__(self, path, sigma=3):
        if not isinstance(path, str):
            raise TypeError("path must be a string")
        elif not isinstance(sigma, int):
            raise TypeError("sigma must be a int")
        self.path = path
        self.sigma = sigma
        ds = dcmread(self.path)
        self.original = ds.pixel_array
        self.filtered = gaussian_filter(self.original, sigma)
        self.ipp = ds.ImagePositionPatient

class DcmRotate:
    def __init__(self, path, angle=180):
        if not isinstance(path, str):
            raise TypeError("path must be a string")
        elif not isinstance(angle, int):
            raise TypeError("angle must be a int")
        self.path = path
        self.angle = angle
        ds = dcmread(self.path)
        self.original = ds.pixel_array
        if angle == 90:
            m = 1
        elif angle == 180:
            m = 2
        elif angle == 270:
            m=3
        else:
            raise TypeError("the angle of Rotation must be 90, 180 or 270")
        self.rotated = np.rot90(self.original, m)
        self.ipp = ds.ImagePositionPatient

def check_ipp(filterA, filterB):
    equal = True
    for i in range(0, 3):
        if filterA.ipp[i] != filterB.ipp[i]:
            equal = False
    print(equal)

class IncorrectNumberOfImages(Exception):
    pass
class SameImagePositionPatient(Exception):
    pass

def main():
    directorio = (r"C:\Users\Quibim\PycharmProjects\pythonProject\T1_3D_TFE-301/")
    contenido = os.listdir(directorio)
    if len(contenido) != 2:
        raise IncorrectNumberOfImages("Incorrect Number of Images. Aborting")
    path1 = os.path.join(directorio, contenido[0])
    path2 = os.path.join(directorio, contenido[1])
    f1 = DcmFilter(path1)
    f2 = DcmFilter(path2)

    if f1.ipp == f2.ipp:
        raise SameImagePositionPatient("The DICOM files appear to be the same")
    else:
        UnfilteredResidue = f1.original - f2.original
        FilteredResidue = f1.filtered - f2.filtered
        #He tenido problemas para implementar una función save_as_jpeg, como me tengo que ir al hospital
        #Muestro por si quiero imprimir las imagenes resultantes en esquema como aparece en el enunciado.
        plt.figure(figsize=(9, 3))
        plt.subplot(131)
        plt.imshow(f1.original, cmap=plt.cm.gray)
        plt.xlabel("Image 01 Unfiltered")
        plt.subplot(132)
        plt.imshow(f2.original, cmap=plt.cm.gray)
        plt.xlabel("Image 02 Unfiltered")
        plt.subplot(133)
        plt.imshow(UnfilteredResidue, cmap=plt.cm.gray)
        plt.xlabel("Unfiltered Residue")
        plt.show()

        plt.figure(figsize=(9, 3))
        plt.subplot(131)
        plt.imshow(f1.filtered, cmap=plt.cm.gray)
        plt.xlabel("Image 01 filtered")
        plt.subplot(132)
        plt.imshow(f2.filtered, cmap=plt.cm.gray)
        plt.xlabel("Image 02 filtered")
        plt.subplot(133)
        plt.imshow(FilteredResidue, cmap=plt.cm.gray)
        plt.xlabel("Filtered Residue")
        plt.show()






