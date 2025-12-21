import os
import sys
import socket
import webbrowser
import subprocess
from http.server import SimpleHTTPRequestHandler
from socketserver import ThreadingTCPServer

# Always run in script directory
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

DEFAULT_PORT = 9000
APP_NAME = "app.html"

def is_termux() -> bool:
    return (
        "com.termux" in os.getenv("PREFIX", "") or
        os.path.exists("/data/data/com.termux/files/usr")
    )

def open_browser(url: str) -> None:
    """Open a browser depending on environment."""
    if is_termux():
        commands = [
            ["termux-open-url", url],
            ["termux-open", url],
            ["xdg-open", url],
            ["am", "start", "-a", "android.intent.action.VIEW", "-d", url],
        ]
        for cmd in commands:
            try:
                subprocess.run(cmd, check=True,
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)
                return
            except Exception:
                pass
        print(" ! Could not open browser automatically.")
        print(" ! Please open manually:", url)
    else:
        webbrowser.open(url)

def get_all_ips() -> list:
    """Return ALL IPv4 addresses on the system, including loopback."""
    ips = set()
    try:
        hostname = socket.gethostname()
        for info in socket.getaddrinfo(hostname, None, family=socket.AF_INET):
            ip = info[4][0]
            if ip and ip != "0.0.0.0":
                ips.add(ip)
    except Exception:
        pass
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            if ip and ip != "0.0.0.0":
                ips.add(ip)
    except Exception:
        pass
    ips.add("127.0.0.1")
    return sorted(ips)

def print_banner(host: str, port: int, directory: str):
    print(" * Serving HTTP files")
    print(f" * Directory: {directory}")
    if host == "0.0.0.0":
        for ip in get_all_ips():
            print(f" * Running on http://{ip}:{port}")
        print(f" * try 'python {sys.argv[0]}' to serve only on http://127.0.0.1:{port}")
    else:
        print(f" * Running only on http://127.0.0.1:{port}")
        print(f" * try 'python {sys.argv[0]} --all' to serve on all network interfaces.")
    print("Press CTRL+C to quit\n")

def start_server(host: str, port: int):
    print_banner(host, port, os.getcwd())
    with ThreadingTCPServer((host, port), SimpleHTTPRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
        finally:
            httpd.server_close()

def main():
    use_all = "--all" in [i.lower() for i in sys.argv]
    host = "0.0.0.0" if use_all else "127.0.0.1"
    port_arg = next((int(arg) for arg in sys.argv if arg.isdigit()), DEFAULT_PORT)
    open_browser(f"http://127.0.0.1:{port_arg}/{APP_NAME}")
    start_server(host, port_arg)

if __name__ == "__main__":
    main()