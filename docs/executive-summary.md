# Project 3: Predictive Customer Churn Engine

## Business Challenge
A subscription-based SaaS company was experiencing ongoing customer attrition and lacked an early warning system to identify high-risk accounts before they canceled. This created a reactive customer success model with avoidable revenue impact.

## Objectives
- predict which customers are likely to churn
- identify behavioral patterns linked to attrition
- support proactive customer success outreach
- reduce avoidable revenue loss from cancellations

## Success Criteria
- maintain a strong recall rate for churn detection
- define a practical risk threshold for customer intervention
- generate an outreach-ready list of high-risk accounts

## Tools
- Python
- NumPy
- Pandas
- scikit-learn
- Random Forest Classifier

## Methodology
1. load and validate customer engagement data
2. engineer predictive features from activity and account signals
3. split the data into training and validation sets
4. train a classification model to estimate churn risk
5. evaluate performance with classification metrics
6. rank accounts by risk probability and export high-priority outreach targets

## Model Summary
The model estimates the likelihood that a customer will churn based on engagement signals such as tenure, payment profile, support usage, and login activity. Accounts above a defined threshold are flagged for customer success outreach.

## Business Impact
This project demonstrates the value of predictive analytics for business protection. Instead of reacting after customers leave, the organization can identify risk early and intervene before the churn event occurs.

## Relevant Skills Demonstrated
- predictive modeling
- machine learning evaluation
- customer risk segmentation
- feature engineering
- data-driven retention strategy
- business value translation
