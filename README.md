---
title: Restaurant Revenue Predictor
emoji: 🍽️
colorFrom: green
colorTo: blue
sdk: streamlit
sdk_version: "1.32.2"
app_file: app.py
pinned: false
---

# 🍽️ Restaurant Revenue Predictor

Bu proje, bir restoranın açılış tarihi, tipi ve 37 farklı özellik kullanılarak **yıllık gelirini tahmin eden** bir makine öğrenmesi modelini içerir.

## 📊 Kullanılan Veri Seti

- [Kaggle - Restaurant Revenue Prediction](https://www.kaggle.com/competitions/restaurant-revenue-prediction)
- `train.csv` dosyası: restoran bilgileri ve gelir verisi içerir.

## ⚙️ Kullanılan Özellikler

- 37 sayısal özellik (P1 - P37)
- Açılış yılına göre hesaplanan restoran yaşı (Years)
- Kategorik değişkenler:
  - City Group (Big Cities, Other)
  - Restaurant Type (IL, FC, DT, MB)

## 🧠 Kullanılan Model

- `RandomForestRegressor` (sklearn)
- R² ve RMSE değerlendirmeleriyle test edilmiştir.
- `restaurant_revenue_model.pkl` olarak kaydedildi.

## 🚀 Streamlit Uygulaması

- Kullanıcıdan restoran bilgileri alınır.
- Model tahmini yapılır ve sonuç ekranda gösterilir.

## 🔧 Nasıl Çalıştırılır?

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🧾 Gerekli Dosyalar

- `app.py`
- `restaurant_revenue_model.pkl`
- `requirements.txt`
- `README.md`

## 📝 Lisans

MIT License