import sys
import os


pyfile = (sys.platform[:3] == "win" and "python.exe") or "python"
pypath = sys.executable


def fixWindowsPath(cmdLine: str) -> str:
    splitline = cmdLine.lstrip().split(" ")
    fixedPath = os.path.normpath(splitline[0])
    return " ".join([fixedPath] + splitline[1:])


class LaunchMode:
    def __init__(self, label, command) -> None:
        self.what = label
        self.where = command

    def __call__(self) -> None:
        self.announce(self.what)
        self.run(self.where)

    def announce(self, text: str) -> None:
        print(text)

    def run(self, cmdline: str) -> None:
        assert False, "run must be defined"


class System(LaunchMode):
    def run(self, cmdline: str) -> None:
        cmdline = fixWindowsPath(cmdLine=cmdline)
        os.system("%s %s" % (pypath, cmdline))


class Popen(LaunchMode):
    def run(self, cmdline: str) -> None:
        cmdline = fixWindowsPath(cmdLine=cmdline)
        os.popen(pypath + " " + cmdline)


class Fork(LaunchMode):
    """
    run command in explitly created new process
    for Unix-like systems only, inluding cygwin
    """

    def run(self, cmdline: str) -> None:
        assert hasattr(os, "fork")
        cmdline = cmdline.split()
        if os.fork() == 0:
            os.execvp(pypath, [pyfile] + cmdline)


class Start(LaunchMode):
    """
    run command independent of caller
    for Windows only: uses filename associations
    """

    def run(self, cmdline: str) -> None:
        assert sys.platform[:3] == "win"
        cmdline = fixWindowsPath(cmdLine=cmdline)
        os.startfile(cmdline)  # startfile may deprecated


class StartArgs(LaunchMode):
    """
    For Windows only: args may require real 
    start forward slashes are okay here
    """

    def run(self, cmdline: str) -> None:
        assert sys.platform[:3] == "win"
        os.system("start " + cmdline)


class Spawn(LaunchMode):
    """
    run python in new process independent of caller
    for Windows or Unix; use P_NOWAIT for dos box;
    forward slashes are okay here
    """

    def run(self, cmdline):
        os.spawnv(os.P_DETACH, pypath, (pyfile, cmdline))


class TopLavel(LaunchMode):
    """
    run in new window, same process
    tbd: requires GUI class info too
    """

    def run(self, cmdline: str) -> None:
        assert False, "Sorry - mode not yet implemented"


if sys.platform[:3] == "win":
    PortableLauncher = Spawn
else:
    PortableLauncher = Fork


class QuietPortableLauncher(PortableLauncher):
    def announce(self, text) -> None:
        pass


def main():
    file = "echo.py"
    input("default mode...")
    launcher = PortableLauncher(file, file)
    launcher()

    input("system mode...")
    System(file, file)()

    if sys.platform[:3] == "win":
        input("DOS start mode...")
        StartArgs(file, file)()


if __name__ == "__main__":
    main()
