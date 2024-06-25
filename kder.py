import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Set page config with a new icon related to IT
st.set_page_config(page_title="Kader Belem", page_icon="💻", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/d4b66f91-c56e-4055-8ab3-c74f425fcf51/w8r6sCmQyU.json")
lottie_web_dev = load_lottieurl("https://lottie.host/f0baeaa2-40b1-4638-8911-85ef66e3336b/c7GYPkIOlK.json")  # Web Development
lottie_marketing = load_lottieurl("https://lottie.host/4bde2a2e-2590-4583-8038-7650c6e836e4/pjp9A6QeRy.json")  # Marketing
lottie_business_dev = load_lottieurl("https://lottie.host/d0218bcf-ea2f-44d0-9c56-f7c52d4ecbed/5rzSlHpzTR.json")  # Business Development

# Check if animations loaded correctly
if lottie_coding is None:
    st.error("Failed to load coding animation.")
if lottie_web_dev is None:
    st.error("Failed to load web development animation.")
if lottie_marketing is None:
    st.error("Failed to load marketing animation.")
if lottie_business_dev is None:
    st.error("Failed to load business development animation.")

img_contact_form = Image.open("images/calculatrice.png")
img_lottie_animation = Image.open("images/librairie.png")
img_third_image = Image.open("images/jdv.png")  # Load the third image

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hello, Je suis Kader Belem 💻")
    st.title("Etudiant,")
    st.write(
        """
        Je m’appelle Kader Belem, j’ai 19 ans, et j’habite à Saint-Nazaire. 
        Après avoir obtenu mon baccalauréat professionnel en Système Numérique
        avec une option en Audio-Visuel, Réseau et Équipement Domestique, et
        avoir été accepté au lycée La Colinière à Nantes, je suis actuellement
        étudiant en première année de BTS SIO (Services Informatiques aux
        Organisations).
        """
    )
    st.write("[Plus d'informations >][Linkedin >](https://www.linkedin.com/in/vicky-percy-63a666209?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)")

# ---- COMPETENCES ACQUISES ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Compétences acquises")
        st.write("##")
        st.write(
            """
            Compétences acquises:
            - Travailler en mode projet
            - Analyser les objectifs et les modalités d’organisation d’un projet.
            - Planifier les activités. 
            - Évaluer les indicateurs de suivi d’un projet et analyser les écarts.
            - Organiser son développement professionnel.
            - Mettre en place son environnement d’apprentissage personnel.
            _ Mettre en œuvre des outils et stratégies de veille informationnelle.
            - Gérer son identité professionnelle  Développer son projet professionne. 

            
            """
        )
        st.write("[Linkedin >](https://www.linkedin.com/in/kader-belem-688699213/)")
    with right_column:
        if lottie_coding:
            st_lottie(lottie_coding, height=300, key="coding")

# ---- CE QUE JE FAIS ----
with st.container():
    st.write("---")
    st.header("Veille informatique")
    st.write("##")
    st.write(
        """
        Sujet de veille informatique:
        - Les enjeux de la cybersécurité en 2024.
        - L'intelligence artificielle et l'automatisation.
        - Blockchain et ses applications.
        - Le développement durable dans le secteur IT.
        """
    )
    left_column, right_column = st.columns(2)
    with left_column:
        if lottie_web_dev:
            st_lottie(lottie_web_dev, height=300, key="web_dev")
    with right_column:
        if lottie_marketing:
            st_lottie(lottie_marketing, height=300, key="marketing")

# ---- MES PROJETS ----
with st.container():
    st.write("---")
    st.header("Mes Projets")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Gestionnaire de librairie")
        st.write(
            """
            Ce projet consiste en la création d'une application de gestion de bibliothèque utilisant Python et une interface graphique.
            L'application permet aux utilisateurs de gérer les livres, les emprunts, et les retours de manière efficace.
            Le projet se concentre sur la création d'une interface utilisateur intuitive et facile à utiliser
            """
        )
        st.markdown("[Local URL:...](http://localhost:8501/)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Projet de calculatrice")
        st.write(
            """
            Ce projet consiste en la création d'une calculatrice graphique utilisant la bibliothèque Tkinter en Python.
            La calculatrice permet de réaliser des opérations arithmétiques de base telles que l'addition, la soustraction,
            la multiplication et la division. Le projet se concentre sur la création d'une interface utilisateur intuitive et esthétique.
            """
        )
        st.markdown("[Local URL...](http://localhost:8502/)")

# ---- THIRD IMAGE SECTION ----
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_third_image)  # Display the third image
    with text_column:
        st.subheader("Jeux de voiture")
        st.write(
            """
            Ce projet consiste en la création d'un jeu vidéo utilisant la bibliothèque Pygame en Python.
            Le jeu propose une interface interactive où les utilisateurs peuvent interagir avec des éléments graphiques et audio.
            Le projet se concentre sur la création d'une expérience de jeu engageante avec des graphismes attrayants et une jouabilité fluide..
            """
        )
        st.markdown("[Local URL...](http://localhost:8503/)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Contactez-moi!")
    st.write("##")

    # Documentation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/mickaelvp8@GMAIL.COM" method="POST">
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
        if lottie_business_dev:
            st_lottie(lottie_business_dev, height=300, key="business_dev")
