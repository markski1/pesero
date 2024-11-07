import flask
import sys

from dotenv import load_dotenv

from core import create_app

print(f"Version de Python: {sys.version}")
print(f"Version de Flask: {flask.__version__}")

load_dotenv()

app = create_app()
