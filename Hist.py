'''
Histogram Eqalization Algorithm compare Program
Using Python, Opencv
github : https://github.com/Lua-developer
blog : https://blog.naver.com/bjjy1113
'''

import cv2
import numpy as np
# 인풋 이미지가 크게 나와서 하나는 출력용으로 두개를 부름
img = cv2.imread("tesla.jpg")
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
# Y차원 히스토그램 평활화 적용
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
# Step 2 직접 구현
# Y차원 밝기 영역의 픽셀 row, column 값을 뽑아낸다
y, cr, cb = cv2.split(img_yuv)
height, width = cr.shape
hist = [0] * 256
pmf = [0] * 256
cdf = [0] * 256
levelBaru = [0] * 256
# 히스토그램 생성
for i in range(0, height) :
  for j in range(0, width) :
    hist[y.item(i,j)] += 1
# 밝기값을 정규화
region = float(width * height)
for i in range(0, 256) :
  hist[i] = hist[i] / region
cdf[0] = hist[0]
for i in range(1, 256) :
  cdf[i] = cdf[i-1] + hist[i]
for i in range(1,256):            
  levelBaru[i] = int(cdf[i]*255)

after_img = cv2.merge((y, cr, cb))
after_img = cv2.cvtColor(after_img, cv2.COLOR_YCR_CB2BGR)
for i in range(0,height):
  for j in range(0,width):
    for k in range (0,256):
      if(y.item(i,j)==k):
        y.itemset((i,j),levelBaru[k])
# Ycbcr 을 BGR로 변환
img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YCR_CB2BGR)
print("opencv 내부 함수를 사용한 PSNR 값 : ", cv2.PSNR(img, img_output))
print("직접 계산를 사용한 PSNR 값 : ", cv2.PSNR(img, after_img))
img_output = cv2.resize(img_output, [480, 320])
after_img = cv2.resize(after_img, [480, 320])
img = cv2.resize(img, [480,360])
cv2.imshow('Color input image', img)
cv2.imshow('Histogram equalized', img_output)
cv2.imshow('Histogram equalized2', after_img)
cv2.waitKey(0)
