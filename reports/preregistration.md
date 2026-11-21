# Analysis Preregistration

## 1. Research Question

Can customer financial characteristics and payment history help predict whether a customer will become delinquent?

## 2. Hypotheses

**Null Hypothesis (H0):** Customer financial characteristics and payment history have no significant relationship with customer delinquency.

**Alternative Hypothesis (H1):** Customer financial characteristics and payment history are associated with customer delinquency.

Expected direction: Customers with higher financial risk and poor payment history may have a higher likelihood of delinquency.

## 3. Population, Sample, and Exclusions

**Target Population:** Customers represented in the Geldium dataset.

**Unit of Analysis:** Individual customer.

**Inclusion Rules:**
- Include records containing valid customer information.
- Include records with valid delinquency target values (0 or 1).

**Exclusion Rules:**
- Remove duplicate customer records.
- Exclude records with invalid target values.
- Handle missing values during preprocessing.

**Stopping Rule:** Analysis will stop after the planned data cleaning, exploratory analysis, and model evaluation are completed.

## 4. Variables and Measures

**Outcome Variable:** Delinquent_Account.

**Predictor Variables:** Customer financial characteristics, employment status, and payment-related information available in the dataset.

**Data Transformations:**
- Remove duplicate records.
- Clean categorical values.
- Handle missing values.
- Remove invalid target values.

## 5. Analysis Plan

- Perform data cleaning and preprocessing.
- Conduct exploratory data analysis (EDA).
- Analyze relationships between customer characteristics and delinquency.
- Apply suitable classification models.
- Evaluate model performance using accuracy, precision, recall, and F1-score.
- Perform robustness checks where appropriate.

Significance level: 0.05 for applicable statistical tests.

## 6. Deviations

Any changes to the original analysis plan will be documented with the date, reason, and description of the change.