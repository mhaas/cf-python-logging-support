""" Module to test the cf_logging library """
import logging
import io
from json import JSONDecoder
import cf_logging

from cf_logging.formatters.json_formatter import JsonFormatter
from json_validator.validator import JsonValidator
from tests.log_schemas import CLI_LOG_SCHEMA
from tests.util import config_root_logger

# pylint: disable=protected-access

def test_critical():
    """ Test the cf_logger as a standalone """
    cf_logging.init(level=logging.DEBUG)
    logger, stream = config_root_logger('cli.test')
    logger.info('hi')
    log_json = JSONDecoder().decode(stream.getvalue())
    _, error = JsonValidator(CLI_LOG_SCHEMA).validate(log_json)

    cf_logging._setup_done = False

    assert error == {}