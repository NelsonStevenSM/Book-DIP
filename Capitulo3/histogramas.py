import cv2
import numpy as np
import matplotlib.pyplot as plt

def CDF(img):

    imagen = np.zeros(256)
    acum = 0 
    for i in range(0,256):
        imagen[i] = sum(img[0:i+1])

    return imagen


def PDF(img):
    imagen = np.zeros(256)    

    for i in img:
        imagen[i] += 1
    
    return imagen/(len(img))

img = cv2.imread("img/tomografia.png",0)

## Funcion de probabilidad de s
nelson = PDF(img.flatten())*CDF(PDF(img.flatten()))

### funcion "s"
#nelson = 255*CDF(PDF(img.flatten()))

#img = cv2.imread("img/ciudad.png",0)

#plt.plot(list(map(int,np.linspace(0,255,256))), PDF(img.flatten()))
#plt.show()

plt.plot(list(map(int,np.linspace(0,255,256))),nelson)
plt.show()

#plt.plot(list(map(int,np.linspace(0,255,256))), 255*CDF(PDF(img.flatten())))
#plt.show()



key = cv2.waitKey(0)

cv2.destroyAllWindows()
