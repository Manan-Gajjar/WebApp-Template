import os
from app import create_app

env = os.environ.get("ENV")
if not env:
    env = 'local'

app = create_app(env)

if __name__ == '__main__':
    app.run()
