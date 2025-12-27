from mcp.server.fastmcp import FastMCP
from ssh_client import KaliSSH

mcp = FastMCP("kali-mcp")

_ssh = None


@mcp.tool()
def run_command(cmd: str) -> str:
    """
    Run a command on Kali Linux via SSH.
    """
    global _ssh
    if _ssh is None:
        _ssh = KaliSSH()
    return _ssh.run(cmd)


if __name__ == "__main__":
    mcp.run()
