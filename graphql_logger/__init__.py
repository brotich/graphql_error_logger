import logging

from flask_graphql import GraphQLView
from graphql_server import default_format_error


def init_logger(logger=None):
    if not logger:
        logger = logging.getLogger("graphql-error-logger")
        logger.setLevel(logging.ERROR)

    @staticmethod
    def test_logging_update(error):
        logger.error('error in resolvers', exc_info=error.original_error)
        return default_format_error(error)

    GraphQLView.format_error = test_logging_update