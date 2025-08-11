import streamlit as st
import random

# --- Page config ---
st.set_page_config(
    page_title="Mon Site Web",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------
# INITIALISATIONS SESSION
# ---------------------------
if "points" not in st.session_state:
    st.session_state.points = 0
if "inventaire" not in st.session_state:
    st.session_state.inventaire = []
if "achievements" not in st.session_state:
    st.session_state.achievements = set()
if "pet" not in st.session_state:
    st.session_state.pet = "none"
if "pet_xp" not in st.session_state:
    st.session_state.pet_xp = 0
if "secret_unlocked" not in st.session_state:
    st.session_state.secret_unlocked = False
if "total_wins" not in st.session_state:
    st.session_state.total_wins = 0
if "consecutive_wins" not in st.session_state:
    st.session_state.consecutive_wins = 0

# ---------------------------
# FONCTIONS UTILITAIRES
# ---------------------------
def award_points(points_gain=0, reason=None):
    """Ajoute des points globaux, gère bonus et succès."""
    bonus = 0
    if "🎩 Chapeau magique" in st.session_state.inventaire:
        bonus += 1
    total_points = points_gain + bonus
    st.session_state.points += total_points

    if reason:
        st.success(f"+{total_points} points ({reason})")

    # succès liés aux victoires
    if points_gain > 0:
        st.session_state.total_wins += 1
        st.session_state.consecutive_wins += 1
    else:
        st.session_state.consecutive_wins = 0

    if st.session_state.total_wins >= 5:
        st.session_state.achievements.add("Vainqueur x5")
    if st.session_state.consecutive_wins >= 3:
        st.session_state.achievements.add("Série de 3 victoires")

    # progression de l'animal
    if st.session_state.pet != "none":
        st.session_state.pet_xp += points_gain
        evolve_pet_if_needed()

    # déblocage mini-jeu secret
    if st.session_state.points >= 100:
        st.session_state.secret_unlocked = True

def evolve_pet_if_needed():
    """Fait évoluer l'animal virtuel selon ses points gagnés."""
    if st.session_state.pet == "egg" and st.session_state.pet_xp >= 10:
        st.session_state.pet = "puppy"
        st.success("🐣 Ton oeuf a éclos en chiot !")
        st.session_state.achievements.add("Naissance du compagnon")
    elif st.session_state.pet == "puppy" and st.session_state.pet_xp >= 30:
        st.session_state.pet = "adult"
        st.success("🐶 Ton chiot est devenu adulte !")
        st.session_state.achievements.add("Compagnon adulte")
    elif st.session_state.pet == "adult" and st.session_state.pet_xp >= 100:
        st.session_state.pet = "legend"
        st.success("👑 Ton compagnon est devenu légendaire !")
        st.session_state.achievements.add("Compagnon légendaire")

def show_pet_area():
    """Affiche l'animal virtuel et interactions."""
    st.subheader("🐾 Ton animal virtuel")
    visuals = {
        "none": "Pas encore d'animal. Achète-le dans la boutique !",
        "egg": "🥚 (oeuf)",
        "puppy": "🐶 (chiot)",
        "adult": "🐕 (adulte)",
        "legend": "🐕‍🦺✨ (légendaire)"
    }
    st.write(f"Statut : **{visuals.get(st.session_state.pet)}**")
    st.write(f"Points gagnés par le compagnon : {st.session_state.pet_xp}")

    if st.session_state.pet != "none":
        if st.button("Caresser (+1 point compagnon)"):
            st.session_state.pet_xp += 1
            evolve_pet_if_needed()
            st.success("❤️ Ton compagnon est content !")
        if st.button("Donner une friandise (+3 points compagnon)"):
            st.session_state.pet_xp += 3
            evolve_pet_if_needed()
            st.success("🍖 Ton compagnon adore ça !")

# ---------------------------
# MENU
# ---------------------------
menu_items = ["Accueil", "Jeux externes", "Devine le nombre", "Pierre-Papier-Ciseaux", "Pendu", "Boutique", "Animal", "Succès"]
if st.session_state.secret_unlocked:
    menu_items.append("Mini-jeu secret")

menu = st.radio("🎮 Choisis une section :", menu_items)
st.markdown(f"**💰 Points : {st.session_state.points}**")

# ---------------------------
# ACCUEIL
# ---------------------------
if menu == "Accueil":
    st.markdown("<h1 style='text-align:center'>Bienvenue sur mon site de jeux ✨</h1>", unsafe_allow_html=True)
    name = st.text_input("Quel est votre nom ?")
    if name:
        st.success(f"Enchanté, {name} ! 😊")
    st.write("Amuse-toi, gagne des points, débloque le mini-jeu secret et fais évoluer ton animal !")

# ---------------------------
# JEUX EXTERNES
# ---------------------------
elif menu == "Jeux externes":
    st.header("🎮 Mes jeux externes")
    jeux = [
        {"titre": "cible", "desc": "As-tu le meilleur score ?", "lien": "https://zmwguswsyytnolqexffdfj.streamlit.app/"},
        {"titre": "RPG", "desc": "Combattez les monstres !", "lien": "https://je7erdurjykggnaagdzyzt.streamlit.app/"},
        {"titre": "Quiz", "desc": "Répondez aux questions", "lien": "https://hyu2irxjzdthppfbix6duf.streamlit.app/"},
        {"titre": "Dé", "desc": "Faites un grand total", "lien": "https://essaie-2-hcaltzcmtgndkwfuei7snk.streamlit.app/"},
        {"titre": "Morpion", "desc": "Jouez contre une IA", "lien": "https://essaie-p44xbuapphmrcwqw65nys44.streamlit.app/"}
    ]
    for j in jeux:
        st.subheader(j["titre"])
        st.write(j["desc"])
        st.markdown(f"[Voir le jeu]({j['lien']})")

# ---------------------------
# DEVINE LE NOMBRE
# ---------------------------
elif menu == "Devine le nombre":
    st.header("🎲 Devine le nombre")
    if "secret" not in st.session_state:
        st.session_state.secret = random.randint(1, 20)
    guess = st.number_input("Entrez un nombre entre 1 et 20", min_value=1, max_value=20, step=1)
    if st.button("Vérifier"):
        if guess == st.session_state.secret:
            award_points(5, "Devine le nombre gagné")
            st.session_state.secret = random.randint(1, 20)
        elif guess < st.session_state.secret:
            st.info("C'est plus grand !")
        else:
            st.info("C'est plus petit !")

# ---------------------------
# PIERRE-PAPIER-CISEAUX
# ---------------------------
elif menu == "Pierre-Papier-Ciseaux":
    st.header("✂️ Pierre-Papier-Ciseaux")
    choix = st.radio("Faites votre choix :", ["Pierre", "Papier", "Ciseaux"])
    if st.button("Jouer"):
        bot = random.choice(["Pierre", "Papier", "Ciseaux"])
        st.write(f"L'ordinateur a choisi : {bot}")
        if choix == bot:
            st.info("Égalité ! 🤝")
        elif (choix == "Pierre" and bot == "Ciseaux") or \
             (choix == "Papier" and bot == "Pierre") or \
             (choix == "Ciseaux" and bot == "Papier"):
            award_points(2, "Chifoumi gagné")
        else:
            st.error("Perdu 😢")

# ---------------------------
# PENDU
# ---------------------------
elif menu == "Pendu":
    st.header("🪢 Pendu amélioré")
    mots_possibles = ["python", "famille", "ordinateur", "jeu", "tom", "arcade", "chat", "pizza", "robot", "streamlit"]
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

    lettre = st.text_input("Proposez une lettre :", max_chars=1)
    if st.button("Proposer la lettre"):
        l = lettre.lower()
        if l and l.isalpha():
            if l in mot_secret and l not in st.session_state.lettres_trouvees:
                st.session_state.lettres_trouvees.append(l)
                st.success(f"✅ La lettre **{l}** est dans le mot !")
            elif l not in mot_secret:
                st.session_state.erreurs += 1
                st.error(f"❌ La lettre **{l}** n'est pas dans le mot.")
            else:
                st.warning(f"⚠️ La lettre **{l}** a déjà été proposée.")
        else:
            st.warning("⚠️ Entrez une seule lettre valide.")

    if "_" not in mot_affiche:
        award_points(3, "Pendu gagné")
        st.session_state.mot_secret = random.choice(mots_possibles)
        st.session_state.lettres_trouvees = []
        st.session_state.erreurs = 0

    if st.session_state.erreurs >= len(pendu_etapes) - 1:
        st.error(f"💀 Pendu ! Le mot était **{mot_secret}**.")
        st.session_state.mot_secret = random.choice(mots_possibles)
        st.session_state.lettres_trouvees = []
        st.session_state.erreurs = 0

# ---------------------------
# BOUTIQUE
# ---------------------------
elif menu == "Boutique":
    st.header("🛒 Boutique")
    st.write(f"Points disponibles : **{st.session_state.points}**")
    articles = [
        {"nom": "🎩 Chapeau magique", "prix": 10, "desc": "Donne +1 point par victoire."},
        {"nom": "🐶 Animal virtuel", "prix": 15, "desc": "Obtient un compagnon évolutif."},
        {"nom": "🚀 Fusée miniature", "prix": 20, "desc": "Effet visuel lors des victoires."},
        {"nom": "💎 Gemme rare", "prix": 50, "desc": "Objet de collection prestigieux."}
    ]

    if st.session_state.inventaire:
        st.subheader("Inventaire")
        for item in list(st.session_state.inventaire):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(item)
            with col2:
                if st.button(f"Revendre {item}", key=f"sell_{item}"):
                    prix_rev = next(a["prix"] for a in articles if a["nom"] == item) // 2
                    st.session_state.points += prix_rev
                    st.session_state.inventaire.remove(item)
                    st.success(f"Revendu {item} pour {prix_rev} points.")
                    if item == "🐶 Animal virtuel":
                        st.session_state.pet = "none"
                        st.session_state.pet_xp = 0

    st.markdown("---")
    st.subheader("Acheter")
    for article in articles:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{article['nom']}** - {article['prix']} pts")
            st.caption(article["desc"])
        with col2:
            if st.button(f"Acheter {article['nom']}", key=f"buy_{article['nom']}"):
                if st.session_state.points >= article["prix"]:
                    if article["nom"] in st.session_state.inventaire:
                        st.warning("Déjà acheté.")
                    else:
                        st.session_state.points -= article["prix"]
                        st.session_state.inventaire.append(article["nom"])
                        st.success(f"Acheté {article['nom']} !")
                        if article["nom"] == "🐶 Animal virtuel":
                            st.session_state.pet = "egg"
                            st.session_state.pet_xp = 0
                            st.success("🐣 Tu as reçu un œuf !")
                        if article["nom"] == "🚀 Fusée miniature":
                            st.balloons()
                else:
                    st.error("Pas assez de points.")

# ---------------------------
# ANIMAL
# ---------------------------
elif menu == "Animal":
    st.header("🐶 Animal virtuel")
    show_pet_area()

# ---------------------------
# SUCCÈS
# ---------------------------
elif menu == "Succès":
    st.header("🏆 Succès débloqués")
    if st.session_state.achievements:
        for a in sorted(st.session_state.achievements):
            st.write("•", a)
    else:
        st.write("Aucun succès débloqué.")

# ---------------------------
# MINI-JEU SECRET
# ---------------------------
elif menu == "Mini-jeu secret":
    st.header("🔒 Mini-jeu secret : Trouve le trésor")
    st.write("Tu as 6 essais pour trouver le trésor caché (4x4).")
    width, height = 4, 4
    if "treasure_pos" not in st.session_state:
        st.session_state.treasure_pos = (random.randint(0, width-1), random.randint(0, height-1))
        st.session_state.treasure_attempts = 6
        st.session_state.treasure_found = False

    st.write(f"Essais restants : {st.session_state.treasure_attempts}")
    x = st.slider("Choisis X", 0, width-1, 0)
    y = st.slider("Choisis Y", 0, height-1, 0)
    if st.button("Creuser"):
        if (x, y) == st.session_state.treasure_pos:
            award_points(20, "Trésor trouvé")
            st.session_state.treasure_found = True
            st.success("💎 Tu as trouvé le trésor !")
        else:
            st.session_state.treasure_attempts -= 1
            st.warning("Rien ici...")
            if st.session_state.treasure_attempts <= 0:
                st.error(f"Fin des essais ! Le trésor était en {st.session_state.treasure_pos}")
    if st.button("Recommencer la chasse"):
        st.session_state.treasure_pos = (random.randint(0, width-1), random.randint(0, height-1))
        st.session_state.treasure_attempts = 6
        st.session_state.treasure_found = False
