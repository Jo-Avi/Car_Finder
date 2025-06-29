#!/usr/bin/env python3
"""
Debug script to analyze the HTML structure of car websites
"""

import requests
from bs4 import BeautifulSoup
import json

def get_headers():
    """Return realistic browser headers"""
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

def debug_andrew_simms():
    print("=== Debugging Andrew Simms ===")
    url = "https://www.andrewsimms.co.nz/stock?page=1&keywords=Toyota"
    
    try:
        response = requests.get(url, headers=get_headers(), timeout=30)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Save HTML for inspection
            with open("andrew_simms_debug.html", "w", encoding="utf-8") as f:
                f.write(soup.prettify())
            print("Saved HTML to andrew_simms_debug.html")
            
            # Look for common car listing patterns
            print("\nLooking for car listings...")
            
            # Try different selectors
            selectors = [
                ".car-listing", ".vehicle-item", ".stock-item", 
                "[class*='car']", "[class*='vehicle']", "[class*='stock']",
                ".listing", ".item", ".product",
                "a[href*='/vehicle']", "a[href*='/car']", "a[href*='/stock']"
            ]
            
            for selector in selectors:
                elements = soup.select(selector)
                if elements:
                    print(f"Found {len(elements)} elements with selector: {selector}")
                    if len(elements) > 0:
                        print(f"First element text: {elements[0].get_text()[:100]}...")
                        break
            
            # Look for any links that might be car listings
            all_links = soup.find_all("a", href=True)
            car_links = [link for link in all_links if any(word in link.get("href", "").lower() for word in ["vehicle", "car", "stock"])]
            print(f"Found {len(car_links)} potential car links")
            
            if car_links:
                print("Sample car links:")
                for i, link in enumerate(car_links[:5]):
                    print(f"{i+1}. {link.get('href')} - {link.get_text()[:50]}...")
                    
        else:
            print(f"Failed to fetch page: {response.status_code}")
            
    except Exception as e:
        print(f"Error: {e}")

def debug_nzcheapcars():
    print("\n=== Debugging NZ Cheap Cars ===")
    url = "https://www.nzcheapcars.co.nz/stock?page=1&keywords=Toyota"
    
    try:
        response = requests.get(url, headers=get_headers(), timeout=30)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Save HTML for inspection
            with open("nzcheapcars_debug.html", "w", encoding="utf-8") as f:
                f.write(soup.prettify())
            print("Saved HTML to nzcheapcars_debug.html")
            
            # Look for common car listing patterns
            print("\nLooking for car listings...")
            
            # Try different selectors
            selectors = [
                ".car-listing", ".vehicle-item", ".stock-item", 
                "[class*='car']", "[class*='vehicle']", "[class*='stock']",
                ".listing", ".item", ".product",
                "a[href*='/vehicle']", "a[href*='/car']", "a[href*='/stock']"
            ]
            
            for selector in selectors:
                elements = soup.select(selector)
                if elements:
                    print(f"Found {len(elements)} elements with selector: {selector}")
                    if len(elements) > 0:
                        print(f"First element text: {elements[0].get_text()[:100]}...")
                        break
            
            # Look for any links that might be car listings
            all_links = soup.find_all("a", href=True)
            car_links = [link for link in all_links if any(word in link.get("href", "").lower() for word in ["vehicle", "car", "stock"])]
            print(f"Found {len(car_links)} potential car links")
            
            if car_links:
                print("Sample car links:")
                for i, link in enumerate(car_links[:5]):
                    print(f"{i+1}. {link.get('href')} - {link.get_text()[:50]}...")
                    
        else:
            print(f"Failed to fetch page: {response.status_code}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    debug_andrew_simms()
    debug_nzcheapcars()
    print("\nDebug complete! Check the generated HTML files for detailed structure.") 