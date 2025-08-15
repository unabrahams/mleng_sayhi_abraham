import os
from datetime import datetime
from typing import Final

# User tag included in the output filename
USER_NAME: Final[str] = "abrahamgc"
# Version tag included in the output filename
VERSION:   Final[str] = "1.0.0"

# Container output directory (mapped to host: /opt/assignment_outputs)
DEFAULT_DIR: Final[str] = "/app/data"


def say_hi(msg: str = "Hi!", file_directory: str = DEFAULT_DIR) -> None:
    """
    Write `msg` to a timestamped file in `file_directory`.
    """
    os.makedirs(file_directory, exist_ok=True)

    # UTC timestamp, e.g. 20250815T233012Z
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

    file_name = f"outputfile_{USER_NAME}_{VERSION}_timestamp_{timestamp}.txt"
    file_path = os.path.join(file_directory, file_name)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(msg + "\n")

    print(f"File '{file_path}' created successfully.")


def add_numbers(a: int, b: int) -> int:
    """Helper used by tests."""
    return a + b


if __name__ == "__main__":
    say_hi()

