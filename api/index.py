# api/index.py
from mangum import Mangum
from src.main import app  # Make sure app = FastAPI() is in main.py

handler = Mangum(app)
