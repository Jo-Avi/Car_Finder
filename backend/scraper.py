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
            
            # Look for car listings - adjust selectors based on actual site structure
            car_elements = soup.select(".car-listing, .vehicle-item, .stock-item") or soup.select("[class*='car'], [class*='vehicle'], [class*='stock']")
            
            if not car_elements:
                # Fallback: look for any links that might contain car info
                car_elements = soup.select("a[href*='/vehicle'], a[href*='/car'], a[href*='/stock']")
            
            for element in car_elements:
                try:
                    # Extract title
                    title_elem = element.select_one("h2, h3, .title, .name") or element
                    title = title_elem.get_text(strip=True) if title_elem else ""
                    
                    # Extract link
                    link_elem = element.find("a") if element.name != "a" else element
                    link = link_elem.get("href", "") if link_elem else ""
                    if link and not link.startswith("http"):
                        link = "https://www.andrewsimms.co.nz" + link
                    
                    # Extract image
                    img_elem = element.select_one("img")
                    image = img_elem.get("src", "") if img_elem else ""
                    if image and not image.startswith("http"):
                        image = "https://www.andrewsimms.co.nz" + image
                    
                    # Extract price
                    price_elem = element.select_one(".price, .price-value, [class*='price']")
                    price = price_elem.get_text(strip=True) if price_elem else ""
                    
                    # Extract other details
                    odometer = ""
                    fuel = ""
                    consumption = ""
                    
                    # Look for odometer info
                    odometer_elem = element.select_one(".odometer, .mileage, [class*='odo']")
                    if odometer_elem:
                        odometer = odometer_elem.get_text(strip=True)
                    
                    # Look for fuel info
                    fuel_elem = element.select_one(".fuel, [class*='fuel']")
                    if fuel_elem:
                        fuel = fuel_elem.get_text(strip=True)
                    
                    # Look for consumption info
                    consumption_elem = element.select_one(".consumption, [class*='consumption']")
                    if consumption_elem:
                        consumption = consumption_elem.get_text(strip=True)
                    
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
            
            # Look for car listings - adjust selectors based on actual site structure
            car_elements = soup.select(".car-listing, .vehicle-item, .stock-item") or soup.select("[class*='car'], [class*='vehicle'], [class*='stock']")
            
            if not car_elements:
                # Fallback: look for any links that might contain car info
                car_elements = soup.select("a[href*='/vehicle'], a[href*='/car'], a[href*='/stock']")
            
            for element in car_elements:
                try:
                    # Extract title
                    title_elem = element.select_one("h2, h3, .title, .name") or element
                    title = title_elem.get_text(strip=True) if title_elem else ""
                    
                    # Extract link
                    link_elem = element.find("a") if element.name != "a" else element
                    link = link_elem.get("href", "") if link_elem else ""
                    if link and not link.startswith("http"):
                        link = "https://www.nzcheapcars.co.nz" + link
                    
                    # Extract image
                    img_elem = element.select_one("img")
                    image = img_elem.get("src", "") if img_elem else ""
                    if image and not image.startswith("http"):
                        image = "https://www.nzcheapcars.co.nz" + image
                    
                    # Extract price
                    price_elem = element.select_one(".price, .price-value, [class*='price']")
                    price = price_elem.get_text(strip=True) if price_elem else ""
                    
                    # Extract other details
                    odometer = ""
                    fuel = ""
                    consumption = ""
                    
                    # Look for odometer info
                    odometer_elem = element.select_one(".odometer, .mileage, [class*='odo']")
                    if odometer_elem:
                        odometer = odometer_elem.get_text(strip=True)
                    
                    # Look for fuel info
                    fuel_elem = element.select_one(".fuel, [class*='fuel']")
                    if fuel_elem:
                        fuel = fuel_elem.get_text(strip=True)
                    
                    # Look for consumption info
                    consumption_elem = element.select_one(".consumption, [class*='consumption']")
                    if consumption_elem:
                        consumption = consumption_elem.get_text(strip=True)
                    
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
                        
                except Exception as e:
                    print(f"Error parsing car element: {e}")
                    continue
            
            # Add delay between requests
            time.sleep(1)
            
        except Exception as e:
            print(f"Error processing page {page}: {e}")
            continue
    
    return cars
