import paramiko


class KaliSSH:
    def __init__(self):
        self.host = "192.168.56.106"
        self.user = "kali"
        self.password = "kali"

        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self.client.connect(
            hostname=self.host,
            username=self.user,
            password=self.password,
            timeout=5
        )

    def run(self, cmd: str) -> str:
        stdin, stdout, stderr = self.client.exec_command(cmd)
        out = stdout.read().decode()
        err = stderr.read().decode()
        return out + err
