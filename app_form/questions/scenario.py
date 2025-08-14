# CMO Scenario structure

CMO_SCENARIO = {
    "title": "Scénario structuré recommandé – Communauté Magistère Occitanie (CMO)",
    "description": "Le scénario CMO propose une structuration claire et précise de la formation :",
    "features": [
        "Prise en compte du public cible : qualité, niveau, besoins particuliers",
        "Prise en compte des contraintes de la formation",
        "Modalités : hybride asynchrone (majeure) et synchrone (mineur)",
        "3 à 4 compétences cibles écrites sous formes de verbes d'action dans les domaines cognitif et affectif",
        "Au maximum 8 sections"
    ],
    "sections": [
        {"number": 1, "type": "Accueil", "content": "Présentation générale de la formation, objectifs, déroulé", "modality": "Asynchrone"},
        {"number": 2, "type": "Section d'apprentissage 1", "content": "Compétence 1 – Ressource, activité(s), référentiel, badge, discussion associée", "modality": "Asynchrone"},
        {"number": 3, "type": "Section d'apprentissage 2", "content": "Compétence 2 – Idem", "modality": "Asynchrone"},
        {"number": 4, "type": "Section d'apprentissage 3", "content": "Compétence 3 – Idem", "modality": "Asynchrone"},
        {"number": 5, "type": "Section d'apprentissage 4", "content": "Idem (optionnelle)", "modality": "Asynchrone"},
        {"number": 6, "type": "Classe virtuelle (BBB)", "content": "Point intermédiaire, accompagnement à la demande, approfondissement", "modality": "Synchrone"},
        {"number": 7, "type": "Forum général", "content": "Discussions regroupées par compétence", "modality": "Asynchrone"},
        {"number": 8, "type": "Évaluation de satisfaction", "content": "Bilan à court, moyen et long terme", "modality": "Asynchrone"}
    ],
    "constraints": [
        "Durée de 3h maximum",
        "Poids total de 512 Mo maximum"
    ]
} 