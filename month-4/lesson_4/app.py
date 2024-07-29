from info import log_decorator

class FunctionExecutionError(Exception):
    def __init__(self, message, *args):
        super().__init__(message, *args)
        self.message = message

    def __str__(self):
        return self.message


@log_decorator
def add(a, b):
    return a + b


if __name__ == "__main__":
    add(1, "2")

# date_string = "2024-07-26 16:53:31"
# date_format = "%Y-%m-%d %H:%M:%S"
#
# date_time_obj = datetime.strptime(date_string, date_format)
