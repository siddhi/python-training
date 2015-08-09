should_fail = 0


class NetworkException(Exception):
    pass


def access_db(query_string):
    global should_fail
    if query_string is None or query_string == "":
        raise ValueError("query_string cannot be empty")
    print("Entering function: {0}".format(query_string))
    retries = 0
    exception = None
    while retries < 3:
        try:
            val = 2
            if should_fail:
                should_fail = should_fail - 1
                raise NetworkException("Failure accessing DB")
            print("Returning: {}".format(val))
            return val
        except NetworkException as e:
                exception = e
                print("Failed, retrying")
                retries = retries + 1
        except Exception as e:
            print("Exception: {}".format(e))
            raise
    print("All retries failed")
    raise NetworkException(exception)


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
