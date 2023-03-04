import numpy as np
import streamlit as st

def table_lines(url):
            st.markdown(f"<div style='height:40px; background-color:#FFFFFF;color:#000000;font-size:11px;border-radius:2%; text-align: left; border: 1.5px solid #000000; padding:10px;  '>{url}</div>", unsafe_allow_html=True)
            st.markdown('######')

def line_name(url):
    st.markdown(f"<div style='height:40px; background-color:#FFFFFF;color:#000000;font-size:11px;border-radius:2%; text-align: left; border: 1.5px solid #000000; padding:5px;  '>{url}</div>", unsafe_allow_html=True)

def table_cases(text, font_size, color, background_color):
    st.markdown(f"<div style='height:39px;font-size:{font_size}px; color:#{color};background-color:#{background_color}; border-radius:2%; text-align: center; padding:10px;  display:flex; align-items:center; justify-content:center;'>{text}</div>", unsafe_allow_html=True)
    st.markdown('######')

def rectangle_with_text(height, text, color, background, font_size, padding, border):
    st.markdown("<div style='height:{}px; color:#{}; background-color:#{}; display:flex; align-items:center; justify-content:center; text-align: center; font-size:{}px; padding:{}px; border: {}px solid #000000;'>{}</div>".format(height, color, background, font_size, padding, border, text), unsafe_allow_html=True)

def thematic_titles(height, text):
    st.markdown("<div style='height:{}px; color:#FFFFFF; background-color:#4472C4; display:flex; align-items:center; justify-content:left; font-size:22px; padding:8px;'>{}</div>".format(height, text), unsafe_allow_html=True)
    st.markdown('######')

def section_titles(height, text):
    st.markdown("<div style='height:{}px; color:#000000; background-color:#deeaf6; display:flex; align-items:center; justify-content:left; font-size:18px; padding:8px;'>{}</div>".format(height, text), unsafe_allow_html=True)
    st.markdown('######')

def sub_section_titles(height, text):
    st.markdown("<div style='height:{}px; color:#000000; background-color:#ededed; display:flex; align-items:center; justify-content:left; font-size:16px; padding:8px; '>{}</div>".format(height, text), unsafe_allow_html=True)
    st.markdown('######')

def val_int(feature):
            if not st.session_state[feature].isdigit() and st.session_state[feature] != "" :
                st.session_state[feature] ="🚫entier attendu"

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
      
def val_float(feature):
            value = st.session_state[feature]
            if not isfloat(value):
                if isfloat(value.replace(',', '.')):
                    st.write("ok")
                    st.session_state[feature] =value.replace(',', '.')
                elif value!="":
                    st.session_state[feature] ="🚫décimal attendu"
            # if not isfloat(st.session_state[feature]) and st.session_state[feature] != "" :
            #     st.session_state[feature] ="🚫décimal attendu"

def currency_format(value):
    if isfloat(value):
        return "{:,.2f}€".format(float(value))
    else:
        value = float(value.replace(',', '.'))
        return "{:,.2f}€".format(value)
    
def val_currency(feature):
    value = st.session_state[feature]
    if not isfloat(value):
        if isfloat(value.replace(',', '.')):
            st.write("ok")
            st.session_state[feature] =value.replace(',', '.')
        elif value!="":
            st.session_state[feature] ="🚫décimal attendu"
    # else:
    #     st.s
    # if isfloat(value):
    #     st.session_state[feature] ="{:,.2f}".format(float(value))
    # elif isfloat(value.replace(',', '.')):
    #     st.session_state[feature] ="{:,.2f}".format(float(value.replace(',', '.')))
    # else:
    #     st.session_state[feature] ="🚫décimal attendu"

def val_modification(updated_key, raison_key, value_type):
    """
    Oblige de renseigner la raison de la modification
    """
    if st.session_state[updated_key]!="":
        st.session_state[raison_key] = "🚫Veuillez renseigner la raison"
        if value_type=="float":
            val_float(updated_key)
        elif value_type == "int":
            val_int(updated_key)
        elif value_type=="currency":
            val_currency(updated_key)
    else:
        st.session_state[raison_key] = ""


# def display_colomn(keys_list):
#             for key in keys_list:
#                 st.text_input("", label_visibility="collapsed", on_change=val_int, args=[key], key=key)

# def pourcentage_column(keys_22_l, keys_21_l):
#             for k in range(len(keys_22_l)):
#                 # key = taxe_evol[k]
#                 key_22 =  keys_22_l[k]
#                 value_22 = st.session_state[key_22]
#                 key_21 = keys_21_l[k]
#                 value_21 = st.session_state[key_21]
#                 if value_22.isdigit() and value_21.isdigit() :
#                     pourcentage = (int(value_22) - int(value_21) )/ int(value_21)
#                     pourcentage = int(pourcentage*100)
#                     if pourcentage >=0 :
#                         table_cases("+" + str(pourcentage) + "%", font_size=15, color="000000", background_color="e2f0d9")
#                     else:
#                         table_cases(str(pourcentage) + "%", font_size=15, color="000000", background_color="ffc7ce")
#                 else:
#                     table_cases("", font_size=15, color="000000", background_color="d9d9d9")

def pourcentage_2_keys(key_22, key_21):
            value_22 = st.session_state[key_22]
            value_21 = st.session_state[key_21]
            if isfloat(value_22) and isfloat(value_21) and value_21!=0:
                pourcentage = (float(value_22) - float(value_21) )/ float(value_21)
                pourcentage = int(pourcentage*100)
                if pourcentage >=0 :
                    table_cases("+" + str(pourcentage) + "%", font_size=15, color="000000", background_color="e2f0d9")
                else:
                    table_cases(str(pourcentage) + "%", font_size=15, color="000000", background_color="ffc7ce")
            else:
                table_cases("", font_size=15, color="000000", background_color="d9d9d9")

def somme_2_keys(key_2022, key_2021, sum_key_name):
    sum = 0.00
    value_2022 = st.session_state[key_2022]
    value_2021 = st.session_state[key_2021]
    if isfloat(value_2022) and isfloat(value_2021):
        sum = float(value_2022)+float(value_2021)
    if sum!=0:    
        sum = np.round(sum, 1)
        table_cases(sum, font_size=15, color="000000", background_color="d9d9d9")
    else:
        sum = "NA"
        table_cases(sum, font_size=15, color="000000", background_color="d9d9d9")
    st.session_state[sum_key_name] = sum

def divide_2_keys(key_numerateur, key_denominateur, division_key_name):
    division = "NA"
    value_numerateur = st.session_state[key_numerateur]
    value_denominateur = st.session_state[key_denominateur]
    if isfloat(value_numerateur) and isfloat(value_denominateur) and value_denominateur!=0:
        division = float(value_numerateur)/float(value_denominateur)
        division = np.round(division, 1)
        
    table_cases(division, font_size=15, color="000000", background_color="d9d9d9")
    st.session_state[division_key_name] = division

def display_sum(list_key, total_key_name, currency):
    sum = 0.00
    for key in list_key:
        value = st.session_state[key]
        if isfloat(value):
            sum += float(value)
        elif value == "":
                continue
        else:
            sum = "NA"
            break
    
    st.session_state[total_key_name] = sum
    if isfloat(sum) and currency==True:
            table_cases("{:,.2f}€".format(sum), font_size=14, color="000000", background_color="d9d9d9")
    else:
        table_cases(sum, font_size=14, color="000000", background_color="d9d9d9")

    


def display_sum_updated(questions_ids, total_updated_key_name, values_2021, currency):
    sum = 0.00
    for question_id in questions_ids:
        value_2021_updated = st.session_state[question_id + "_reponse_2021_updated"]
        if isfloat(value_2021_updated):
            sum += float(value_2021_updated)
        elif value_2021_updated == "":
            value_2021 = values_2021[question_id + "_reponse_2021"]
            value_2021 = value_2021.replace(',', '.')
            # st.write(type(value_2021))
            if isfloat(value_2021):
                sum += float(value_2021)
            else:
                st.write("cas 2")
                sum = 'NA'
                break
        else:
            sum = 'NA'
            break
    
    st.session_state[total_updated_key_name] = sum

    if isfloat(sum) and currency==True:
            table_cases("{:,.2f}€".format(sum), font_size=14, color="000000", background_color="d9d9d9")
    else:
        table_cases(sum, font_size=15, color="000000", background_color="d9d9d9")




def display_table(dict, cols, columns_widths, values_2022, values_2021, height_size):
            nb_lines = len(list(dict.values())[0][1])
            for num_line in range(nb_lines) :
                # if num_line <= 3:
                #     list_columns = cols
                # else:
                list_columns = st.columns(columns_widths)
                # nb_cols = len(dict.keys())
                for num_col in dict.keys():
                    col = list_columns[num_col-1]
                    with col :
                        type_col = dict[num_col][0]
                        if type_col == "line_name" :
                            if height_size == "small":
                                table_lines(dict[num_col][1][num_line])
                            else:
                                line_name(dict[num_col][1][num_line])
                        
                        elif type_col == "static_line":
                            value = dict[num_col][1][num_line]    # dict[num_col] = ["static_line", 2021_reponses_values]
                            table_cases(value, font_size=12, color="000000", background_color="d9d9d9")

                        elif type_col == "int":
                            key = dict[num_col][1][num_line]        
                            st.text_input("", label_visibility="collapsed", on_change=val_int, args=[key], key=key)

                        # elif type_col == "int_2021":
                        #     key = dict[num_col][1][num_line]
                        #     st.text_input("", label_visibility="collapsed", on_change=val_int, args=[key], key=key)

                        elif type_col == "float":
                            key = dict[num_col][1][num_line]    # dict[num_col] = ["float",commune_keys]
                            st.text_input("", label_visibility="collapsed", on_change=val_float, args=[key], key=key)
                        
                        elif type_col=="float_2022":
                            key = dict[num_col][1][num_line] + "_reponse_2022"  # key_reponse_2022 = question_id + "_reponse_2022"
                            st.text_input("", label_visibility="collapsed", key=key, value=values_2022[""], on_change=val_float, args=[key])

                        elif type_col == "evol" :
                            key_22 =  dict[num_col][1][num_line]
                            value_22 = st.session_state[key_22]
                            key_21 = dict[num_col][2][num_line]
                            value_21 = st.session_state[key_21]
                            if value_22.isdigit() and value_21.isdigit() :
                                pourcentage = (int(value_22) - int(value_21) )/ int(value_21)
                                pourcentage = int(pourcentage*100)
                                if pourcentage >=0 :
                                    table_cases("+" + str(pourcentage) + "%", font_size=15, color="000000", background_color="e2f0d9")
                                else:
                                    table_cases(str(pourcentage) + "%", font_size=15, color="000000", background_color="ffc7ce")
                            else:
                                table_cases("", font_size=15, color="000000", background_color="d9d9d9")

                        elif type_col == "tot":
                            sum = 0.00
                            listes_keys = dict[num_col][1:]             # listes_keys = [hors_region, region, commune]
                            for list_key in listes_keys:                # list_keys = hors_region
                                key = list_key[num_line]
                                value = st.session_state[key]
                                if isfloat(value):
                                    sum += float(value)
                                elif value == "":
                                     pass
                                else:
                                    break
                            # st.text_input("", label_visibility="collapsed", value=str(sum), disabled=True, key="tot" + str(dict[1][1][num_line]))
                            st.session_state["tot" + str(dict[1][1][num_line])] = sum
                            table_cases(sum, font_size=15, color="000000", background_color="d9d9d9")

def display_table_2021(columns_widths, line_names, questions_ids, questions_values_types, display_booleans, lists_for_selectbox, height_size, values_2022, values_2021):
    list_columns = st.columns(columns_widths)
    with list_columns[1]:
        text = "Année 2022"
        rectangle_with_text(40.5, text, color="FFFFFF", background="009999", font_size=12, padding=8, border=1)
    with list_columns[2]:
        text = "Année 2021"
        rectangle_with_text(40.5, text, color="000000", background="A6A6A6", font_size=12, padding=8, border=1)
    with list_columns[3]:
        text = "Modification de la donnée 2021"
        rectangle_with_text(40.5, text, color="000000", background="fbe4d5", font_size=12, padding=8, border=1)
    with list_columns[4]:
        text = "Raison de la modification"
        rectangle_with_text(40.5, text, color="000000", background="fbe4d5", font_size=12, padding=8, border=1)

    nb_lines = len(questions_ids)
    for num_line in range(nb_lines) :
        question_id = questions_ids[num_line]
        value_type = questions_values_types[num_line]
        list_columns = st.columns(columns_widths)
        # line names
        with list_columns[0]:
            if height_size == "small":
                table_lines(line_names[num_line])
            else:
                line_name(line_names[num_line])
        # 2022
        ### MODIFY THE 2022 VALUES
        with list_columns[1]:
            key = question_id + "_reponse_2022"
            if value_type=="float":
                st.text_input("", label_visibility="collapsed", key=key, value=values_2022[""], on_change=val_float, args=[key])
            elif value_type=="currency":
                st.text_input("", label_visibility="collapsed", key=key, value=values_2022[""], on_change=val_currency, args=[key])
            elif value_type=="int":
                st.text_input("", label_visibility="collapsed", key=key, value=values_2022[""], on_change=val_int, args=[key])
            elif value_type=="select_box":
                options = lists_for_selectbox[num_line]
                st.selectbox("", options=options, label_visibility="collapsed", key=key, index=options.index(values_2022[""]))
            else:
                st.text_input("", label_visibility="collapsed", key=key, value=values_2022[""])

        # Est-ce qu'on affiche/modifie la valeur de 2021 ?
        if display_booleans[num_line] == True:
            # valeur de 2021 : non modifiable
            with list_columns[2]:
                if height_size=="small":
                    if value_type=="currency":
                        amount = currency_format(values_2021[question_id + "_reponse_2021"])
                        # amount = float(values_2021[question_id + "_reponse_2021"].replace(',', '.'))
                        table_cases(amount, font_size=14, color="000000", background_color="d9d9d9")
                    else:
                        table_cases(values_2021[question_id + "_reponse_2021"], font_size=14, color="000000", background_color="d9d9d9")

                else:
                    if value_type=="currency":
                        amount = currency_format(values_2021[question_id + "_reponse_2021"])
                        table_cases(amount, font_size=10, color="000000", background_color="d9d9d9")
                    else:
                        table_cases(values_2021[question_id + "_reponse_2021"], font_size=10, color="000000", background_color="d9d9d9")
            
            # reponse_2021_updated
            with list_columns[3]:
                key = question_id + "_reponse_2021_updated"
                if value_type=="float":
                    st.text_input("", label_visibility="collapsed", key=key, value=values_2021[key], on_change=val_modification, args=[key, question_id+ "_raison_modification_2021", "float"])
                elif value_type=="currency":
                    st.text_input("", label_visibility="collapsed", key=key, value=values_2021[key], on_change=val_modification, args=[key, question_id+ "_raison_modification_2021", "currency"])
                elif value_type=="int":
                    st.text_input("", label_visibility="collapsed", key=key, value=values_2021[key], on_change=val_modification, args=[key, question_id+ "_raison_modification_2021", "int"])
                elif value_type=="select_box":
                    options = lists_for_selectbox[num_line]
                    st.selectbox("", options=options, label_visibility="collapsed", key=key, index=options.index(values_2021[key]), on_change=val_modification, args=[key, question_id+ "_raison_modification_2021", None])
                else:
                    st.text_input("", label_visibility="collapsed", key=key, value=values_2022[""], on_change=val_modification, args=[key, question_id+ "_raison_modification_2021", None])

            # raison de la modification
            with list_columns[4]:
                key = question_id + "_raison_modification_2021"
                st.text_input("", label_visibility="collapsed", key=key, value=values_2021[key])

def display_table_2022(columns_widths, line_names, questions_ids, questions_values_types, lists_for_selectbox, height_size, values_2022):
    list_columns = st.columns(columns_widths)
    with list_columns[1]:
        text = "Année 2022"
        rectangle_with_text(40.5, text, color="FFFFFF", background="009999", font_size=12, padding=8, border=1)

    nb_lines = len(questions_ids)
    for num_line in range(nb_lines) :
        question_id = questions_ids[num_line]
        value_type = questions_values_types[num_line]
        list_columns = st.columns(columns_widths)
        # line names
        with list_columns[0]:
            if height_size == "small":
                table_lines(line_names[num_line])
            else:
                line_name(line_names[num_line])
        # 2022
        ### MODIFY THE 2022 VALUES
        with list_columns[1]:
            key = question_id + "_reponse_2022"
            if value_type=="float":
                st.text_input("", label_visibility="collapsed", key=key, value=values_2022[""], on_change=val_float, args=[key])
            elif value_type=="currency":
                st.text_input("", label_visibility="collapsed", key=key, value=values_2022[""], on_change=val_currency, args=[key])
            elif value_type=="int":
                st.text_input("", label_visibility="collapsed", key=key, value=values_2022[""], on_change=val_int, args=[key])
            elif value_type=="select_box":
                options = lists_for_selectbox[num_line]
                st.selectbox("", options=options, label_visibility="collapsed", key=key, index=options.index(values_2022[""]))
            else:
                st.text_input("", label_visibility="collapsed", key=key, value=values_2022[""])

def display_moyenne_2022(question_id, values_2022):
    ### A ENLEVER CAR DEJA FAIT AU DEBUT NORMALEMENT
    values_2022[question_id + "_nombre_repondants_2022"] = 20

    nombre_repondants = values_2022[question_id + "_nombre_repondants_2022"]
    if nombre_repondants>1:
        ### A ENLEVER CAR DEJA FAIT AU DEBUT NORMALEMENT
        values_2022[question_id + "_moyenne_2022"] = 0.7

        moyenne = values_2022[question_id + "_moyenne_2022"]
        text = str(moyenne) + " (sur " + str(nombre_repondants) + " répondants)"
        table_cases(text, font_size=14, color="000000", background_color="d9d9d9")
    else:
        table_cases("Pas assez de répondants", font_size=14, color="000000", background_color="d9d9d9")


def display_ecart_moyenne_2022(question_id, values_2022):
    ### A ENLEVER CAR DEJA FAIT AU DEBUT NORMALEMENT
    values_2022[question_id + "_nombre_repondants_2022"] = 20

    nombre_repondants = values_2022[question_id + "_nombre_repondants_2022"]
    if nombre_repondants>1:
        ### A ENLEVER CAR DEJA FAIT AU DEBUT NORMALEMENT
        values_2022[question_id + "_moyenne_2022"] = 0.7

        moyenne = values_2022[question_id + "_moyenne_2022"]
        

        value_2022 = st.session_state[question_id + "_reponse_2022"]
        
        ### On suppose que la moyenne est bien un float dans la BDD donc pas besoin de vérifier ici
        if isfloat(value_2022)  and moyenne!=0:
            pourcentage = (float(value_2022) - moyenne)/ moyenne
            pourcentage = int(pourcentage*100)
            if pourcentage >=0 :
                table_cases("+" + str(pourcentage) + "%", font_size=14, color="000000", background_color="e2f0d9")
            else:
                table_cases(str(pourcentage) + "%", font_size=14, color="000000", background_color="ffc7ce")
        else:
            table_cases("NA", font_size=14, color="000000", background_color="d9d9d9")
    else:
        table_cases("Pas assez de répondants", font_size=14, color="000000", background_color="d9d9d9")