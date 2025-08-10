import streamlit as st
import random

st.set_page_config(page_title="Mon Site Web", page_icon="🌐")

# --- Page config ---
st.set_page_config(
    page_title="Mon Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS ---
st.markdown("""
    <style>
    body {
        background-color: #f4f4f4;
    }
    .title {
        font-size: 48px;
        color: #4B8BBE;
        text-align: center;
        margin-bottom: 30px;
    }
    .subtitle {
        font-size: 24px;
        color: #333;
        text-align: center;
        margin-bottom: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="title">Bienvenue sur mon site de jeux en ligne ✨</div>', unsafe_allow_html=True)
st.write("""
Bonjour ! Je suis un jeune développeur passionné par Python et les jeux vidéos.

Ce site vous permet de jouer en ligne à mes créations

Amusez vous bien !!!!!! 🎉
""")
st.markdown("---")

# --- Nom utilisateur ---
name = st.text_input("Quel est votre nom ?")
if name:
    st.success(f"Enchanté, {name} ! 😊")

st.markdown("---")
st.subheader("Quelques boutons :")
if st.button("Dire bonjour"):
    st.write("👋 Bonjour !")
if st.button("Clique si tu aimes"):
    st.write("cool 😎")

# --- Section Jeux existants ---
st.header("🎮 Mes jeux externes")
jeux = [
    {"titre": "Petit et Grand", "desc": "A tu fais le meilleure score ? mange le vite.", "lien": "https://replit.com/@tom77puls/totogame?v=1"},
    {"titre": "Cliquer dessus", "desc": "Touchez-le !", "lien": "https://replit.com/@tom77puls/WonderfulAltruisticBinary?v=1"},
]
for j in jeux:
    st.subheader(j["titre"])
    st.write(j["desc"])
    st.markdown(f"[Voir le jeu]({j['lien']})")

# --- Mini-jeux Python intégrés ---
st.markdown("---")
st.header("🕹️ Mini-jeux en Python directement ici")

# 1️⃣ Devine le nombre
st.subheader("🎲 Devine le nombre")
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 20)
guess = st.number_input("Entrez un nombre entre 1 et 20", min_value=1, max_value=20, step=1)
if st.button("Vérifier"):
    if guess == st.session_state.secret:
        st.success("Bravo ! 🎉 Vous avez trouvé le nombre !")
        st.session_state.secret = random.randint(1, 20)
    elif guess < st.session_state.secret:
        st.info("C'est plus grand !")
    else:
        st.info("C'est plus petit !")

# 2️⃣ Pierre-Papier-Ciseaux
st.subheader("✂️ Pierre-Papier-Ciseaux")
choix = st.radio("Faites votre choix :", ["Pierre", "Papier", "Ciseaux"])
if st.button("Jouer"):
    bot = random.choice(["Pierre", "Papier", "Ciseaux"])
    st.write(f"L'ordinateur a choisi : {bot}")
    if choix == bot:
        st.info("Égalité ! 🤝")
    elif (choix == "Pierre" and bot == "Ciseaux") or \
         (choix == "Papier" and bot == "Pierre") or \
         (choix == "Ciseaux" and bot == "Papier"):
        st.success("Gagné ! 🎉")
    else:
        st.error("Perdu 😢")

# 3️⃣ Pendu
st.subheader("🪢 Jeu du pendu")
mot_secret = "python"
if "lettres_trouvees" not in st.session_state:
    st.session_state.lettres_trouvees = []
lettre = st.text_input("Proposez une lettre :").lower()
if st.button("Proposer"):
    if lettre and lettre not in st.session_state.lettres_trouvees:
        st.session_state.lettres_trouvees.append(lettre)
mot_affiche = " ".join([l if l in st.session_state.lettres_trouvees else "_" for l in mot_secret])
st.write(f"Mot à deviner : {mot_affiche}")
if "_" not in mot_affiche:
    st.success("Bravo ! Vous avez trouvé le mot 🎉")

