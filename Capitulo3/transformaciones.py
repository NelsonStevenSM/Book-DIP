import cv2
import numpy as np
import matplotlib.pyplot as plt


def powerLaw(img, gamma=0.4, c=1):

    img = np.float32(img)
    img_log = c*np.power(img,gamma)

    funcG = img_log - min(img_log.flatten())
    g_s = 255*(funcG/max(funcG.flatten()))

    return np.uint8(g_s)

def negative(img):

    return 255 - img


def logTransform(img,c=1):
    img = np.float32(img)
    img_log = c*np.log(1+img)

    funcG = img_log - min(img_log.flatten())
    g_s = 255*(funcG/max(funcG.flatten()))

    return np.uint8(g_s)

img = cv2.imread("./img/ciudad.png",0)

negatProc = negative(img)

logtrans =logTransform(img, c=5)

power = powerLaw(img, gamma = 3, c=4)

cv2.imshow("Mamografia", img)

cv2.imshow("NegativeRGB", negatProc)

cv2.imshow("LogRGB", logtrans)

cv2.imshow("Power", power)
#
#plt.plot(img.flatten(), logtrans.flatten())
#plt.plot(img.flatten(), img.flatten())
#plt.show()



key = cv2.waitKey(0)


cv2.destroyAllWindows()






