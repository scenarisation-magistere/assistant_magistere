# Questions configuration for Contraintes Formation (second form)

QUESTIONS_CONTRAINTES = [
	{
		"id": 1,
		"type": "radio",
		"question": "❓ Nombre estimé de participants",
		"options": [
			"Moins de 10 personnes",
			"Entre 10 et 20 personnes (format idéal CMO)",
			"Entre 21 et 30 personnes (possible mais demande une animation renforcée)",
			"Plus de 30 personnes (déconseillé dans le scénario CMO)"
		],
		"field_name": "nombre_participants"
	},
	{
		"id": 2,
		"type": "radio",
		"question": "❓ Modalités d’animation",
		"options": [
			"Un seul formateur",
			"Co-animation (plusieurs formateurs)"
		],
		"field_name": "animation"
	},
	{
		"id": 3,
		"type": "radio",
		"question": "❓ Exigences institutionnelles particulières (précisez le cas échéant)",
		"options": [
			"Aucune exigence identifiée",
			"Exigence institutionnelle particulière"
		],
		"field_name": "exigences_institutionnelles",
		"text_input_options": [
			"Exigence institutionnelle particulière"
		],
		"text_placeholder": "Précisez (ex. validation INSPE, PAF, certification...)",
		"text_placeholder_map": {
			"Exigence institutionnelle particulière": "Précisez (ex. validation INSPE, PAF, certification...)"
		}
	},
	{
		"id": 4,
		"type": "radio",
		"question": "❓ Restrictions techniques particulières (précisez le cas échéant)",
		"options": [
			"Aucune restriction identifiée",
			"Restriction technique"
		],
		"field_name": "restrictions_techniques",
		"text_input_options": [
			"Restriction technique"
		],
		"text_placeholder": "Précisez (ex. pas de visioconf., bande passante, outils, RGPD...)",
		"text_placeholder_map": {
			"Restriction technique": "Précisez (ex. pas de visioconf., bande passante, outils, RGPD...)"
		}
	}
] 