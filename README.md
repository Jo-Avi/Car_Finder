# Car Scraper Project

A full-stack web application that scrapes car listings from multiple sources (Andrew Simms and NZ Cheap Cars) and provides a modern React frontend for searching and filtering results.

## Project Structure

```
Car_Scraper_Projects/
├── backend/          # Flask API server
│   ├── app.py        # Main Flask application
│   ├── scraper.py    # Web scraping logic
│   └── requirements.txt
└── frontend/         # React TypeScript frontend
    ├── src/
    ├── public/
    └── package.json
```

## Prerequisites

Before running this project, make sure you have the following installed:

- **Python 3.8+** (for backend)
- **Node.js 16+** (for frontend)
- **npm** or **yarn** (package managers)
- **Git** (for cloning the repository)

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Jo-Avi/Car_Scraping.git
cd Car_Scraping
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd ../frontend

# Install Node.js dependencies
npm install
```

## Running the Project

### Option 1: Run Both Backend and Frontend (Recommended)

#### Terminal 1 - Backend:
```bash
cd backend
# Activate virtual environment if not already activated
# On Windows: venv\Scripts\activate
# On macOS/Linux: source venv/bin/activate

# Start the Flask server
python app.py
```

The backend will start on `http://localhost:5000`

#### Terminal 2 - Frontend:
```bash
cd frontend

# Start the React development server
npm start
```

The frontend will start on `http://localhost:3000`

### Option 2: Run Only Frontend (Uses Deployed Backend)

If you want to run only the frontend and use the deployed backend:

```bash
cd frontend
npm start
```

The frontend will connect to the deployed backend at `https://car-scraping-6sl5.onrender.com`

## Usage

1. **Open your browser** and go to `http://localhost:3000`
2. **Enter a search term** in the search box (e.g., "Toyota", "Nissan", "Honda")
3. **Click Search** or press Enter
4. **View results** from both Andrew Simms and NZ Cheap Cars
5. **Use filters** to sort by price, fuel type, or consumption
6. **Click on car cards** to view more details

## API Endpoints

### Backend API (when running locally):

- **Health Check**: `GET http://localhost:5000/`
- **Search Cars**: `GET http://localhost:5000/search?q={query}&max_pages={pages}`

### Example API Usage:

```bash
# Search for Toyota cars (max 3 pages)
curl "http://localhost:5000/search?q=Toyota&max_pages=3"
```

## Development

### Backend Development

- **Main file**: `backend/app.py`
- **Scraper logic**: `backend/scraper.py`
- **Dependencies**: `backend/requirements.txt`

### Frontend Development

- **Main component**: `frontend/src/pages/Home.tsx`
- **Components**: `frontend/src/components/`
- **Styling**: CSS files in respective component directories

### Making Changes

1. **Backend changes**: The Flask server will auto-reload when you save changes
2. **Frontend changes**: The React development server will hot-reload automatically

## Troubleshooting

### Common Issues:

1. **Port already in use**:
   - Backend: Change port in `app.py` or kill process using port 5000
   - Frontend: React will automatically suggest an alternative port

2. **Module not found errors**:
   - Backend: Make sure virtual environment is activated and dependencies are installed
   - Frontend: Run `npm install` again

3. **CORS errors**:
   - Backend has CORS enabled, but if issues persist, check the CORS configuration in `app.py`

4. **Scraping fails**:
   - Check internet connection
   - The scrapers might need updates if website structures change
   - Check the debug files in backend directory for more information

### Debug Files

The backend creates debug HTML files when scraping fails:
- `backend/andrew_simms_debug.html`
- `backend/nzcheapcars_debug.html`

## Deployment

### Backend Deployment
- Already deployed on Render at `https://car-scraping-6sl5.onrender.com`
- See `backend/DEPLOYMENT_GUIDE.md` for deployment details

### Frontend Deployment
- See `frontend/DEPLOYMENT.md` for Render deployment instructions

## Features

- **Multi-source scraping**: Andrew Simms and NZ Cheap Cars
- **Real-time search**: Instant results as you type
- **Advanced filtering**: Filter by fuel type, price, consumption
- **Responsive design**: Works on desktop and mobile
- **Error handling**: Graceful error messages and fallbacks
- **Loading states**: Visual feedback during searches

## Technologies Used

### Backend:
- **Flask**: Web framework
- **Selenium**: Web scraping
- **BeautifulSoup**: HTML parsing
- **Flask-CORS**: Cross-origin resource sharing

### Frontend:
- **React 18**: UI framework
- **TypeScript**: Type safety
- **CSS3**: Styling
- **Fetch API**: HTTP requests

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational purposes. Please respect the terms of service of the websites being scraped.
