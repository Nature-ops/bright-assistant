import logging
from pathlib import Path

# Create logs directory if it doesn't exist
log_dir = Path("data/logs")
log_dir.mkdir(parents=True, exist_ok=True)

log_file = log_dir / "bright_assistant.log"

logger = logging.getLogger("bright-assistant")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

# Console output
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# File output
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)

# Avoid duplicate handlers when Uvicorn reloads
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)