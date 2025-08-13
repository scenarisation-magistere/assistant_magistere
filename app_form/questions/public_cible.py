# Questions configuration for Public Cible (first form)

QUESTIONS_PUBLIC_CIBLE = [
    {
        "id": 1,
        "type": "text",
        "question": "Quel est le titre (ou projet de titre) de ta formation ?",
        "examples": [
            "Développer les compétences orales en classe hétérogène",
            "Améliorer la gestion de classe avec les outils numériques",
            "Développer des compétences orales en classe hétérogène"
        ],
        "field_name": "titre_formation"
    },
    {
        "id": 2,
        "type": "textarea",
        "question": "Quel est l'objectif général de cette formation ?",
        "examples": [
            "Accompagner les enseignants à concevoir et animer des activités permettant aux élèves de s'exprimer oralement avec confiance et clarté.",
            "Accompagner les enseignants dans l'utilisation des outils numériques pour améliorer la gestion de la classe et favoriser l'engagement des élèves.",
            "Former les enseignants à l'animation de discussions et de débats en classe en utilisant des ressources multimédia adaptées."
        ],
        "field_name": "objectif_general"
    },
    {
        "id": 3,
        "type": "checkbox",
        "question": "Quel est le type de public visé ? (plusieurs réponses possibles)",
        "options": [
            "Enseignants 1er degré",
            "Enseignants 2d degré",
            "Formateurs académiques",
            "Formateurs INSPE / chercheurs",
            "Inspecteurs",
            "Équipes pluri-catégorielles",
            "Autre (à préciser)"
        ],
        "field_name": "type_de_public"
    },
    {
        "id": 4,
        "type": "radio",
        "question": "Quel est le niveau d'expertise global du public visé ?",
        "options": [
            "Débutant",
            "Intermédiaire",
            "Avancé",
            "Expert ou formateur confirmé",
            "Je ne sais pas encore"
        ],
        "field_name": "niveau_expertise"
    },
    {
        "id": 5,
        "type": "radio",
        "question": "Le groupe est-il homogène ou hétérogène ?",
        "options": [
            "Groupe homogène (mêmes profils, mêmes besoins)",
            "Groupe hétérogène",
            "Je ne sais pas encore"
        ],
        "field_name": "profil_groupe"
    },
    {
        "id": 6,
        "type": "checkbox",
        "question": "Des besoins spécifiques sont-ils connus pour ce public ?",
        "options": [
            "Aucun besoin identifié",
            "Préférence pour certaines modalités (oral, écrit, visuel…)",
            "Besoins liés à l'accessibilité (supports adaptés, ajustements pour mieux comprendre et participer)",
            "Besoins spécifiques d'accompagnement dans certaines compétences ou outils (par exemple, pour renforcer la confiance dans l'utilisation du numérique, etc.)"
        ],
        "field_name": "besoins_specifiques"
    }
] 