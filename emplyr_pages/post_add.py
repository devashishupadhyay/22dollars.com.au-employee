import streamlit as st
from datetime import date
import random
import json


def post_add():
    cont = st.empty()
    with cont.container():
        datePosted = str(date.today())
        hashJobId = random.randint(10000, 10000**2)
        st.header("Post a job add for free")
        form = st.form("my_form")
        JobTitle = form.text_input("Job Title")
        form.write("💡 Choose a title that best describes the job to appear in relevant searches. <br>E.g. Phone Sales Consultant", unsafe_allow_html=True)
        jobType = form.selectbox(
            'Job Type',
            ('Full Time', 'Part Time', 'Casual/Temporary', "Permanent"))
        visaSponsered = form.checkbox("Work visa can be sponsered")
        form.write(
            "💡 If you leave the checkbox unselected, “Working rights required for this role” will be shown in the job ad.")
        experience = form.radio(
            "Required work experience",
            ('No experience required', '1 year of experience', '2-3 years of experience', 'More than 4 years of experience'))
        form.write("💡 Selecting “More than 4 years of experience” will be shown as “More than 4 years of relevant work experience required for this role” in the job ad.")
        jobDesp = form.text_area("Job Description")
        submit = form.form_submit_button("Post")
        # if submit:
        data = {"hashJobId": hashJobId, "numApplicants": 0, "JobTitle": JobTitle, "jobType": jobType, "datePosted": datePosted, "visaSponsered": (
        visaSponsered == True and "Work visa can be sponsered") or "No sponsorship", "experience": experience, "jobDesp": jobDesp}
    return cont, submit,data


def post_submit(cont,data):
    cont = cont.empty()
    with cont.container():
        try:
            with open('posts.json','r') as lt:
                lst = json.load(lt)                
            lt.close()
            lst.append(data)
            with open('posts.json','w') as test:
                json.dump(lst,test)
                cont.write("Your new job has been posted successfully 😊")
        except:
            cont.write("Error on backend! Contact ADMIN.")

