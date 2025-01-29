def enable_cors(handler):
    handler.send_header('Access-Control-Allow-Origin', '*')
    handler.send_header('Access-Control-Allow-Methods', 'GET')
    handler.send_header('Access-Control-Allow-Headers', 'Content-Type')
