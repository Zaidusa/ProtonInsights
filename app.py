import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="ProtonInsights", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----


lottie_coding1 = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_9ye8w8M9JF.json")
lottie_coding0 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_q5qvqtnr.json")
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/Corporate1.jpg")
img_lottie_animation = Image.open("images/Corporate2.jpg")

# ---- HEADER SECTION ----

with st.container():
    st.markdown("""
    <style>
    .big-font {
        font-size:100px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">@@@ Proton Insights</p>', unsafe_allow_html=True)
    left_column, right_column = st.columns(2)
    with right_column:
        st.header("---We Deliver what we Promise!!!")


    left_column,right_column = st.columns(2)
    with left_column:
        st_lottie(lottie_coding1, height=500, key="coding1")

    with right_column:
        st_lottie(lottie_coding0, height=600, key="coding0")



# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Us!")
    st.write("contactus: +9140-2444-3076")
    st.write("Address:Flat 705,Rajeev swagruha,Bandlaguda,Nagole,500062")
    st.write("Email:you_contactus@proton.me")

    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/you_contactus@proton.me" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
