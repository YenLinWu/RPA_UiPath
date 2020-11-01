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
 




## 作者
<span> - &copy; Tom Wu (<a href="https://github.com/YenLinWu">Github</a>) </span>  
