#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Importing the required Libraries
import streamlit as st
import pickle

#Loading the Model
model=pickle.load(open('Model.pkl','rb'))


def run():

    st.title("BANKING LOAN APPROVAL PREDICTION WEB APP")

    #Account Number
    account_no=st.text_input("**Account Number:**", )
    
    #Name
    name=st.text_input("**Name:**",  )
    
    #1.For gender
    gender = ('Female','Male')
    gen_options=list(range(len(gender)))
    gen=st.selectbox("**Gender**",gen_options, format_func=lambda x:gender[x])
    
    #2.For Marriage
    marriage = ('No','Yes')
    marriage_options=list(range(len(marriage)))
    mar=st.selectbox("**Marriage**",marriage_options, format_func=lambda x:marriage[x])
    
    #3.For Dependents
    dependents = ('No','One','Two','More than two ')
    dep_options=list(range(len(dependents)))
    dep=st.selectbox("**Dependents**",dep_options, format_func=lambda x:dependents[x])
    
    #4.For Education
    education = ('Not Graduate','Graduate')
    edu_options=list(range(len(gender)))
    edu=st.selectbox("**Education**",edu_options, format_func=lambda x:education[x])
    
    #5.For Employment
    employment=('Job','Business')
    emp_options=list(range(len(employment)))
    emp=st.selectbox("**Employment**",emp_options,format_func=lambda x:employment[x])
    
    #6.Applicant Monthly Income
    mon_income = st.number_input("**Applicant's Monthly Income ($)**", value=0)
    
    #7.Co-AppLicant Monthly. Income
    comon_income = st.number_input("**Co-Applicant's Monthly Income ($)**", value=0)
    
    #8.Loan Amount
    Loan_amt = st.number_input("**Loan Amount**", value=0)
    
    #9.Loan duration
    dur_display =['2 Month', '6 Month', '8 Month', '1 Year','16 Month']
    dur_options = range(len(dur_display))
    dur=st.selectbox("**Loan Duration**",dur_options, format_func=lambda x:dur_display[x])
    
    #10.Credit 
    credit_disp=('Between 300 to 500','More than 500')
    credit_options=list(range(len(credit_disp)))
    credit=st.selectbox("**Credit**",credit_options,format_func=lambda x:credit_disp[x])
        
    #11.Property
    property_disp=('Rural','Semi-Urban','Urban')
    prop_options=list(range(len(property_disp)))
    prop=st.selectbox("**Property**",prop_options, format_func=lambda x:property_disp[x])
    
    
    
    if st.button("Submit"):
        duration=0 
        if dur==0: 
            duration=60
        if dur==1:
            duration=180
        if dur==2:
            duration=240
        if dur==3:
            duration=360
        if dur==4:
            duration=480
        
        features=[[gen,mar,dep,edu,emp,mon_income,comon_income,Loan_amt,dur,credit,prop]]
        print(features)
        prediction=model.predict(features)
        l = [str(i) for i in prediction]
        ans=float(" ".join(l))
        
        
        if ans == 0:
            st.error(
                " Hello Customer : " + name + "//"
                "having Account Number:" + account_no + "//"
                "According to our Calculation." 
                "We deeply regret to inform you that your Loan will not get Approved !!"
                    ) 
        else: 
            st.success(" Hello Customer : " + name + "//" " with Account Holder no:" + account_no + "//"
                "According to our Calculation. Your Loan Will get Approved!!." 
                      )

run()                



















