import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from streamlit_option_menu import option_menu  # Assure-toi que cette ligne est présente !

# Charger le fichier de configuration pour l'authentification
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Initialiser l'authentificateur
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# Afficher le message de bienvenue pour le login si l'utilisateur n'est pas encore authentifié
if 'authentication_status' not in st.session_state or not st.session_state['authentication_status']:
    st.write("**Bienvenue, pour te connecter le username est Flo et le password abc**")

# Barre latérale et gestion du login
authenticator.login()

if st.session_state['authentication_status']:
    authenticator.logout()  # Option de déconnexion
    st.title(f'Welcome *{st.session_state["name"]}*')
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')

# Créer le menu dans la barre latérale si l'utilisateur est authentifié
if st.session_state.get('authentication_status'):

    # Définir la sélection du menu dans la barre latérale
    with st.sidebar:
        selection = option_menu(
            menu_title="MENU",  # Titre du menu
            options=["Accueil", "Photos"],  # Options du menu
            icons=["house", "camera"],  # Icônes pour chaque option
            menu_icon="cast",  # Icône du menu
            default_index=0,  # Option par défaut
            orientation="vertical",  # Orientation verticale
        )

    # Affichage en fonction de la sélection du menu
    if selection == "Accueil":
        st.title("Bienvenue sur la page d'accueil !")
        st.image('Bienvenue.png')  # Affichage de l'image d'accueil

    elif selection == "Photos":
        st.title("Bienvenue sur mon album photo")

        # Créer 4 colonnes pour afficher les images
        col1, col2, col3, col4 = st.columns(4)

        # Afficher les images dans chaque colonne en utilisant use_container_width
        with col1:
            st.image('IMG_20220916_142739.jpg', use_container_width=True)
        with col2:
            st.image('IMG_20220923_144202.jpg', use_container_width=True)
        with col3:
            st.image('IMG_20221007_132848.jpg', use_container_width=True)
        with col4:
            st.image('IMG_20221125_204625.jpg', use_container_width=True)

else:
    st.warning('Veuillez vous connecter pour accéder au contenu.')