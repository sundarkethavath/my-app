def enable_cors(handler):
    handler.send_header('Access-Control-Allow-Origin', '*')
    handler.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')  # Allow OPTIONS for pre-flight
    handler.send_header('Access-Control-Allow-Headers', 'Content-Type')
    if handler.command == 'OPTIONS':
        handler.send_response(200)
        handler.end_headers()
