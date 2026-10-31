import datetime
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

print(f"[{datetime.datetime.now()}] Initializing Predictive ML Pipeline...")


def load_and_clean_data():
    np.random.seed(42)
    sample_size = 5000

    data = {
        "customer_id": range(1001, 1001 + sample_size),
        "tenure_months": np.random.randint(1, 48, size=sample_size),
        "monthly_charges": np.random.uniform(20.0, 150.0, size=sample_size),
        "support_tickets_raised": np.random.randint(0, 10, size=sample_size),
        "app_logins_last_30d": np.random.randint(0, 30, size=sample_size),
        "churned": np.random.choice([0, 1], size=sample_size, p=[0.82, 0.18]),
    }

    df = pd.DataFrame(data)
    df.loc[df["app_logins_last_30d"] < 0, "app_logins_last_30d"] = 0
    return df


df_clean = load_and_clean_data()

X = df_clean.drop(columns=["customer_id", "churned"])
y = df_clean["churned"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=8,
    random_state=42,
    class_weight="balanced",
)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

print("\n--- ENTERPRISE EVALUATION METRICS ---")
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))


def run_retention_routing(original_df, model_instance, scaler_instance):
    features_scaled = scaler_instance.transform(
        original_df.drop(columns=["customer_id", "churned"])
    )

    churn_probabilities = model_instance.predict_proba(features_scaled)[:, 1]
    original_df["Churn_Risk_Probability_%"] = np.round(churn_probabilities * 100, 2)

    high_risk_pipeline = original_df[
        original_df["Churn_Risk_Probability_%"] >= 75.0
    ]

    output_path = "targeted_retention_outreach.csv"
    high_risk_pipeline[
        ["customer_id", "Churn_Risk_Probability_%", "support_tickets_raised"]
    ].to_csv(output_path, index=False)

    print(
        f"\n[PIPELINE SUCCESS] Exported {len(high_risk_pipeline)} high-risk target accounts to '{output_path}'."
    )


run_retention_routing(df_clean, model, scaler)
