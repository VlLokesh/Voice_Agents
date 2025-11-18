import asyncio
from deepgram import DeepgramClient, LiveOptions
from app.core.logger import get_logger

logger = get_logger("STT")

class STTStream:
    def __init__(self, api_key):
        logger.info("Initializing Deepgram STT client")
        self.client = DeepgramClient(api_key)

    async def start(self, callback):

        logger.info("Connecting to Deepgram STT (Realtime)...")

        try:
            # OPEN STREAM
            stream = self.client.listen.live.v("1")

            # START STREAM
            await stream.start(
                LiveOptions(
                    model="nova-2",
                    smart_format=True,
                    language="ta,en,hi,kn,te",
                    punctuate=True
                )
            )

            logger.info("STT WebSocket connected. Speak now...")

            # ATTACH CALLBACK
            async def on_transcript(dg_data, **rest):
                try:
                    text = dg_data.channel.alternatives[0].transcript
                    if text.strip():
                        callback(text)
                except Exception as e:
                    logger.error(f"Transcript parse error: {e}")

            stream.on_transcript = on_transcript

            # KEEP STREAM OPEN
            while True:
                await asyncio.sleep(0.1)

        except Exception as e:
            logger.error(f"Deepgram STT Error: {e}")