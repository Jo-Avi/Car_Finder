#!/usr/bin/env python3
"""
Test script to verify the scraper works locally
"""

from scraper import get_andrew_simms_cars, get_nzcheapcars_cars
import json

def test_scraper():
    print("Testing car scraper...")
    
    # Test query
    query = "Toyota"
    max_pages = 1  # Just test 1 page for speed
    
    print(f"Searching for: {query}")
    print("=" * 50)
    
    try:
        # Test Andrew Simms
        print("Testing Andrew Simms scraper...")
        results1 = get_andrew_simms_cars(query, max_pages=max_pages)
        print(f"Found {len(results1)} results from Andrew Simms")
        
        if results1:
            print("Sample result from Andrew Simms:")
            print(json.dumps(results1[0], indent=2))
        
        print("-" * 30)
        
        # Test NZ Cheap Cars
        print("Testing NZ Cheap Cars scraper...")
        results2 = get_nzcheapcars_cars(query, max_pages=max_pages)
        print(f"Found {len(results2)} results from NZ Cheap Cars")
        
        if results2:
            print("Sample result from NZ Cheap Cars:")
            print(json.dumps(results2[0], indent=2))
        
        print("-" * 30)
        
        # Combined results
        combined = results1 + results2
        print(f"Total results: {len(combined)}")
        
        if combined:
            print("All results:")
            for i, car in enumerate(combined[:3]):  # Show first 3
                print(f"{i+1}. {car['title']} - {car['price']} ({car['source']})")
        
        return True
        
    except Exception as e:
        print(f"Error during testing: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_scraper()
    if success:
        print("\n✅ Scraper test completed successfully!")
    else:
        print("\n❌ Scraper test failed!") 