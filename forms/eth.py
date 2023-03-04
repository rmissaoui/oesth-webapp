import streamlit as st
from streamlit_option_menu import option_menu

from utils.utils import table_lines
from utils.utils import table_cases
from utils.utils import rectangle_with_text
from utils.utils import thematic_titles
from utils.utils import section_titles
from utils.utils import sub_section_titles
from utils.utils import val_int
# from utils.utils import display_colomn
# from utils.utils import pourcentage_column
from utils.utils import display_table
from utils.utils import display_sum



def eth(placeholder) :
    placeholder.empty()

    selected = option_menu(
        menu_title=None,
        ### AJOUTER PREAMBULE
        options=["Sommaire", "0.Identité", "1.Emplois", "2.Sous-traitance", "3.Données économiques", "3.bis.Fréquentation", "4.Indicateurs financiers", "Taxes et impôts", "Environnement", "Validation"],
        icons = ["bookmarks", "person-lines-fill", "briefcase-fill", "diagram-3-fill", "graph-up-arrow", "people-fill", "speedometer2", "file-earmark-text", "tree-fill", "bookmark-check-fill"],
        orientation = "horizontal",
        styles = {
        "nav-link" : {"font-size" : "13px"}
        }
    )
    if selected == "0.Identité" :
        st.markdown("""<h1 style='text-align: center; font-size:15px; color:#FFC000'>Il vous est demandé de vérifier les données présentées dans cet onglet et de compléter les données si besoin. <br/>
                    Merci de veiller également à renseigner vos coordonnées.  
                    </h1>""", unsafe_allow_html=True
        )

        placeholder = st.empty()
        with placeholder.form("formulaire"):
            # RAISON SOCIALE DE L'EXPLOITANT
            st.subheader("RAISON SOCIALE DE L'EXPLOITANT")
            st.text_input("", label_visibility="collapsed", key="raison sociale")
            st.markdown('#')

            # STATION THERMALE DE :
            st.subheader("STATION THERMALE DE :")
            st.selectbox("", options=["Aix-les-Bains", "Allevard-les-Bains", "Amélie-les-Bains-Palalda", "Amnéville-les-Thermes", "Argelès-Gazost"], label_visibility="collapsed", key="ville")
            with st.expander("Autre (si ne figure pas dans la liste déroulante) : "):
                comment = st.text_area("", placeholder="", key = "Station_thermale_de/autre")
            st.markdown('#')

            # FORME JURIDIQUE
            st.subheader("FORME JURIDIQUE :")
            st.selectbox("", ["S.A.", "S.A.S.", "S.A.R.L", "S.N.C.", "S.E.M.", "S.P.L.", "Association", "Régie"], label_visibility="collapsed", key="forme_juridique")
            st.markdown("###### *Si Régie, préciser :*")
            st.markdown('####')

            st.markdown("###### *1/ Le niveau géographique :* ")
            st.selectbox("Régie municipale :", ["VRAI", "FAUX", "NA"], key="FORME JURIDIQUE/1/régie municipale")
            st.selectbox("Régie intercommunale :", ["VRAI", "FAUX", "NA"], key="FORME JURIDIQUE/1/régie intercommunale")
            st.selectbox("Régie départementale :", ["VRAI", "FAUX", "NA"], key="FORME JURIDIQUE/1/régie départementale")
            st.selectbox("Régie régionale :", ["VRAI", "FAUX", "NA"], key="FORME JURIDIQUE/1/régie régionale")
            st.markdown('####')

            st.markdown("###### *2/ Le type de régie :* ")
            st.selectbox("Régie dotée de la seule autonomie financière :", ["VRAI", "FAUX", "NA"], key="FORME JURIDIQUE/2/seule autonomie financière")
            st.selectbox("Régie dotée de la personnalité morale et de l’autonomie financière :", ["VRAI", "FAUX", "NA"], key="FORME JURIDIQUE/2/régie personnalié morale")
            st.markdown('####')

            st.markdown("###### *3/ L'existence de prestation de service :* ")
            st.selectbox("Régie avec prestation de service :", ["VRAI", "FAUX", "NA"], key="FORME JURIDIQUE/3/avec prestation service")
            st.selectbox("Régie sans prestation de service :", ["VRAI", "FAUX", "NA"], key="FORME JURIDIQUE/3/sans prestation service")
            st.markdown('#')
            
            # MODE DE GESTION
            st.subheader("MODE DE GESTION")
            st.radio("", ["Gestion directe", "Concession", "Affermage", "Crédit-bail", "BEA", "Gérance", "Autre :"], horizontal=False, label_visibility="collapsed",key = "MODE DE GESTION")
            with st.expander("Si autre, préciser : "):
                comment = st.text_area("", placeholder="", key = "Mode_de_gestion/autre")
            st.markdown('#')

            # NOM(S) DE (DES) L'ETABLISSEMENT(S)
            st.subheader("NOM(S) DE (DES) L'ETABLISSEMENT(S)")
            st.text_input("", label_visibility="collapsed", key="NOM(S) DE (DES) L'ETABLISSEMENT(S)/1")
            st.text_input("", label_visibility="collapsed", key="NOM(S) DE (DES) L'ETABLISSEMENT(S)/2")
            st.text_input("", label_visibility="collapsed", key="NOM(S) DE (DES) L'ETABLISSEMENT(S)/3")
            st.text_input("", label_visibility="collapsed", key="NOM(S) DE (DES) L'ETABLISSEMENT(S)/4")
            st.text_input("", label_visibility="collapsed", key="NOM(S) DE (DES) L'ETABLISSEMENT(S)/5")

            with st.expander("Si plus de 5 établissements thermaux sont gérés par la même entité juridique \
                                dans la station, lister les autres établissements ensemble en cliquant sur cette case : "):
                comment = st.text_area("", placeholder="", key = "NOM(S) DE (DES) L'ETABLISSEMENT(S)/autre")
            st.markdown('#')

            # NOMS DES AUTRES STRUCTURES GEREES PAR LA MEME ENTITE JURIDIQUE (dans la station thermale)
            ##### COMMENT SULIGNER UN SUBHEADER ??? 
            st.subheader("NOMS DES AUTRES STRUCTURES GEREES PAR LA MEME ENTITE JURIDIQUE (dans la station thermale)")
            
            c1, c2 = st.columns((8,2))
            with c1 :
                st.text_input("", label_visibility="collapsed", key="NOMS DES AUTRES STRUCTURES GEREES PAR LA MEME ENTITE JURIDIQUE (dans la station thermale)/1")
                st.text_input("", label_visibility="collapsed", key="NOMS DES AUTRES STRUCTURES GEREES PAR LA MEME ENTITE JURIDIQUE (dans la station thermale)/2")
                st.text_input("", label_visibility="collapsed", key="NOMS DES AUTRES STRUCTURES GEREES PAR LA MEME ENTITE JURIDIQUE (dans la station thermale)/3")
                st.text_input("", label_visibility="collapsed", key="NOMS DES AUTRES STRUCTURES GEREES PAR LA MEME ENTITE JURIDIQUE (dans la station thermale)/4")
                st.text_input("", label_visibility="collapsed", key="NOMS DES AUTRES STRUCTURES GEREES PAR LA MEME ENTITE JURIDIQUE (dans la station thermale)/5")

            with c2:
                text = "Ex : centres thermoludiques, hébergements, restauration, etc., si le statut juridique \
                est différent de l'établissement thermal, sinon intégrer ces activités à celles de l'établessement thermal"
                background = "#ECECEC"
                st.markdown(rectangle_with_text(265, text, color="#FFFFFF", background=background, font_size=12, padding=18, border=1))
            
            with st.expander("Si plus de 5 établissements (non thermaux) sont gérés par la même entité juridique \
                                dans la station, lister les autres établissements ensemble en cliquant sur cette case : "):
                comment = st.text_area("", placeholder="", key = "NOMS DES AUTRES STRUCTURES GEREES PAR LA MEME ENTITE JURIDIQUE (dans la station thermale)/autre")
            st.markdown('#')

            # NOMS DES AUTRES STRUCTURES GEREES PAR LA MEME ENTITE JURIDIQUE (implantées hors de la station thermale)
            st.subheader("NOMS DES AUTRES STRUCTURES GEREES PAR LA MEME ENTITE JURIDIQUE (implantées hors de la station thermale)")
            st.markdown("""
                *Veuillez indiquer les codes postaux des établissements en question :*

                *Listez les autres établissements ensemble dans la case ci-dessous en indiquant leurs codes postaux*
            """)
            st.text_input("", label_visibility="collapsed", key="NOMS DES AUTRES STRUCTURES GEREES PAR LA MEME ENTITE JURIDIQUE (implantées hors de la station thermale)")
            st.markdown('#')

            # APPARTENANCE A UN GROUPE
            st.subheader("APPARTENANCE A UN GROUPE")
            st.radio("", ["OUI", "NON"], horizontal=False, label_visibility="collapsed",key = "APPARTENANCE A UN GROUPE")
            with st.expander("Si oui, préciser : ") :
                comment = st.text_area("", placeholder="", key = "APPARTENANCE A UN GROUPE/autre")
            st.markdown('#')

            # COORDONNEES
            st.subheader("COORDONNEES")
            c1, c2 = st.columns((8,2))
            with c1 :
                st.text_input("Nom de la personne qui remplit ce questionnaire : ", label_visibility="visible", key="COORDONNEES/Nom de la personne qui remplit ce questionnaire")
                st.text_input("Fonction de la personne qui remplit ce questionnaire : ", label_visibility="visible", key="COORDONNEES/Fonction de la personne qui remplit ce questionnaire")
                st.text_input("Téléphone : ", label_visibility="visible", key="COORDONNEES/Téléphone")
                st.text_input("Mail : ", value=st.session_state["Mail"], label_visibility="visible", disabled=True, key="COORDONNEES/Mail")

            # POUR LE MAIL ON L A DEJA  DONC PAS BESOIN ?

            with c2 :
                ##### AJOUTER NOM PERSONNEL
                text = "Pour rappel : si vous avez déjà répondu lors de la précédente édition, le nom de la personne qui  \
                avait rempli le formulaire est le suivant : AJOUTER NOM"
                background = "#ECECEC"
                st.markdown(rectangle_with_text(340, text, color="#FFFFFF", background=background, font_size=12, padding=18, border=1))
            
            # submitted = st.form_submit_button("Enregistrer")






    if selected == "1.Emplois" :
        thematic_titles(40, "1/ EMPLOIS")

        st.write("""<p style="font-size:14px; color:black;">
        <i>Cette section concerne les emplois relatifs à l'ensemble de l'entité juridique, <b>au sein de la station </b> (i.e. les établissements thermaux + les spas, hôtels-restaurants, résidences, etc., si applicable).
        Les établissements et structures implantés en dehors de la station thermale de référence ne sont pas inclus dans le périmètre d'étude</i></p>  
        """,
        unsafe_allow_html=True) 

        text = "1.1. NOMBRE D'EMPLOIS"
        section_titles(30, text)

        text = "1.1.1. TEMPS PLEIN"
        sub_section_titles(30, text)

        st.write("""<div style="font-size:18px; color:#51698F;">
        <b>/ CDD</b> </div>
        <div><i>Veuillez inclure les CDII.</i></div>
        """,
        unsafe_allow_html=True) 
        
        

        # Merged columns
        c1, c2, c3, c4, c5, c6, c7, c8 = st.columns((2, 2, 0.5, 2, 0.5, 2, 0.5, 3))
        
        # 22
        with c2 :
            text = "Sur l'année 2022"
            rectangle_with_text(40, text, color="FFFFFF", background="009999", font_size=11, padding=8, border=1)
        # 21
        with c4 :
            text = "Sur l'année 2021"
            rectangle_with_text(40, text, color="000000", background="fbe4d5", font_size=11, padding=8, border=1)
        # evolution
        with c6 :
            text = "Evolution 2021 - 2022"
            rectangle_with_text(40, text, color="000000", background="A6A6A6", font_size=11, padding=8, border=1)


        # Sous-colonnes

        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, colo11 = st.columns((2, 1, 1, 0.5, 1, 1, 0.5, 1, 1, 0.5, 3))
        # Blank space
        with c1:
            rectangle_with_text(60, "", color="FFFFFF", background="FFFFFF", font_size=11, padding=8, border=0)
        # 22
        with c2:
            text = "Saisonniers"
            rectangle_with_text(60, text, color="FFFFFF", background="009999", font_size=11, padding=8, border=1)
        
        with c3:
            text = "Non saisonniers"
            rectangle_with_text(60, text, color="FFFFFF", background="009999", font_size=11, padding=8, border=1)
        
        # 21
        with c5:
            text = "Saisonniers"
            rectangle_with_text(60, text, color="000000", background="fbe4d5", font_size=11, padding=8, border=1)
        with c6:
            text = "Non saisonniers"
            rectangle_with_text(60, text, color="000000", background="fbe4d5", font_size=11, padding=8, border=1)
        
        # evolution
        with c8:
            text = "Saisonniers"
            rectangle_with_text(60, text, color="000000", background="A6A6A6", font_size=11, padding=8, border=1)
        with c9:
            text = "Non saisonniers"
            rectangle_with_text(60, text, color="000000", background="A6A6A6", font_size=11, padding=8, border=1)

        ## commentaire   
        with colo11: 
            text = """Commentaires : <br>
            Si vous procédez à des modifications dans les onglets 2021, veuillez en expliquer la raison ici : 
            """
            rectangle_with_text(60, text, color="OOOOO", background="fbe4d5", font_size=10, padding=6, border=0)
            # st.text_input("", label_visibility="collapsed", key="2.1.1 comm 1")
            st.text_area("", label_visibility="collapsed",  placeholder="", key = "2.1.1 comm 1", height=12)
        

        # Lignes du tableau
        line_names = ["Personnes physiques", "ETP (Equivalent Temps Plein)"]
        
        saiso_22_keys = ["22_saiso_Pers", "22_saiso_ETS"]
        non_saiso_22_keys = ["22_non_saiso_Pers", "22_non_saiso_ETS"]
        
        saiso_21_keys = ["21_saiso_Pers", "21_saiso_ETS"]
        non_saiso_21_keys = ["21_non_saiso_Pers", "21_non_saiso_ETS"]
        
        columns_widths = (2, 1, 1, 0.5, 1, 1, 0.5, 1, 1, 0.5, 3)
        dict = {1:["line_name", line_names], 2:["int_2022",saiso_22_keys], 3:["int_2022", non_saiso_22_keys], 5:["int_2021", saiso_21_keys], 6:["int_2021", non_saiso_21_keys], 8:["evol", saiso_22_keys, saiso_21_keys], 9:["evol", non_saiso_22_keys, non_saiso_21_keys]}
        

        display_table(dict, (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, colo11), columns_widths, values_2022={}, values_2021={}, height_size="small")


        # Intérim
    
    
    if selected == "2.Sous-traitance":
        # 2/ SOUS-TRAITANCE / FOURNISSEURS* / PRESTATAIRES
        section_titles(40, "2/ SOUS-TRAITANCE / FOURNISSEURS* / PRESTATAIRES")
        st.write("""
        <p style="font-size:14px; color:black;">
        <i>* Tâche donnée en délégation à un tiers, contrat de fourniture ou de prestation qui permet à l'exploitant de réaliser son 
        activité (exemples : entretien/maintenance, ménage, communication, etc.) </i> </p>
        """,
        # 2.1 MONTANTS DES PRESTATIONS SOUS-TRAITEES ET DES ACHATS (en € HT)
        unsafe_allow_html=True)

        sub_section_titles(30, "2.1 MONTANTS DES PRESTATIONS SOUS-TRAITEES ET DES ACHATS (en € HT)")
        st.write("""
        <p style="font-size:14px; color:black;">
        <i>Remarque : Le montant total des marchés contractualisés est très important pour mesurer les impacts économiques indirects
          du thermalisme </i> </p>
        """,
        unsafe_allow_html=True)
        

        # Merged columns
        c1, c2, c3, c4, c5, c6, c7, c8 = st.columns((3, 4.5, 1.5, 1, 0.5, 1, 0.5, 2))
        
        # 22
        with c2 :
            text = "Dépense supportée par l'entité juridique dans son ensemble au sein de la station thermale (en € HT) en 2019"
            rectangle_with_text(45, text, color="FFFFFF", background="009999", font_size=11, padding=8, border=1)

        # Sous-colonnes
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10 = st.columns((3, 1.5, 1.5, 1.5, 1.5, 1, 0.5, 1, 0.5, 2))

        # Blank space
        with c1:
            rectangle_with_text(90, "", color="FFFFFF", background="FFFFFF", font_size=10, padding=3, border=0)
        # 22
        with c2:
            text = "Montant de l'ensemble des marchés contractualisés sur le périmètre de la commune"
            rectangle_with_text(90, text, color="FFFFFF", background="009999", font_size=10, padding=3, border=1)
        
        with c3:
            text = "Montant de l'ensemble des marchés contractualisés sur le périmètre régional"
            rectangle_with_text(90, text, color="FFFFFF", background="009999", font_size=10, padding=3, border=1)
        
        with c4:
            text = "Montant de l'ensemble des marchés contractualisés hors du périmètre régional"
            rectangle_with_text(90, text, color="FFFFFF", background="009999", font_size=10, padding=3, border=1)

        with c5:
            text = "Dépense supportée par le groupe pour le compte de l'entité juridique (en € HT) en 2019"
            rectangle_with_text(90, text, color="FFFFFF", background="009999", font_size=10, padding=3, border=1)
        with c6:
            text = "TOTAL 2022"
            rectangle_with_text(90, text, color="000000", background="A6A6A6", font_size=10, padding=3, border=1)

        ## evolution
        with c8:
            text = "Evolution 2021 - 2022"
            rectangle_with_text(90, text, color="000000", background="A6A6A6", font_size=10, padding=3, border=1)
        ## commentaire    
        with c10:
            text = "Commentaires"
            rectangle_with_text(90, text, color="OOOOO", background="fbe4d5", font_size=11, padding=6, border=0)
            # st.text_input("", label_visibility="collapsed", key="2.1.1 comm 1")
            st.text_area("", label_visibility="collapsed",  placeholder="", key = "2.1.1 comm 1", height=12)
        

        # Lignes du tableau
        line_names = ["Eau (matière première)", "Boues (matière première)", "Equipements de soin", "Accessoires et produits de soins", "Linge / blanchisserie",
                       "Ménage" , "Jardinage", "Sécurité", "Denrées alimentaires (agriculture locale***)", "Denrées alimentaires (autre)", 
                       "Communication", "Comptabilité", "Juridique et assurance", "Fournitures et mobilier", "Entretien / maintenance", 
                       "Réparations / gros œuvre", "Autre (préciser : .................)"]

        commune_keys = ["commune_key" + str(k) for k in range(len(line_names))]
        region_keys = ["region_key" + str(k) for k in range(len(line_names))]
        hors_region_keys = ["hors_region_key" + str(k) for k in range(len(line_names))]
        entit_jur_keys = ["entit_jur_key" + str(k) for k in range(len(line_names))]
        
        dict = {1:["line_name", line_names], 2:["float",commune_keys], 3:["float", region_keys], 4:["float", hors_region_keys], 5:["float", entit_jur_keys], 6:["tot", commune_keys, region_keys, hors_region_keys, entit_jur_keys]}
        columns_widths = (3, 1.5, 1.5, 1.5, 1.5, 1, 0.5, 1, 0.5, 2)
        display_table(dict, (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10), columns_widths=columns_widths, values_2022={}, values_2021={}, height_size="small")
        
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10 = st.columns((3, 1.5, 1.5, 1.5, 1.5, 1, 0.5, 1, 0.5, 2))
        with c1:
            text = "TOTAL"
            st.markdown("<div style='height:40px; color:#000000; background-color:#A6A6A6; display:flex; align-items:center; justify-content:right; text-align: right; font-size:13px; padding:8px; border: 1px solid #000000;'>{}</div>".format(text), unsafe_allow_html=True)
            text = "*** Producteur situé à < 50 km de la station thermale)"
            st.markdown("<div style='height:40px; color:#000000; background-color:#FFFFFF; display:flex; align-items:center; justify-content:center; text-align: left; font-size:11px; padding:3px; '>{}</div>".format(text), unsafe_allow_html=True)
        with c2:
            display_sum(commune_keys, "commune")  
        with c3:
            display_sum(region_keys, "region") 
        with c4:
            display_sum(hors_region_keys, "hors_region")
        with c5:
            display_sum(entit_jur_keys, "entit_jur_keys")
        with c6:
            display_sum(["tot_commune", "tot_region", "tot_hors_region", "tot_entit_jur_keys"], "tot_tot")
        with c8:
            table_cases("besoin donnée 2021", font_size=8, color="000000", background_color="d9d9d9")    