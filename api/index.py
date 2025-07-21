# /api/index.py
from mangum import Mangum
from src.main import app

handler = Mangum(app)
