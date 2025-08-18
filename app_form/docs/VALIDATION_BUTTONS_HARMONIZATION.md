# Validation Buttons Harmonization

## Overview

This document summarizes the harmonization of validation buttons across all templates to ensure consistent behavior and navigation based on the `pages_config.py` configuration.

## Changes Made

### 1. Common JavaScript Functions

Created `app_form/static/js/common_validation.js` with harmonized functions:
- `createHarmonizedSubmitButton()` - Creates standardized submit button handlers
- `processFormData()` - Common form data processing
- `showSuccessModal()` - Standardized success modal display
- `continueToNextStep()` - Navigation to next page
- `goToPreviousStep()` / `goToNextStep()` - Navigation functions

### 2. Common Templates

Created reusable template includes:
- `app_form/templates/includes/success_modal.html` - Standardized success modal
- `app_form/templates/includes/navigation_buttons.html` - Standardized navigation buttons

### 3. Configuration Updates

Updated `app_form/config/pages_config.py`:
- Added `get_page_name_by_step()` function for dynamic page name resolution
- Enhanced navigation helper functions

### 4. Template Updates

#### Public Cible (`public_cible.html`)
- ✅ Updated submit button text to use dynamic page names
- ✅ Replaced custom navigation buttons with common template
- ✅ Replaced custom success modal with common template
- ✅ Updated JavaScript to use harmonized submit handler

#### Contraintes (`contraintes.html`)
- ✅ Updated submit button text to use dynamic page names
- ✅ Replaced custom navigation buttons with common template
- ✅ Replaced custom success modal with common template
- ✅ Updated JavaScript to use harmonized submit handler with custom data processor

#### Scenario (`scenario.html`)
- ✅ Updated submit button text to use dynamic page names
- ✅ Replaced custom navigation buttons with common template
- ✅ Updated JavaScript to use harmonized submit handler

#### Compétences (`competences.html`)
- ✅ Updated submit button text to use dynamic page names
- ✅ Replaced custom success modal with common template
- ✅ Maintained complex functionality while harmonizing navigation

#### Référentiels (`referentiels.html`)
- ✅ Updated final validation button text to use dynamic page names
- ✅ Replaced custom navigation buttons with common template

#### Contenus (`contenus.html`)
- ✅ Updated final validation button text to use dynamic page names
- ✅ Replaced custom navigation buttons with common template

## Benefits

### 1. Consistency
- All submit buttons now follow the same pattern: "✅ Valider et Continuer vers [Next Page Name]"
- Navigation buttons are identical across all pages
- Success modals have consistent structure and behavior

### 2. Maintainability
- Changes to button behavior can be made in one place (`common_validation.js`)
- Navigation logic is centralized in `pages_config.py`
- Template includes reduce code duplication

### 3. Dynamic Navigation
- Button text automatically updates based on page configuration
- Navigation routes are determined by `pages_config.py`
- No hardcoded page names or routes

### 4. Error Handling
- Standardized error handling across all forms
- Consistent loading states and user feedback
- Unified success/error modal behavior

## Usage

### For New Pages
1. Include the common JavaScript: `<script src="{{ url_for('static', filename='js/common_validation.js') }}"></script>`
2. Include navigation buttons: `{% include 'includes/navigation_buttons.html' %}`
3. Include success modal: `{% include 'includes/success_modal.html' %}`
4. Override navigation functions for template-specific logic
5. Use `createHarmonizedSubmitButton()` for form submission

### Example Implementation
```javascript
// Override navigation functions
function getNextRouteFromNavInfo() {
    {% if nav_info and nav_info.next_route %}
        return '{{ nav_info.next_route }}';
    {% endif %}
    return null;
}

// Create harmonized submit button
const submitHandler = createHarmonizedSubmitButton({
    buttonId: 'submitBtn',
    buttonText: '✅ Valider et Continuer vers {{ get_page_name_by_step(nav_info.step + 1) }}',
    endpoint: '/submit_endpoint',
    dataProcessor: () => processFormData('formId'),
    loadingText: '⏳ Sauvegarde en cours...'
});

// Attach to form
document.getElementById('questionnaireForm').addEventListener('submit', submitHandler);
```

## Page Order (from pages_config.py)

1. **Public Cible** (Step 1) → Contraintes
2. **Contraintes** (Step 2) → Compétences  
3. **Compétences** (Step 3) → Référentiels
4. **Référentiels** (Step 4) → Contenus
5. **Contenus** (Step 5) → Export
6. **Export** (Step 6) → End

## Notes

- All validation buttons now save data to YAML and navigate to the next page
- Navigation is fully dependent on `pages_config.py` configuration
- Success modals show YAML data and provide navigation options
- Error handling is consistent across all forms
- Loading states provide user feedback during submission
