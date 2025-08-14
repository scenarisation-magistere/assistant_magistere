# Questions configuration for Contraintes Formation (second form)

QUESTIONS_CONTRAINTES = [
    {
        "id": 1,
        "type": "radio",
        "question": "Type de parcours",
        "description": "Création d'un nouvel espace ou migration d'un parcours existant ?",
        "options": [
            "Création d'un nouvel espace",
            "Migration d'un parcours existant"
        ],
        "field_name": "type_parcours"
    },
    {
        "id": 2,
        "type": "radio",
        "question": "Temps estimé de la formation",
        "options": [
            "Moins de 3h — Recommandé par la CMO",
            "Entre 3h et 6h",
            "6h ou plus"
        ],
        "field_name": "temps_total"
    },
    {
        "id": 3,
        "type": "radio",
        "question": "Autonomie souhaitée des participants",
        "options": [
            "Autoformation (sans accompagnement)",
            "Formation tutorée (accompagnement ponctuel) — Recommandé par la CMO"
        ],
        "field_name": "autonomie"
    },
    {
        "id": 4,
        "type": "radio",
        "question": "Modalités d'animation",
        "options": [
            "Formation animée par un seul intervenant",
            "Coanimation prévue (2 intervenants ou plus)"
        ],
        "field_name": "animation"
    },
    {
        "id": 5,
        "type": "radio",
        "question": "Contraintes de calendrier",
        "options": [
            "Début d'année scolaire",
            "2e trimestre",
            "Fin d'année",
            "Période imposée – précisez"
        ],
        "field_name": "calendrier",
        "text_input_options": ["Période imposée – précisez"],
        "text_placeholder": "Précisez la période imposée..."
    },
    {
        "id": 6,
        "type": "radio",
        "question": "Contraintes d'horaires (temps synchrone)",
        "options": [
            "Sur temps de travail (journée / service)",
            "Hors temps de travail (soir, à partir de 17h00)",
            "Horaires précis à définir – précisez"
        ],
        "field_name": "horaires",
        "text_input_options": ["Horaires précis à définir – précisez"],
        "text_placeholder": "Précisez les horaires..."
    },
    {
        "id": 7,
        "type": "radio",
        "question": "Nombre estimé de participants",
        "options": [
            "Moins de 10 personnes",
            "Entre 10 et 20 personnes",
            "Plus de 20 personnes",
            "Autoformation (public illimité)"
        ],
        "field_name": "nombre_participants"
    },
    {
        "id": 8,
        "type": "radio",
        "question": "Exigences institutionnelles particulières",
        "options": [
            "Oui – à préciser",
            "Non"
        ],
        "field_name": "exigences_institutionnelles",
        "text_input_options": ["Oui – à préciser"],
        "text_placeholder": "Précisez les exigences institutionnelles..."
    },
    {
        "id": 9,
        "type": "radio",
        "question": "Restrictions techniques connues",
        "options": [
            "Oui – à préciser",
            "Non"
        ],
        "field_name": "restrictions_techniques",
        "text_input_options": ["Oui – à préciser"],
        "text_placeholder": "Précisez les restrictions techniques..."
    }
] 