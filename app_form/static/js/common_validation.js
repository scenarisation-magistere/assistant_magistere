/**
 * Common validation functions for harmonized submit buttons
 * Works with pages_config.py configuration
 */

// Common submit button functionality
function createHarmonizedSubmitButton(config) {
    const {
        buttonId = 'submitBtn',
        buttonText = '✅ Valider et Continuer',
        endpoint = null,
        dataProcessor = null,
        successCallback = null,
        errorCallback = null,
        loadingText = '⏳ Sauvegarde en cours...',
        nextPageRoute = null
    } = config;

    return function(event) {
        if (event) event.preventDefault();
        
        const submitBtn = document.getElementById(buttonId);
        if (!submitBtn) {
            console.error(`Submit button with id '${buttonId}' not found`);
            return;
        }

        const originalText = submitBtn.innerHTML;
        const originalDisabled = submitBtn.disabled;
        
        // Show loading state
        submitBtn.innerHTML = loadingText;
        submitBtn.disabled = true;

        // Process data if processor provided
        let dataToSubmit = {};
        if (dataProcessor) {
            dataToSubmit = dataProcessor();
        }

        // If no endpoint provided, just navigate to next page
        if (!endpoint) {
            if (nextPageRoute) {
                window.location.href = nextPageRoute;
            } else {
                // Try to get next route from navigation info
                const nextRoute = getNextRouteFromNavInfo();
                if (nextRoute) {
                    window.location.href = nextRoute;
                }
            }
            return;
        }

        // Submit data to endpoint
        fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dataToSubmit)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Call success callback if provided
                if (successCallback) {
                    successCallback(data);
                } else {
                    // Default success behavior
                    showSuccessModal(data);
                }
            } else {
                throw new Error(data.error || 'Erreur lors de la sauvegarde');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            
            // Call error callback if provided
            if (errorCallback) {
                errorCallback(error);
            } else {
                // Default error behavior
                alert('Erreur lors de la sauvegarde : ' + error.message);
            }
            
            // Reset button
            submitBtn.innerHTML = originalText;
            submitBtn.disabled = originalDisabled;
        });
    };
}

// Get next route from navigation info (if available in template)
function getNextRouteFromNavInfo() {
    // This will be overridden by template-specific logic
    return null;
}

// Show success modal with navigation options
function showSuccessModal(data) {
    const modal = document.getElementById('successModal');
    if (modal) {
        // Update modal content
        const filenameDisplay = document.getElementById('filenameDisplay');
        const resultMessage = document.getElementById('resultMessage');
        const recapContainer = document.getElementById('recapContainer');
        const recapBlock = document.getElementById('recapBlock');
        
        if (filenameDisplay && data.filename) {
            filenameDisplay.textContent = data.filename;
        }
        
        if (resultMessage && data.message) {
            resultMessage.textContent = data.message;
        }
        
        // Build user-friendly recap
        const recapEnabled = window.RECAP_ENABLED === true;
        if (recapBlock) {
            recapBlock.style.display = recapEnabled ? 'block' : 'none';
        }
        if (recapEnabled && recapContainer) {
            recapContainer.innerHTML = buildUserFriendlyRecap(data.yaml_data || {});
        }
        
        modal.style.display = 'block';
    } else {
        // If no modal, just navigate to next page
        const nextRoute = getNextRouteFromNavInfo();
        if (nextRoute) {
            window.location.href = nextRoute;
        }
    }
}

// Close modal and navigate to next page
function continueToNextStep() {
    const modal = document.getElementById('successModal');
    if (modal) {
        modal.style.display = 'none';
    }
    
    const nextRoute = getNextRouteFromNavInfo();
    if (nextRoute) {
        window.location.href = nextRoute;
    }
}

// Navigation functions
function goToPreviousStep() {
    // This will be overridden by template-specific logic
    const prevRoute = getPreviousRouteFromNavInfo();
    if (prevRoute) {
        window.location.href = prevRoute;
    }
}

function goToNextStep() {
    const nextRoute = getNextRouteFromNavInfo();
    if (nextRoute) {
        window.location.href = nextRoute;
    }
}

function getPreviousRouteFromNavInfo() {
    // This will be overridden by template-specific logic
    return null;
}

// Common form data processor
function processFormData(formId = 'questionnaireForm') {
    const form = document.getElementById(formId);
    if (!form) return {};
    
    const formData = new FormData(form);
    const data = {};
    
    // Handle different input types
    for (let [key, value] of formData.entries()) {
        if (data[key]) {
            if (Array.isArray(data[key])) {
                data[key].push(value);
            } else {
                data[key] = [data[key], value];
            }
        } else {
            data[key] = value;
        }
    }
    
    // Handle checkboxes that might not be checked
    const checkboxes = form.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        if (!data[checkbox.name]) {
            data[checkbox.name] = [];
        }
    });
    
    return data;
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('successModal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
}

// Close modal function
function closeModal() {
    const modal = document.getElementById('successModal');
    if (modal) {
        modal.style.display = 'none';
    }
}

// Build a user-friendly recap HTML from step data
function buildUserFriendlyRecap(stepData) {
    try {
        // Detect which step structure is present
        if (stepData && stepData.public_cible) {
            const pc = stepData.public_cible;
            const ctx = stepData.contexte_formation || {};
            return `
                <div style="background: var(--light-gray); padding: var(--spacing-md); border-radius: var(--radius-small);">
                    <div style="margin-bottom: var(--spacing-sm);"><strong>🎓 Titre</strong>: ${escapeHtml(ctx.titre || '')}</div>
                    <div style="margin-bottom: var(--spacing-sm);"><strong>🎯 Objectif général</strong>: ${escapeHtml(ctx.objectif_general || '')}</div>
                    <div style="margin-bottom: var(--spacing-sm);"><strong>👥 Public visé</strong>: ${(pc.type_de_public || []).map(escapeHtml).join(', ')}</div>
                    <div style="margin-bottom: var(--spacing-sm);"><strong>📚 Type de formation</strong>: ${escapeHtml(pc.type_de_formation || '')}${pc.type_de_formation_precisions ? ' — ' + escapeHtml(pc.type_de_formation_precisions) : ''}</div>
                    <div style="margin-bottom: var(--spacing-sm);"><strong>🏫 Niveaux scolaires</strong>: ${(pc.niveaux_scolaires || []).map(escapeHtml).join(', ')}</div>
                    <div style="margin-bottom: var(--spacing-sm);"><strong>📈 Niveau d’expertise</strong>: ${(pc.niveau_expertise || []).map(escapeHtml).join(', ')}</div>
                    <div><strong>🧩 Besoins spécifiques</strong>: ${(pc.besoins_specifiques || []).map(escapeHtml).join(', ') || 'Aucun'}</div>
                </div>
            `;
        }
        if (stepData && stepData.contraintes_formation) {
            const c = stepData.contraintes_formation;
            return `
                <div style="background: var(--light-gray); padding: var(--spacing-md); border-radius: var(--radius-small);">
                    <div style="margin-bottom: var(--spacing-sm);"><strong>🧭 Type de parcours</strong>: ${escapeHtml(c.type_parcours || '')}</div>
                    <div style="margin-bottom: var(--spacing-sm);"><strong>⏱️ Temps total</strong>: ${escapeHtml(c.temps_total || '')}</div>
                    <div style="margin-bottom: var(--spacing-sm);"><strong>🧑‍🏫 Animation</strong>: ${escapeHtml(c.animation || '')}</div>
                    <div style="margin-bottom: var(--spacing-sm);"><strong>🗓️ Calendrier</strong>: ${escapeHtml(c.calendrier || '')}</div>
                    <div style="margin-bottom: var(--spacing-sm);"><strong>🕒 Horaires</strong>: ${escapeHtml(c.horaires || '')}</div>
                    <div style="margin-bottom: var(--spacing-sm);"><strong>👥 Nombre de participants</strong>: ${escapeHtml(c.nombre_participants || '')}</div>
                    <div style="margin-bottom: var(--spacing-sm);"><strong>🏛️ Exigences institutionnelles</strong>: ${escapeHtml(c.exigences_institutionnelles || '')}</div>
                    <div><strong>🛠️ Restrictions techniques</strong>: ${escapeHtml(c.restrictions_techniques || '')}</div>
                </div>
            `;
        }
        // Fallback: show minimal JSON pretty but not as YAML
        return `<pre style="white-space: pre-wrap;">${escapeHtml(JSON.stringify(stepData, null, 2))}</pre>`;
    } catch (e) {
        return '';
    }
}

function escapeHtml(unsafe) {
    if (unsafe === undefined || unsafe === null) return '';
    return String(unsafe)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}
