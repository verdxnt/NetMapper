import socket
import argparse

def check_port(host, port, timeout=2) -> bool:
    """Check if a specific port is open on the given host
        Return True if the port is open, False otherwise (closed or filtered)
    ."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect_ex((host, port))
        s.close()
        return result == 0

    except socket.gaierror:
        """
        socket.gaierror in Python is the same kind of error as “Could not resolve hostname” 
        in the terminal—both mean DNS resolution failed.
        Remember DNS resolution is the process of converting a hostname (like www.example.com) into an IP address 
        (like: "example.com"  →  DNS lookup  →  93.184.216.34)
        """
        print(f"[ERROR] Could not resolve hostname: {host}")
        return False
    except socket.error as e:
        """
        socket.error is a general exception for socket-related errors, which can include issues like:
            The network interface going down mid-scan
            The OS refusing to create a socket (too many open connections)
            A firewall on your own machine blocking the outbound connection
            The target actively resetting the connection in an unexpected way

            as e captures the specific error message, it can provide more insight 
            into what went wrong during the scanning process.
        """
        print(f"[ERROR] Socket error: {e}")
        return False
    
def scan_ports(host, start_port, end_port):
    """Scan a range of ports on the given host and print the results."""

    open_ports = [] #open ports found will be stored in this array
    print(f"Scanning {host} from port {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        if check_port(host, port):
            print(f"[+] Port {port} is OPEN.")
            open_ports.append(port)
        else:
            print(f"[-] Port {port} is CLOSED or FILTERED.")
    
    print(f"Scan complete. {len(open_ports)} Open ports found: {open_ports}")
    return open_ports

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple TCP Port Scanner")
    parser.add_argument("--host", required=True, help="Target hostname or IP")
    parser.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end", type=int, default=1024, help="End port (default: 1024)")
    args = parser.parse_args()

    open_ports = scan_ports(args.host, args.start, args.end)