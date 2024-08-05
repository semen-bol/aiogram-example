def checkForCommand(s: list):
    if s[0] == "/" or s[0] == "!":
        return True
    else: return False

def cmdnoprefandargs(s: list):
    del s[0]; c = "".join(s).split(" ")[0]
    return c