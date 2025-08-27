import streamlit as st

# --- CONFIGURATION GLOBALE ---
st.set_page_config(page_title="Portfolio - Ingénieur Logiciel", layout="wide")

# --- MENU LATERAL ---
pages = ["🏠 Accueil", "👨‍💻 Profil Technique", "🛠️ Stack & Compétences", "📊 Réalisations", "📬 Contact", "📄 Télécharger mon CV"]
choice = st.sidebar.radio("Navigation", pages)

# --- PAGES ---
if choice == "🏠 Accueil":
    st.title("🚀 Portfolio - Ingénieur en Génie Logiciel")
    st.write("""
    Développeur **Full-Stack** (Django, PHP) et Data Engineer débutant,  
    avec une expertise en **Business Intelligence** et en **Linux Systems**.
    """)

elif choice == "👨‍💻 Profil Technique":
    st.header("Profil Technique")
    st.write("""
    - Conception et développement d’applications **Web** avec Django (Python) et PHP.  
    - Déploiement et administration sur systèmes **Linux (Ubuntu, Kali Linux)**.  
    - Intégration de modèles d’**IA légère** pour la prévision et l’analyse décisionnelle.  
    """)

elif choice == "🛠️ Stack & Compétences":
    st.header("Stack & Compétences")
    st.subheader("Langages de programmation")
    st.write("Python | PHP | JavaScript | SQL")

    st.subheader("Frameworks & Outils")
    st.write("Django | Streamlit | Flask | Bootstrap")

    st.subheader("Data & IA")
    st.write("Pandas | Scikit-learn | Prophet | Visualisation (Matplotlib, Seaborn)")

    st.subheader("DevOps & Systèmes")
    st.write("Linux (Ubuntu, Kali) | Docker | Git | CI/CD")

elif choice == "📊 Réalisations":
    st.header("Réalisations (Projects)")

    # Projet 1 - Django / PHP
    st.subheader("🌐 Plateforme Web (Django / PHP)")
    st.write("""
    Développement d’une application web robuste avec :
    - Authentification sécurisée (OAuth2 Google/Facebook)
    - Gestion utilisateurs et base de données relationnelle
    - Déploiement sur serveur Linux
    """)

    if st.button("Voir captures - Django / PHP"):
        st.image("assets/django_project1.png", caption="Page login", use_column_width=True)
        st.image("assets/django_project2.png", caption="Dashboard admin", use_column_width=True)

    # Projet 2 - PharmaInsight
    st.subheader("💊 PharmaInsight (Streamlit + Python)")
    st.write("""
    Tableau de bord analytique pour la parapharmacie Pharmavie :
    - Prévisions de ventes
    - Recommandation de produits
    - Détection automatique de ruptures de stock
    - Identification des produits phares
    """)

    if st.button("Voir captures - PharmaInsight"):
        st.image("assets/pharmainsight1.png", caption="Dashboard accueil", use_column_width=True)
        st.image("assets/pharmainsight2.png", caption="Graphiques ventes", use_column_width=True)

elif choice == "📬 Contact":
    st.header("Contact Professionnel")
    st.write("📧 Email : ton.email@exemple.com")
    st.write("💼 LinkedIn : [linkedin.com/in/tonprofil](https://linkedin.com)")
    st.write("🐙 GitHub : [github.com/tonprofil](https://github.com)")

elif choice == "📄 Télécharger mon CV":
    st.header("Télécharger mon CV")
    with open("assets/cv.pdf", "rb") as pdf_file:
        st.download_button(
            label="📄 Télécharger mon CV",
            data=pdf_file,
            file_name="CV_Oumaima.pdf",
            mime="application/pdf"
        )
