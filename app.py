import streamlit as st
import random

# --- Configuration de la page ---
st.set_page_config(
    page_title="Mon Site Web",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Initialisation du score global et inventaire ---
if "points" not in st.session_state:
    st.session_state.points = 0
if "inventaire" not in st.session_state:
    st.session_state.inventaire = []

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
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="title">Bienvenue sur mon site de jeux en ligne ✨</div>', unsafe_allow_html=True)
st.write("Bonjour ! Je suis un jeune développeur passionné par Python et les jeux vidéos.\n"
         "Ce site vous permet de jouer en ligne à mes créations.\n"
         "Amusez-vous bien !!!!!! 🎉")

# --- Menu de navigation ---
menu = st.radio(
    "🎮 Choisis une section :",
    ["Accueil", "Jeux externes", "Devine le nombre", "Pierre-Papier-Ciseaux", "Pendu", "Boutique"]
)
st.markdown(f"**💰 Score global : {st.session_state.points} points**")

# --- Fonction pour calculer bonus de points ---
def bonus_points():
    return 1 if "🎩 Chapeau magique" in st.session_state.inventaire else 0

# --- Fonction pour effets de victoire ---
def effets_victoire():
    if "🐶 Animal virtuel" in st.session_state.inventaire:
        st.image("https://place-puppy.com/200x200", caption="Votre fidèle compagnon 🐶")
    if "🚀 Fusée miniature" in st.session_state.inventaire:
        st.balloons()

# --- Accueil ---
if menu == "Accueil":
    name = st.text_input("Quel est votre nom ?")
    if name:
        st.success(f"Enchanté, {name} ! 😊")

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
            gain = 5 + bonus_points()
            st.session_state.points += gain
            st.success(f"🎉 Bravo ! Trouvé en {st.session_state.essais} essais (+{gain} points)")
            effets_victoire()
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
            gain = 2 + bonus_points()
            st.session_state.points += gain
            st.success(f"🎉 Gagné ! (+{gain} points)")
            effets_victoire()
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
        gain = 3 + bonus_points()
        st.session_state.points += gain
        st.success(f"🎉 Bravo ! Tu as trouvé le mot **{mot_secret}** (+{gain} points)")
        effets_victoire()
        st.session_state.mot_secret = random.choice(mots_possibles)
        st.session_state.lettres_trouvees = []
        st.session_state.erreurs = 0

    if st.session_state.erreurs >= len(pendu_etapes) - 1:
        st.error(f"💀 Pendu ! Le mot était **{mot_secret}**.")
        st.session_state.mot_secret = random.choice(mots_possibles)
        st.session_state.lettres_trouvees = []
        st.session_state.erreurs = 0

# --- Boutique ---
elif menu == "Boutique":
    st.header("🛒 Boutique des récompenses")
    st.write(f"💰 Vous avez actuellement **{st.session_state.points} points**.")

    # Articles disponibles
    articles = [
        {"nom": "🎩 Chapeau magique", "prix": 10, "desc": "Augmente vos gains de points de 1 à chaque victoire."},
        {"nom": "🐶 Animal virtuel", "prix": 15, "desc": "Fait apparaître un chien mignon après chaque victoire."},
        {"nom": "🚀 Fusée miniature", "prix": 20, "desc": "Montre une animation de ballons après vos victoires."},
        {"nom": "💎 Gemme rare", "prix": 50, "desc": "Objet de collection prestigieux."}
    ]

    # Inventaire
    st.subheader("🎁 Inventaire")
    if st.session_state.inventaire:
        for item in st.session_state.inventaire:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(item)
            with col2:
                prix_revente = next(a["prix"] for a in articles if a["nom"] == item) // 2
                if st.button(f"Revendre {item}", key=f"sell_{item}"):
                    st.session_state.points += prix_revente
                    st.session_state.inventaire.remove(item)
                    st.success(f"💸 Vous avez revendu {item} pour {prix_revente} points.")
    else:
        st.write("Aucun article pour l'instant.")

    st.markdown("---")

    # Liste à acheter
    st.subheader("🛍️ Articles disponibles")
    for article in articles:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{article['nom']}** - {article['prix']} points")
            st.caption(article["desc"])
        with col2:
            if st.button(f"Acheter {article['nom']}", key=f"buy_{article['nom']}"):
                if st.session_state.points >= article["prix"]:
                    st.session_state.points -= article["prix"]
                    st.session_state.inventaire.append(article["nom"])
                    st.success(f"✅ Vous avez acheté {article['nom']} !")
                    if article["nom"] == "🎩 Chapeau magique":
                        st.balloons()
                    elif article["nom"] == "🐶 Animal virtuel":
                        st.image("https://place-puppy.com/200x200", caption="Votre nouveau compagnon 🐶")
                    elif article["nom"] == "🚀 Fusée miniature":
                        st.balloons()
                    elif article["nom"] == "💎 Gemme rare":
                        st.success("💎 Vous possédez maintenant un trésor rare.")
                else:
                    st.error("❌ Pas assez de points.")
