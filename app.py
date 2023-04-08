import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
from emplyr_pages.post_add import post_add, post_submit
from emplyr_pages.view_jobs import display_view_posts
from emplyr_pages.home import display_home
from emplyr_pages.apply_for_jobs import apply_display_view_posts
from yaml.loader import SafeLoader
import yaml
import json

with open('./creds.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def load_from_json(fname):
    f = open(fname)
    a = json.load(f)
    f.close()
    return a

#-----------------------------------------------------------------------------------------------------------
#LOGO CODE
st.set_page_config(page_title="21dolloars.com.au")
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<div class="navbar-logo">
<nav class="navbar fixed-top navbar-expand-lg navbar-dark">
  <a class="navbar-brand" href="#">
    <img src="https://i.ibb.co/HVjwQkg/cover-better.png" alt="Logo" width="255.6" height="35" align="center">
  </a>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav ml-auto">
      <!-- Remove all list items -->
    </ul>
  </div>
</nav>
</div>
""", unsafe_allow_html=True)
hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

#----------------------------------------------------------------------------------------------------------------

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)


st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

local_css("design.css")

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    MENU = option_menu(None, ["Home", "Apply for Job", "View Jobs", 'Settings'],
                       icons=['house', 'cloud-upload', "list-task", 'gear'],
                       menu_icon="cast", default_index=0, orientation="horizontal")
    # -------------------------------------------------------------------------------------------------------------------------------
    if MENU == "New Job":
        post_job_object = post_add()
        if post_job_object[1]:
            post_submit(post_job_object[0],post_job_object[2])

    if MENU == "View Jobs":
        st.header("Jobs Applied")
        a = load_from_json("applied.json")
        display_view_posts(a)
        st.balloons()

    if MENU=="Apply for Job":
        st.header("Open Jobs")
        a = load_from_json("posts.json")
        apply_display_view_posts(a)
        st.balloons()

    if MENU == "Home":
        display_home(name)

    if MENU == "Settings":
        st.header("Settings")
        a,b,c,d=st.columns(4)
        e,f,g,h= st.columns(4)
        with a:
            authenticator.logout('Logout', 'main')
        with b:
            st.button("Settings")
        with c:
            st.button("Profile")
        with d:
            st.button("Go Pro+")
        with e:
            st.button("Contact Us")
        with f:
             st.button("T&c")

#--------------------------------------------------------------------------------------------------------------------------------#
elif authentication_status is False:
    st.error('Username or password is incorrect')

elif authentication_status is None:
    st.warning('Please enter your username and password')