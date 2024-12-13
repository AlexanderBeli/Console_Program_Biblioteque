from src.config.messages import MESSAGES
from src.presentation.cli.logic import run


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print(MESSAGES["exit_message"])
