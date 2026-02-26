# network-scanner
🛡️ Python Network Scanner &amp; Port Analyzer
A beginner-friendly, Python-based network reconnaissance tool that scans hosts for open ports, identifies running services, grabs banners, and logs results in a structured format.

This project is built to learn how tools like Nmap work under the hood, not just how to use them. It focuses on raw sockets, TCP connections, basic service detection, and practical security concepts like attack surface and reconnaissance.

*🚀 Features*

✅ Scan a target host for open TCP ports

✅ Identify common services (HTTP, SSH, FTP, etc.) by port and banner

✅ Grab service banners where available

✅ Run scans in parallel using threading / concurrent.futures for speed

✅ Log results to a file (JSON or plain text)

✅ Simple command-line interface (CLI) using argparse

🌱 Stretch goal: Flag potentially risky ports and explain why they matter

*🧠 What This Project Teaches*
Networking (Network+ Reinforcement)

How TCP connections actually work (SYN → SYN-ACK → ACK)

What ports and sockets are at the code level

Why ports like 22, 80, 443, 3389 are important
x
The difference between open, closed, and filtered ports

How scanning traffic looks on the wire (great to pair with Wireshark)

*Security Concepts*

Reconnaissance as the first phase of security testing and attacks

Banner grabbing and why version info matters

What “attack surface” means in real systems

Why firewalls and port filtering exist

*Python Skills*

Using the built-in socket library

Writing concurrent code for faster scans

Building a real CLI tool with argparse

Saving structured output with the json module

Organizing a small but real-world style project

*🛠 Requirements*

Python 3.8+

Linux, macOS, or Windows (tested on Linux Mint)

No external Python libraries required for the core scanner

Optional but highly recommended:

	Nmap (for comparison):

	sudo apt install nmap

Wireshark (to watch your packets in action)

*📦 Installation*

Clone the repository:

	git clone https://github.com/your-username/network-scanner.git
	cd network-scanner

(Optional) Create a virtual environment:

	python3 -m venv venv
	source venv/bin/activate
*▶️ Usage*

Basic scan of a target:

	python scanner.py scan 192.168.1.1

Scan a specific port range:

	python scanner.py scan 192.168.1.1 --ports 1-1024

Save results to a JSON file:

	python scanner.py scan 192.168.1.1 --output results.json

Increase speed with more threads:

	python scanner.py scan 192.168.1.1 --threads 100
📄 Example Output (JSON)
{
  "target": "192.168.1.1",
  "open_ports": [
    {
      "port": 22,
      "service": "SSH",
      "banner": "OpenSSH 8.2p1 Ubuntu"
    },
    {
      "port": 80,
      "service": "HTTP",
      "banner": "Apache/2.4.41"
    }
  ]
}
