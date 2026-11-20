# Testing and reproducibility

## Environment

Use Python 3.10+ and install the project with its development dependency:

```bash
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
# Linux/macOS: source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

Run the complete test suite from the repository root:

```bash
python -m pytest
```

For verbose output, use `python -m pytest -v`. On Windows environments where pytest's default virtualized temporary path cannot be written by subprocesses, use a temporary directory inside the checkout:

```powershell
python -m pytest -q --basetemp=.pytest-run
Remove-Item -LiteralPath .pytest-run -Recurse -Force
```

Do not commit `.pytest-run`; it is local test output.

## What the suite covers

- `test_parser.py`: PCAP validation, protocol metadata, and packet normalization.
- `test_flows.py`: canonical flow keys and directional accounting.
- `test_statistics.py`: protocol, endpoint, packet size, and time series metrics.
- `test_detectors.py`: six implemented detector rules.
- `test_reporting.py`: CSV, JSON, Markdown, PDF export behavior.
- `test_cli.py`: CLI success and error paths.
- `test_integration.py`: offline pipeline integration.
- `test_live.py`: mocked capture lifecycle and recording behavior.

The tests do not open physical network interfaces, require admin/root access, or verify Npcap/libpcap operation.

## Reproduce a sample analysis

The sample capture is `samples/synthetic_demo.pcap`. Recreate it deterministically with:

```bash
python samples/generate_sample_pcap.py
```

Then run:

```bash
python -m packetstats.cli --input samples/synthetic_demo.pcap --output reports/repro --charts
```

Review generated local files under `reports/repro/`. These include report exports and chart images. Timing fields can vary across runs and machines.

## Manual GUI and live-capture checks

1. Run `python -m packetstats.gui` and load the sample PCAP.
2. Confirm summary, protocol rows, flows, endpoints, alerts, charts, and Packet Explorer rows appear.
3. Select packets and verify the decoded header fields are consistent with the displayed packet.
4. Export a report and confirm the selected output path contains the requested artifacts.
5. For live capture only, install the platform backend, run `python -m packetstats.cli interfaces`, select an authorized interface, capture briefly, stop, and parse the recorded PCAPNG offline.

Manual live checks are platform-dependent and should be recorded separately from automated test results.
