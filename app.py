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
    {"titre": "cible", "desc": "A tu fais le meilleure score ? tire vite.", "lien": "https://zmwguswsyytnolqexffdfj.streamlit.app/"},
    {"titre": "RPG", "desc": "Tuez le !", "lien": "https://je7erdurjykggnaagdzyzt.streamlit.app/"},
    {"titre": "Quiz", "desc": "répondez !!!", "lien": "https://hyu2irxjzdthppfbix6duf.streamlit.app/"},
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
st.subheader("🪢 Jeu du pendu amélioré")

import random

# Liste de mots possibles
mots_possibles = ["python", "famille", "ordinateur", "jeu", "tom", "arcade", "chat", "pizza", "robot"]

# Initialiser le mot secret UNE seule fois
if "mot_secret" not in st.session_state:
    st.session_state.mot_secret = random.choice(mots_possibles)

mot_secret = st.session_state.mot_secret

# Dessins ASCII du pendu
pendu_etapes = [
    """
      +---+
          |
          |
          |
         ===""",
    """
      +---+
      O   |
          |
          |
         ===""",
    """
      +---+
      O   |
      |   |
          |
         ===""",
    """
      +---+
      O   |
     /|   |
          |
         ===""",
    """
      +---+
      O   |
     /|\\  |
          |
         ===""",
    """
      +---+
      O   |
     /|\\  |
     /    |
         ===""",
    """
      +---+
      O   |
     /|\\  |
     / \\  |
         ==="""
]

# Initialisation
if "lettres_trouvees" not in st.session_state:
    st.session_state.lettres_trouvees = []
if "erreurs" not in st.session_state:
    st.session_state.erreurs = 0

# Affichage mot
mot_affiche = " ".join([l if l in st.session_state.lettres_trouvees else "_" for l in mot_secret])
st.write(f"Mot à deviner : **{mot_affiche}**")

# Affichage dessin pendu
st.code(pendu_etapes[st.session_state.erreurs])

# Lettres déjà proposées
lettres_proposees = " ".join(sorted(st.session_state.lettres_trouvees))
st.write(f"📜 Lettres trouvées : {lettres_proposees if lettres_proposees else 'Aucune'}")

# Proposition de lettre
lettre = st.text_input("Proposez une lettre :", max_chars=1).lower()

if st.button("Proposer la lettre") and not st.session_state.erreurs >= len(pendu_etapes) - 1:
    if lettre and lettre.isalpha():
        if lettre in mot_secret and lettre not in st.session_state.lettres_trouvees:
            st.session_state.lettres_trouvees.append(lettre)
            st.success(f"✅ Bien joué, la lettre **{lettre}** est dans le mot !")
        elif lettre not in mot_secret:
            st.session_state.erreurs += 1
            st.error(f"❌ La lettre **{lettre}** n'est pas dans le mot.")
        else:
            st.warning(f"⚠️ La lettre **{lettre}** a déjà été proposée.")
    else:
        st.warning("⚠️ Entrez une seule lettre valide.")

# Victoire
if "_" not in mot_affiche:
    st.balloons()
    st.success(f"🎉 Bravo ! Tu as trouvé le mot **{mot_secret}** !")
    st.session_state.mot_secret = random.choice(mots_possibles)
    st.session_state.lettres_trouvees = []
    st.session_state.erreurs = 0

# Défaite
if st.session_state.erreurs >= len(pendu_etapes) - 1:
    st.error(f"💀 Pendu ! Le mot était **{mot_secret}**.")
    st.session_state.mot_secret = random.choice(mots_possibles)  # Nouveau mot
    st.session_state.lettres_trouvees = []
    st.session_state.erreurs = 0
