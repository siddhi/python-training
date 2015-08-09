should_fail = 0


class NetworkException(Exception):
    pass


def not_null(param):
    def decorator(fn):
        def not_null_fn(**kwargs):
            val = kwargs[param]
            if val is None or val == "":
                raise ValueError("{} cannot be empty".format(param))
            return fn(**kwargs)
        return not_null_fn
    return decorator


def log(fn):
    def logged_fn(**kwargs):
        try:
            print("Entering function: {0}".format(kwargs))
            val = fn(**kwargs)
            print("Returning: {}".format(val))
            return val
        except Exception as e:
            print("Exception: {}".format(e))
            raise Exception(e)
    return logged_fn


def retry(fn):
    def retry_fn(**kwargs):
        retries = 0
        exception = None
        while retries < 3:
            try:
                return fn(**kwargs)
            except NetworkException as e:
                exception = e
                print("Failed, retrying")
                retries = retries + 1
        print("All retries failed")
        raise NetworkException(exception)
    return retry_fn


@not_null("query_string")
@log
@retry
def access_db(query_string):
    global should_fail
    val = 2
    if should_fail:
        should_fail = should_fail - 1
        raise NetworkException("Failure accessing DB")
    return val

if __name__ == "__main__":
    import sys
    if "--temporary-fail" in sys.argv:
        should_fail = 2
    if "--permanent-fail" in sys.argv:
        should_fail = 4
    if "--null" in sys.argv:
        access_db(query_string=None)
    else:
        access_db(query_string="select * from table;")
