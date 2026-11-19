# NetScope

NetScope is a Python desktop and command-line application for offline PCAP/PCAPNG analysis and optional live packet capture. It parses packet metadata, aggregates bidirectional flows, calculates traffic statistics, evaluates six explainable heuristic rules, and exports reports.

It does not decrypt encrypted traffic, inject packets, or establish that an alert is an attack. Use it only on captures and networks you are authorized to inspect.

## Current features

- PCAP and PCAPNG parsing with Scapy.
- IPv4/IPv6, TCP/UDP, ICMP/ICMPv6, ARP and IGMP classification, with decoded header metadata where available.
- Bidirectional flow aggregation with direction-specific packet and byte counts.
- Protocol, endpoint, packet size, and time-bucket statistics.
- Six configurable heuristic detectors with evidence and benign-use context.
- Tkinter desktop app with summary, flow, endpoint, alert, chart, report, live monitoring, and paginated Packet Explorer views.
- CLI for offline analysis, inspection, flows, alerts, live capture, and interface listing.
- CSV, JSON, Markdown, and PDF reports, plus PNG charts.
- Optional PCAPNG recording during live capture.

The Packet Explorer displays 500 rows per page and supports protocol filtering and text search. It shows decoded header metadata; raw payload bytes are not retained by default.

## Requirements

- Python 3.10 or later.
- Tkinter for the desktop GUI (often included with Python on Windows; Linux distributions may package it separately).
- Live capture requires an OS packet capture backend and suitable permissions. Windows requires Npcap. Offline capture analysis does not require capture privileges.

## Reproducible setup

Clone the repository and create an isolated environment from the repository root.

### Windows PowerShell

```powershell
git clone https://github.com/kavni-29/netscope.git
Set-Location netscope
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

If PowerShell blocks activation, allow it for the current process and retry:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### Linux and macOS

```bash
git clone https://github.com/kavni-29/netscope.git
cd netscope
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

Alternatively, install runtime requirements with `pip install -r requirements.txt`; install pytest separately if you plan to run tests. The editable install also exposes the `netscope` command.

## Run the application

### Desktop GUI

```bash
python -m netscope.gui
```

Choose a PCAP/PCAPNG using **Browse**, then select **Analyse Capture**. The Packet Explorer, Flows, Endpoints, Anomaly Alerts, Visualisations, Reports, and Live Monitoring views are available in the notebook tabs.

### CLI quick start

Analyze the included sample capture and create reports:

```bash
python -m netscope.cli --input samples/synthetic_demo.pcap --output reports/demo --charts
```

On Windows PowerShell, the same command works with backslashes in paths. The `reports/` directory is local generated output and is ignored by Git.

Useful commands:

```bash
python -m netscope.cli --help
python -m netscope.cli inspect samples/synthetic_demo.pcap --limit 20
python -m netscope.cli flows samples/synthetic_demo.pcap --top 10
python -m netscope.cli alerts samples/synthetic_demo.pcap
python -m netscope.cli interfaces
```

Generate the deterministic sample capture again:

```bash
python samples/generate_sample_pcap.py
```

## Live capture

Install [Npcap](https://npcap.com/) on Windows, or the relevant libpcap/BPF backend on Linux/macOS. Restart the application after installing a driver. List interfaces with `python -m netscope.cli interfaces`, then select one in the GUI or pass its identifier to the CLI:

```bash
python -m netscope.cli live --interface "<interface-id>" --duration 10 --record captures/session.pcapng
python -m netscope.cli --input captures/session.pcapng --output reports/session
```

Live capture observes traffic available at the selected capture point; it does not generate traffic. Raw capture recording is opt-in. Capture files may contain sensitive metadata and should be handled accordingly. Automated tests mock capture and do not verify a physical interface or driver.

## Tests

Run from the repository root:

```bash
python -m pytest
```

The suite covers parsing, flow aggregation, statistics, detectors, report exports, CLI behavior, offline integration, and mocked live-capture behavior. It does not require Npcap or root/administrator access. A manual live-capture check is still needed on the target machine.

## Packet accounting

The summary reports captured records, fully parsed records, partial parses, parse failures, classified records, records included in flows, and records without flow endpoints separately. Each yielded record receives one primary protocol label; failed records use `CORRUPTED`. Protocol counts therefore sum to yielded capture records. Flow aggregation requires both IP endpoints, so flow packet totals can be lower.

Endpoint packet totals count participation at both ends of a packet and can sum to twice the capture count. The endpoint concentration detector instead reports source-originated share, with captured packet count as its denominator; this share cannot exceed 100%. See [data model and accounting](docs/data_model.md).

## Known limitations

NetScope is a student network analysis project, not a full protocol forensic suite. It does not currently provide dedicated TCP handshake or DNS transaction dashboards, capture-to-capture comparison, topology graphing, comprehensive protocol decoding, or all the advanced detectors described in possible future plans. GUI payload hex inspection, light/dark theme switching, and persistent theme preferences are also not implemented. Detection results are heuristics and can produce false positives. Encrypted application payloads are not decoded.

## Repository map

```text
netscope/       Application package (parser, flows, statistics, detectors, GUI, CLI)
tests/          Automated unit and integration tests
samples/        Synthetic PCAP generator and sample capture
docs/           Architecture, deployment, data model, detection, and testing notes
```

## Documentation

- [Architecture](docs/architecture.md)
- [Data model and accounting](docs/data_model.md)
- [Deployment and setup](docs/deployment.md)
- [Detection rules](docs/detection_rules.md)
- [Testing](docs/testing.md)
