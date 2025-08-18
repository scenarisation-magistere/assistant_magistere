#!/usr/bin/env python3
"""
Simple test for Bloom taxonomy with basic parameters
"""

import requests
import json

def test_simple_bloom():
    """Test Bloom taxonomy with simple parameters"""
    try:
        # Test with a simple parameter first
        response = requests.get("http://localhost:5000/get_bloom_verbs/test")
        print(f"Simple test status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Simple test response: {json.dumps(data, indent=2, ensure_ascii=False)}")
        
        # Test with a niveau that should work
        niveau = "Bas : Se rappeler"
        encoded_niveau = requests.utils.quote(niveau)
        url = f"http://localhost:5000/get_bloom_verbs/{encoded_niveau}"
        print(f"\nTesting URL: {url}")
        
        response = requests.get(url)
        print(f"Complex test status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Complex test response: {json.dumps(data, indent=2, ensure_ascii=False)}")
        else:
            print(f"Response text: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - Flask app is not running")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_simple_bloom()
