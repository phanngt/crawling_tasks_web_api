import os

from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
