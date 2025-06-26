from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import get_andrew_simms_cars, get_nzcheapcars_cars

app = Flask(__name__)
CORS(app)

@app.route('/search')
def search():
    q = request.args.get('q', '')
    max_pages = int(request.args.get('max_pages', 3))

    results1 = get_andrew_simms_cars(q, max_pages=max_pages)
    results2 = get_nzcheapcars_cars(q, max_pages=max_pages)
    
    combined = results1 + results2

    print(f"Total results fetched: {len(combined)}")
    return jsonify(combined)

if __name__ == "__main__":
    app.run(port=5000)
