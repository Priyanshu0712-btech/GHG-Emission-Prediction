# 🌍 GHG Emission Prediction using Supply Chain Data (2010–2016)

This project aims to build a machine learning pipeline to predict **Supply Chain Emission Factors with Margin** using historical GHG emission data across industries and commodities. The project also includes a deployable Streamlit web application for real-time predictions.

---

## ❓ Problem Statement

In the face of increasing climate change, it is critical to monitor and predict greenhouse gas (GHG) emissions generated across supply chains.  
Organizations and policymakers require accurate forecasting of emission factors to make data-driven decisions, reduce environmental impact, and comply with sustainability regulations.

This project solves that real-world challenge by predicting emission factors using ML models trained on multi-year industry data.

---

## 🎯 Objectives

- Merge multi-year Excel data (2010–2017) across sectors
- Clean, preprocess, encode, and scale data
- Train and evaluate machine learning models
- Select the best-performing model using metrics like RMSE and R² Score
- Build a user-friendly web interface with Streamlit for prediction

---

## 🧰 Tools & Technologies Used

| Category          | Tools / Libraries                          |
|------------------|---------------------------------------------|
| Language          | Python 3                                    |
| IDE/Platform      | Jupyter Notebook (Anaconda)                 |
| Data Processing   | pandas, numpy                               |
| Visualization     | matplotlib, seaborn                         |
| Machine Learning  | scikit-learn, joblib                        |
| Deployment        | Streamlit                                   |

---

## 📂 Dataset Info

- 📁 `SupplyChainEmisionFactorsForIndustriesCommodities.xlsx`
- 💼 Contains industry & commodity-wise data from 2010 to 2017
- Key features: Emission factors, DQ metrics (reliability, correlation), Substance, Source, Unit

---

## 🔁 Methodology

1. **Data Merging**  
   Merged 14 Excel sheets from 2010 to 2016 for both Industry & Commodity sources

2. **Data Cleaning & Transformation**  
   - Removed empty columns
   - Standardized unit columns
   - Encoded categorical features (`Substance`, `Source`, `Unit`)
   - Scaled numeric features using `StandardScaler`

3. **Modeling**  
   - Trained 3 models:
     - Linear Regression ✅
     - Random Forest (default)
     - Random Forest (GridSearchCV tuned)
   - Evaluation Metrics:
     - **R² Score:** 0.99999 (Linear Regression)
     - **RMSE:** 0.00028

4. **Model Selection & Saving**  
   - Linear Regression was selected as the best model
   - Saved model and scaler using `joblib`

5. **Streamlit App**  
   - UI to input features
   - Predicts Emission Factor with Margin

---

## 📊 Model Comparison

| Model                   | RMSE     | R² Score |
|------------------------|----------|----------|
| Random Forest (Default)| 0.00605  | 0.99935  |
| Linear Regression       | 0.00028  | 0.99999  |
| Random Forest (Tuned)  | 0.00589  | 0.99938  |

✅ **Linear Regression** outperformed others with highest accuracy.

---

## 🚀 Streamlit App

The Streamlit web app allows users to:
- Input Substance, Source, Emission values, and DQ scores  
- Predict Supply Chain Emission Factor with Margin  
- Get results instantly using the trained ML model

📦 Includes custom `preprocessor.py` to clean user inputs  
📁 App Code: `app.py`  
📁 Model Path: `models/LR_model.pkl`

---

## 📦 Folder Structure

GHG-Emission-Prediction/
├── app.py
├── models/
│ ├── LR_model.pkl
│ └── scaler.pkl
├── utils/
│ └── preprocessor.py
├── SupplyChainEmisionFactorsForIndustriesCommodities.xlsx
├── GHG_Emissions_Analysis.ipynb
├── README.md


---

## ✅ Conclusion

- Built a complete end-to-end GHG emission prediction system  
- Achieved near-perfect accuracy using Linear Regression  
- Web app deployed with Streamlit for live demo use  
- Ready for scaling and real-time deployment in sustainability projects

---

## ✍️ Author

**Name:** Priyanshu Kumar
🎓 *B.Tech – AI/ML, 4th Semester*  
