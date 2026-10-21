# Demo video script (about 1 minute)

**0:00–0:10** – Open a terminal in the project folder and run `streamlit run app.py`. Show the browser opening on the app page.
Say: "This app loads my saved model best_model.pkl and predicts customer churn."

**0:10–0:35** – Enter a risky customer:
- Contract: Month-to-month, Tenure: 2, Monthly charges: 95, Internet: Fiber optic, Payment: Electronic check
- Click **Predict** → shows "This customer is at risk of leaving ⚠️" (about 78% probability).

**0:35–0:55** – Enter a loyal customer:
- Contract: Two year, Tenure: 60, Monthly charges: 40, Total charges: 2400, Internet: DSL, Payment: Credit card (automatic)
- Click **Predict** → shows "This customer is likely to stay ✅" (about 18% probability).

**0:55–1:00** – Say: "Tuned Logistic Regression, recall of 78% on churners."

Tip: record with Win+G (Xbox Game Bar) on Windows or OBS.
