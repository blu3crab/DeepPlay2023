import time


class stopwatch:
    def __init__(self, start=time.time(), stop=time.time()):
        self.starttime = start
        self.stoptime = stop

    def start(self):
        self.starttime = time.time()

    def stop(self):
        self.stoptime = time.time()
        print(f"timer duration -> {((self.stoptime - self.starttime) / 60):.2f}m")

    def stopwatch_wrapper(func):
        def wrapper(*args, **kwargs):
            # start the timer
            start_time = time.time()
            # call the decorated function
            result = func(*args, **kwargs)
            # remeasure the time
            end_time = time.time()
            # compute the elapsed time and print it
            execution_time = end_time - start_time
            print(f"{func.__name__} Execution time: {execution_time/60:.2f}m")
            # return the result of the decorated function execution
            return result
        # return reference to the wrapper function
        return wrapper