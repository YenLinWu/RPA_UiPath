# Tesseract OCR x UiPath   
![Python3.6](https://img.shields.io/badge/Python-3.6-blue.svg)

> 當網站登入具驗證碼(Capctha)機制時，先藉由 OpenCV 對圖像的前處理後，再透過 Tesseract OCR 的影像識別，使得 RPA 機器人成功登入網站。   


## 示範  
本專案以 RPA 機器人登入[財團法人保險事業發展中心 保險統計資料庫加值服務](http://insdb.tii.org.tw/pivot/)為範例，本次執行登入過程中，在第 6 次執行時登入成功 :
![image](./Demo.gif)

在這 6 次嘗試登入時，各次驗證碼圖片的前處理及 OCR 識別結果如下:     
| 次數 | 原始驗證碼圖片 | 圖片前處理 | Tesseract OCR 識別 |
| :----------: | ---------- | ----------- | :-----------: |
| 1 | ![image](./Captcha_Images/1st_Captcha.png) | ![image](./Captcha_Images/1st_Prediction__34.png) | **34** |
| 2 | ![image](./Captcha_Images/2nd_Captcha.png) | ![image](./Captcha_Images/2nd_Prediction__4441.png) | **4441** |
| 3 | ![image](./Captcha_Images/3rd_Captcha.png) | ![image](./Captcha_Images/3rd_Prediction__1425.png) | **1425** |
| 4 | ![image](./Captcha_Images/4th_Captcha.png) | ![image](./Captcha_Images/4th_Prediction__6037.png) | **6037** |
| 5 | ![image](./Captcha_Images/5th_Captcha.png) | ![image](./Captcha_Images/5th_Prediction__21410.png) | **21410** |
| 6 | ![image](./Captcha_Images/6th_Captcha.png) | ![image](./Captcha_Images/6th_Prediction__6615.png) | **6615** |
 
 
## 圖片前處理 Image Preprocessing   
透過 OpenCV 套件(Open Source Computer Vision Library)所提供圖片前處理的工具，能讓驗證碼圖片中的數字更清楚地呈現。
 
- ### Step 1 讀取驗證碼圖片  
```command
import cv2

# img_path : 驗證碼圖片的路徑(含副檔名 .png)
bgr_img = cv2.imread( img_path )

# Convert BGR to RGB
rgb_img = bgr_img[ :,:,::-1 ]
```   
![image](./Captcha_Images_Preprocessing/Step_1_Loading.png) &larr; 原始驗證碼圖片

- ### Step 2 縮放驗證碼圖片   
>> 將原始圖片從 104 x 24 (寬x高)的原大小縮放成 104 x 32 的大小:
```command
img_pixel = cv2.resize( rgb_img, (104,32) )
```  
![image](./Captcha_Images_Preprocessing/Step_2_Resize.png) 

- ### Step 3 圖片二值化  
>> 透過圖像二值化(Image Binarization)的方法，能使圖片呈現出明顯的黑白效果，從而清楚地凸顯出圖片中的目標輪廓:
```command
img_pixel = cv2.threshold( img_pixel, 20, 255, cv2.THRESH_BINARY )[1]
```  
![image](./Captcha_Images_Preprocessing/Step_3_Thresholding.png)

- ### Step 4 圖片去躁  
>> 透過圖像去躁(Image Denoising)的手法，能移除圖片中不必要且多餘的雜訊，從而保留住圖片中較重要的資訊:
```command
img_pixel = cv2.fastNlMeansDenoisingColored( img_pixel, None, 55, 55, 5, 15 )
```  
![image](./Captcha_Images_Preprocessing/Step_4_Denoising.png)

- ### Step 5 圖片二值化  
```command
img_pixel = cv2.threshold( img_pixel, 50, 255, cv2.THRESH_BINARY )[1]
```  
![image](./Captcha_Images_Preprocessing/Step_5_Thresholding.png)

- ### Step 6 圖片侵蝕  
```command
img_pixel = cv2.erode( img_pixel, (5,5), iterations=1 )
```  
![image](./Captcha_Images_Preprocessing/Step_6_Erosion.png)

## 作者
<span> - &copy; Tom Wu (<a href="https://github.com/YenLinWu">Github</a>) </span>  
