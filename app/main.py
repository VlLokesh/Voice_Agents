import asyncio
from app.config.settings import settings
from app.core.logger import get_logger
from app.core.stt import STTStream

logger = get_logger("Main")

def stt_callback(text):
    logger.info(f"[STT] {text}")

async def main():
    logger.info("=== STT Test Mode Started ===")
    stt = STTStream(settings.DEEPGRAM_API_KEY)
    await stt.start(stt_callback)

if __name__ == "__main__":
    asyncio.run(main())
