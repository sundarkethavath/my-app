import json
import os
from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler
from CORS import enable_cors

# Load the student data from the file
def load_student_data():
    try:
        with open(os.path.join(os.path.dirname(__file__), 'data/students.json')) as f:
            return json.load(f)
    except FileNotFoundError:
        raise Exception("students.json file not found")
    except json.JSONDecodeError:
        raise Exception("Error decoding students.json")

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS for all origins
        enable_cors(self)
        
        # Parse query parameters
        query_params = parse_qs(self.path.split('?')[1])
        names = query_params.get('name', [])
        
        # Load student data
        students = load_student_data()
        
        # Find marks of the requested names
        marks = []
        for name in names:
            student = next((s for s in students if s['name'] == name), None)
            if student:
                marks.append(student['marks'])
            else:
                marks.append(None)  # Handle case where name is not found
        
        # Prepare the response data
        response_data = {'marks': marks}
        
        # Send JSON response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode('utf-8'))
        return
