# TensorFlow 2.3 x CRNN x UiPath   
![Python3.6](https://img.shields.io/badge/Python-3.6-blue.svg) ![TensorFlow](https://img.shields.io/badge/TensorFlow-2.3-yellow.svg)

> 藉由 TensorFlow 2.3 建置及訓練一個卷積遞迴神經網絡( Convolutional Recurrent Neural Network, CRNN )模型，並將此模型配置於 UiPath 程式碼中，使得 RPA 機器人能精確地辨識驗證碼圖片。

![image](./README_gif/Demo.gif)

## 系統環境
作者開發環境如下:

- Windows 10/ 16 GB RAM/ Intel i7 CPU    
- UiPath Studio Pro 2020.4.3 以上
- Python 3.6
- TensorFlow 2.3

   
## TensorFlow 2.x 環境建置步驟     
- ### Step 1 下載安裝 Miniconda  
>> 下載網址 : [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

- ### Step 2 開啟 Anaconda Prompt(miniconda3)   
>> 【開始】&rarr; 以系統管理員身分執行【Anaconda Prompt(miniconda3)】

- ### Step 3 查看目前已有的虛擬環境     
```console
conda env list
```

- ### Step 4 創建新的 Python 3.6 虛擬環境  
```console
conda create --name 虛擬環境名稱 python=3.6
```

- ### Step 5 啟動新建立的 Python 3.6 虛擬環境  
```console
activate 虛擬環境名稱
```

- ### Step 6 安裝 TensorFlow 2.x 
```console
pip install "tensorflow>=2.0.0"
```

- ### Step 7 檢查 TensorFlow 2.x 是否安裝成功
```console
python   
import tensorflow as tf 
print( tf.__version__ )
``` 
![image](./README_gif/Verify_TF_Installation.png)
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
