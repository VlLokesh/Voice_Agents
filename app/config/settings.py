import os
from dotenv import load_dotenv
from app.core.logger import get_logger

logger = get_logger("Config")

class Settings:
    def __init__(self):
        # Load .env from project root
        load_dotenv()
        logger.info(".env loaded")

        self.DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

        if not self.DEEPGRAM_API_KEY:
            logger.warning("DEEPGRAM_API_KEY is missing in .env")
        else:
            logger.info("DEEPGRAM_API_KEY found")

        if not self.OPENAI_API_KEY:
            logger.warning("OPENAI_API_KEY is missing in .env")
        else:
            logger.info("OPENAI_API_KEY found")

settings = Settings()
