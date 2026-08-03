import pandas as pd
import os


OUTPUT = "kobo/evaluation_application_web.xlsx"


os.makedirs("kobo", exist_ok=True)


# =====================================================
# SURVEY
# =====================================================

survey = [

# -------------------------
# SECTION 1
# -------------------------

{
"type":"begin_group",
"name":"section1",
"label":"SECTION 1 : Informations sur l’évaluateur"
},


{
"type":"date",
"name":"date_evaluation",
"label":"Date de l’évaluation",
"required":"yes"
},


{
"type":"text",
"name":"nom_evaluateur",
"label":"Votre nom (facultatif)"
},


{
"type":"select_one role",
"name":"role",
"label":"Votre rôle / profession",
"required":"yes"
},


{
"type":"text",
"name":"autre_profession",
"label":"Autre profession",
"required":"${role}='Autre'",
"relevant":"${role}='Autre'"
},


{
"type":"select_one acces",
"name":"acces_application",
"label":"Comment avez-vous accédé à l’application ?",
"required":"yes"
},


{
"type":"select_one oui_non",
"name":"premiere_utilisation",
"label":"Est-ce votre première utilisation de l’application ?",
"required":"yes"
},


{
"type":"select_one frequence",
"name":"nombre_utilisation",
"label":"Combien de fois l’avez-vous utilisée auparavant ?",
"relevant":"${premiere_utilisation}='Non'"
},


{
"type":"end_group"
},



# -------------------------
# SECTION 2
# -------------------------

{
"type":"begin_group",
"name":"section2",
"label":"SECTION 2 : Première impression et interface"
},


{
"type":"select_one echelle",
"name":"interface",
"label":"L’interface est attrayante et bien conçue",
"required":"yes"
},


{
"type":"select_one echelle",
"name":"navigation",
"label":"L’application est facile à naviguer",
"required":"yes"
},


{
"type":"select_one echelle",
"name":"menus",
"label":"Les menus et les boutons sont clairement libellés",
"required":"yes"
},


{
"type":"select_one echelle",
"name":"chargement",
"label":"L’application se charge rapidement",
"required":"yes"
},


{
"type":"select_one echelle",
"name":"appareil",
"label":"L’application fonctionne bien sur mon appareil",
"required":"yes"
},


{
"type":"end_group"
},



# -------------------------
# SECTION 3
# -------------------------

{
"type":"begin_group",
"name":"section3",
"label":"SECTION 3 : Fonctionnalités et performances"
},


{
"type":"select_multiple fonctionnalites",
"name":"fonctionnalites_testees",
"label":"Quelles fonctionnalités avez-vous testées ?",
"required":"yes"
},


{
"type":"select_one echelle",
"name":"besoins",
"label":"Les fonctionnalités répondent à mes besoins",
"required":"yes"
},


{
"type":"select_one echelle",
"name":"facilite",
"label":"Les fonctionnalités sont faciles à utiliser",
"required":"yes"
},


{
"type":"select_one echelle",
"name":"precision",
"label":"Les résultats fournis sont précis",
"required":"yes"
},


{
"type":"select_one echelle",
"name":"efficacite",
"label":"L’application m’aide à accomplir mes tâches efficacement",
"required":"yes"
},


{
"type":"select_one echelle",
"name":"aide",
"label":"Les instructions et l’aide sont claires et utiles",
"required":"yes"
},


{
"type":"end_group"
},



# -------------------------
# SECTION 4
# -------------------------

{
"type":"begin_group",
"name":"section4",
"label":"SECTION 4 : Problèmes rencontrés"
},


{
"type":"select_one oui_non",
"name":"problemes",
"label":"Avez-vous rencontré des problèmes ou des erreurs ?",
"required":"yes"
},


{
"type":"select_multiple problemes_type",
"name":"type_probleme",
"label":"Quel(s) type(s) de problème(s) ?",
"relevant":"${problemes}='Oui'"
},


{
"type":"text",
"name":"description_probleme",
"label":"Veuillez décrire le(s) problème(s) en détail",
"relevant":"${problemes}='Oui'",
"appearance":"multiline"
},


{
"type":"end_group"
},



# -------------------------
# SECTION 5
# -------------------------

{
"type":"begin_group",
"name":"section5",
"label":"SECTION 5 : Satisfaction globale"
},


{
"type":"integer",
"name":"rating",
"label":"Note globale de l’application",
"required":"yes",
"constraint":". >=0 and .<=10",
"constraint_message":"La note doit être comprise entre 0 et 10."
},


{
"type":"calculate",
"name":"niveau_satisfaction",
"label":"Niveau de satisfaction",
"calculation":"if(${rating}>=9,'Excellent',if(${rating}>=7,'Très bon',if(${rating}>=5,'Bon',if(${rating}>=3,'Passable','Médiocre'))))"
},


{
"type":"select_one recommandation",
"name":"recommandation",
"label":"Recommanderiez-vous cette application ?",
"required":"yes"
},


{
"type":"select_one reutilisation",
"name":"utilisation_future",
"label":"Utiliseriez-vous cette application à nouveau ?",
"required":"yes"
},


{
"type":"end_group"
},



# -------------------------
# SECTION 6
# -------------------------

{
"type":"begin_group",
"name":"section6",
"label":"SECTION 6 : Suggestions d’amélioration"
},


{
"type":"text",
"name":"points_forts",
"label":"Quels sont les principaux points forts de cette application ?",
"required":"yes",
"appearance":"multiline"
},


{
"type":"text",
"name":"ameliorations",
"label":"Qu’est-ce qui pourrait être amélioré ?",
"required":"yes",
"appearance":"multiline"
},


{
"type":"text",
"name":"fonctionnalites_manquantes",
"label":"Quelles fonctionnalités manquantes aimeriez-vous voir ajoutées ?",
"appearance":"multiline"
},


{
"type":"text",
"name":"commentaires",
"label":"Commentaires ou suggestions supplémentaires",
"appearance":"multiline"
},


{
"type":"end_group"
}

]


survey_df = pd.DataFrame(survey)



# =====================================================
# CHOICES
# =====================================================

choices=[


["role","Etudiant","Étudiant"],
["role","Enseignant","Enseignant"],
["role","Chercheur","Chercheur"],
["role","Analyste","Analyste de données"],
["role","Developpeur","Développeur"],
["role","Chef","Chef de projet"],
["role","Autre","Autre"],


["acces","Ordinateur","Ordinateur"],
["acces","Tablette","Tablette"],
["acces","Smartphone","Smartphone"],


["oui_non","Oui","Oui"],
["oui_non","Non","Non"],


["frequence","2_3","2 à 3 fois"],
["frequence","4_5","4 à 5 fois"],
["frequence","plus5","Plus de 5 fois"],


["echelle","1","Tout à fait en désaccord"],
["echelle","2","En désaccord"],
["echelle","3","Neutre"],
["echelle","4","D’accord"],
["echelle","5","Tout à fait d’accord"],


["fonctionnalites","scraping","Collecte (scraping) de données"],
["fonctionnalites","download","Téléchargement"],
["fonctionnalites","formulaire","Remplissage du formulaire"],
["fonctionnalites","dashboard","Tableau de bord des données"],


["problemes_type","chargement","Erreur de chargement"],
["problemes_type","affichage","Problème d’affichage"],
["problemes_type","fonction","Fonctionnalité non fonctionnelle"],
["problemes_type","donnees","Perte de données"],
["problemes_type","performance","Performance lente"],
["problemes_type","interface","Interface confuse"],
["problemes_type","autre","Autre"],


["recommandation","oui1","Oui, sans hésiter"],
["recommandation","oui2","Oui, probablement"],
["recommandation","peutetre","Peut-être"],
["recommandation","non1","Probablement pas"],
["recommandation","non2","Non"],


["reutilisation","regulier","Oui, régulièrement"],
["reutilisation","occasionnel","Oui, occasionnellement"],
["reutilisation","peutetre","Peut-être"],
["reutilisation","probablement_non","Probablement pas"],
["reutilisation","non","Non"]

]


choices_df=pd.DataFrame(
choices,
columns=[
"list_name",
"name",
"label"
]
)



# =====================================================
# EXPORT XLSFORM
# =====================================================

with pd.ExcelWriter(
OUTPUT,
engine="openpyxl"
) as writer:


    survey_df.to_excel(
        writer,
        sheet_name="survey",
        index=False
    )


    choices_df.to_excel(
        writer,
        sheet_name="choices",
        index=False
    )



print("================================")
print("XLSForm Kobo créé avec succès")
print(OUTPUT)
print("================================")