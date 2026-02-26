In Step 3: Create a socket object
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
AF_INET means IPv4 addresses
SOCK_STREAM means TCP (as opposed to UDP)

SOCK_STREAM means:
    “I want a stream-based, reliable, connection-oriented socket.”

In practice, that means:
    👉 You are using TCP
    SOCK_STREAM = TCP socket
    Reliable delivery ✔️
    Ordered data ✔️
    Connection required ✔️ (3-way handshake: SYN → SYN-ACK → ACK)
    Data arrives as a continuous stream of bytes
---------------------------------------------------------------------------------------------------------------------------------

The Contrast: SOCK_DGRAM
socket.SOCK_DGRAM
This means:
    “I want a datagram-based, connectionless socket.”
Which is:
    👉 UDP
    So:
    SOCK_DGRAM = UDP socket
    No connection handshake ❌
    No guaranteed delivery ❌
    No guaranteed order ❌
    Faster, but less reliable

---------------------------------------------------------------------------------------------------------------------------------

How connect_ex() Works:

Return value:
    - 0 means the connection was successful (no error)
    - Any non-zero integer means the connection failed (with that specific error code)

Common Error Codes 
The error codes are operating system-specific, but some common ones include:

    - 0 - Success! Connection established
    - 111 (on Linux) - Connection refused (nothing listening on that port)
    - 110 (on Linux) - Connection timed out (host unreachable or very slow)
    - 113 - No route to host (network issue)
    - 10061 (on Windows) - Connection refused

Why Use connect_ex() Instead of connect()?

connect() - Raises an exception if it fails (you must use try/except)
connect_ex() - Returns an error code (cleaner for just checking if a port is open)  

---------------------------------------------------------------------------------------------------------------------------------

gaierror = Get Address Info error

It comes from the function getaddrinfo(), which is what your system uses to:
    Turn a hostname like google.com into an IP address like 142.250.72.14

    Before your socket can connect, Python (via the OS) must do DNS resolution:
        "example.com"  →  DNS lookup  →  93.184.216.34

^ How this relates to the terminal

🖥️ The terminal case
When you type something like:
    ping notarealhost.zzz

    or:

    ssh madeuphost

You’ll often see an error like:
    ping: notarealhost.zzz: Name or service not known
    or:
    ssh: Could not resolve hostname madeuphost: Name or service not known

What’s happening?

    The OS tries to:
        - Resolve the hostname via DNS (or /etc/hosts)

        - That lookup fails

        - The tool prints an error and stops

That’s the same failure as socket.gaierror.

---------------------------------------------------------------------------------------------------------------------------------

socket.error is a general exception for socket-related errors, which can include issues like:
            The network interface going down mid-scan
            The OS refusing to create a socket (too many open connections)
            A firewall on your own machine blocking the outbound connection
            The target actively resetting the connection in an unexpected way

---------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__": -> Not used ot writing this, in school i always wrote def main(): then called main()

Means:
    “Only run this code if this file is being executed directly, not imported.”

I leanred that he best practice: use both together

In real projects, I'll usually see this:

def main():
    parser = argparse.ArgumentParser(description="Simple TCP Port Scanner")
    parser.add_argument("--host", required=True, help="Target hostname or IP")
    parser.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end", type=int, default=1024, help="End port (default: 1024)")
    args = parser.parse_args()

    scan_ports(args.host, args.start, args.end)


if __name__ == "__main__":
    main()
---------------------------------------------------------------------------------------------------------------------------------

def main(): → “Here’s my program’s entry point”

if __name__ == "__main__": → “Only start the program if this file is run directly”

Together they mean:
    “Run main() only when this script is executed, not when imported.”

example: 
    def main():
    parser = argparse.ArgumentParser(description="Simple TCP Port Scanner")
    parser.add_argument("--host", required=True, help="Target hostname or IP")
    parser.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end", type=int, default=1024, help="End port (default: 1024)")
    args = parser.parse_args()

    scan_ports(args.host, args.start, args.end)


if __name__ == "__main__":
    main()

---------------------------------------------------------------------------------------------------------------------------------

So what does this do specifically? (More details) 

A little bit about ports:
    In the network, there are a total of 65,535 possible ports

    Well Known ports (0-1023) Reserved for system services and standard protocols
         (e.g., 22 for SSH, 80 for HTTP, 443 for HTTPS).

    Registered Ports (1024-49151): Used by specific applications or vendors.

    and

    Dynamic/Ephemeral Ports (49152-65535): Used for temporary, client-side communication. 

    

The Scanner is looking at the TCP ports in the range i specify from the command i made using:
     --start *start number* & --end *end number*