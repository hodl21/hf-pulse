import requests
import pandas
import datetime
import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


HF_API_BASE = "https://huggingface.co/api"
BRONZE_PATH = os.path.join(os.path.dirname(__file__), "../data/bronze")
AMX_MODELS = 5000

