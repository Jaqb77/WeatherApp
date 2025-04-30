def logsWrite(filename, x: str):
    with open(filename, "a") as logs:
        logs.write(x)

def logsRead(filename):
    with open('logs.txt') as file:
        print(file.read())