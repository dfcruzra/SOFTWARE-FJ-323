"""
logger.py

Centralized logging utility for the project.

Purpose:
- Store system errors in a text file
- Keep a history of failures for debugging
- Automatically create log folders/files if they do not exist
- Prevent the application from crashing while logging errors
"""

# Built-in module used for date and time handling
from datetime import datetime

# Built-in module used for file and directory operations
import os


# Main log directory
LOG_FOLDER = "logs"

# Main log file path
LOG_FILE = os.path.join(LOG_FOLDER, "log.txt")


def register_log(error):
    """
    Save error information into a log file.

    Parameters:
        error (Exception | str):
            The error object or custom message to save.

    Behavior:
    - Creates the logs folder automatically if missing
    - Creates log.txt automatically if missing
    - Appends new logs without deleting old logs
    - Adds timestamp for easier debugging
    """

    try:
        # --------------------------------------------------
        # Create logs directory if it does not exist
        # --------------------------------------------------
        os.makedirs(LOG_FOLDER, exist_ok=True)

        # --------------------------------------------------
        # Build timestamp
        # Example:
        # 2026-05-07 18:45:31
        # --------------------------------------------------
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # --------------------------------------------------
        # Build final log line
        # --------------------------------------------------
        log_message = f"[{timestamp}] ERROR -> {str(error)}\n"

        # --------------------------------------------------
        # Append log safely
        # UTF-8 prevents encoding issues with symbols
        # --------------------------------------------------
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(log_message)

    except Exception as critical_error:
        """
        Final safety layer.

        If logging itself fails, we print the problem.
        This prevents silent failures.
        """

        print("\nCRITICAL LOGGING FAILURE")
        print(f"Could not save log: {critical_error}")
