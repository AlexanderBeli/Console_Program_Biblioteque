from src.messages import MESSAGES
from src.Application.UseCase.BibliotequeAdministratingUseCase import run


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print(MESSAGES["exit_message"])
