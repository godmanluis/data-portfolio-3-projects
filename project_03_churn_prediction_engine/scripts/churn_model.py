# Project 3: Predictive Customer Churn Engine

## Business Challenge
A subscription-based SaaS provider experienced a steady decline in customer retention and lacked a proactive mechanism for identifying at-risk accounts before they canceled.

## Objectives
- Build a churn prediction model
- Identify the strongest customer behaviors linked to attrition
- Prioritize at-risk accounts for outreach
- Reduce the cost of reactive customer support efforts

## Success Criteria
- Maintain strong recall for churn detection
- Create an operational risk threshold for customer success teams
- Export high-risk accounts for targeted intervention

## Tools
- Python
- NumPy
- Pandas
- scikit-learn
- Random Forest Classifier

## Methodology
1. Load and clean customer engagement data
2. Engineer predictive features
3. Split into training and validation sets
4. Train a classification model
5. Evaluate classification metrics
6. Rank customer risk and export outreach candidates

## Model Summary
The model uses churn-related customer signals to estimate the probability that a customer will leave. Accounts above a defined risk threshold are prioritized for retention outreach.

## Business Impact
This project demonstrates the ability to translate machine learning into commercial value by enabling proactive retention actions and helping protect recurring revenue.

## Suggested Next Steps
- Add a more realistic customer dataset or synthetic example
- Include risk scoring thresholds and segmentation logic
- Add dashboard output or sample retention outreach exports
