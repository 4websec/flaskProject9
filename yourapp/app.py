# app.py located at c:\Code\flaskProject9\yourapp\app.py
from yourapp import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
