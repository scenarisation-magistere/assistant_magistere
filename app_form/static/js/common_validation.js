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
        const yamlOutput = document.getElementById('yamlOutput');
        
        if (filenameDisplay && data.filename) {
            filenameDisplay.textContent = data.filename;
        }
        
        if (resultMessage && data.message) {
            resultMessage.textContent = data.message;
        }
        
        if (yamlOutput && data.yaml_data) {
            yamlOutput.textContent = JSON.stringify(data.yaml_data, null, 2);
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
