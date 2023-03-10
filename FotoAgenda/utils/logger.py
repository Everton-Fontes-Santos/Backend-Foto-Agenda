import logging

from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)


def logger() -> logging.Logger:
    """Get a Rich adapted logger."""
    return logging.getLogger("rich")
