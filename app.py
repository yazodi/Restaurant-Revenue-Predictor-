
import streamlit as st
import pandas as pd
import joblib
import numpy as np
from datetime import datetime

# 🎯 Modeli yükle
model = joblib.load("restaurant_revenue_model.pkl")

# 🌆 Giriş alanları
st.title("🍽️ Restaurant Revenue Predictor")
st.write("Restoran bilgilerinizi girerek tahmini geliri öğrenin.")

# Kullanıcıdan giriş al
open_date = st.date_input("Açılış Tarihi", value=datetime(2015, 1, 1))
years = datetime.now().year - open_date.year

city_group = st.selectbox("City Group", ["Big Cities", "Other"])
type_rest = st.selectbox("Restaurant Type", ["IL", "FC", "DT", "MB"])

# Sayısal özellikler (P1 - P37 arası 37 özellik)
inputs = {}
for i in range(1, 38):
    inputs[f"P{i}"] = st.number_input(f"Feature P{i}", value=0)

# Encode işlemleri
inputs["Years"] = years
inputs["City Group_Other"] = 1 if city_group == "Other" else 0
inputs["Type_FC"] = 1 if type_rest == "FC" else 0
inputs["Type_IL"] = 1 if type_rest == "IL" else 0
inputs["Type_MB"] = 1 if type_rest == "MB" else 0

# Eksik olan kolonları ekle (eğitim setindeki sıralama ile uyumlu olmalı!)
feature_order = [f"P{i}" for i in range(1, 38)] + [
    "Years", "City Group_Other", "Type_FC", "Type_IL", "Type_MB"
]

input_df = pd.DataFrame([inputs])[feature_order]

# 🔍 Tahmin yap
if st.button("Tahmini Geliri Göster"):
    prediction = model.predict(input_df)[0]
    st.success(f"📊 Tahmini Gelir: ${prediction:,.2f}")
