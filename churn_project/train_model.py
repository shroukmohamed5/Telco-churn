# Retrains the final tuned model (same steps as the notebook) and saves best_model.pkl
# using the SAME Python / scikit-learn version that runs the Streamlit app.
import joblib, numpy as np, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, f1_score

df = pd.read_csv('Telco-Customer-Churn.csv')
for c in df.select_dtypes('object').columns:
    df[c] = df[c].str.strip()
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'].replace('', np.nan)).fillna(0)
df = df.drop(columns='customerID')

X = df.drop(columns='Churn'); y = (df['Churn'] == 'Yes').astype(int)
num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
cat_cols = [c for c in X.columns if c not in num_cols]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

prep = ColumnTransformer([('num', StandardScaler(), num_cols),
                          ('cat', OneHotEncoder(handle_unknown='ignore', drop='if_binary'), cat_cols)])
# best params found by GridSearchCV in the notebook: C=1, class_weight='balanced'
model = Pipeline([('prep', prep), ('clf', LogisticRegression(C=1, class_weight='balanced', max_iter=1000, random_state=42))])
model.fit(X_train, y_train)
pred = model.predict(X_test)
print('Accuracy', round(accuracy_score(y_test, pred), 4), 'Recall', round(recall_score(y_test, pred), 4), 'F1', round(f1_score(y_test, pred), 4))
joblib.dump(model, 'best_model.pkl')
print('Saved best_model.pkl')
