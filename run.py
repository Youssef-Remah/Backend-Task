"""
This file is the entry point for starting the application
"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    #running in dev mode
    app.run(debug=True)
