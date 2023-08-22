# Network Scanner

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

## Description

A simple Python-based port scanner that allows you to scan open ports on a specified IPv4 address within a given port range. The scanner validates IP addresses, scans the specified ports, and displays open ports along with their associated protocols.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/Kairos-T/Network-Scanner/tree/main
cd Network-Scanner
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the script with the following command:

```bash
python networkscanner.py
```
2. Follow the prompts to enter the IPv4 address and port range you want to scan.

3. The script will display a list of open ports along with their associated protocols.

4. To exit the program, enter 'exit' when prompted for the IP address.

## Output
The script outputs a list of open ports on the specified IP address along with their associated protocols.

Sample Output:

![image](https://github.com/Kairos-T/Network-Scanner/assets/80029462/1c0038ee-4bfc-4042-b97f-f465af748339)


## Dependencies
- Python 3.x
- Python pyfiglet library

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.
