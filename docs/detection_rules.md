# Detection rules

PacketStats currently implements six deterministic heuristic rules. A triggered rule means the observed values crossed a configured threshold; it does not prove malicious activity. Capture duration, direction visibility, sampling, and ordinary application behavior affect results.

Rules are evaluated by `DetectionEngine` in `packetstats/detectors.py`. Thresholds and windows are defined in `DetectionConfig` (`packetstats/config.py`) and can be loaded from JSON. See `python -m packetstats.cli --help` and the config class for available options.

## 1. High Packet Rate Observation

Counts source-originated packet timestamps in a sliding window of width `high_packet_rate_window_sec`. An alert is generated when the highest window count is greater than `high_packet_rate_threshold`. The configured policy may count source only or both endpoint participations. Bursty downloads, streaming, and backups can trigger it.

## 2. Destination Port Diversity

For each source, counts distinct destination ports within `port_diversity_window_sec`. An alert is generated when the observed maximum is greater than `port_diversity_threshold`. Browsers, peer-to-peer software, and service discovery can contact many ports legitimately.

## 3. High TCP SYN Ratio Without ACK

For each source, computes the fraction of its observed TCP packets that have SYN set and ACK clear. It evaluates only when the configured minimum TCP packet count is met and the ratio reaches `syn_ratio_threshold`. Asymmetric capture, loss, or incomplete captures can make an ordinary connection look incomplete. This rule does not establish that a handshake failed at the remote host.

## 4. Traffic Volume Statistical Deviation

Calculates byte totals for configured time buckets, then compares each bucket with the capture's mean using a sample standard deviation. A bucket can trigger when it exceeds `volume_deviation_zscore`, subject to the minimum bucket count. Short captures and highly uneven traffic provide weak baselines; a spike can be a normal transfer.

## 5. Endpoint Traffic Concentration

This rule uses **source-originated share**, not endpoint participation:

```text
source share = packets_sent_for_endpoint / total_captured_packets
```

It evaluates captures meeting `traffic_concentration_min_packets` and alerts when the share reaches `traffic_concentration_threshold`. Source-originated shares across endpoints cannot exceed 100%. Endpoint participation counts a packet at both ends and is a separate metric; see [data_model.md](data_model.md).

Central servers, gateways, resolvers, and narrowly targeted captures commonly concentrate traffic.

## 6. Repeated Communication Pattern

Groups traffic by source, destination, and destination port, then evaluates packet counts in a sliding `repeated_comm_window_sec` window. An alert is generated when the maximum count exceeds `repeated_comm_threshold`. Keep-alives, polling, and synchronization traffic may trigger it.

## Interpretation

Alerts include rule name, severity, observed value, threshold, explanation, and supporting metadata where available. Treat an alert as a lead for packet/flow review. Validate it against the capture point, capture duration, expected application behavior, and other evidence.

The repository does not currently implement dedicated SYN flood, retransmission, failed-connection, ICMP burst, DNS NXDOMAIN, or packet-size anomaly rules. Those are possible extensions, not current features.
