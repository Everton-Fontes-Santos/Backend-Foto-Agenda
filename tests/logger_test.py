import logging

from FotoAgenda.utils.logger import logger


def test_get_logging_Logger_return():
    """Test if logger func return anything but not None."""
    log = logger()
    assert log != None


def test_get_logging_Logger_intance():
    """Test if logger func return a Logger instance."""
    log = logger()
    assert isinstance(log, logging.Logger)
