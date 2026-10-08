import subprocess
import platform


class PingTool:

    def ping(self, host):
        param = "-n" if platform.system() == "Windows" else "-c"

        subprocess.run(["ping", param, "4", host])