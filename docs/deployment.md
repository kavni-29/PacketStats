# Installation and operation

## Requirements

- Python 3.10 or newer.
- Tkinter for the GUI.
- Windows, Linux, or macOS for offline analysis. Live capture depends on platform support and permissions.
- Windows live capture requires Npcap. Linux/macOS require an available libpcap/BPF capture backend.

## Install from a Git checkout

### Windows PowerShell

```powershell
git clone https://github.com/kavni-29/packetstats.git
Set-Location packetstats
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

If activation is blocked for the current PowerShell session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
git clone https://github.com/kavni-29/packetstats.git
cd packetstats
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

## Offline operation

Launch the GUI:

```bash
python -m packetstats.gui
```

Analyze the checked-in sample capture using the CLI:

```bash
python -m packetstats.cli --input samples/synthetic_demo.pcap --output reports/demo --charts
```

Use `python -m packetstats.cli --help` to see CLI commands. Offline analysis does not need admin/root privileges or an active capture interface. Reports are written locally and are ignored by Git.

Regenerate the synthetic sample if needed:

```bash
python samples/generate_sample_pcap.py
```

## Live capture

Install the OS capture driver/backend separately. For Windows, use the [official Npcap site](https://npcap.com/). Restart the terminal or application after installation. Interface discovery:

```bash
python -m packetstats.cli interfaces
```

CLI capture and recording example:

```bash
python -m packetstats.cli live --interface "<interface-id>" --duration 10 --record captures/session.pcapng
python -m packetstats.cli --input captures/session.pcapng --output reports/session
```

The GUI provides interface selection and start/stop controls in **Live Monitoring**. Select only interfaces and networks you are authorized to monitor. Packet recording is optional and may retain sensitive network metadata. PacketStats does not inject or transmit traffic.

Automated tests use a mocked backend; they cannot confirm Npcap installation, physical adapter operation, or capture permissions. Validate those manually on each target system.

## Configuration and output

Detection thresholds use `DetectionConfig` in `packetstats/config.py`; JSON load/save helpers are provided by that class. CLI configuration options are described by `python -m packetstats.cli --help`. CLI output formats are `all`, `csv`, `json`, `md`, `pdf`, and `none`; `--charts` saves standalone PNGs.

## CI

The GitHub Actions workflow is in `.github/workflows/ci.yml`. It runs automated checks on configured Python/platform combinations and uses synthetic captures. CI does not perform physical live capture.
