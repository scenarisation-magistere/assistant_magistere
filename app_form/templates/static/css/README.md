# Common CSS Implementation

## Overview
This directory contains the common CSS file (`common.css`) that consolidates all shared styles across the Formation Assistant templates.

## File Structure
```
app_form/templates/static/css/
├── common.css          # Main common styles file
└── README.md          # This documentation file
```

## What's Included in common.css

### 1. Reset and Base Styles
- CSS reset for consistent cross-browser styling
- Base body styles with gradient background
- Typography settings

### 2. Layout Components
- Container layouts (standard and compact)
- Content and form containers
- Responsive grid system

### 3. Header Styles
- Gradient header backgrounds
- Typography for headers
- Step indicators

### 4. Form Elements
- Form groups and labels
- Input fields and textareas
- Radio buttons and checkboxes
- Button styles (primary, success, warning, secondary)

### 5. Navigation
- Step indicators
- Navigation buttons (previous/next)
- Progress indicators

### 6. Content Components
- Info banners
- Section cards
- Question containers
- Examples sections

### 7. Specialized Components
- Competence items
- Referentiel items
- Export sections
- Public cible recall sections

### 8. Utility Classes
- Text alignment
- Margin and padding helpers
- Display utilities

### 9. Responsive Design
- Mobile-first approach
- Breakpoints for tablets and phones
- Responsive navigation

## Usage in Templates

### Adding to a Template
```html
<head>
    <!-- ... other head elements ... -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/common.css') }}">
    <style>
        /* Page-specific styles here */
    </style>
</head>
```

### Page-Specific Styles
Each template should only include styles that are unique to that page. Common styles like:
- Body background
- Container layouts
- Button styles
- Form elements
- Typography

Should NOT be duplicated in individual templates.

## Benefits

1. **Consistency**: All templates share the same base styling
2. **Maintainability**: Changes to common styles only need to be made in one place
3. **Performance**: Reduced CSS duplication across templates
4. **Scalability**: Easy to add new templates with consistent styling

## Templates Updated

The following templates have been updated to use the common CSS:

- ✅ `index.html` - Main questionnaire page
- ✅ `public_cible.html` - Public target questionnaire
- ✅ `contraintes.html` - Constraints questionnaire
- ✅ `competences.html` - Competencies page
- ✅ `referentiels.html` - Referentials page
- ✅ `contenus.html` - Content page
- ✅ `export.html` - Export page
- ✅ `scenario.html` - Scenario page
- ⚠️ `error.html` - Uses Bootstrap (left unchanged)

## Flask Configuration

The Flask app has been configured to serve static files from the templates directory:

```python
app = Flask(__name__, static_folder='templates/static', static_url_path='/static')
```

This allows the templates to reference the CSS file using:
```html
{{ url_for('static', filename='css/common.css') }}
```

## Future Improvements

1. **CSS Variables**: Consider using CSS custom properties for colors and spacing
2. **Component Library**: Create reusable CSS components
3. **Theme System**: Implement multiple color themes
4. **Optimization**: Minify CSS for production
5. **Documentation**: Add more detailed component documentation
