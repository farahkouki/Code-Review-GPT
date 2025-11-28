from dotenv import load_dotenv
import os

load_dotenv()  # charge les variables du fichier .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
DUPLICATION_SIM_THRESHOLD = float(os.getenv("DUPLICATION_SIM_THRESHOLD", 0.85))
