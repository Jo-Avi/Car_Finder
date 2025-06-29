from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import get_andrew_simms_cars, get_nzcheapcars_cars
import logging
import traceback
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

@app.route('/')
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "Car scraper API is running"})

@app.route('/search')
def search():
    try:
        start_time = time.time()
        
        # Get query parameters
        q = request.args.get('q', '')
        max_pages = int(request.args.get('max_pages', 3))
        
        if not q.strip():
            return jsonify({"error": "Query parameter 'q' is required"}), 400
        
        logger.info(f"Starting search for query: '{q}' with max_pages: {max_pages}")
        
        # Search both sources
        logger.info("Searching Andrew Simms...")
        results1 = get_andrew_simms_cars(q, max_pages=max_pages)
        logger.info(f"Found {len(results1)} results from Andrew Simms")
        
        logger.info("Searching NZ Cheap Cars...")
        results2 = get_nzcheapcars_cars(q, max_pages=max_pages)
        logger.info(f"Found {len(results2)} results from NZ Cheap Cars")
        
        # Combine results
        combined = results1 + results2
        
        elapsed_time = time.time() - start_time
        logger.info(f"Search completed in {elapsed_time:.2f} seconds. Total results: {len(combined)}")
        
        return jsonify({
            "results": combined,
            "total_count": len(combined),
            "search_time": elapsed_time,
            "query": q
        })
        
    except Exception as e:
        logger.error(f"Error in search endpoint: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({
            "error": "An error occurred while searching",
            "details": str(e)
        }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
