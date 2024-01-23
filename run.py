# run.py located at C:\Code\flaskProject9\run.py
from dotenv import load_dotenv
load_dotenv()
from yourapp import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
