#!/usr/bin/env python3
"""
Test script to verify the Flask API works correctly
"""

import requests
import json

def test_api():
    print("Testing Flask API...")
    
    # Test health check
    try:
        response = requests.get("http://localhost:5000/")
        print(f"Health check status: {response.status_code}")
        if response.status_code == 200:
            print("Health check passed!")
        else:
            print("Health check failed!")
    except Exception as e:
        print(f"Health check error: {e}")
    
    # Test search endpoint
    try:
        response = requests.get("http://localhost:5000/search?q=Toyota&max_pages=1")
        print(f"Search status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Response keys: {list(data.keys())}")
            
            if 'results' in data:
                results = data['results']
                print(f"Found {len(results)} cars")
                if results:
                    print("Sample car:")
                    print(json.dumps(results[0], indent=2))
            else:
                print("No 'results' key in response")
                print("Response:", data)
        else:
            print(f"Search failed with status {response.status_code}")
            
    except Exception as e:
        print(f"Search error: {e}")

if __name__ == "__main__":
    test_api() 