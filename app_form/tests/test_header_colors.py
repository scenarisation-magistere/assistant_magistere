#!/usr/bin/env python3
"""
Test script to verify header gradient configuration
"""

from config.pages_config import PAGES_CONFIG, get_page_config

def test_header_gradients():
    """Test that all pages have header gradient configuration"""
    print("Testing header gradient configuration...")
    print("=" * 50)
    
    for page_name, config in PAGES_CONFIG.items():
        header_gradient = config.get('header_gradient', 'NOT SET')
        print(f"Page: {page_name}")
        print(f"  Name: {config.get('name', 'N/A')}")
        print(f"  Step: {config.get('step', 'N/A')}")
        print(f"  Header Gradient: {header_gradient}")
        print()
    
    print("Testing get_page_config function...")
    print("=" * 50)
    
    for page_name in PAGES_CONFIG.keys():
        page_config = get_page_config(page_name)
        header_gradient = page_config.get('header_gradient', 'NOT SET')
        print(f"{page_name}: {header_gradient}")

if __name__ == "__main__":
    test_header_gradients()
