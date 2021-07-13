# Practical Examples in UiPath   

## 作者
<span> - &copy; Tom Wu (<a href="https://github.com/YenLinWu">Github</a>) </span>  

## 實作範例  
* [Trading Details of Foreign Investors](#Trading_Details_of_Foreign_Investors)
* [Google News](#Google_News)
* [Worldwide Tax Summaries Online](#Worldwide_Tax_Summaries_Online)

## Trading_Details_of_Foreign_Investors
在 [嗨投資](https://histock.tw/) 網站中抓取當日台股大盤三大法人買賣超的資訊   
- 將網頁中爬取到的表格寫入 Excel ( [20210713_三大法人買賣超.xlsx](https://github.com/YenLinWu/RPA_UiPath/blob/master/Examples/Trading_Details_of_Foreign_Investors/Output/20210713_%E4%B8%89%E5%A4%A7%E6%B3%95%E4%BA%BA%E8%B2%B7%E8%B3%A3%E8%B6%85.xlsx) )。   

![image](./Trading_Details_of_Foreign_Investors/README_gif/Trading_Details_of_Foreign_Investors.gif)

Back to [實作範例](#實作範例)

## Google_News 
在 Google 中查詢多家上市公司的新聞資訊
- 使用「site:」運算子搜尋特定網站中的相關新聞；    
- 產出一彙整表( [GoogleNews_( Search Date 20210527 ).xlsx](https://github.com/YenLinWu/RPA_UiPath/blob/master/Examples/Google_News/Output/20210527/GoogleNews_(%20Search%20Date%2020210527%20).xlsx) )紀錄查詢結果，且將新聞標題插入超連結網址。 
   
![image](./Google_News/README_gif/Google_News.gif)

Back to [實作範例](#實作範例)

## Worldwide_Tax_Summaries_Online   
在 [Worldwide Tax Summaries Online](https://taxsummaries.pwc.com/) 網站中查詢多個國家的稅率資訊   
- 將每個查詢結果，以列印另存 PDF 的方式存檔；   
- 在每個查詢結果的頁面中，擷取特定的稅率，且產出一彙整表( [彙總表_20210522.xlsx](https://github.com/YenLinWu/RPA_UiPath/blob/master/Examples/Worldwide_Tax_Summaries_Online/Output/20210522/%E5%BD%99%E7%B8%BD%E8%A1%A8_20210522.xlsx) )總結每個國家的特定稅率。  
   
![image](./Worldwide_Tax_Summaries_Online/README_gif/Worldwide_Tax_Summaries_Online.gif)

Back to [實作範例](#實作範例)
