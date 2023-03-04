import streamlit as st
from streamlit_option_menu import option_menu

from utils.utils import display_sum, table_lines
from utils.utils import table_cases
from utils.utils import rectangle_with_text
from utils.utils import thematic_titles
from utils.utils import section_titles
from utils.utils import sub_section_titles
from utils.utils import display_table
from utils.utils import pourcentage_2_keys

    
def ot(placeholder) :
    placeholder.empty()

    selected = option_menu(
        menu_title=None,
        ### AJOUTER PREAMBULE
        options=["Préambule", "0.Identité", "1.Capacité touristique", "2.TS & Freq 2022", "Taux de remplissage", "Validation"],
        icons = [],
        orientation = "horizontal",
        styles = {
        "nav-link" : {"font-size" : "13px"}
        }
    )


    if selected == "2.TS & Freq 2022" :
        thematic_titles(40, "2/ TAXE DE SEJOUR et FREQUENTATION ")
        st.write("""<div style="font-size:15px; color:black;">
        <b>Sommaire</b><br/>
        </div>
        <div style="font-size:15px; color:#0563C1;">
        2.1 Taxe de séjour et fréquentation dans la station<br/>
        <blockquote>2.1.1. Types d'activités touristiques de la station<br/>
        2.1.2. Taxe de séjour et fréquentation - hors opérateurs numériques (dans la station)<br/>
        2.1.3. Taxe de séjour et fréquentation - opérateurs numériques (dans la station)<br/>
        2.1.4. Autres données relatives à la fréquentation dans la station<br/> </blockquote>
        2.2. Taxe de séjour et fréquentation en dehors de la station<br/>
        </div>
        """,
        unsafe_allow_html=True)
    
        st.markdown('####')
        st.date_input("Date d'ouverture des thermes :", key="Date d'ouverture des thermes :")
        st.date_input("Date de fermeture des thermes :", key="Date de fermeture des thermes :")
        st.markdown('#')

        # 2.1 TAXE DE SEJOUR et FREQUENTATION DANS LA STATION
        section_titles(30, "2.1 TAXE DE SEJOUR et FREQUENTATION  &nbsp; <u>DANS LA STATION</u> ")

        # 2.1.1. TYPES D'ACTIVITES TOURISTIQUES DE LA STATION
        sub_section_titles(30, "2.1.1. TYPES D'ACTIVITES TOURISTIQUES DE LA STATION")
        st.write("""<p style="font-size:12px; color:black;">
        En vous basant sur votre connaissance du contexte local, pouvez-vous indiquer <b> quelles sont 
        les principales activités touristiques qui attirent des touristes et génèrent des revenus </b>
        dans votre station et ses alentours proches ? Pouvez-vous <b>numéroter ces activités par ordre
        d'importance </b>, avec 1 la plus importante (plusieurs activités peuvent porter le même numéro) ? <br> 
        <b>NB:</b> indiquez N/A pour les activités non pertinentes / non présentes dans votre station.
        </p>
        """,
        unsafe_allow_html=True)


        # Tableau
        c1, c2, c3, c4 = st.columns((4, 1, 1, 3))
        
        # lignes du tableau
        line_names = ["Thermalisme (cures)",
        "Thermoludisme et activites de bien-etre autour de l'eau thermale *",
        "Sports d'hiver",
        "Tourisme balnéaire (plage, sports nautiques, etc.)",
        "Randonnée",
        "Vélo",
        "Autres activités sportives (ex : escalade, etc.)",
        "Fatrimoine culturel (monuments, architecture, musées, théâtres, concerts, artisanat, etc.)",
        "Patrimoine naturel (paysages, nature environnante, etc.)",
        "Gastronomie",
        "Festivals et événementiel",
        "Tourisme d'affaires (y compris salons et foires)",
        "Casino",
        "Autres (préciser)"]
        with c1:
            for line_name in line_names :
                table_lines(line_name)
            st.write("""<div style="height:45px;display: table-cell;vertical-align: middle;text-align: left;font-size:11px; color:black; background-color:#fbe4d5; padding:10px">
        *activités aqualudiques, de bien-être, de détente, réalisées à létablissement 
        thermal ou dans un autre centre (ex: spa), avec ou sans e au thermale. Il s'agit de 
        pratiques  &nbsp; <u>sans suivi médical</u>
        </div>
        """,
        unsafe_allow_html=True)
        #     text = """*activités aqualudiques, de bien-être, de détente, réalisées à létablissement 
        #     thermal ou dans un autre centre (ex: spa), avec ou sans e au thermale. Il s'agit de 
        #     pratiques  &nbsp; <u>sans suivi médical</u> """
        #     rectangle_with_text(70, text, color="OOOOO", background="fbe4d5", font_size=12, padding=8, border=0)
        with c2:
            ### A REMPLACER PAR LES VRAIES KEYS
            for key in line_names:
                st.selectbox("", options=range(0,10), label_visibility="collapsed", key=key)
        with c4:
            text = "Commentaires (préciser) : "
            rectangle_with_text(50, text, color="OOOOO", background="fbe4d5", font_size=15, padding=8, border=0)
            st.text_input("", label_visibility="collapsed", key="2.1.1 comm 1")
            
        # Fin tableau
        st.write("#")

        st.write('#')
        st.write("""<p style="font-size:13px; color:black;">
        <b> Tourisme de réunions, congrès, conventions et voyages de gratification en 2022</b></p>  
        <p style="font-size:13px; color:black;">
        Cette section porte sur le <b>marché du MICE </b>(de l'acrongme anglais "Meetings, 
        incentives, conferencing, exhibitions", "réunions, congrès, conventions et voyages de 
        gratification" en Français). Ce marché est un type de tourisme dans lequel des entreprises 
        organisent des événements pour leurs employés ou leurs clients (par ex. <b>réunions, conférences
        et expositions ou congres)</b>.
        </p>
        """,
        unsafe_allow_html=True)


        st.write("#")
        c1, c2, c3 = st.columns((3,1, 2))
        
        # CHANGER LES KEYS
        with c1:
            st.text_input("""**La station / commune hébergeant la station dispose-t-elle d'une offre 
                          ciblée pour le tourisme MICE en 2022 ?**""", key="2.1.1.1")
            st.text_input("""**Si oui, comment se caractérise cette offre ?** (Présence de sites 
            événementiels et lieux pouvant accueillir des événements professionnels (par ex. salles 
            de sÉminaire, salle de reunion, palais des congres...). En l'absence d'une telle offre,
            indiquer "NA" """, key="2.1.1.2")
            st.text_input("""**Si oui, quel est le chiffre d'affaires lié à cette activité ?** En
            l'absence d'une telle offre, indiquer "NA", en l'absence de la donnée,
            indiquer "NC" """, key="2.1.1.3")
            st.text_input("""**SSi oui quel est le nombre d'emplogés dédiés à cette activité ?** (en ETP).
            En l'absence d'une telle offre, indiquer "NA', en l'absence de la donnée, indiquer "NC" 
            """, key="2.1.1.4")

        with c3:
            text = "Commentaires : "
            rectangle_with_text(50, text, color="OOOOO", background="fbe4d5", font_size=15, padding=8, border=0)
            st.text_input("", label_visibility="collapsed", key="2.1.1 comm 2")
        st.write("#")

        # 2.1.2. TYPES D'ACTIVITES TOURISTIQUES DE LA STATION
        sub_section_titles(30, """2.1.2. TAXE DE SEJOUR et FREQUENTATION (Nombre de nuitées*) - 
                           HORS OPERATEURS NUMERIQUES (dans la station)""")

        # Merged columns
        c1, c2, c3, c4, c5, c6 = st.columns((2, 2, 1, 2, 1, 2))
        
        
        ## 22
        with c2 :
            text = "Valeurs annuelles"
            rectangle_with_text(40, text, color="FFFFFF", background="009999", font_size=11, padding=8, border=1)
        ## 21
        with c4 :
            text = "Valeurs annuelles données en 2021"
            rectangle_with_text(40, text, color="000000", background="fbe4d5", font_size=11, padding=8, border=1)
        ## evolution
        with c6 :
            text = "Evolution 2021 - 2022"
            rectangle_with_text(40, text, color="000000", background="A6A6A6", font_size=11, padding=8, border=1)


        # Sous-colonnes
        c1, c2, c3, c4, c5, c6, c7, c8, c9 = st.columns((2, 1, 1, 1, 1, 1, 1, 1, 1))

        with c1:
            rectangle_with_text(70, "", color="FFFFFF", background="FFFFFF", font_size=11, padding=8, border=0)

        ## 22
        with c2:
            text = "Montant de la taxe de séjour collectée sur le mois (en €)"
            rectangle_with_text(70, text, color="FFFFFF", background="009999", font_size=11, padding=8, border=1)
        
        with c3:
            text = "Nombre de nuitées"
            rectangle_with_text(70, text, color="FFFFFF", background="009999", font_size=11, padding=8, border=1)
        
        ## 21
        with c5:
            text = "Taxe de séjour"
            rectangle_with_text(70, text, color="000000", background="fbe4d5", font_size=11, padding=8, border=1)
        with c6:
            text = "Nuitées"
            rectangle_with_text(70, text, color="000000", background="fbe4d5", font_size=11, padding=8, border=1)
        
        ## evolution
        with c8:
            text = "Taxe de séjour"
            rectangle_with_text(70, text, color="000000", background="A6A6A6", font_size=11, padding=8, border=1)
        with c9:
            text = "Nuitées"
            rectangle_with_text(70, text, color="000000", background="A6A6A6", font_size=11, padding=8, border=1)
        
        # Lignes du tableau
        line_names = ["Gîtes et meublés de tourisme", "Résidences de tourisme", "Palaces", "Hôtels", "Villages de vacances", "Chambres d'hôtes", "Camping", "Camping-car", "Auberges de jeunesse - Centres sportifs"]
        
        taxe_22_keys = ["2022_taxe_gites", "2022_taxe_residences", "2022_taxe_palaces", "2022_taxe_hotels", "2022_taxe_villages", "2022_taxe_chambres", "2022_taxe_camping", "2022_taxe_camping_car", "2022_taxe_auberge"]
        nuitees_22_keys = ["2022_nuitees_gites", "2022_nuitees_residences", "2022_nuitees_palaces", "2022_nuitees_hotels", "2022_nuitees_villages", "2022_nuitees_chambres", "2022_nuitees_camping", "2022_nuitees_camping_car", "2022_nuitees_auberge"]
        
        taxe_21_keys = ["2021_taxe_gites", "2021_taxe_residences", "2021_taxe_palaces", "2021_taxe_hotels", "2021_taxe_villages", "2021_taxe_chambres", "2021_taxe_camping", "2021_taxe_camping_car", "2021_taxe_auberge"]
        nuitees_21_keys = ["2021_nuitees_gites", "2021_nuitees_residences", "2021_nuitees_palaces", "2021_nuitees_hotels", "2021_nuitees_villages", "2021_nuitees_chambres", "2021_nuitees_camping", "2021_nuitees_camping_car", "2021_nuitees_auberge"]
        
        columns_widths = (2, 1, 1, 1, 1, 1, 1, 1, 1)
        dict = {1:["line_name", line_names], 2:["int",taxe_22_keys], 3:["int", nuitees_22_keys], 5:["int", taxe_21_keys], 6:["int", nuitees_21_keys], 8:["evol", taxe_22_keys, taxe_21_keys], 9:["evol", nuitees_22_keys, nuitees_21_keys]}
        
        display_table(dict, (c1, c2, c3, c4, c5, c6, c7, c8, c9), columns_widths, values_2022={}, values_2021={}, height_size="small")

        c1, c2, c3, c4, c5, c6, c7, c8, c9 = st.columns((2, 1, 1, 1, 1, 1, 1, 1, 1))
        with c1:
            text = "TOTAL"
            st.markdown("<div style='height:40px; color:#000000; background-color:#A6A6A6; display:flex; align-items:center; justify-content:right; text-align: right; font-size:13px; padding:8px; border: 1px solid #000000;'>{}</div>".format(text), unsafe_allow_html=True)
        with c2:
            display_sum(taxe_22_keys, "tot_taxe_22")  
        with c3:
            display_sum(nuitees_22_keys, "tot_nuitees_22") 
        with c5:
            display_sum(taxe_21_keys, "tot_taxe_21")
        with c6:
            display_sum(nuitees_21_keys, "tot_nuitees_21")
        with c8:
            pourcentage_2_keys("tot_taxe_22", "tot_taxe_21")
        with c9:
            pourcentage_2_keys("tot_nuitees_22", "tot_nuitees_21")

        