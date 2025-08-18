#!/usr/bin/env python3
"""
Test script to check available routes in Flask app
"""

import requests
import json

def test_available_routes():
    """Test what routes are available"""
    try:
        # Test the main route first
        response = requests.get("http://localhost:5000/")
        print(f"Main route status: {response.status_code}")
        
        # Test the competences route
        response = requests.get("http://localhost:5000/competences")
        print(f"Competences route status: {response.status_code}")
        
        # Test a simple bloom route without spaces
        response = requests.get("http://localhost:5000/get_bloom_verbs/test")
        print(f"Simple bloom route status: {response.status_code}")
        
        # Test with a different niveau
        niveau = "Haut : Créer / Évaluer / Analyser"
        encoded_niveau = requests.utils.quote(niveau)
        url = f"http://localhost:5000/get_bloom_verbs/{encoded_niveau}"
        print(f"Testing URL: {url}")
        
        response = requests.get(url)
        print(f"Complex bloom route status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Response data: {json.dumps(data, indent=2, ensure_ascii=False)}")
        else:
            print(f"Response text: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - Flask app is not running")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_available_routes()
