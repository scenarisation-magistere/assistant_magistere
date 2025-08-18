# Dynamic Header Colors Implementation

## Overview
This document describes the implementation of dynamic header colors for each page using the `pages_config.py` configuration file.

## Implementation Details

### 1. Configuration (`pages_config.py`)
Added `header_gradient` property to each page configuration:

```python
PAGES_CONFIG = {
    'public_cible': {
        'name': 'Public Cible',
        'step': 1,
        'previous': None,
        'next': 'contraintes',
        'route': '/',
        'template': 'public_cible.html',
        'header_gradient': 'var(--gradient-primary)'  # Blue gradient for primary page
    },
    'contraintes': {
        'name': 'Contraintes',
        'step': 2,
        'previous': 'public_cible',
        'next': 'competences',
        'route': '/contraintes',
        'template': 'contraintes.html',
        'header_gradient': 'var(--gradient-danger)'  # Red gradient for constraints
    },
    'competences': {
        'name': 'Compétences',
        'step': 3,
        'previous': 'contraintes',
        'next': 'referentiels',
        'route': '/competences',
        'template': 'competences.html',
        'header_gradient': 'var(--gradient-success)'  # Green gradient for content pages
    },
    # ... other pages with green gradient
}
```

### 2. Route Updates
Updated all route files to pass `header_gradient` to templates:

#### Main Routes (`routes/main.py`)
```python
@app.route('/')
def index():
    nav_info = get_navigation_info('public_cible')
    page_config = get_page_config('public_cible')
    return render_template('public_cible.html', 
                         questions=QUESTIONS_PUBLIC_CIBLE, 
                         nav_info=nav_info,
                         header_gradient=page_config.get('header_gradient', 'var(--gradient-primary)'))
```

#### Other Routes
- `routes/competences.py`
- `routes/referentiels.py`
- `routes/contenus.py`
- `routes/export.py`

### 3. Template Updates
Updated all HTML templates to use dynamic header gradient:

```html
<div class="header" style="background: {{ header_gradient }};">
    <h1>🧭 Questionnaire Public Cible</h1>
    <p>Déterminez les caractéristiques du public cible de votre formation</p>
    {% include 'includes/navigation.html' %}
</div>
```

### 4. Function Updates
Updated `questions/referentiels.py` to accept and pass `header_gradient`:

```python
def referentiels_page(nav_info=None, header_gradient='var(--gradient-success)'):
    # ... function logic ...
    return render_template('referentiels.html', 
                         sections=sections,
                         besoins_specifiques=besoins_specifiques,
                         yaml_data=yaml_data,
                         existing_referentiels=existing_referentiels,
                         nav_info=nav_info,
                         header_gradient=header_gradient)
```

## Color Scheme

### CSS Variables Used
- `var(--gradient-primary)`: Blue gradient for primary pages (public_cible)
- `var(--gradient-danger)`: Red gradient for constraints page
- `var(--gradient-success)`: Green gradient for content pages (competences, referentiels, contenus, export)

### Page Color Mapping
1. **Public Cible** (Step 1): Blue gradient (`var(--gradient-primary)`)
2. **Contraintes** (Step 2): Red gradient (`var(--gradient-danger)`)
3. **Compétences** (Step 3): Green gradient (`var(--gradient-success)`)
4. **Référentiels** (Step 4): Green gradient (`var(--gradient-success)`)
5. **Contenus** (Step 5): Green gradient (`var(--gradient-success)`)
6. **Export** (Step 6): Green gradient (`var(--gradient-success)`)

## Benefits

1. **Centralized Configuration**: All header colors are defined in one place (`pages_config.py`)
2. **Easy Maintenance**: Changing colors requires only updating the configuration file
3. **Consistent Theming**: Each page type has a distinct color while maintaining visual consistency
4. **Dynamic Application**: Colors are applied automatically based on page configuration
5. **Fallback Support**: Default colors are provided if configuration is missing

## Testing

Run the test script to verify configuration:
```bash
python test_header_colors.py
```

## Files Modified

### Configuration
- `config/pages_config.py` - Added header_gradient property

### Routes
- `routes/main.py` - Updated index, contraintes, scenario routes
- `routes/competences.py` - Updated competences route
- `routes/referentiels.py` - Updated referentiels route
- `routes/contenus.py` - Updated contenus route
- `routes/export.py` - Updated export route

### Templates
- `templates/public_cible.html` - Added dynamic header gradient
- `templates/contraintes.html` - Added dynamic header gradient
- `templates/scenario.html` - Added dynamic header gradient
- `templates/competences.html` - Added dynamic header gradient
- `templates/referentiels.html` - Added dynamic header gradient
- `templates/contenus.html` - Added dynamic header gradient
- `templates/export.html` - Added dynamic header gradient

### Functions
- `questions/referentiels.py` - Updated referentiels_page function

## Future Enhancements

1. **Additional Color Schemes**: Add more gradient options for different page types
2. **User Preferences**: Allow users to customize color schemes
3. **Theme Switching**: Implement light/dark theme support
4. **Animation**: Add smooth transitions between different header colors
