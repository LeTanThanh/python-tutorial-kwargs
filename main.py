if __name__ == "__main__":
  # Introduction to the Python **kwargs parameters

  def connect(**kwargs):
    print(type(kwargs))
    print(kwargs)

  connect()
  connect(server = "localhost", port = 3306, user = "root", password = "Py1hon!Xt")

  config = {
    "server": "localhost",
    "port": 3306,
    "user": "root",
    "password": "Py1hon!Xt"
  }
  connect(**config)

  def connect(fn, **kwargs):
    print(kwargs)
