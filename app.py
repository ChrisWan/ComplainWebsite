"""
Complaint Management System - Main Flask Application
A colorful and animated web application to help manage complaints with encouraging quotes.
"""

from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime
import random
from config.settings import Config
from config.quotes import ENCOURAGING_QUOTES

app = Flask(__name__)
app.config.from_object(Config)

def load_complaints():
    """Load complaints from JSON file"""
    if os.path.exists(app.config['COMPLAINTS_FILE']):
        try:
            with open(app.config['COMPLAINTS_FILE'], 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading complaints: {e}")
            return []
    return []

def save_complaints(complaints):
    """Save complaints to JSON file"""
    try:
        # Ensure data directory exists
        os.makedirs(os.path.dirname(app.config['COMPLAINTS_FILE']), exist_ok=True)
        with open(app.config['COMPLAINTS_FILE'], 'w', encoding='utf-8') as f:
            json.dump(complaints, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving complaints: {e}")

@app.route('/')
def index():
    """Main page route"""
    return render_template('index.html')

@app.route('/api/quote')
def get_quote():
    """Get a random encouraging quote"""
    quote = random.choice(ENCOURAGING_QUOTES)
    return jsonify({'quote': quote})

@app.route('/api/complaints', methods=['GET'])
def get_complaints():
    """Get all open complaints"""
    complaints = load_complaints()
    return jsonify(complaints)

@app.route('/api/complaints', methods=['POST'])
def add_complaint():
    """Add a new complaint"""
    data = request.get_json()
    complaint_text = data.get('complaint', '').strip()
    
    if not complaint_text:
        return jsonify({'error': 'Complaint text is required'}), 400
    
    complaints = load_complaints()
    new_complaint = {
        'id': len(complaints) + 1,
        'text': complaint_text,
        'timestamp': datetime.now().isoformat(),
        'status': 'open'
    }
    
    complaints.append(new_complaint)
    save_complaints(complaints)
    
    return jsonify({'success': True, 'complaint': new_complaint})

@app.route('/api/complaints/<int:complaint_id>', methods=['DELETE'])
def remove_complaint(complaint_id):
    """Remove a complaint by ID"""
    complaints = load_complaints()
    complaints = [c for c in complaints if c['id'] != complaint_id]
    save_complaints(complaints)
    
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
