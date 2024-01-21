from dotenv import load_dotenv

load_dotenv()

from yourapp.app import create_app

app = create_app()
