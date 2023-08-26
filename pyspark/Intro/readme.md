- Task:
  Split the dataset into 2
    dataset 1: Loan_ID, Loan Amount, Loan_Amount_Term, Loan_Status
            p: 0, 8, 9, 12
    dataset 2: Loan_ID,Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,Credit_History,Property_Area
  -         p: 0,1,2,3,4,5,6,7,10, 11

intro.py -> read dataset [ ] and create two separate dataset loan_data and personal data