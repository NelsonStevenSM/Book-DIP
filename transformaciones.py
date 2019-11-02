import cv2
import numpy as np

def negative(img):

    return 255 - img


def logTransform(img,c=1):

    img_log = c*np.log(1+img)

    funcG = img_log - min(img_log.flatten())
    g_s = 255*(funcG/max(funcG.flatten()))

    return np.uint8(g_s)

img = cv2.imread("./img/tomografia.png",0)

negatProc = negative(img)

logtrans =logTransform(img, c=5)

cv2.imshow("Mamografia", img)

cv2.imshow("NegativeRGB", negatProc)

cv2.imshow("LogRGB", logtrans)

key = cv2.waitKey(0)


cv2.destroyAllWindows()






