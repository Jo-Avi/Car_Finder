# scraper.py (Selenium version)
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Configure headless browser
def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)

def get_andrew_simms_cars(query, max_pages=3):
    cars = []
    driver = get_driver()
    
    for page in range(1, max_pages + 1):
        url = f"https://www.andrewsimms.co.nz/stock?page={page}&keywords={query}"
        driver.get(url)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, "html.parser")

        for title_tag in soup.select("a.si-title"):
            title = title_tag.get("title", "").strip()
            link = "https://www.andrewsimms.co.nz" + title_tag.get("href", "")
            container = title_tag
            for _ in range(3):
                container = container.parent if container else None

            image_tag = container.find("img") if container else None
            image = image_tag.get("src") if image_tag else ""
            price_tag = container.find("span", class_="price-value") if container else None
            price = price_tag.get_text(strip=True) if price_tag else ""

            year = title_tag.find("span", class_="year")
            make = title_tag.find("span", class_="make")
            model = title_tag.find("span", class_="model")
            badge = title_tag.find("span", class_="badge")
            detailed_title = " ".join(filter(None, [
                year.get_text(strip=True) if year else "",
                make.get_text(strip=True) if make else "",
                model.get_text(strip=True) if model else "",
                badge.get_text(strip=True) if badge else "",
            ])).strip() or title

            features_tag = container.find("a", class_="si-features") if container else None
            odometer_tag = features_tag.find("span", class_="odometer") if features_tag else None
            odometer = odometer_tag.get_text(strip=True) if odometer_tag else ""
            fuel_tag = features_tag.find("span", class_="fuel") if features_tag else None
            fuel = fuel_tag.get_text(strip=True) if fuel_tag else ""
            consumption_tag = features_tag.find("span", class_="consumption") if features_tag else None
            consumption = consumption_tag.get_text(strip=True) if consumption_tag else ""

            if query.strip().lower() in detailed_title.lower():
                cars.append({
                    "title": detailed_title,
                    "link": link,
                    "image": image,
                    "price": price,
                    "odometer": odometer,
                    "fuel": fuel,
                    "consumption": consumption,
                    "source": "Andrew Simms"
                })
    
    driver.quit()
    return cars


def get_nzcheapcars_cars(query, max_pages=3):
    cars = []
    driver = get_driver()

    for page in range(1, max_pages + 1):
        url = f"https://www.nzcheapcars.co.nz/stock?page={page}&keywords={query}"
        driver.get(url)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, "html.parser")

        for title_tag in soup.select("a.si-title"):
            title = title_tag.get("title", "").strip()
            link = "https://www.nzcheapcars.co.nz" + title_tag.get("href", "")

            year = title_tag.find("span", class_="year")
            make = title_tag.find("span", class_="make")
            model = title_tag.find("span", class_="model")
            badge = title_tag.find("span", class_="badge")
            detailed_title = " ".join(filter(None, [
                year.get_text(strip=True) if year else "",
                make.get_text(strip=True) if make else "",
                model.get_text(strip=True) if model else "",
                badge.get_text(strip=True) if badge else "",
            ])).strip() or title

            parent = title_tag
            for _ in range(4):
                parent = parent.parent if parent and not parent.find("img") else parent
            image_tag = parent.find("img") if parent else None
            image = image_tag.get("src") if image_tag else ""
            price_tag = parent.find("span", class_="price-value") if parent else None
            price = price_tag.get_text(strip=True) if price_tag else ""

            features_tag = parent.find("a", class_="si-features") if parent else None
            odometer_tag = features_tag.find("span", class_="odometer") if features_tag else None
            odometer = odometer_tag.get_text(strip=True) if odometer_tag else ""
            fuel_tag = features_tag.find("span", class_="fuel") if features_tag else None
            fuel = fuel_tag.get_text(strip=True) if fuel_tag else ""
            consumption_tag = features_tag.find("span", class_="consumption") if features_tag else None
            consumption = consumption_tag.get_text(strip=True) if consumption_tag else ""

            if query and query.lower() in detailed_title.lower():
                cars.append({
                    "title": detailed_title,
                    "link": link,
                    "image": image,
                    "price": price,
                    "odometer": odometer,
                    "fuel": fuel,
                    "consumption": consumption,
                    "source": "NZ Cheap Cars"
                })



    driver.quit()
    return cars
