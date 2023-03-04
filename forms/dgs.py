#  couleurs grands titres & decalage cases tableau
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from PIL import Image
import datetime

from utils.utils import currency_format, display_ecart_moyenne_2022, display_moyenne_2022, display_sum, display_sum_updated, display_table, display_table_2022, divide_2_keys, line_name, somme_2_keys, thematic_titles, val_float, val_modification, display_table_2021
from utils.utils import section_titles
from utils.utils import sub_section_titles
from utils.utils import table_cases
from utils.utils import table_lines
from utils.utils import rectangle_with_text
from utils.utils import isfloat



yesno_list = ["Oui", "Non", "NC", "NA", ""]


def dgs(placeholder) :
    placeholder.empty()
            
    selected = option_menu(
        menu_title=None,
        ### AJOUTER PREAMBULE
        options=["Préambule", "0.Identité", "1.Fiscalité", "2.Investissements", "3.Endettement", "4.Emplois et act.", "Taux de remplissage", "Enregistrement/Validation"],
        icons = ["bookmarks", "person-lines-fill", "briefcase-fill", "diagram-3-fill", "graph-up-arrow", "people-fill", "speedometer2"],
        orientation = "horizontal",
        styles = {
        "nav-link" : {"font-size" : "13px"}
        }
    )
   
    # Récuperer les données de la BDD
    ### Filtre selon entity_id, puis selon 
    reponses_2021 = pd.read_csv("data/reponses_2021_vittel.csv")
    reponses_2021.fillna("", inplace=True)
    # Filtre selon display_reponse_2021==True 
    reponses_2021_displayed = reponses_2021[reponses_2021["display_reponse_2021"]==True]
    # A MODIFIER DANS LA BASE FINALE
    reponses_2021_displayed.rename(columns={"raison_modification" : "raison_modification_2021"})

    # values_2021 et values_2022 contiennent ce que va voir l'utilisateur à l'ouverture du formulaire
    values_2021 = {}
    question_ids_2021 = reponses_2021_displayed["question_id"].values
    for question_id in question_ids_2021:
        question_tuple = reponses_2021_displayed[reponses_2021_displayed["question_id"]==question_id]
        values_2021[question_id + "_reponse_2021"] = question_tuple["reponse_2021"].values[0]

        if question_tuple["reponse_2021_updated"].values[0] != "":
            # values_2021[question_id + "_checkbox_modification_2021"] = True
            values_2021[question_id + "_reponse_2021_updated"] = question_tuple["reponse_2021_updated"]
            values_2021[question_id + "_raison_modification_2021"] = question_tuple["raison_modification_2021"]
            
        else:
            # values_2021[question_id + "_checkbox_modification_2021"] = False
            values_2021[question_id + "_reponse_2021_updated"] = ""
            values_2021[question_id + "_raison_modification_2021"] = ""

    # # Pour 2022 :
    values_2022 = {}
    values_2022[""] = ""
    question_ids_2022 = pd.read_csv("data/Formulaire_OESTh_DGS_2023_V1.csv", sep=";", encoding='iso-8859-1')["New ID"].values
    questions_ids_2022_inclus_taux = pd.read_csv("data/Formulaire_OESTh_DGS_2023_V1.csv", sep=";", encoding='iso-8859-1')[pd.read_csv("data/Formulaire_OESTh_DGS_2023_V1.csv", sep=";", encoding='iso-8859-1')["Inclus dans taux"]==True]["New ID"].values
    # Permet de gérer les ratios qui demandent des grandeurs d'autres onglets
    for key in question_ids_2022:
         if key+"_reponse_2022" not in st.session_state:
              st.session_state[key+"_reponse_2022"] = ""
    # for key in question_ids_2022:
    #      if key+"_reponse_2022" not in st.session_state:
    #         st.session_state[key+"_reponse_2022"] = ""
    # question_ids_2022 = []
    # for question_id in question_ids_2022:
    #     question_tuple = reponses_2022[reponses_2022["question_id"]==question_id]
    #     values_2022[question_id + "_reponse_2022"] = question_tuple["reponse_2022"].values[0]
    #     question_ind_calc_tuple = question_tuple.join(indic_calc_affiches ON question_id)
    #     if question_ind_calc_tuple[display_nombre_repondants_2022]==True:
    #           values_2022[question_id + "_nombre_repondants_2022"] = question_tuple["nombre_repondants_2022"].values[0]
    #     if question_ind_calc_tuple[display_moyenne_2022]==True:
    #           values_2022[question_id + "_moyenne_2022"] = question_ind_calc_tuple["moyenne_2022"].values[0]



    ### CES VALEURS SERONT ISSUES D UNE AUTRE SOURCE
    st.session_state["DGS_ID_nom"] = "Vittel"
    st.session_state["DGS_ID_INSEE"] = "88516"
    st.session_state["DGS_ID_Dept"] = "88"
    st.session_state["DGS_ID_Reg"] = "Grand Est"
    st.session_state["DGS_ID_Typo"] = "F2"
    st.session_state["DGS_ID_col"] = "Ville de Vittel"
    st.session_state["DGS_ID_EPCI"] = "Communauté de communes Terre d'Eau"
    
    

    if selected == "Préambule":
        for k, v in st.session_state.items():
            st.session_state[k] = v
        thematic_titles(40, "PREAMBULE")
        st.write("En attente de Fabien")

    if selected == "0.Identité" :
        # permet de garder les valeurs affichées quand on change d'onglet et qu'on revient sur l'onglet initial
        for k, v in st.session_state.items():
            st.session_state[k] = v
        thematic_titles(40, "0. IDENTITE")
        section_titles(40, "1/ PERIMETRE CONCERNE")

        # Tableau
        c1, c2, c3 = st.columns((3.5, 4, 4))
        line_names = ["Station thermale", "Code INSEE", "Département", "Région", "Catégorie de la typologie", "Collectivite de rattachement ", "EPCI concerné"]
        station_keys = ["DGS_ID_nom", "DGS_ID_INSEE", "DGS_ID_Dept", "DGS_ID_Reg", "DGS_ID_Typo", "DGS_ID_col", "DGS_ID_EPCI"]
        station_values = [st.session_state[key] for key in station_keys]

        dict = {1:["line_name", line_names], 2:["static_line", station_values] }
        columns_widths = (3.5, 4, 4)
        display_table(dict, (c1, c2, c3), columns_widths=columns_widths, values_2022= values_2022, values_2021=values_2021, height_size="small")

        # commentaire 
        with st.expander("*Commentaires :* "):
                comment = st.text_area("", placeholder="", key = "DGS_IN_Com_reponse_2022")    
        

        st.write("#")
        # 2/ IDENTITE DU REPONDANT
        section_titles(40, "2/ IDENTITE DU REPONDANT")

        columns_widths = (4, 3, 3, 3, 3) # table
        line_names = ["Nom de la personne qui remplit ce questionnaire :", "Fonction de la personne qui remplit ce questionnaire :", "Service / département de rattachement :", "Téléphone :", "Mail :"]
        questions_ids = ["DGS_ID_perso", "DGS_ID_fctpers", "DGC_ID_servpers", "DGS_ID_telpers", "DGS_ID_mailpers"]
        questions_values_types = [None] * 5
        display_booleans = [True] + [False]*4
        height_line = "small"
        display_table_2021(columns_widths, line_names, questions_ids, questions_values_types, display_booleans, None, height_line, values_2022, values_2021, )


    if selected == "1.Fiscalité":
        for k, v in st.session_state.items():
            st.session_state[k] = v
        thematic_titles(40, "1. FISCALITE")
        st.write("""<p style="font-size:14px; color:black;">
        Il vous est demandé de remplir les données fiscales à deux échelles : à l'échelle de la station thermale uniquement (lignes 13 à 37 <u>A MODIFIER</u>) et à l'échelle de l'EPCI (lignes 38 à 65 <u>A MODIFIER</u>))<br/></p>  
        """,
        unsafe_allow_html=True) 

        # 1.1. POPULATION ET SURCLASSEMENT
        section_titles(40, "1.1. POPULATION ET SURCLASSEMENT")

        # Population DGF et INSEE de la station
        text = st.session_state["DGS_ID_nom"]
        st.write("""<p style="font-size:14px; color:#51698F;"><b>/ Population DGF et INSEE de la station :  {}</b>
        </p>""".format(text), unsafe_allow_html=True) 
 
        columns_widths = (5.5, 1.5, 1.5, 1.5, 3) # table
        line_names = ["<b>Population INSEE de la commune (en nombre d'habitants) en 2022</b>", "<b>Population DGF de la commune (en nombre d'habitants) en 2022</b>"]
        questions_ids = ["DGS_FIS_pop_INSEE", "DGS_FIS_pop_DGF"]
        questions_values_types = ["float", "float"]
        display_booleans = [False, True]
        height_line = "small"
        display_table_2021(columns_widths, line_names, questions_ids, questions_values_types, display_booleans, None, height_line, values_2022, values_2021, )
        

        # Population INSEE de l'EPCI
        st.write('#')
        st.write("""<p style="font-size:14px; color:#51698F;">
        <b>/ Population INSEE de l'EPCI : </b> </p>  """, unsafe_allow_html=True) 
         
        columns_widths = (5.5, 1.5, 1.5, 1.5, 3) # table
        line_names = ["<b>Population INSEE de l'ensemble des communes de l'EPCI  (en nombre d'habitants) en 2022</b>", "Quelle est la source de la donnée \"population de l'ensemble des communes de l'EPCI\""]
        questions_ids = ["DGS_FIS_pop_EPCI", "DGS_FIS_pop_com"]
        questions_values_types = ["float", None]
        display_booleans = [True, False]
        height_line = "small"
        display_table_2021(columns_widths, line_names, questions_ids, questions_values_types, display_booleans, None, height_line, values_2022, values_2021, )


        # Surclassement de la station
        st.write('#')
        text = st.session_state["DGS_ID_nom"]
        st.write("""<p style="font-size:14px; color:#51698F;"><b>/ Surclassement de la station : {}</b>
        </p>  """.format(text), unsafe_allow_html=True) 

        columns_widths = (3, 3, 1, 3, 1) # table
        line_names = ["<b>Votre commune est-elle classée station de tourisme en 2022</b>", "<b>Si oui, votre commune est-elle surclassée dans une catégorie démographique supérieure ?</b>",
                      "<b> Si oui, depuis quand ? </b>(préciser l'année du surclassement). Si votre commune n'est pas surclassée, indiquer \"NA\".",
                      "<b>A quelle strate démographique votre commune est-elle rattachée en 2021 ?</b>"]
        questions_ids = ["DGS_SURC_com_classé", "DGS_SURC_surclassé", "DGS_SURC_date", "DGS_SURC_strate"]
        questions_values_types = ["select_box", "select_box", None, "select_box"]
        display_booleans = [True, True, True, True]
        height_line = "big"
        strates_communes_liste = ["", "Communes de moins de 100 habitants", "Communes de 100 à 199 habitants","Communes de 200 à 499 habitants","Communes de 500 à 1 999 habitants",
                                      "Communes de 2 000 à 3 499 habitants","Communes de 3 500 à 4 999 habitants","Communes de 5 000 à 9 999 habitants","Communes de 10 000 à 19 999 habitants",
                                      "Communes de 20 000 à 49 999 habitants","Communes de 50 000 à 99 999 habitants","Communes de plus de 100 000 habitant","NA", "NC"]
        lists_for_selectbox = [yesno_list, yesno_list, None, strates_communes_liste]
        display_table_2021(columns_widths, line_names, questions_ids, questions_values_types, display_booleans, lists_for_selectbox, height_line, values_2022, values_2021, )

        with st.expander("*Commentaires :* "): # commentaire 
                comment = st.text_area("", placeholder="", key = "DGS_FIS_Com_reponse_2022")

        

        st.write("#")
        # 1.2. TAXES LOCALES PERCUES AU NIVEAU DE LA STATION THERMALE
        section_titles(40, "1.2. TAXES LOCALES PERCUES AU NIVEAU DE LA STATION THERMALE")

        columns_widths = (5.5, 1.5, 1.5, 1.5, 3) # table
        line_names = ["Montant perçu au titre de la Cotisation Foncière des Entreprises (<b>CFE</b>)",
                      "Montant perçu au titre de la Cotisation sur la Valeur Ajoutée des Entreprises (<b>CVAE</b>)",
                      "Montant perçu au titre de la <b>taxe foncière sur les propriétés bâties/non bâties</b>",
                      "Montant perçu au titre de la taxe d'enlèvement des ordures ménagères (<b>TEOM</b>)",
                      "Montant perçu au titre de la taxe sur les surfaces commerciales (<b>TASCOM</b>)**",
                      "Montant perçu au titre de l'imposition forfaitaire des entreprises de réseaux (<b>IFER</b>)",
                      "Montant perçu au titre de la <b>taxe sur la consommation finale d'électricité</b>",
                      "Montant perçu au titre des <b>droits de mutation</b>",
                      "Montant perçu au titre du <b>versement transport</b>",
                      "Montant perçu au titre de la <b>taxe sur le produit des jeux</b>",
                      "Autres taxes perçues <b>hors taxe de séjour et taxe d'habitation</b>.Si non applicable, préciser 'NA'"]
        questions_ids = ["DGS_FIS_taxst_CFE", "DGS_FIS_taxst_CVAE", "DGS_FIS_taxst_TF", "DGS_FIS_taxst_TEOM", "DGS_FIS_taxst_TASCOM", "DGS_FIS_taxst_IFER", "DGS_FIS_taxst_elec", "DGS_FIS_taxst_mut", 
                         "DGS_FIS_taxst_trans", "DGS_FIS_taxst_PBJ", "DGS_FIS_taxst_au"]
        questions_values_types = ["currency"]*11
        display_booleans = [True]*11
        height_line = "small"
        display_table_2021(columns_widths, line_names, questions_ids, questions_values_types, display_booleans, lists_for_selectbox=None, height_size="small", values_2022=values_2022, values_2021=values_2021)

        c1, c2, c3, c4, c5 = st.columns((5.5, 1.5, 1.5, 1.5, 3))
        with c1:
            text = "TOTAL des taxes locales percues au niveau de la station thermale "
            st.markdown("<div style='height:40px; color:#000000; background-color:#A6A6A6; display:flex; align-items:center; justify-content:left; text-align: left; font-size:13px; padding:8px; border: 1px solid #000000;'>{}</div>".format(text), unsafe_allow_html=True)
            text = "<i>** Condition d'application de la taxe sur les surfaces commerciales (TASCOM) : surface de vente au détail > 400 m²</i>"
            st.markdown("<div style='height:40px; color:#000000; background-color:#FFFFFF; display:flex; align-items:center; justify-content:left; text-align: left; font-size:11px; padding:3px; '>{}</div>".format(text), unsafe_allow_html=True)
        with c2:
            display_sum([question_id+"_reponse_2022" for question_id in questions_ids], "DGS_FIS_taxst_TOTAL", currency=True)
        with c3:
            table_cases(currency_format(values_2021["DGS_FIS_taxst_TOTAL"+"_reponse_2021"]), font_size=14, color="000000", background_color="d9d9d9")
        with c4:
            questions_ids = ["DGS_FIS_taxst_CFE", "DGS_FIS_taxst_CVAE", "DGS_FIS_taxst_TF", "DGS_FIS_taxst_TEOM", "DGS_FIS_taxst_TASCOM", "DGS_FIS_taxst_IFER", "DGS_FIS_taxst_elec", "DGS_FIS_taxst_mut", 
                         "DGS_FIS_taxst_trans", "DGS_FIS_taxst_PBJ", "DGS_FIS_taxst_au"]
            display_sum_updated(questions_ids, "DGS_FIS_taxst_TOTAL_reponse_2021_updated", values_2021, currency=True)


        st.write("#")
        st.text_input("""Pouvez-vous préciser **les autres taxes taxes perçues hors taxe de séjour et taxe d'habitation** renseignés en case C55 ? Si non applicable, préciser \"NA\" """, 
                      key="DGS_FIS_taxst_nomau", value=values_2022[""])
        st.text_input("""Pouvez-vous détailler les **spécificités qui s'appliquent à votre collectivité en matière de fiscalité** ?
(ex : population < 5 000 habitants, station classée, etc.) """, 
                      key="DGS_FIS_taxst_spec", value=values_2022[""])
        
        # commentaire 
        with st.expander("*Commentaires :* "):
                comment = st.text_area("", placeholder="", key = "DGS_FIS_taxst_com_reponse_2022")

        
        st.write("#")
        # 1.3. TAXES LOCALES PERCUES AU NIVEAU DE L'EPCI
        section_titles(40, "1.3. TAXES LOCALES PERCUES AU NIVEAU DE L'EPCI")

        columns_widths = (5.5, 6, 1.5, 1.5, 3) # table
        line_names = ["<b>Régime fiscal de L'EPCI</b>"]
        questions_ids = ["DGS_FIS_regfisc_EPCI"]
        questions_values_types = ["select_box"]
        regimes_EPCI_list = ["", "EPCI à fiscalité propre, EPCI à fiscalité professionnelle unique (FPU)", "EPCI à fiscalité propre, EPCI à fiscalité additionnelle",
                                   "EPCI sans fiscalité propre, contribution budgétaire", "EPCI sans fiscalité propre, contribution fiscalisée", 'NA', 'NC', 
                                   "Autre  (préciser en commentaire)"]
        lists_for_selectbox = [regimes_EPCI_list]
        height_size = "small"
        display_table_2022(columns_widths, line_names, questions_ids, questions_values_types, lists_for_selectbox, height_size, values_2022)

        # commentaire 
        with st.expander("*Commentaires :* "):
                comment = st.text_area("", placeholder="", key = "DGS_FIS_regfisc_EPCI_com_reponse_2022")

        st.write("#")
        columns_widths = (5.5, 1.5, 1.5, 1.5, 3) # table
        line_names = ["<b>Produit fiscal perçu par l’EPCI sur le territoire de la commune (en €)</b>",
                      "<b>Produit fiscal perçu par l’EPCI sur le territoire de l'ensemble des communes de l'EPCI (en €)</b>"]
        questions_ids = ["DGS_FIS_epcicom_TOTAL", "DGS_FIS_epci_TOTAL"]
        questions_values_types = ["float", "float"]
        display_booleans = [True, True]
        height_line = "small"
        display_table_2021(columns_widths, line_names, questions_ids, questions_values_types, display_booleans, None, height_line, values_2022, values_2021)

        # commentaire 
        with st.expander("*Commentaires :* "):
                comment = st.text_area("", placeholder="", key = "DGS_FIS_epci_com_reponse_2022")

        
        st.write('#')
        st.write("""<p style="font-size:14px; color:#51698F;"><b> Graphiques automatiques pour contrôle de cohérence</b>
        </p>  """, unsafe_allow_html=True) 

        
        pop_commune = st.session_state["DGS_FIS_pop_INSEE_reponse_2022"]
        pop_EPCI = st.session_state["DGS_FIS_pop_EPCI_reponse_2022"]
        if isfloat(pop_commune) and isfloat(pop_EPCI) :
            fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,5))
            pop_commune = float(pop_commune)
            pop_EPCI = float(pop_EPCI)
            pop_tot = pop_commune+pop_EPCI
            proportions = [pop_commune/pop_tot, pop_EPCI/pop_tot]
            ax1.pie(proportions,
                    colors = ['#4472C4', '#A5A5A5'],
                    explode = [0, 0.1],
                    autopct='%1.1f%%',
                    )
            ax1.set_title("Poids de la commune dans la population de l'EPCI")
            ax1.legend(labels=["population de la commune", "Population de l'ensemble de l'EPCI"], loc="lower right")
            # plt.legend(loc=3, labels=["population de la commune", "Population de l'ensemble de l'EPCI"])
            
            st.pyplot(fig)



    if selected == "2.Investissements":
            for k, v in st.session_state.items():
                st.session_state[k] = v
            thematic_titles(40, "2.INVESTISSEMENTS")
            ### MODIFIER NUMEROS DE LIGNES
            st.write("""<p style="font-size:14px; color:black;">
            <i>Il vous est demandé de <b>distinguer 1/ les investissements liés à l'activité thermale </b> (cf. lignes 21 à 57 ex :  ressource en eau, hébergements de l'établissement thermal), <br/>
            <b> et 2/ le total des autres investissements réalisés sur la station thermale </b>(cf. lignes 58 à 66). <br/>
            Dans un second temps, il vous est demandé de renseigner le <b> taux d'endettement </b> de la station (cf. lignes 105 à 128).  
            </i></p>
            """,
            unsafe_allow_html=True) 


        
            st.write("#")
            # 2.1. INVESTISSEMENTS DE LA STATION LIES A L'ACTIVITE THERMALE
            section_titles(40, "2.1. INVESTISSEMENTS DE LA STATION LIES A L'ACTIVITE THERMALE")
            text = "<b>NB1 : Les deux informations demandés dans les colonnes ci-dessous sont mutuellement exclusives.</b> Les subventions et investissements versées à la commune par des acteurs externes doivent être comptabilisés dans la colonne « Montant investi par les coinvestisseurs publics »"
            st.markdown(f"<div style='color:#000000; background-color:#F3D6E0; align-items:left; justify-content:left; font-size:14px; padding:8px;'>{text}</div>", unsafe_allow_html=True)
            st.write("#####")
            text = "<b>NB2 </b>: Le \"montant annuel investi par les co-investisseurs publics sur l'année\" désigne à la fois les montants investis par les partenaires publics sous maîtrise d’ouvrage de la commune et les montants investis par les partenaires publics lorsque la maîtrise d’ouvrage n’est pas la commune mais que le projet concerne la commune."
            st.markdown(f"<div style='color:#000000; background-color:#F3D6E0; align-items:left; justify-content:left; font-size:14px; padding:8px;'>{text}</div>", unsafe_allow_html=True)
            st.write("#####")
            text = "<b> NB3 : Un liste d'exemples d'investissements pour chaque catégorie du tableau ci-dessous est disponible en bas de page.</b>"
            st.markdown(f"<div style='color:#000000; background-color:#F3D6E0; align-items:left; justify-content:left; font-size:14px; padding:8px;'>{text}</div>", unsafe_allow_html=True)

            st.write("#")
            c1, c2, c3, c4, c5, c6 = st.columns((3.5, 1, 1, 0.1, 1, 1))
            with c1:
                text = "Type d'investissement (Budget Principal + Budgets Annexes)"
                rectangle_with_text(80, text, color="FFFFFF", background="51698F", font_size=12, padding=3, border=0)
            with c2:
                text = "Montant investi par la collectivité locale sur l'année 2022 (en €)"
                rectangle_with_text(80, text, color="FFFFFF", background="009999", font_size=12, padding=3, border=1)
            with c3:
                text = "TOTAL investi par la collectivité locale sur l'année 2021 (en €)"
                rectangle_with_text(80, text, color="000000", background="A6A6A6", font_size=12, padding=3, border=1)

            with c5:
                text = "Montant annuel investi par les co-investisseurs publics sur l'année 2022 (en €)"
                rectangle_with_text(80, text, color="FFFFFF", background="009999", font_size=12, padding=3, border=1)
            with c6:
                text = "TOTAL investi par les co-investisseurs publics sur l'année 2021 (en €)"
                rectangle_with_text(80, text, color="000000", background="A6A6A6", font_size=12, padding=3, border=1)


            line_names = ["Investissements liés à la <b>ressource en eau </b>: forage, protection de la ressource, transport de la ressource", 
                          "Investissements liés aux <b>établissements thermaux </b> : construction,  rénovation, extension, équipements", 
                          "Investissements liés aux <b>établissements thermoludiques</b> : construction,  rénovation, extension, équipements",
                          "Investissements liés à l'<b> hébergement thermal * </b> : construction,  rénovation, extension", 
                          "Investissements liés à la <b> restauration thermale * </b> : construction,  rénovation, extension", 
                          "Investissements liés à la <b> promotion thermale </b>", 
                          "Autres investissements liés à l'activité thermale. Si non applicable, préciser \"NA\" dans cette case et celles de droite."]

            questions_ids_collectivite_locale = ["DGS_IN_cl_eau", "DGS_IN_cl_eth", "DGS_IN_cl_therm", "DGS_IN_cl_heb", "DGS_IN_cl_rest", "DGS_IN_cl_prom", "DGS_IN_cl_aut"]
            questions_ids_co_investisseurs_pub = ["DGS_IN_coinvp_eau", "DGS_IN_coinvp_eth", "DGS_IN_coinvp_therm", "DGS_IN_coinvp_heb", "DGS_IN_coinvp_rest", "DGS_IN_coinvp_prom", "DGS_IN_coinvp_aut"]
            
            dict = {1:["line_name", line_names], 2:["float_2022",questions_ids_collectivite_locale], 5:["float_2022", questions_ids_co_investisseurs_pub]}
            columns_widths = (3.5, 1, 1, 0.1, 1, 1)
            display_table(dict, (c1, c2, c3, c4, c5, c6), columns_widths=columns_widths, values_2022=values_2022, values_2021=values_2021, height_size="big")

            c1, c2, c3, c4, c5, c6 = st.columns((3.5, 1, 1, 0.1, 1, 1))
            with c1:
                text = "TOTAL des investissements annuels liés à l'activité thermale"
                st.markdown("<div style='height:40px; color:#000000; background-color:#A6A6A6; display:flex; align-items:center; justify-content:left; text-align: left; font-size:13px; padding:8px; border: 1px solid #000000;'>{}</div>".format(text), unsafe_allow_html=True)
                text = "<i>* Il est entendu par \"hébergement thermal\" et \"restauration thermale\" tout établissement d'hébergement ou de restauration <b>géré par la même entité juridique que l'établissement thermal.</i></b>"
                st.markdown("<div style='height:40px; color:#000000; background-color:#FFFFFF; display:flex; align-items:center; justify-content:left; text-align: left; font-size:11px; padding:3px; '>{}</div>".format(text), unsafe_allow_html=True)
            with c2:
                display_sum([question_id+"_reponse_2022" for question_id in questions_ids_collectivite_locale], "DGS_IN_cl_TOTAL_reponse_2022", currency=True)
            with c3:
                table_cases(values_2021["DGS_IN_cl_TOTAL"+"_reponse_2021"], font_size=15, color="000000", background_color="d9d9d9")
            with c5:
                display_sum([question_id+"_reponse_2022" for question_id in questions_ids_co_investisseurs_pub], "DGS_IN_coinvp_TOTAL", currency=True)
            with c6:
                table_cases(values_2021["DGS_IN_coinvp_TOTAL"+"_reponse_2021"], font_size=15, color="000000", background_color="d9d9d9")
            
            with st.expander("↓ Exemples d'investissements pour chaque catégorie du tableau listant les investissements de la station : ↓"):
                image = Image.open('./images/dgs//Investissements/exemples_investissements.png')
                st.image(image, width=1000)

            with st.expander("*Commentaires :* "):
                comment = st.text_area("", placeholder="", key = "DGS_IN_typinc_com_reponse_2022")  

            
            st.write("#")
            # 2.2. AUTRES INVESTISSEMENTS DE LA STATION
            section_titles(40, "2.2. AUTRES INVESTISSEMENTS DE LA STATION")

            st.write("""<p style="font-size:14px; color:#51698F;">
            <b>/ Autres investissements de la station, non directement liés à l'activité thermale (ex : transport, voirie, réseau, etc.). </b> </p>  """, unsafe_allow_html=True)

            columns_widths = (6, 1.3, 1.3, 1.3, 3) # table
            line_names = ["<b>Montant investi par la collectivité locale (Budget Principal + Budgets Annexes) sur l'année 2022 (en €)",
                         "<b>Montant annuel investi par les co-investisseurs publics sur l'année 2022 (en €)"]
            questions_ids = ["DGS_IN_auinv_col", "DGS_IN_auinv_coinvp"]
            questions_values_types = ["float", "float"]
            display_booleans = [True, True]
            height_line = "small"
            display_table_2021(columns_widths, line_names, questions_ids, questions_values_types, display_booleans, None, height_line, values_2022, values_2021)

            with st.expander("*Commentaires :* "):
                comment = st.text_area("", placeholder="", key = "DGS_IN_autrinv_com_reponse_2022")

            columns_widths = (6, 1.3, 1.3, 1.3, 3) # table
            line_names = ["<b>Y a-t-il des spécificités de votre commune ou de l'exercice étudié qui expliquent le montant particulièrement faible ou particulièrement élevé des investissements de votre commune ?"]
            questions_ids = ["DGS_IN_coll_spec"]
            questions_values_types = ["float"]
            display_booleans = [False]
            height_line = "big"
            display_table_2021(columns_widths, line_names, questions_ids, questions_values_types, display_booleans, None, height_line, values_2022, values_2021)

            # st.write("#")
            st.text_input("""**Si oui, préciser. Si non, indiquer "NA" :** """, 
                    key="DGS_FIS_taxst_nomau", value=values_2022[""])
            text = "<i>Exemples : Fermeture exceptionnelle des thermes pendant une partie de l’année, ce qui explique le faible montant d’investissements thermaux, investissement thermal exceptionnel car rachat d’un établissement thermal privé, station qui porte les investissements du village d’une station de ski, etc.</i></b>"
            st.markdown("<div style='height:40px; color:#000000; background-color:#FFFFFF; display:flex; align-items:center; justify-content:left; text-align: left; font-size:11px; padding:3px; '>{}</div>".format(text), unsafe_allow_html=True)

            with st.expander("*Commentaires :* "):
                comment = st.text_area("", placeholder="", key = "DGS_END_spec_com_reponse_2022")

            st.write("#")
            st.write("""<p style="font-size:14px; color:#000000;">
            <b>/ Calcul automatique pour contrôle de cohérence </b> </p>  """, unsafe_allow_html=True)
            
            c1, c2, c3, c4, c5 = st.columns((3, 1, 1, 1, 1))
            with c2:
                text = "Année 2022"
                rectangle_with_text(100, text, color="FFFFFF", background="009999", font_size=12, padding=3, border=1)
            with c3:
                text = "Année 2021"
                rectangle_with_text(100, text, color="000000", background="A6A6A6", font_size=12, padding=3, border=1)
            
            with c4:
                date = str(datetime.date.today().strftime("%d/%m/%Y"))
                text = f"""Moyenne nationale des répondants le {date}. </br><i>Indicateur amené à changer d'ici la fin de l'enquête </i>"""
                st.markdown(f"<div style='height:100px; background-color:#A6A6A6;color:#000000;font-size:12px;border-radius:2%; text-align: center; border: 1px solid #000000; padding:4px;  '>{text}</div>", unsafe_allow_html=True)
            with c5:
                text = "Ecart à la moyenne sur 2022"
                rectangle_with_text(100, text, color="000000", background="A6A6A6", font_size=12, padding=3, border=1)
            
            c1, c2, c3, c4, c5 = st.columns((3, 1, 1, 1, 1))
            with c1:
                 table_lines("<b>Total des investissements Budget Principal et Budgets Annexes (hors chapitre 16) :")
            with c2:
                 somme_2_keys("DGS_IN_auinv_col_reponse_2022", "DGS_IN_cl_TOTAL_reponse_2022", "DGS_IN_coll_tot_reponse_2022")
            with c3:
                 table_cases(values_2021["DGS_IN_coll_tot_reponse_2021"], font_size=15, color="000000", background_color="d9d9d9")

            c1, c2, c3, c4, c5 = st.columns((3, 1, 1, 1, 1))
            with c1:
                 line_name("<b>Part de l'investissement thermal dans le montant total des investissements de la collectivité locale")
            with c2:
                 divide_2_keys("DGS_IN_cl_TOTAL_reponse_2022", "DGS_IN_coll_tot_reponse_2022", "DGS_IN_coll_parttherm_reponse_2022")
            with c3:
                 table_cases(np.round(float(values_2021["DGS_IN_coll_parttherm_reponse_2021"]), 1), font_size=15, color="000000", background_color="d9d9d9")
    

    if selected=="3.Endettement":
            for k, v in st.session_state.items():
                st.session_state[k] = v
            thematic_titles(40, "3.ENDETTEMENT")
            # 3.1. TAUX D'ENDETTEMENT DE LA STATION en 2022
            section_titles(40, "3.1. TAUX D'ENDETTEMENT DE LA STATION en 2022")
            st.write("""<p style="font-size:14px; color:#51698F;"><b>/ Budget principal en 2022</b>
            </p>""", unsafe_allow_html=True) 
            columns_widths = (6, 2, 2, 2, 3) # table
            line_names = ["/ Budget pricipal en 2022 - Encours total de la dette au 31 décembre (Valeur totale en €)", 
                          "/ Budget pricipal en 2022 - Capacité d'autofinancement (Valeur totale en €)"]
            questions_ids = ["DGS_END_dette_bp", "DGS_END_capauto_bp"]
            questions_values_types = ["currency"]*2
            display_booleans = [True]*2
            height_line = "small"
            display_table_2021(columns_widths, line_names, questions_ids, questions_values_types, display_booleans, None, height_line, values_2022, values_2021, )
    
            st.write("#")
            # 2e tableau
            c1, c2, c3, c4, c5 = st.columns((3, 1, 1, 1, 1))
            with c2:
                text = "Année 2022"
                rectangle_with_text(100, text, color="FFFFFF", background="009999", font_size=12, padding=3, border=1)
            with c3:
                text = "Année 2021"
                rectangle_with_text(100, text, color="000000", background="A6A6A6", font_size=12, padding=3, border=1)
            with c4:
                date = str(datetime.date.today().strftime("%d/%m/%Y"))
                text = f"""Moyenne nationale des répondants le {date}. </br><i>Indicateur amené à changer d'ici la fin de l'enquête </i>"""
                st.markdown(f"<div style='height:100px; background-color:#A6A6A6;color:#000000;font-size:12px;border-radius:2%; text-align: center; border: 1px solid #000000; padding:4px;  '>{text}</div>", unsafe_allow_html=True)
            with c5:
                text = "Ecart à la moyenne sur 2022"
                rectangle_with_text(100, text, color="000000", background="A6A6A6", font_size=12, padding=3, border=1)

            c1, c2, c3, c4, c5 = st.columns((3, 1, 1, 1, 1))
            with c1:
                 line_name("<b>/ Budget pricipal en 2022 - Encours total de la dette au 31 décembre(Valeur totale en €/habitant INSEE)")
            with c2:    # ratio 2022
                 divide_2_keys("DGS_END_dette_bp_reponse_2022", "DGS_FIS_pop_INSEE_reponse_2022", "DGS_END_dethab_bp_reponse_2022")
            with c3:    # valeur ratio 2021
                 table_cases(values_2021["DGS_END_dethab_bp_reponse_2021"], font_size=15, color="000000", background_color="d9d9d9")
            # 2nd line
            c1, c2, c3, c4, c5 = st.columns((3, 1, 1, 1, 1))
            with c1:
                 table_lines("<b>/ Budget pricipal en 2022 -  Capacité d'autofinancement (Valeur totale en €/habitant INSEE)")
            with c2:    # ratio 2022
                 divide_2_keys("DGS_END_capauto_bp_reponse_2022", "DGS_FIS_pop_INSEE_reponse_2022", "DGS_END_autohab_bp_reponse_2022")
            # 3rd line
            c1, c2, c3, c4, c5 = st.columns((3, 1, 1, 1, 1))
            with c1:
                 table_lines("<b>/ Budget pricipal en 2022 - Capacité de désendettement (valeur en années)")
            with c2:    # ratio 2022
                 divide_2_keys("DGS_END_dette_bp_reponse_2022", "DGS_END_capauto_bp_reponse_2022", "DGS_END_desend_bp_reponse_2022")

            with c1:
                text = "<i>NB : Plus la capacité de désendettement (en année) est faible, plus la solvabilité de la commune, selon cet indicateur, est élevée.</i></b>"
                st.markdown("<div style='height:40px; color:#000000; background-color:#FFFFFF; display:flex; align-items:center; justify-content:left; text-align: left; font-size:11px; padding:3px; '>{}</div>".format(text), unsafe_allow_html=True)
            
            with st.expander("*Commentaires :* "): # commentaire
                comment = st.text_area("", placeholder="", key = "DGS_END_com_reponse_2022")    

            # / Budget annexe en 2022
            st.write("#")
            st.write("""<p style="font-size:14px; color:#51698F;"><b>/ Budget annexe en 2022</b>
            </p>""", unsafe_allow_html=True) 

            columns_widths = (6, 2, 2, 2, 3) # table
            line_names = ["<b>/ Budget annexe en 2022 - Encours total de la dette au 31 décembre (Valeur totale en €)", 
                          "<b>/ Budget annexe en 2022 - Capacité d'autofinancement (Valeur totale en €)"]
            questions_ids = ["DGS_END_dette_ba", "DGS_END_capauto_ba"]
            questions_values_types = ["currency"]*2
            display_booleans = [True]*2
            height_line = "small"
            display_table_2021(columns_widths, line_names, questions_ids, questions_values_types, display_booleans, None, height_line, values_2022, values_2021, )

            # 3e ligne
            c1, c2, c3, c4, c5 = st.columns((6, 2, 2, 2, 3))
            with c1:
                 line_name("<b>/ Budget annexe en 2022 - Encours total de la dette au 31 décembre (Valeur totale en €/habitant INSEE)")
            with c2:    # ratio 2022
                 divide_2_keys("DGS_END_dette_ba_reponse_2022", "DGS_FIS_pop_INSEE_reponse_2022", "DGS_END_dethab_ba_reponse_2022")

            # 4e ligne
            c1, c2, c3, c4, c5 = st.columns((6, 2, 2, 2, 3))
            with c1:
                 line_name("<b>/ Budget annexe en 2022 - Capacité d'autofinancement (Valeur totale en €/habitant INSEE)")
            with c2:    # ratio 2022
                 divide_2_keys("DGS_END_capauto_ba_reponse_2022", "DGS_FIS_pop_INSEE_reponse_2022", "DGS_END_autohab_ba_reponse_2022")
                
            # 5e ligne
            c1, c2, c3, c4, c5 = st.columns((6, 2, 2, 2, 3))
            with c1:
                 line_name("<b>/ Budget annexe en 2022 - Capacité de désendettement (valeur en années)")
            with c2:    # ratio 2022
                 divide_2_keys("DGS_END_capauto_bp_reponse_2022", "DGS_END_capauto_ba_reponse_2022", "DGS_END_desend_ba_reponse_2022")
                
            with c1:
                text = "<i>NB : Plus la capacité de désendettement (en année) est faible, plus la solvabilité de la commune, selon cet indicateur, est élevée.</i></b>"
                st.markdown("<div style='height:40px; color:#000000; background-color:#FFFFFF; display:flex; align-items:center; justify-content:left; text-align: left; font-size:11px; padding:3px; '>{}</div>".format(text), unsafe_allow_html=True)
            
            with st.expander("*Commentaires :* "): # commentaire
                comment = st.text_area("", placeholder="", key = "DGS_END_com_ba_reponse_2022")

            
            # 3.2. TAUX D'ENDETTEMENT DE LA STATION SUR LES DERNIERES ANNEES (BUDGET PRINCIPAL SEUL)
            st.write("#")
            section_titles(40, "3.2. TAUX D'ENDETTEMENT DE LA STATION SUR LES DERNIERES ANNEES (BUDGET PRINCIPAL SEUL)")
            c1, c2, c3, c4, c5 = st.columns((3, 1, 1, 1, 1))
            
            with c2:
                text = "2018"
                rectangle_with_text(40, text, color="000000", background="FFFFFF", font_size=12, padding=3, border=1)
            with c3:
                text = "2019"
                rectangle_with_text(40, text, color="000000", background="FFFFFF", font_size=12, padding=3, border=1)

            with c4:
                text = "2010"
                rectangle_with_text(40, text, color="000000", background="FFFFFF", font_size=12, padding=3, border=1)
            with c5:
                text = "2021"
                rectangle_with_text(40, text, color="000000", background="FFFFFF", font_size=12, padding=3, border=1)
           

            line_names = ["<b>Encours total de la dette au 31 décembre"]
            question_id_encours_2018 = ["DGS_END_dette_2017"]
            question_id_encours_2019 = ["DGS_END_dette_2018"]
            question_id_encours_2020 = ["DGS_END_dette_2019"]
            question_id_encours_2021 = ["DGS_END_dette_2020"]
            dict = {1:["line_name", line_names], 2:["float_2022",question_id_encours_2018], 3:["float_2022",question_id_encours_2019], 4:["float_2022",question_id_encours_2020], 5:["float_2022",question_id_encours_2021] }
            columns_widths = (3, 1, 1, 1, 1)
            display_table(dict, (c1, c2, c3, c4, c5), columns_widths=columns_widths, values_2022=values_2022, values_2021=values_2021, height_size="small")

            # 2e ligne
            line_names = ["<b>Capacité d'autofinancement"]
            question_id_capacite_autofinancement_2018 = ["DGS_END_autofin_2017"]
            question_id_capacite_autofinancement_2019 = ["DGS_END_autofin_2018"]
            question_id_capacite_autofinancement_2020 = ["DGS_END_autofin_2019"]
            question_id_capacite_autofinancement_2021 = ["DGS_END_autofin_2020"]
            dict = {1:["line_name", line_names], 2:["float_2022",question_id_capacite_autofinancement_2018], 3:["float_2022",question_id_capacite_autofinancement_2019], 4:["float_2022",question_id_capacite_autofinancement_2020], 5:["float_2022",question_id_capacite_autofinancement_2021] }
            columns_widths = (3, 1, 1, 1, 1)
            display_table(dict, (c1, c2, c3, c4, c5), columns_widths=columns_widths, values_2022=values_2022, values_2021=values_2021, height_size="small")

            # 3e ligne
            c1, c2, c3, c4, c5 = st.columns((3, 1, 1, 1, 1))
            with c1:
                 table_lines("<b>Capacité de désendettement")
            with c2:    
                divide_2_keys("DGS_END_dette_2017_reponse_2022", "DGS_END_autofin_2017_reponse_2022", "DGS_END_desend_2017_reponse_2022")
            with c3:    
                divide_2_keys("DGS_END_dette_2018_reponse_2022", "DGS_END_autofin_2018_reponse_2022", "DGS_END_desend_2018_reponse_2022")
            with c4:  
                divide_2_keys("DGS_END_dette_2019_reponse_2022", "DGS_END_autofin_2019_reponse_2022", "DGS_END_desend_2019_reponse_2022")
            with c5:    
                divide_2_keys("DGS_END_dette_2020_reponse_2022", "DGS_END_autofin_2020_reponse_2022", "DGS_END_desend_2020_reponse_2022")
            
            with st.expander("*Commentaires :* "): # commentaire
                comment = st.text_area("", placeholder="", key = "DGS_END_dettepasses_com_reponse_2022")


    if selected=="4.Emplois et act.":
            for k, v in st.session_state.items():
                st.session_state[k] = v
            thematic_titles(40, "4. EMPLOIS ET ACTIVITES SPECIFIQUES en 2022")

            # 4.1. Emplois dans la station et son EPCI en 2022							
            section_titles(40, "4.1. Emplois dans la station et son EPCI en 2022")

            # 4.1.1. Emplois totaux
            sub_section_titles(40, "4.1.1. Emplois totaux")
            # /Emplois dans la station
            st.write("""<p style="font-size:14px; color:#51698F;"><b>/ Emplois dans la station</b>
            </p>""", unsafe_allow_html=True) 

            columns_widths = (6, 2, 2, 2, 3) # table
            line_names = ["<b>Station - Nombre total d'emplois dans la station (en ETP)", 
                          "<b>Station - Nombre total d'emplois dans la station (en nombre) :",
                          "Station - Année de l'information", 		
                         " Station - Source de l'information"]
            questions_ids = ["DGS_EMP_empst_ETP", "DGS_EMP_empst_nb", "DGS_EMP_empst_year", "DGS_EMP_empst_src"]
            questions_values_types = ["int", "int", "int", None]
            display_booleans = [True, True, False, False]
            height_line = "small"
            display_table_2021(columns_widths, line_names, questions_ids, questions_values_types, display_booleans, None, height_line, values_2022, values_2021, )

            with st.expander("*Commentaires :* "): # commentaire
                comment = st.text_area("", placeholder="", key = "DGS_EMP_empst_com_reponse_2022")

            # /Emplois dans l'EPCI
            st.write("###")
            st.write("""<p style="font-size:14px; color:#51698F;"><b>/ Emplois dans l'EPCI</b>
            </p>""", unsafe_allow_html=True) 

            columns_widths = (6, 2, 2, 2, 3) # table
            line_names = ["<b>Station - Nombre total d'emplois dans la station (en ETP)", 
                          "<b>Station - Nombre total d'emplois dans la station (en nombre) :",
                          "Station - Année de l'information", 		
                         " Station - Source de l'information"]
            questions_ids = ["DGS_EMP_empepci_ETP", "DGS_EMP_empepci_nb", "DGS_EMP_empepci_year", "DGS_EMP_empepci_src"]
            questions_values_types = ["int", "int", "int", None]
            display_booleans = [True, True, False, False]
            height_line = "small"
            display_table_2021(columns_widths, line_names, questions_ids, questions_values_types, display_booleans, None, height_line, values_2022, values_2021, )

            with st.expander("*Commentaires :* "): # commentaire
                comment = st.text_area("", placeholder="", key = "DGS_EMP_empepci_com_reponse_2022")

            # 4.1.2. Emplois municipaux
            sub_section_titles(40, "4.1.2. Emplois municipaux")
            columns_widths = (6, 2, 2, 2, 3) # table
            line_names = ["<b>Nombre d'employés municipaux dans la station (en ETP)", 
                          "<b>Nombre d'employés municipaux dans la station (en nombre) :",
                          "<b>Budget principal (Compte 012) - Masse salariale de la commune", 		
                          "<b>Budget annexe (Compte 012) - Masse salariale de la commune"]
            questions_ids = ["DGS_EMP_empmun_ETP", "DGS_EMP_empmun_nb", "DGS_EMP_empmun_msbp", "DGS_EMP_empmun_msba"]
            questions_values_types = ["int", "int", "currency", "currency"]
            display_booleans = [True, True, False, False]
            height_line = "small"
            display_table_2021(columns_widths, line_names, questions_ids, questions_values_types, display_booleans, None, height_line, values_2022, values_2021, )

            st.write("###")
            st.write("""<p style="font-size:14px; color:#000000;">
            <b>/ Calcul automatique pour contrôle de cohérence </b> </p>  """, unsafe_allow_html=True)

            c1, c2, c3, c4 = st.columns((6, 2, 3, 2))
            with c2:
                text = "Année 2022"
                rectangle_with_text(85, text, color="FFFFFF", background="009999", font_size=12, padding=3, border=1)
            with c3:
                date = str(datetime.date.today().strftime("%d/%m/%Y"))
                text = f"""Moyenne nationale des répondants le {date}. </br><i>Indicateur amené à changer d'ici la fin de l'enquête </i>"""
                st.markdown(f"<div style='height:85px; background-color:#A6A6A6;color:#000000;font-size:12px;border-radius:2%; text-align: center; border: 1px solid #000000; padding:4px;  '>{text}</div>", unsafe_allow_html=True)
            with c4:
                text = "Ecart à la moyenne sur 2022"
                rectangle_with_text(85, text, color="000000", background="A6A6A6", font_size=12, padding=3, border=1)

            c1, c2, c3, c4 = st.columns((6, 2, 3, 2))
            with c1:
                 line_name("<b>Nombre d'employés municipaux par habitant (population DGF, renseignée en onglet 1. Fiscalité)")
            with c2:    # ratio 2022
                 divide_2_keys("DGS_EMP_empmun_nb_reponse_2022", "DGS_FIS_pop_DGF_reponse_2022", "DGS_EMP_empmun_parhab_reponse_2022")
            with c3:
                question_id = "DGS_EMP_empmun_parhab"
                display_moyenne_2022(question_id, values_2022)
            with c4:
                display_ecart_moyenne_2022(question_id, values_2022)
                    
            # 2nd line
            c1, c2, c3, c4 = st.columns((6, 2, 3, 2))
            with c1:
                 table_lines("<b>Masse salariale en euros par habitant (population DGF; Budget principal)")
            with c2:    # ratio 2022
                 divide_2_keys("DGS_EMP_empmun_msbp_reponse_2022", "DGS_FIS_pop_DGF_reponse_2022", "DGS_EMP_empmun_msparhab_reponse_2022")
            with c3:
                question_id = "DGS_EMP_empmun_msparhab"
                display_moyenne_2022(question_id, values_2022)
            with c4:
                display_ecart_moyenne_2022(question_id, values_2022)

            with st.expander("*Commentaires :* "):
                comment = st.text_area("", placeholder="", key = "DGS_EMP_empmun_com_reponse_2022")

            
            # 4.2. Casinos en 2022							
            section_titles(40, "4.2. Casinos en 2022")
            columns_widths = (6, 2, 2, 2, 3) # table
            line_names = ["<b>Votre commune dispose-t-elle d'un Casino en 2022 ?", 
                          "<b>Si oui, le casino est-il indépendant ou dépend-il d'un groupe ? (préciser \"indépendant\" ou le nom du groupe). S'il n'y a pas de Casino dans votre commune, indiquer \"NA\" ",
                          "<b>Si oui, quel est le chiffre d'affaires de l'établissement en 2021 ? S'il n'y a pas de Casino dans votre commune, indiquer \"NA\" ", 		
                          "<b>Si oui, quel est le nombre d'employés de l'établissement ? (en ETP). S'il n'y a pas de Casino dans votre commune, indiquer \"NA\" "]		
            questions_ids = ["DGS_EMP_casino", "DGS_EMP_casino_groupe", "DGS_EMP_casino_ca", "DGS_EMP_casino_etp"]
            questions_values_types = ["select_box", None, "currency", "int"]
            display_booleans = [True, True, True, True]
            height_line = "big"
            lists_for_selectbox = [yesno_list, None, None, None]
            display_table_2021(columns_widths, line_names, questions_ids, questions_values_types, display_booleans, lists_for_selectbox=lists_for_selectbox, values_2022=values_2022, values_2021=values_2021, height_size=height_line)

            with st.expander("*Commentaires :* "):
                comment = st.text_area("", placeholder="", key = "DGS_EMP_casino_com_reponse_2022")


            # 4.3. Industries cosmétiques en 2022	
            st.write("#")						
            section_titles(40, "4.3. Industries cosmétiques en 2022")
            columns_widths = (6, 4) # table
            line_names = ["<b>Existe-t-il une gamme / ligne de produits cosmétiques utilisant l'eau thermale de votre station ?</b>",
                          "<b>Si oui, par quel marque / laboratoire est fabriquée la gamme ?</b> </br> S'il n'y a pas de gamme de cosmétiques liée à votre commune, indiquer \"NA\"",
                          "<b>Si oui, quel est l'emplacement du site de production des cosmétiques ? (indiquez la ville / le pays si pertinent)? </b> </br>Sinon, indiquer \"NA\" ",
                          "<b>Si oui, quel est le nombre d'employés du site de production ? </b> </br> Sinon, indiquer \"NA\""]	

            questions_ids = ["DGS_EMP_cosm", "DGS_EMP_cosm_fab", "DGS_EMP_cosm_site", "DGS_EMP_cosm_etp"]
            questions_values_types = ["select_box", None, None, "int"]
            lists_for_selectbox = [yesno_list, None, None, None]
            height_size = "big"
            display_table_2022(columns_widths, line_names, questions_ids, questions_values_types, lists_for_selectbox, height_size, values_2022)

            st.write("""<p style="font-size:12px; color:#000000;">
            <b>Si oui, que représente la gamme de cosmétiques utilisant de l'eau thermale dans l'ensemble de la production du site ? </b> </br>
            S'il n'y a pas de gamme de cosmétiques liée à votre commmune, indiquer \"NA\"
            </p>  """, unsafe_allow_html=True)
            columns_widths = (6, 4) # table
            line_names = ["<b>En valeur (en %)</b>",
                          "<b>En volume (en %)"]	
            questions_ids = ["DGS_EMP_cosm_partca", "DGS_EMP_cosm_partvol"]
            questions_values_types = ["float", "float"]
            height_size = "small"
            display_table_2022(columns_widths, line_names, questions_ids, questions_values_types, lists_for_selectbox=None, height_size=height_size , values_2022=values_2022)

            st.write("""<p style="font-size:12px; color:#000000;">
            <b>Si votre commune est concernée et que vous ne disposez pas des informations demandées, pouvez-vous indiquer le contact d'une personne
              susceptible d'avoir les informations à sa disposition.  </b> </br>
            S'il n'y a pas de gamme de cosmétiques liée à votre commune, indiquer \"NA\" dans l'ensemble des cases
            </p>  """, unsafe_allow_html=True)
            columns_widths = (6, 4) # table
            line_names = ["<b>Nom de la personne :</b>",
                          "<b>Fonction de la personne :</b>",
                          "<b>Organisme de rattachement : </b>",
                          "<b>Téléphone : </b>",
                          "<b>Mail : </b>"]	

            questions_ids = ["DGS_EMP_cosm_nompers", "DGS_EMP_cosm_fctpers", "DGS_EMP_cosm_orgpers", "DGS_EMP_cosm_telpers", "DGS_EMP_cosm_mailpers"]
            questions_values_types = [None]*5
            height_size = "small"
            display_table_2022(columns_widths, line_names, questions_ids, questions_values_types, lists_for_selectbox, height_size, values_2022)

            with st.expander("*Commentaires :* "):
                comment = st.text_area("", placeholder="", key = "DGS_EMP_cosm_com_reponse_2022")

    if selected=="Taux de remplissage":
            for k, v in st.session_state.items():
                st.session_state[k] = v
            repondu = 0
            for question_id in questions_ids_2022_inclus_taux:
                if st.session_state[question_id + "_reponse_2022"] != "":
                    repondu+=1
            st.write("Votre formulaire est rempli à " + str(np.round(repondu/len(question_ids_2021), 1)) + "%")

    if selected=="Enregistrement/Validation":
            for k, v in st.session_state.items():
                st.session_state[k] = v
            repondu = 0
            for question_id in questions_ids_2022_inclus_taux:
                if st.session_state[question_id + "_reponse_2022"] != "":
                    repondu+=1
            st.write("Votre formulaire est rempli à " + str(np.round(repondu/len(question_ids_2021), 1)) + "%")

            c1, c2, c3, c4 = st.columns((2, 2, 5, 2))
            with c1:
                 enregirstrement_button = st.button(label="Enregistrer")
                 if enregirstrement_button:
                        timestamp = datetime.datetime.now()
                        st.success('Votre formulaire a bien été enregistré', icon="✅")
                    #   # Modification de chaque ligne dans la BDD    
                    #     # Pour 2021
                    #     for question_id in question_ids_2021:
                    #         reponse_2021_updated = st.session_state[question_id + "_reponse_2021_updated"] 
                    #         raison_modification_2021 = st.session_state[question_id + "_raison_modification_2021"] 
                    #         cur.execute("UPDATE responses_2021 SET reponse_2021_updated=? raison_modification_2021=? timestamp_last_updated=? WHERE entity_id=? AND question_id=?", (reponse_2021_updated, raison_modification_2021, timestamp, entity_id, question_id))
                        
                    #     # Pour 2022 :
                    #     for question_id in question_ids_2022:
                    #         reponse_2022 = st.session_state[question_id + "_reponse_2022"] 
                    #         cur.execute("UPDATE responses_2022 SET reponse_2022=? timestamp_last_updated=? WHERE entity_id=? AND question_id=?", (reponse_2022, timestamp, entity_id, question_id))
            with c3:
                 submission_button = st.button(label="Soumettre")
                 st.write("""<p style="font-size:15px; color:#FF0000;">
                    <b>ATTENTION : Si vous cliquez sur ce bouton, vous ne pourrez plus modifier votre formulaire </b> </p>  """, unsafe_allow_html=True)
                 if submission_button:
                    # liste des id2022 non remplies
                    non_remplies = []
                    # liste des id2022 avec des NA
                    na = []
                    for question_id in questions_ids_2022_inclus_taux:
                        if st.session_state[question_id + "_reponse_2022"]=="":
                            non_remplies.append(question_id)
                        elif st.session_state[question_id + "_reponse_2022"]=="NA":
                            na.append(question_id)
                    if non_remplies or na:
                        # st.error("Certaines données ne sont pas remplies ou contiennent la valeur 'NA'", icon="🚨")
                        
                        st.write("Les données non remplies sont les suivantes :")
                        for question_id in non_remplies :
                            st.write(question_id) 
                        
                        st.write("Les données contenant la valeur 'NA' sont les suivantes")
                        for question_id in na :
                            st.write(question_id) 
                    else:
                        st.success("Vous avez bien soumis votre formulaire. Vous pouvez fermer l'application. Nous vous remercions pour votre participation", icon="✅")
