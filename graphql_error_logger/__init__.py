import logging

from flask_graphql import GraphQLView
from graphql_server import default_format_error


def init_logger(logger: logging = None):
    """binds the logger for GraphQL view to show the stacktrace on stdout

    - This adds a hook into the "GraphQLView.format_error" function in
        flask_graphql to also log the expection in the GraphQLView to the stdout
    - once the exception is logged, call the default error hander for the
        graphql_server package

    Keyword Arguments:
        logger {logging} -- user provided intialized logger if available
                            (default: {None})
    """
    if not logger:
        # initialize logger if not provided
        logger = logging.getLogger("graphql-error-logger")
        logger.setLevel(logging.ERROR)

    @staticmethod
    def log_and_format_exception(error):
        """captures the exception catch in graphql_server and log to the stdout
        with the stacktrace included.

        once thats done, call the default_format_error for the  graphql_server
        package

        Arguments:
            error {[type]} -- error catch by the graphql server

        Returns:
            [str] -- constaining the string representation of the error
                     encountered by the graphql endpoint
        """
        if hasattr(error, "original_error") and isinstance(
            error.original_error, Exception
        ):
            logger.error("error in GraphQL view", exc_info=error.original_error)
        return default_format_error(error)

    GraphQLView.format_error = log_and_format_exception
