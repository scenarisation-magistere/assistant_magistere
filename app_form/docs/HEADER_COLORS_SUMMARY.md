# Header Colors Summary - Different Background Colors per Page

## Current Configuration

The application is configured to display different header background colors for each page using CSS variables and dynamic styling.

### Page-by-Page Header Colors

| Page | Step | Header Color | CSS Variable | Description |
|------|------|--------------|--------------|-------------|
| **Public Cible** | 1 | 🔵 Blue Gradient | `var(--gradient-primary)` | Primary page - Blue gradient |
| **Contraintes** | 2 | 🔴 Red Gradient | `var(--gradient-danger)` | Constraints page - Red gradient |
| **Compétences** | 3 | 🟢 Green Gradient | `var(--gradient-success)` | Competencies page - Green gradient |
| **Référentiels** | 4 | 🟢 Green Gradient | `var(--gradient-success)` | References page - Green gradient |
| **Contenus** | 5 | 🟢 Green Gradient | `var(--gradient-success)` | Contents page - Green gradient |
| **Export** | 6 | 🟢 Green Gradient | `var(--gradient-success)` | Export page - Green gradient |

### Color Scheme Logic

- **🔵 Blue (Primary)**: Used for the first page (Public Cible) - represents the starting point
- **🔴 Red (Danger)**: Used for the constraints page - represents limitations and requirements
- **🟢 Green (Success)**: Used for all content pages - represents progress and completion

### Technical Implementation

#### 1. Configuration (`pages_config.py`)
```python
PAGES_CONFIG = {
    'public_cible': {
        'header_gradient': 'var(--gradient-primary)'  # Blue
    },
    'contraintes': {
        'header_gradient': 'var(--gradient-danger)'   # Red
    },
    'competences': {
        'header_gradient': 'var(--gradient-success)'  # Green
    },
    # ... other pages with green gradient
}
```

#### 2. CSS Variables (`static/css/common.css`)
```css
:root {
    --gradient-primary: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);  /* Blue */
    --gradient-success: linear-gradient(135deg, #20bf6b 0%, #0fb9b1 100%);  /* Green */
    --gradient-danger: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);   /* Red */
}
```

#### 3. Template Implementation
```html
<div class="header" style="background: {{ header_gradient }};">
    <h1>Page Title</h1>
    <p>Page description</p>
</div>
```

#### 4. Route Integration
```python
@app.route('/page')
def page():
    page_config = get_page_config('page_name')
    return render_template('template.html', 
                         header_gradient=page_config.get('header_gradient'))
```

### Available CSS Variables

The following gradient variables are available for use:

- `--gradient-primary`: Blue gradient (Primary pages)
- `--gradient-success`: Green gradient (Content pages)
- `--gradient-danger`: Red gradient (Warning/Constraint pages)
- `--gradient-secondary`: Purple gradient (Alternative)
- `--gradient-gray`: Gray gradient (Neutral)

### Visual Flow

```
Public Cible (🔵 Blue) 
    ↓
Contraintes (🔴 Red)
    ↓
Compétences (🟢 Green)
    ↓
Référentiels (🟢 Green)
    ↓
Contenus (🟢 Green)
    ↓
Export (🟢 Green)
```

### Benefits

1. **Visual Hierarchy**: Different colors help users understand their progress
2. **Page Identification**: Users can quickly identify which page they're on
3. **Consistent Design**: All pages follow the same design pattern
4. **Easy Maintenance**: Colors are centrally managed through CSS variables
5. **Flexible**: Easy to change colors by modifying the configuration

### Testing

To verify the header colors are working:

1. **Manual Test**: Visit each page and verify the header color
2. **Configuration Test**: Run `test_config_alignment.py` to verify setup
3. **CSS Test**: Open `test_header_styles.html` to test CSS variables

### Troubleshooting

If header colors are not showing:

1. Check Flask static folder configuration in `app.py`
2. Verify CSS variables are defined in `static/css/common.css`
3. Ensure templates have the correct inline style syntax
4. Confirm routes are passing `header_gradient` parameter
5. Check browser developer tools for CSS loading issues
