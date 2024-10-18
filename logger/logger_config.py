import logging

# ANSI escape codes for colored output
LOG_COLORS = {
    "DEBUG": "\033[94m",    # Blue
    "INFO": "\033[92m",     # Green
    "WARNING": "\033[93m",  # Yellow
    "ERROR": "\033[91m",    # Red
    "CRITICAL": "\033[95m", # Magenta
    "RESET": "\033[0m"      # Reset to default
}

# Custom Formatter with Color Support
class ColoredFormatter(logging.Formatter):
    def format(self, record):
        log_color = LOG_COLORS.get(record.levelname, LOG_COLORS["RESET"])
        reset_color = LOG_COLORS["RESET"]
        # Use record.getMessage() to correctly retrieve the log message
        formatted_message = f"{log_color}{record.levelname}: {record.getMessage()}{reset_color}"
        return formatted_message

# Create a Named Pipe Handler or Fall Back to Console
def get_pipe_handler():
    try:
        # Open the named pipe for writing, with line buffering
        pipe = open("titans.log", "w", buffering=1)  
        return logging.StreamHandler(pipe)
    except Exception as e:
        print(f"Failed to open pipe: {e}")
        return None  # Fallback to console if the pipe isn't available

# Configure and Return a Logger
def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Set log level to capture all messages

    # Use pipe handler if available, otherwise fall back to console
    handler = get_pipe_handler() or logging.StreamHandler()
    handler.setLevel(logging.DEBUG)  # Set the log level for the handler
    handler.setFormatter(ColoredFormatter())  # Use the colored formatter

    # Avoid adding multiple handlers if logger is re-used
    if not logger.handlers:
        logger.addHandler(handler)

    return logger