import logging

def get_logger(name: str = "VoiceAgent"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # change to INFO later if too noisy

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s",
            "%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
