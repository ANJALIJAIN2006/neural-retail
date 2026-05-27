def churn_score(tenure, monthly_charges):
    score = (monthly_charges / 1000) - (tenure / 100)

    if score > 1:
        return "High Risk"
    else:
        return "Low Risk"