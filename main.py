import cv2
import numpy as np

img = cv2.imread('./LdqQKoXa6Aw.jpg')

h = img.shape[0]
w = img.shape[1]


gist = []
for i in range(0, 256):
    gist.append(0)

for y in range(0, h):
    for x in range(0, w):
        s = int(round(img[y, x][0] * 0.0722 + img[y, x]
                      [1] * 0.7152+img[y, x][2] * 0.2126))

        gist[s] += 1


def otsu(histogram, pixelNumbers):
    summ, sumB, wB, wF, mB, mF, maxx, between, threshold = 0, 0, 0, 0, 0, 0, 0, 0, 0
    for i in range(0, 256):
        wB += histogram[i]
        if wB == 0:
            continue
        wF = pixelNumbers - wB
        if wF == 0:
            break
        sumB += i * histogram[i]
        mB = sumB / wB
        mF = (summ - sumB) / wF
        between = wB * wF * (mB - mF) ** 2
        if between > maxx:
            maxx = between
            threshold = i
    return threshold


print(gist)
print(h*w)

threshold = otsu(gist, (h * w)/2)
print(threshold)

for y in range(0, h):
    for x in range(0, w):
        img[y, x] = int(round(img[y, x][0] * 0.0722 + img[y, x]
                              [1] * 0.7152+img[y, x][2] * 0.2126))
        img[y, x] = 0 if img[y, x][0] < threshold else 255

cv2.imshow(f'{threshold}', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
