from datetime import datetime


def print_message(level: str, message: str) -> None:
    now = datetime.now()
    formated_now = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{formated_now} [{level}] => {message}")


def info(message: str) -> None:
    print_message("INFO", message)


def debug(message: str) -> None:
    print_message("DEBUG", message)


def warning(message: str) -> None:
    print_message("WARNING", message)


def error(message: str) -> None:
    print_message("ERROR", message)
