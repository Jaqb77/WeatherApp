def logsWrite(x: str):
    with open("logs.txt", "a") as logs:
        logs.write(x)

def logsRead():
    with open('logs.txt') as file:
        print(file.read())