# scraper.py (Requests version - works on Render)
import requests
from bs4 import BeautifulSoup
import time
import random

def get_headers():
    """Return realistic browser headers to avoid being blocked"""
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    ]
    return {
        'User-Agent': random.choice(user_agents),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

def safe_request(url, max_retries=3):
    """Make a safe HTTP request with retries and error handling"""
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=get_headers(), timeout=30)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"Request failed (attempt {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                print(f"Failed to fetch {url} after {max_retries} attempts")
                return None

def get_andrew_simms_cars(query, max_pages=3):
    cars = []
    
    for page in range(1, max_pages + 1):
        try:
            url = f"https://www.andrewsimms.co.nz/stock?page={page}&keywords={query}"
            response = safe_request(url)
            
            if not response:
                continue
                
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Use the correct selector based on the actual HTML structure
            car_elements = soup.select(".stock-item")
            
            print(f"Found {len(car_elements)} stock items on page {page}")
            
            for element in car_elements:
                try:
                    # Extract title from si-title
                    title_elem = element.select_one(".si-title")
                    if not title_elem:
                        continue
                        
                    # Build title from year, make, model, badge
                    year_elem = title_elem.select_one(".year")
                    make_elem = title_elem.select_one(".make")
                    model_elem = title_elem.select_one(".model")
                    badge_elem = title_elem.select_one(".badge")
                    
                    year = year_elem.get_text(strip=True) if year_elem else ""
                    make = make_elem.get_text(strip=True) if make_elem else ""
                    model = model_elem.get_text(strip=True) if model_elem else ""
                    badge = badge_elem.get_text(strip=True) if badge_elem else ""
                    
                    title = " ".join(filter(None, [year, make, model, badge])).strip()
                    
                    # Extract link
                    link = title_elem.get("href", "")
                    if link and not link.startswith("http"):
                        link = "https://www.andrewsimms.co.nz" + link
                    
                    # Extract image from the first slide
                    img_elem = element.select_one(".embla__slide img")
                    image = img_elem.get("src", "") if img_elem else ""
                    
                    # Extract price
                    price_elem = element.select_one(".price-value")
                    price = price_elem.get_text(strip=True) if price_elem else ""
                    
                    # Extract features
                    features_elem = element.select_one(".si-features")
                    odometer = ""
                    fuel = ""
                    consumption = ""
                    
                    if features_elem:
                        odometer_elem = features_elem.select_one(".odometer")
                        fuel_elem = features_elem.select_one(".fuel")
                        consumption_elem = features_elem.select_one(".consumption")
                        
                        odometer = odometer_elem.get_text(strip=True) if odometer_elem else ""
                        fuel = fuel_elem.get_text(strip=True) if fuel_elem else ""
                        consumption = consumption_elem.get_text(strip=True) if consumption_elem else ""
                    
                    # Only add if it matches the query and has basic info
                    if (query.strip().lower() in title.lower() and 
                        title and link and 
                        len(title) > 5):
                        cars.append({
                            "title": title,
                            "link": link,
                            "image": image,
                            "price": price,
                            "odometer": odometer,
                            "fuel": fuel,
                            "consumption": consumption,
                            "source": "Andrew Simms"
                        })
                        print(f"Added: {title}")
                        
                except Exception as e:
                    print(f"Error parsing car element: {e}")
                    continue
            
            # Add delay between requests
            time.sleep(1)
            
        except Exception as e:
            print(f"Error processing page {page}: {e}")
            continue
    
    return cars

def get_nzcheapcars_cars(query, max_pages=3):
    cars = []
    
    for page in range(1, max_pages + 1):
        try:
            url = f"https://www.nzcheapcars.co.nz/stock?page={page}&keywords={query}"
            response = safe_request(url)
            
            if not response:
                continue
                
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Use the correct selector based on the actual HTML structure
            car_elements = soup.select(".stock-item")
            
            print(f"Found {len(car_elements)} stock items on page {page}")
            
            for element in car_elements:
                try:
                    # Extract title from si-title
                    title_elem = element.select_one(".si-title")
                    if not title_elem:
                        continue
                        
                    # Build title from year, make, model, badge
                    year_elem = title_elem.select_one(".year")
                    make_elem = title_elem.select_one(".make")
                    model_elem = title_elem.select_one(".model")
                    badge_elem = title_elem.select_one(".badge")
                    
                    year = year_elem.get_text(strip=True) if year_elem else ""
                    make = make_elem.get_text(strip=True) if make_elem else ""
                    model = model_elem.get_text(strip=True) if model_elem else ""
                    badge = badge_elem.get_text(strip=True) if badge_elem else ""
                    
                    title = " ".join(filter(None, [year, make, model, badge])).strip()
                    
                    # Extract link
                    link = title_elem.get("href", "")
                    if link and not link.startswith("http"):
                        link = "https://www.nzcheapcars.co.nz" + link
                    
                    # Extract image from the first slide
                    img_elem = element.select_one(".embla__slide img")
                    image = img_elem.get("src", "") if img_elem else ""
                    
                    # Extract price
                    price_elem = element.select_one(".price-value")
                    price = price_elem.get_text(strip=True) if price_elem else ""
                    
                    # Extract features
                    features_elem = element.select_one(".si-features")
                    odometer = ""
                    fuel = ""
                    consumption = ""
                    
                    if features_elem:
                        odometer_elem = features_elem.select_one(".odometer")
                        fuel_elem = features_elem.select_one(".fuel")
                        consumption_elem = features_elem.select_one(".consumption")
                        
                        odometer = odometer_elem.get_text(strip=True) if odometer_elem else ""
                        fuel = fuel_elem.get_text(strip=True) if fuel_elem else ""
                        consumption = consumption_elem.get_text(strip=True) if consumption_elem else ""
                    
                    # Only add if it matches the query and has basic info
                    if (query.strip().lower() in title.lower() and 
                        title and link and 
                        len(title) > 5):
                        cars.append({
                            "title": title,
                            "link": link,
                            "image": image,
                            "price": price,
                            "odometer": odometer,
                            "fuel": fuel,
                            "consumption": consumption,
                            "source": "NZ Cheap Cars"
                        })
                        print(f"Added: {title}")
                        
                except Exception as e:
                    print(f"Error parsing car element: {e}")
                    continue
            
            # Add delay between requests
            time.sleep(1)
            
        except Exception as e:
            print(f"Error processing page {page}: {e}")
            continue
    
    return cars
