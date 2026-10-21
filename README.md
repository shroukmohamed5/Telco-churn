[README.md](https://github.com/user-attachments/files/33748519/README.md)
# Telco Customer Churn – Prediction & Deployment
<img width="1787" height="899" alt="image" src="https://github.com/user-attachments/assets/ec1bd25b-1efb-4e67-802f-dd91f932966f" />
<img width="929" height="848" alt="image" src="https://github.com/user-attachments/assets/535cf43d-cee4-42c3-9816-c4683dbf8dd0" />
<img width="1429" height="756" alt="image" src="https://github.com/user-attachments/assets/a20189b4-8858-4d63-97b4-337ac95c5b6e" />


## Files
| File | Purpose |
|---|---|
| `Telco_Churn_Notebook.ipynb` | Preprocessing, 7-model comparison, GridSearchCV tuning, saving the model |
| `best_model.pkl` | Final tuned model (full pipeline: encoder + scaler + Logistic Regression) |
| `app.py` | Streamlit web app |
| `Telco-Customer-Churn.csv` | Dataset |
| `requirements.txt` | Library versions |
| `Demo_Video_Script.md` | Step-by-step script for the 1-minute demo video |

## Run
```
pip install -r requirements.txt
streamlit run app.py
```
(To retrain: open the notebook and run all cells; it regenerates `best_model.pkl`.)

## Results (test set, churn class)
| Model | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| Logistic Regression | 0.806 | 0.657 | 0.559 | 0.604 |
| AdaBoost | 0.801 | 0.644 | 0.556 | 0.597 |
| SVM | 0.796 | 0.652 | 0.500 | 0.566 |
| XGBoost | 0.776 | 0.590 | 0.519 | 0.552 |
| KNN | 0.762 | 0.554 | 0.532 | 0.543 |
| Random Forest | 0.781 | 0.612 | 0.481 | 0.539 |
| Decision Tree | 0.725 | 0.483 | 0.497 | 0.490 |

Best model: Logistic Regression (by F1). After GridSearchCV (`C=1`, `class_weight='balanced'`): Recall 0.78, F1 0.61, ROC-AUC 0.84.
