#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Test script to test the Bloom taxonomy route directly
"""

import requests
import json

def test_bloom_route():
    """Test the Bloom taxonomy route"""
    try:
        # Test the route with a specific niveau
        niveau = "Moyen : Appliquer / Comprendre"
        encoded_niveau = requests.utils.quote(niveau)
        url = f"http://localhost:5000/get_bloom_verbs/{encoded_niveau}"
        
        print(f"Testing URL: {url}")
        
        response = requests.get(url)
        print(f"Response status: {response.status_code}")
        print(f"Response headers: {dict(response.headers)}")
        
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
    test_bloom_route()
