import streamlit as st

# Menu principal
st.sidebar.title("Menu Principal")
menu = st.sidebar.radio("Naviguer vers", ["CV", "Projet"])

# ---------------- CV Section ----------------
if menu == "CV":
    st.title("CV Interactif - Yacine KHELIFA")
    
    # Sous-sections du CV
    page_cv = st.sidebar.radio("CV Sections", ["Accueil", "Expériences", "Compétences", "Formations", "Contact"])
    
    if page_cv == "Accueil":
        st.header("Bienvenue sur mon CV interactif")
        st.subheader("Lettre de Motivation")
        st.write("""
        **Objet** : Candidature au poste de Data Analyst
        
        Madame, Monsieur,
        
        Passionné par l’analyse de données et diplômé d’une formation spécialisée chez Datascientest.com, 
        je maîtrise des outils comme Python, SQL et Power BI, que j’ai utilisés dans plusieurs projets 
        pour transformer des données complexes en insights exploitables. 
        
        Mon expérience en suivi de raccordement de la fibre optique m’a permis de développer 
        des tableaux de bord interactifs et des indicateurs clés de performance, améliorant la prise de décision 
        et la satisfaction client. 
        
        Rejoindre votre équipe serait une opportunité de mettre à profit mes compétences techniques et 
        humaines pour contribuer à vos projets innovants. Je suis convaincu que ma polyvalence et 
        ma capacité d’adaptation seront des atouts précieux pour votre organisation.
        
        Cordialement,  
        **Yacine KHELIFA**
        """)
    
    elif page_cv == "Expériences":
        st.header("Expériences Professionnelles")
        st.subheader("Reclaim Finance - Bénévole")
        st.write("- Recherche et collecte de données.")
        st.write("- Consolidation et traitement au format Excel.")
        st.subheader("Orange - Service Accueil Prestige")
        st.write("""- Analyse des données de déploiement de la fibre optique.  
        - Création de tableaux de bord interactifs.""")

    elif page_cv == "Compétences":
        st.header("Compétences Techniques")
        st.write("""
        - **Python** : Analyse et visualisation de données.  
        - **SQL** : Requêtes avancées pour bases relationnelles.  
        - **Power BI** : Tableaux de bord interactifs.  
        - **Machine Learning** : Modélisation et prédictions avec scikit-learn.
        """)

    elif page_cv == "Formations":
        st.header("Formations")
        st.write("""
        - **Data Analyst** - Datascientest.com (2024)  
        - **Licence en Langue et Cultures Amazighes** - Université Abderramane Mira
        """)

    elif page_cv == "Contact":
        st.header("Contact")
        st.write("- **Email** : [yacine.metal@hotmail.com](mailto:yacine.metal@hotmail.com)")
        st.write("- **LinkedIn** : [linkedin.com/in/yacine-khelifa](https://linkedin.com/in/yacine-khelifa)")
        st.write("- **GitHub** : [github.com/khelifaYacine](https://github.com/khelifaYacine)")

# ---------------- Project Section ----------------
elif menu == "Projet":
    st.title("Projet - Analyse du Bien-Être sur Terre")
    
    # Sous-menu pour les pages du projet
    pages = ["Exploration", "DataVizualisation", "Préprocessing", "Modélisation", "Interprétabilité"]
    page_projet = st.sidebar.radio("Pages Projet", pages)

    if page_projet == "Exploration":
        st.header("Exploration des Données")
        st.write("## Introduction")
        st.write("""
        Ce projet vise à analyser le World Happiness Report pour évaluer les facteurs influençant le bonheur des pays. 
        Les données incluent des indicateurs socio-économiques comme la santé, la corruption, l'économie et l'espérance de vie.
        """)
        # Exemple de visualisation ou affichage de données
        st.write("Affichage des premières lignes du dataset :")
        # Vérifiez que `df` est défini
        try:
            st.dataframe(df.head())
        except NameError:
            st.warning("Dataset introuvable. Assurez-vous que les données sont chargées.")
    
    elif page_projet == "DataVizualisation":
        st.header("Visualisations des Données")
        # Exemple d'histogramme
        st.write("### Distribution des scores de bonheur")
        # Ajoutez votre visualisation ici...
    
    elif page_projet == "Préprocessing":
        st.header("Préparation des Données")
        st.write("## Traitement des Valeurs Manquantes et Encodage")
        # Ajoutez les étapes de préprocessing ici...

    elif page_projet == "Modélisation":
        st.header("Modélisation")
        st.write("## Entraînement des Modèles")
        # Ajoutez votre code de modélisation ici...

    elif page_projet == "Interprétabilité":
        st.header("Interprétabilité des Modèles")
        st.write("## Importance des Caractéristiques")
        # Ajoutez les visualisations SHAP ou autres analyses ici...

# Footer
st.markdown("---")
st.markdown("© 2024 Yacine KHELIFA - CV Interactif construit avec Streamlit")
