# Navigation CSS Extraction - Separate Navigation Styles

## Overview

Navigation-related styles have been extracted from the main CSS files into a dedicated `navigation.css` file to improve code organization and maintainability.

## What Was Extracted

### Navigation Components
- **Step Indicator**: Progress indicator showing current step
- **Navigation Buttons**: Previous/Next buttons
- **Navigation Utilities**: Helper classes for navigation states
- **Navigation Progress**: Progress bar component
- **Navigation Breadcrumbs**: Breadcrumb navigation component
- **Navigation Menu**: Menu component for future use
- **Responsive Navigation**: Mobile-friendly navigation styles

### CSS Classes Extracted

#### Step Indicator
```css
.step-indicator
.step-indicator .step
.step-indicator .step.active
.step-indicator .step.inactive
.step-indicator .step:hover
```

#### Navigation Buttons
```css
.navigation-buttons
.navigation-buttons .btn-prev
.navigation-buttons .btn-next
.navigation-buttons .btn-prev:hover
.navigation-buttons .btn-next:hover
.navigation-buttons .btn-prev:active
.navigation-buttons .btn-next:active
```

#### Navigation Utilities
```css
.nav-disabled
.nav-hidden
.nav-visible
```

#### Navigation Progress
```css
.nav-progress
.nav-progress-fill
```

#### Navigation Breadcrumbs
```css
.breadcrumb-nav
.breadcrumb-nav .breadcrumb-item
.breadcrumb-nav .breadcrumb-item.active
.breadcrumb-nav .breadcrumb-item a
```

#### Navigation Menu
```css
.nav-menu
.nav-menu-item
.nav-menu-link
.nav-menu-link:hover
.nav-menu-link.active
```

## Files Modified

### Created
- `app_form/static/css/navigation.css` - New dedicated navigation CSS file

### Updated
- `app_form/static/css/common.css` - Removed navigation styles, added import comment
- `app_form/templates/static/css/common.css` - Removed navigation styles, added import comment

### Templates Updated
All templates now include the navigation CSS file:
- `public_cible.html`
- `contraintes.html`
- `competences.html`
- `referentiels.html`
- `contenus.html`
- `export.html`
- `scenario.html`
- `index.html`

## Template Changes

### Before
```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/common.css') }}">
```

### After
```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/common.css') }}">
<link rel="stylesheet" href="{{ url_for('static', filename='css/navigation.css') }}">
```

## Benefits

1. **Better Organization**: Navigation styles are now centralized in one file
2. **Easier Maintenance**: Changes to navigation styles only require editing one file
3. **Improved Readability**: Main CSS files are cleaner and more focused
4. **Reusability**: Navigation styles can be easily reused across different projects
5. **Modularity**: Navigation components can be developed independently

## CSS Structure

The new `navigation.css` file is organized into sections:

```css
/* ========================================
   NAVIGATION STYLES
   ======================================== */

/* Step Indicator */
.step-indicator { ... }

/* Navigation Buttons */
.navigation-buttons { ... }

/* Navigation Utilities */
.nav-disabled { ... }

/* Navigation Progress */
.nav-progress { ... }

/* Navigation Breadcrumbs */
.breadcrumb-nav { ... }

/* Navigation Menu */
.nav-menu { ... }

/* Responsive Navigation */
@media (max-width: 768px) { ... }
@media (max-width: 480px) { ... }
```

## Dependencies

The navigation CSS file depends on CSS variables defined in `common.css`:
- `--spacing-*` variables for spacing
- `--radius-*` variables for border radius
- `--gradient-*` variables for button backgrounds
- `--shadow-*` variables for box shadows
- `--font-size-*` variables for typography
- `--primary-*` and `--secondary-*` variables for colors

## Usage

To use navigation styles in new templates:

1. Include the navigation CSS file:
   ```html
   <link rel="stylesheet" href="{{ url_for('static', filename='css/navigation.css') }}">
   ```

2. Use the navigation classes in your HTML:
   ```html
   <div class="step-indicator">
       <span class="step active">Step 1</span>
       <span class="step inactive">Step 2</span>
   </div>
   
   <div class="navigation-buttons">
       <button class="btn-prev">Previous</button>
       <button class="btn-next">Next</button>
   </div>
   ```

## Future Enhancements

The navigation CSS file includes additional components for future use:
- **Breadcrumb Navigation**: For complex multi-level navigation
- **Navigation Menu**: For dropdown or sidebar navigation
- **Navigation Progress**: For progress bars
- **Navigation Utilities**: For disabled/hidden states

These components are ready to use when needed and follow the same design system as the existing navigation elements.
