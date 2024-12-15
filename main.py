from src.config.messages import MESSAGES
from src.presentation.cli.logic import run
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        logging.error(MESSAGES["exit_message"])
