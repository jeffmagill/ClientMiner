from clientminer import app
import sys

if __name__ == '__main__':
    target = sys.argv[1]
    app.run(target)
