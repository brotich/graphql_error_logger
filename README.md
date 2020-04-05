## Summary
- allows for the logging of the exception happening in the flask-graphql framework.
- this hooks into the graphql error handler and logs the original error, along with its stacktrace

- this allows one to see the data for an error like
```graphql
{
  "errors": [
    {
      "message": "sdsd",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": [
        "users"
      ]
    }
  ],
  "data": {
    "users": null
  }
}
```

as
```pythontb
2020-04-06 00:02:43,217 - LIA-logger:30 - ERROR - error in resolvers
Traceback (most recent call last):
  File "/Users/brianrotich/.pyenv/versions/3.6.10/envs/test-app/lib/python3.6/site-packages/graphql/execution/executor.py", line 452, in resolve_or_error
    return executor.execute(resolve_fn, source, info, **args)
  File "/Users/brianrotich/.pyenv/versions/3.6.10/envs/test-app/lib/python3.6/site-packages/graphql/execution/executors/sync.py", line 16, in execute
    return fn(*args, **kwargs)
  File "/Users/brianrotich/.pyenv/versions/3.6.10/envs/test-app/lib/python3.6/site-packages/graphene/relay/connection.py", line 161, in connection_resolver
    resolved = resolver(root, info, **args)
  File "/Users/brianrotich/codes/app/test-app/__init__.py", line 187, in resolve_users
    raise ValueError('sdsd')
ValueError: sdsd
```

## Usage
a. using an existing logger in the `app.py`
```python
import logging

import graphql_error_logger

def create_app():
    # logger initialization and configuration
    logger= logging.getLogger(__name__)
    graphql_error_logger.init_logger(logger)
```

b. if no logger is provided, the library creates a logger called `graphql-error-logger` automatically

```python

import graphql_error_logger

def create_app():
    graphql_error_logger.init_logger()
```

- this logger is configured to use the `ERROR` log level to log the exception stacktrace
