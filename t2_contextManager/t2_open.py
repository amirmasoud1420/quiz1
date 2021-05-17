import jdatetime


class file_open:
    def __init__(self, *args, **kwargs):
        self.f = open(*args, **kwargs)
        self.file_path = args[0]

    def __enter__(self):
        self.open_time = jdatetime.datetime.now
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_time = jdatetime.datetime.now
        with open(self.file_path, 'a')as f:
            f.write('\nOpen Time : ' + self.open_time)
            f.write('\nClose Time : ' + self.close_time)
        self.f.close()
        return True

