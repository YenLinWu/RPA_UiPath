# TensorFlow 2.3 x CRNN x UiPath   
![Python3.6](https://img.shields.io/badge/Python-3.6-blue.svg) ![TensorFlow](https://img.shields.io/badge/TensorFlow-2.3-yellow.svg)

> 藉由 TensorFlow 2.3 建置及訓練一個卷積遞迴神經網絡( Convolutional Recurrent Neural Network, CRNN )模型，並將此模型配置於 UiPath 程式碼中，使得 RPA 機器人能精確地辨識驗證碼圖片。

![image](./README_gif/Demo.gif)

## 系統環境
作者開發環境如下:

- Windows 10
- 16 GB RAM  
- Intel i7 CPU  
- UiPath Studio Pro 2020.4.3 以上
- Python 3.6
- TensorFlow 2.3

   
## TensorFlow 2.x 環境建置步驟     
- ### Step 1 下載安裝 Miniconda  
>> 下載網址 : [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

- ### Step 2 開啟   
>> 將原始圖片從 104 x 24 (寬x高)的原大小縮放成 104 x 32 的大小:
```command
img_pixel = cv2.resize( rgb_img, (104,32) )
```  
![image](./Captcha_Images_Preprocessing/Step_2_Resize.png) 

- ### Step 3 圖片二值化  
>> 透過圖片二值化(Image Binarization)的方法，能使圖片呈現出明顯的黑白效果，從而清楚地凸顯出圖片中的目標輪廓:
```command
img_pixel = cv2.threshold( img_pixel, 20, 255, cv2.THRESH_BINARY )[1]
```  
![image](./Captcha_Images_Preprocessing/Step_3_Thresholding.png)

- ### Step 4 圖片去躁  
>> 透過圖片去躁(Image Denoising)的手法，能移除圖片中不必要且多餘的雜訊，從而保留住圖片中較重要的資訊:
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
>> 影像形態學(Morphology)中的侵蝕(Erosion)手法，其作用為將圖像中高亮度的區域進行縮減；在本專案的範例中，經過二值化及去躁處理過後的驗證碼圖片，侵蝕能加粗圖片中的數字，使資訊更加明顯可見:
```command
img_pixel = cv2.erode( img_pixel, (5,5), iterations=1 )
```  
![image](./Captcha_Images_Preprocessing/Step_6_Erosion.png)

- ### Step 7 Tesseract OCR 辨識  
>> 經由上述 Step 2 ~ Step 6 前處理的過程後，使用 Tesseract OCR 套件對前處理過的圖片進行辨識:  
```command
#pip install pytesseract
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
text = pytesseract.image_to_string( img_pixel, lang='eng', config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789' ) 
print( text )
```  
<br/>  


## 結論    
在這個簡單的範例中，雖然我們可藉由 OpenCV 的圖片前處理與 Tesseract OCR 的影像辨識，來幫助 RPA 機器人辨識出驗證碼中的資訊，但此方法仍有許多需改進的空間: 
- 首先，辨識的準確率不夠高，經作者實測的經驗，當 RPA 機器人成功登入時，平均每次需反覆重試的次數為 5 ~ 8 次，也就是說，每次執行需約 5 ~ 8 次的嘗試才能登入成功；
- 再者，若當驗證碼的圖片更加複雜時，例如: 英文字母與數字混合、字體更加歪斜、更多的干擾線等，將大福降低此方法的可行性。   

因此，對於其他網站的驗證碼識別，若經上述兩點考量後，發覺此方法並不可行時，建議可透過訓練一個 AI 模型: 卷積遞迴神經網絡(CRNN)，來克服此方法在技術上的不足與侷限。  
> 註: 如何訓練一個卷積遞迴神經網絡(CRNN)? 可參考[ CRNN_with_CTC_Loss ](https://github.com/YenLinWu/CRNN_with_CTC_Loss)。
<br/>  


## 參考文獻  
- [Img Recognition/Classification with Tensorflow2.0 + UiPath step by step — local](https://medium.com/@reginwon/img-recognition-with-tensorflow-uipath-step-by-step-38accc241662) 
- [輕鬆學習 Python：conda 的核心功能](https://medium.com/datainpoint/python-essentials-conda-quickstart-1f1e9ecd1025)
- [Installing TensorFlow 2.3.0 and Torch 1.6.0 on Windows 10 with CUDA Support](https://medium.com/@mhfateen/installing-tensorflow-2-3-0-and-torch-1-6-0-on-windows-10-with-cuda-support-97ea4ff4f8fa)


## 作者
<span> - &copy; Tom Wu (<a href="https://github.com/YenLinWu">Github</a>) </span>  
