# Analysis Preregistration

**Project:** Geldium Customer Delinquency Analysis

**Date:** 17 November 2026

**Dataset:** Geldium Customer Dataset

## 1. Research question

Can customer financial characteristics and payment history help distinguish delinquent customers from non-delinquent customers in the Geldium dataset?

The study will evaluate Logistic Regression and Decision Tree models for customer delinquency classification.

## 2. Hypotheses

**Null Hypothesis (H0):**

The predictive model does not demonstrate better out-of-sample discrimination than a baseline model.

**Alternative Hypothesis (H1):**

The predictive model demonstrates better out-of-sample discrimination than the baseline model, measured using PR-AUC.

## 3. Population, sample, and exclusions

**Target population:** Geldium customers represented in the dataset.

**Sample:**
- Total customers: 500
- Non-delinquent: 420 (84%)
- Delinquent: 80 (16%)

**Unit of analysis:** Individual customer.

**Inclusion criteria:**
- Valid customer records.
- Valid binary delinquency target.

**Exclusion criteria:**
- Missing or invalid target values.
- Duplicate customer records after verification.
- Customer_ID as a predictive feature.
- Features confirmed to contain information recorded after the outcome.

**Stopping rule:** Use all eligible available records. No additional observations will be collected.

The exact prediction date and outcome window remain unconfirmed.

## 4. Variables and measures

**Outcome variable:**
- Delinquent_Account
- 0 = Non-delinquent
- 1 = Delinquent

**Candidate predictors:**
- Missed_Payments
- Month_1 to Month_6
- Credit_Utilization
- Debt_to_Income_Ratio
- Credit_Score
- Income
- Loan_Balance
- Account_Tenure

**Missing values:**
- Income: 39
- Loan_Balance: 29
- Credit_Score: 2

**Data transformations:**
1. Check missing values and duplicates.
2. Standardize inconsistent category labels after verification.
3. Validate utilization values above 100%.
4. Investigate payment-history inconsistencies.
5. Apply median imputation using training data only.
6. Encode categorical variables.
7. Scale numerical variables for Logistic Regression.
8. Prevent data leakage through training-fold preprocessing.

## 5. Analysis plan

**Primary model:** Logistic Regression.

**Comparison model:** Shallow Decision Tree.

**Validation:** Stratified 5-fold cross-validation.

**Primary metric:** PR-AUC.

**Secondary metrics:**
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Brier score

**Significance level:** 0.05 for exploratory statistical tests.

**Effect sizes:** Report Logistic Regression odds ratios and confidence intervals where appropriate.

**Robustness checks:**
1. Compare both models.
2. Check missing-value handling.
3. Assess class imbalance.
4. Test different classification thresholds.
5. Investigate unusual utilization values.
6. Check subgroup performance.
7. Check for data leakage.

## 6. Deviations

Every deviation will be recorded with its date, description, reason and expected impact.

The initial exploratory data analysis was completed before this modelling-stage plan was documented. This is a retrospective plan for subsequent modelling, not prospective preregistration before the initial EDA.

Synthetic data will be used only for pipeline testing and will not be mixed with actual customer records.
