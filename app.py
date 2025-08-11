import streamlit as st
import random

# --- Configuration de la page ---
st.set_page_config(
    page_title="Mon Site Web",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Initialisation du score global ---
if "points" not in st.session_state:
    st.session_state.points = 0

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
st.write("Bonjour ! Je suis un jeune développeur passionné par Python et les jeux vidéos.\n"
         "Ce site vous permet de jouer en ligne à mes créations.\n"
         "Amusez-vous bien !!!!!! 🎉")

# --- Menu de navigation ---
menu = st.radio("🎮 Choisis une section :", ["Accueil", "Jeux externes", "Devine le nombre", "Pierre-Papier-Ciseaux", "Pendu"])
st.markdown(f"**💰 Score global : {st.session_state.points} points**")

# --- Accueil ---
if menu == "Accueil":
    name = st.text_input("Quel est votre nom ?")
    if name:
        st.success(f"Enchanté, {name} ! 😊")
    if st.button("Dire bonjour"):
        st.write("👋 Bonjour !")
    if st.button("Clique si tu aimes"):
        st.write("cool 😎")

# --- Jeux externes ---
elif menu == "Jeux externes":
    jeux = [
        {"titre": "cible", "desc": "A tu fais le meilleur score ? Tire vite.", "lien": "https://zmwguswsyytnolqexffdfj.streamlit.app/"},
        {"titre": "RPG", "desc": "Tuez le !", "lien": "https://je7erdurjykggnaagdzyzt.streamlit.app/"},
        {"titre": "Quiz", "desc": "Répondez !!!", "lien": "https://hyu2irxjzdthppfbix6duf.streamlit.app/"},
        {"titre": "Dé", "desc": "Faites un plus grand nombre", "lien": "https://essaie-2-hcaltzcmtgndkwfuei7snk.streamlit.app/"},
        {"titre": "Morpions", "desc": "Jouez contre une IA", "lien": "https://essaie-p44xbuapphmrcwqw65nys44.streamlit.app/"}
    ]
    for j in jeux:
        st.subheader(j["titre"])
        st.write(j["desc"])
        st.markdown(f"[Voir le jeu]({j['lien']})")

# --- Devine le nombre ---
elif menu == "Devine le nombre":
    if "secret" not in st.session_state:
        st.session_state.secret = random.randint(1, 20)
        st.session_state.essais = 0
    guess = st.number_input("Entrez un nombre entre 1 et 20", min_value=1, max_value=20, step=1)
    if st.button("Vérifier"):
        st.session_state.essais += 1
        if guess == st.session_state.secret:
            st.success(f"Bravo ! 🎉 Trouvé en {st.session_state.essais} essais.")
            st.session_state.points += 5
            st.session_state.secret = random.randint(1, 20)
            st.session_state.essais = 0
        elif guess < st.session_state.secret:
            st.info("C'est plus grand !")
        else:
            st.info("C'est plus petit !")

# --- Pierre-Papier-Ciseaux ---
elif menu == "Pierre-Papier-Ciseaux":
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
            st.session_state.points += 2
        else:
            st.error("Perdu 😢")

# --- Pendu ---
elif menu == "Pendu":
    mots_possibles = ["python", "famille", "ordinateur", "jeu", "tom", "arcade", "chat", "pizza", "robot"]
    if "mot_secret" not in st.session_state:
        st.session_state.mot_secret = random.choice(mots_possibles)
    mot_secret = st.session_state.mot_secret
    pendu_etapes = [
        "+---+\n    |\n    |\n    |\n   ===",
        "+---+\nO   |\n    |\n    |\n   ===",
        "+---+\nO   |\n|   |\n    |\n   ===",
        "+---+\nO   |\n/|  |\n    |\n   ===",
        "+---+\nO   |\n/|\\ |\n    |\n   ===",
        "+---+\nO   |\n/|\\ |\n/   |\n   ===",
        "+---+\nO   |\n/|\\ |\n/ \\ |\n   ==="
    ]
    if "lettres_trouvees" not in st.session_state:
        st.session_state.lettres_trouvees = []
    if "erreurs" not in st.session_state:
        st.session_state.erreurs = 0

    mot_affiche = " ".join([l if l in st.session_state.lettres_trouvees else "_" for l in mot_secret])
    st.write(f"Mot à deviner : **{mot_affiche}**")
    st.code(pendu_etapes[st.session_state.erreurs])

    lettre = st.text_input("Proposez une lettre :", max_chars=1).lower()
    if st.button("Proposer la lettre"):
        if lettre and lettre.isalpha():
            if lettre in mot_secret and lettre not in st.session_state.lettres_trouvees:
                st.session_state.lettres_trouvees.append(lettre)
                st.success(f"✅ La lettre **{lettre}** est dans le mot !")
            elif lettre not in mot_secret:
                st.session_state.erreurs += 1
                st.error(f"❌ La lettre **{lettre}** n'est pas dans le mot.")
            else:
                st.warning(f"⚠️ La lettre **{lettre}** a déjà été proposée.")
        else:
            st.warning("⚠️ Entrez une seule lettre valide.")

    if "_" not in mot_affiche:
        st.balloons()
        st.success(f"🎉 Bravo ! Tu as trouvé le mot **{mot_secret}** !")
        st.session_state.points += 3
        st.session_state.mot_secret = random.choice(mots_possibles)
        st.session_state.lettres_trouvees = []
        st.session_state.erreurs = 0

    if st.session_state.erreurs >= len(pendu_etapes) - 1:
        st.error(f"💀 Pendu ! Le mot était **{mot_secret}**.")
        st.session_state.mot_secret = random.choice(mots_possibles)
        st.session_state.lettres_trouvees = []
        st.session_state.erreurs = 0
