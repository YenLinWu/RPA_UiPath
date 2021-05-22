# RPA( Robotic Process Automation ) Practical Examples   
使用 UiPath 開發 RPA 流程自動化機器人，本專案將彙整程式開發的實用語法，及日常實務案例的分享。  

##  [What Is RPA?](http://www.youtube.com/watch?v=9URSbTOE4YI)  
[![](http://img.youtube.com/vi/9URSbTOE4YI/0.jpg)](http://www.youtube.com/watch?v=9URSbTOE4YI "RPA In 5 Minutes | What Is RPA - Robotic Process Automation?")  
> [Watch more about RPA](https://www.youtube.com/c/SimplilearnOfficial/search?query=rpa)  
Source of vedio [Simplilearn](https://www.youtube.com/c/SimplilearnOfficial/featured) 
  
## 系統環境 System Environment     
[UiPath 官方建議](https://docs.uipath.com/installation-and-upgrade/docs/studio-hardware-and-software-requirements "Hardware and Software Requirements")   
作者開發環境如下:  
* Windows 10/ 16 GB RAM/ Intel i7 CPU   
* UiPath Studio Pro 2020.4.3 以上   
* Microsoft Office 2016 
* Python 3.6   
  
## 開發筆記 Programming Notes       
- UiPath 程式開發實用語法彙整，請參考 [Wiki](https://github.com/YenLinWu/RPA_UiPath/wiki)。    
- [程式碼片段(Snippets)](https://github.com/YenLinWu/RPA_UiPath/tree/master/Snippets)  

## 實作專案 Practical Projects (by UiPath)  
### 1. [Excel VBA x UiPath](https://github.com/YenLinWu/RPA_UiPath/tree/master/Excel%20VBA%20x%20UiPath)
在 UiPath 中呼叫 Excel VBA 程式碼，進行 Excel 檔的格式調整，例如 : 更新或移除 Excel 檔的外部資料連結、合併儲存格、新增儲存格框線、轉換儲存格的資料型態、重新整理樞紐分析表等。  

### 2. [Python x UiPath](https://github.com/YenLinWu/RPA_UiPath/tree/master/Python%20x%20UiPath)  
當資料量很龐大時，透過 UiPath 與 Python 的結合，能讓 RPA 機器人更有效率且靈活地產製出我們想客製化的報表。   

### 3. [OpenCV x Tesseract x UiPath](https://github.com/YenLinWu/RPA_UiPath/tree/master/OpenCV%20x%20Tesseract%20x%20UiPath)
當某個網站的登入需輸入驗證碼(Capctha)時，可嘗試先藉由 OpenCV 對驗證碼圖片進行前處理，再透過 Tesseract OCR 的影像識別，讓 RPA 機器人成功登入網站。   
  
### 4. [TensorFlow2 x CRNN x UiPath](https://github.com/YenLinWu/RPA_UiPath/tree/master/TensorFlow2%20x%20CRNN%20x%20UiPath)
在 UiPath 中調用一個預訓練完成的 AI 模型 - 卷積遞迴神經網絡( Convolutional Recurrent Neural Network, CRNN )，使得 RPA 機器人能精確地辨識網頁驗證碼圖片。  

### 5. [Practical Examples in UiPath](https://github.com/YenLinWu/RPA_UiPath/tree/master/Examples)
實作開發專案。  

## 開發參考資源 Coding References   
- [UiPath Forum](https://forum.uipath.com/ "UiPath 論壇")
- [Supported Character Encoding](https://docs.uipath.com/activities/docs/supported-character-encoding "讀寫檔編碼方式")
- [字元集 (0-127)](https://docs.microsoft.com/zh-tw/office/vba/language/reference/user-interface-help/character-set-0127 "處理字串時參考")  
- [字元集 (128-255)](https://docs.microsoft.com/zh-tw/office/vba/language/reference/user-interface-help/character-set-128255 "處理字串時參考")  
- [正規表示式(Regular Expression)](https://www.regular-expressions.info/unicode.html "處理字串時參考")    
- [Math 類別](https://docs.microsoft.com/zh-tw/dotnet/api/system.math?view=netframework-4.8 "數值運算時參考")  
- [DateTime.FromOADate(Double) Method](https://docs.microsoft.com/en-us/dotnet/api/system.datetime.fromoadate?view=netframework-4.7.2 "日期序列值轉成日期")
- [DateTime.ToOADate Method](https://docs.microsoft.com/en-us/dotnet/api/system.datetime.tooadate?view=netframework-4.7.2 "日期轉成日期序列值")  
- [EOMONTH 函數](https://support.microsoft.com/zh-tw/office/eomonth-%E5%87%BD%E6%95%B8-7314ffa1-2bc9-4005-9d66-f49db127d628 "Excel 中取得特定月份的最後一日")
- [TEXT 函數](https://support.microsoft.com/zh-tw/office/text-%E5%87%BD%E6%95%B8-20d5ac4d-7b94-49fd-bb38-93d29371225c "Excel 中儲存格格式轉文字型態")

## 作者 Author  
<span> - &copy; Tom Wu (<a href="https://github.com/YenLinWu">Github</a>) </span>  
  
## 致謝 Acknowledgement  
如有轉載、改作、分享，請註明出處。  
Please cite this repository [RPA_UiPath](https://github.com/YenLinWu/RPA_UiPath) if you use it.  
