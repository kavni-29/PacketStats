# PacketStats — Network Traffic Analysis Report
**Generated:** 2026-11-18 23:57:14 UTC  
**Target Capture:** `live interface: \Device\NPF_{ADD140DE-5E06-4124-A825-E49E71690E5F}` (0 bytes)  
**Analysis Runtime:** 0.00 seconds  

---

## 1. Executive Summary

| Metric | Value |
|---|---|
| Total Packets Processed | **253** |
| Packets Skipped / Errors | **0** |
| Total Observed Bytes | **159,818 B** (0.15 MB) |
| Capture Duration | **1.73 seconds** |
| Distinct Endpoints | **9** |
| Bidirectional Flows Identified | **6** |
| Distinct Protocols | **3** |
| Anomaly Alerts Triggered | **6** |

---

## 2. Protocol Distribution

| Protocol | Packet Count | Packet Share | Byte Volume | Byte Share |
|---|---|---|---|---|
| `UDP` | 243 | 96.0% | 159,113 B | 99.6% |
| `IP` | 5 | 2.0% | 270 B | 0.2% |
| `TCP` | 5 | 2.0% | 435 B | 0.3% |

---

## 3. Packet Size Characteristics

| Statistic | Value (Bytes) |
|---|---|
| Minimum Length | 54 B |
| Maximum Length | 1277 B |
| Mean Length | 631.7 B |
| Median Length | 624.0 B |
| 25th Percentile | 124.0 B |
| 75th Percentile | 1135.0 B |
| 95th Percentile | 1254.0 B |
| Standard Deviation | 478.3 B |

### Frame Size Binned Distribution

| Bin Range | Packet Count | Share |
|---|---|---|
| 0-64 B | 5 | 2.0% |
| 65-128 B | 65 | 25.7% |
| 129-256 B | 37 | 14.6% |
| 257-512 B | 2 | 0.8% |
| 513-1024 B | 46 | 18.2% |
| 1025-1518 B | 98 | 38.7% |
| 1519+ B | 0 | 0.0% |

---

## 4. Endpoint Profiles & Traffic Concentration

- **Top 1 Endpoint Concentration:** 95.3% of total packets
- **Top 3 Endpoints Concentration:** 192.5% of total packets
- **Top 5 Endpoints Concentration:** 196.1% of total packets

### Top Talkers (Combined Volume)

| Endpoint IP | Packets Sent | Packets Recv | Total Bytes | Distinct Dst Ports |
|---|---|---|---|---|
| `2001:4860:4864:6:4000::17` | 105 | 136 | 158,845 B | 1 |
| `2405:201:402d:e14b:d0b1:730e:60e7:1189` | 136 | 105 | 158,845 B | 1 |
| `2405:201:402d:e14b:ed7a:7422:37d9:b6a8` | 2 | 3 | 435 B | 1 |
| `192.168.29.69` | 3 | 1 | 376 B | 1 |
| `2606:4700:9641:d8b7:9aa6:6:ccf5:ac50` | 2 | 1 | 274 B | 1 |
| `224.0.0.22` | 0 | 5 | 270 B | 0 |
| `142.250.82.215` | 1 | 1 | 268 B | 1 |
| `192.168.29.60` | 3 | 0 | 162 B | 0 |

---

## 5. Bidirectional Flows Summary (Top 10 by Volume)

| Flow Identifier | Protocol | A -> B Pkts | B -> A Pkts | Total Bytes | Duration |
|---|---|---|---|---|---|
| `UDP:2001:4860:4864:6:4000::17:3478<->2405:201:402d:e14b:d0b1:730e:60e7:1189:52163` | UDP | 105 | 136 | 158,845 B | 1.73s |
| `TCP:2405:201:402d:e14b:ed7a:7422:37d9:b6a8:2363<->2606:4700:9641:d8b7:9aa6:6:ccf5:ac50:443` | TCP | 1 | 2 | 274 B | 0.04s |
| `IP:192.168.29.60<->224.0.0.22` | IP | 3 | 0 | 162 B | 0.00s |
| `IP:192.168.29.69<->224.0.0.22` | IP | 2 | 0 | 108 B | 0.50s |
| `TCP:2405:201:402d:e14b:ed7a:7422:37d9:b6a8:11123<->2606:4700:9642:7cbc:c274:630:5ff2:75c4:443` | TCP | 1 | 1 | 161 B | 0.03s |
| `UDP:142.250.82.215:3478<->192.168.29.69:52162` | UDP | 1 | 1 | 268 B | 0.01s |

---

## 6. Explainable Anomaly Detection Findings

| ID | Severity | Rule Name | Endpoint | Observed vs Threshold | Explanation |
|---|---|---|---|---|---|
| `ALT-CONC-001` | **MEDIUM** | Endpoint Traffic Concentration | `2001:4860:4864:6:4000::17` | `94.0% (141/150 packets)` (Lim: `>=50.0% of capture volume`) | Traffic concentration indicator: Endpoint 2001:4860:4864:6:4000::17 accounted for 141 out of 150 captured packets (94.0%). |
| `ALT-CONC-002` | **MEDIUM** | Endpoint Traffic Concentration | `2405:201:402d:e14b:d0b1:730e:60e7:1189` | `94.0% (141/150 packets)` (Lim: `>=50.0% of capture volume`) | Traffic concentration indicator: Endpoint 2405:201:402d:e14b:d0b1:730e:60e7:1189 accounted for 141 out of 150 captured packets (94.0%). |
| `ALT-RATE-001` | **MEDIUM** | High Packet Rate Observation | `2001:4860:4864:6:4000::17` | `62 packets (62.0 pkts/s)` (Lim: `>50 packets / 1.0s`) | Endpoint 2001:4860:4864:6:4000::17 transmitted 62 packets within a 1.0s window, exceeding the configured threshold of 50 packets. |
| `ALT-RATE-002` | **MEDIUM** | High Packet Rate Observation | `2405:201:402d:e14b:d0b1:730e:60e7:1189` | `79 packets (79.0 pkts/s)` (Lim: `>50 packets / 1.0s`) | Endpoint 2405:201:402d:e14b:d0b1:730e:60e7:1189 transmitted 79 packets within a 1.0s window, exceeding the configured threshold of 50 packets. |
| `ALT-REP-001` | **MEDIUM** | Repeated Communication Pattern | `2001:4860:4864:6:4000::17 -> 2405:201:402d:e14b:d0b1:730e:60e7:1189:52163` | `62 repeated packets` (Lim: `>25 packets / 5.0s`) | Repetitive communication pattern: 2001:4860:4864:6:4000::17 -> 2405:201:402d:e14b:d0b1:730e:60e7:1189:52163 transmitted 62 packets within a 5.0s window. |
| `ALT-REP-002` | **MEDIUM** | Repeated Communication Pattern | `2405:201:402d:e14b:d0b1:730e:60e7:1189 -> 2001:4860:4864:6:4000::17:3478` | `79 repeated packets` (Lim: `>25 packets / 5.0s`) | Repetitive communication pattern: 2405:201:402d:e14b:d0b1:730e:60e7:1189 -> 2001:4860:4864:6:4000::17:3478 transmitted 79 packets within a 5.0s window. |

### Detailed Evidence Breakdown

#### [MEDIUM] ALT-CONC-001: Endpoint Traffic Concentration
- **Target / Scope:** `2001:4860:4864:6:4000::17`
- **Time Window:** Capture Duration
- **Observed Value:** 94.0% (141/150 packets)
- **Configured Threshold:** >=50.0% of capture volume
- **Evidence Summary:** Endpoint total packets: 141, bytes: 89,100. Ratio: 0.940 >= threshold 0.5.
- **Explanation:** Traffic concentration indicator: Endpoint 2001:4860:4864:6:4000::17 accounted for 141 out of 150 captured packets (94.0%).

#### [MEDIUM] ALT-CONC-002: Endpoint Traffic Concentration
- **Target / Scope:** `2405:201:402d:e14b:d0b1:730e:60e7:1189`
- **Time Window:** Capture Duration
- **Observed Value:** 94.0% (141/150 packets)
- **Configured Threshold:** >=50.0% of capture volume
- **Evidence Summary:** Endpoint total packets: 141, bytes: 89,100. Ratio: 0.940 >= threshold 0.5.
- **Explanation:** Traffic concentration indicator: Endpoint 2405:201:402d:e14b:d0b1:730e:60e7:1189 accounted for 141 out of 150 captured packets (94.0%).

#### [MEDIUM] ALT-RATE-001: High Packet Rate Observation
- **Target / Scope:** `2001:4860:4864:6:4000::17`
- **Time Window:** 1.0s [1795046183.981 - 1795046184.965]
- **Observed Value:** 62 packets (62.0 pkts/s)
- **Configured Threshold:** >50 packets / 1.0s
- **Evidence Summary:** Peak packet count: 62 observed in window [1795046183.981 - 1795046184.965]. Policy: source.
- **Explanation:** Endpoint 2001:4860:4864:6:4000::17 transmitted 62 packets within a 1.0s window, exceeding the configured threshold of 50 packets.

#### [MEDIUM] ALT-RATE-002: High Packet Rate Observation
- **Target / Scope:** `2405:201:402d:e14b:d0b1:730e:60e7:1189`
- **Time Window:** 1.0s [1795046184.008 - 1795046184.979]
- **Observed Value:** 79 packets (79.0 pkts/s)
- **Configured Threshold:** >50 packets / 1.0s
- **Evidence Summary:** Peak packet count: 79 observed in window [1795046184.008 - 1795046184.979]. Policy: source.
- **Explanation:** Endpoint 2405:201:402d:e14b:d0b1:730e:60e7:1189 transmitted 79 packets within a 1.0s window, exceeding the configured threshold of 50 packets.

#### [MEDIUM] ALT-REP-001: Repeated Communication Pattern
- **Target / Scope:** `2001:4860:4864:6:4000::17 -> 2405:201:402d:e14b:d0b1:730e:60e7:1189:52163`
- **Time Window:** 5.0s [1795046183.981 - 1795046184.965]
- **Observed Value:** 62 repeated packets
- **Configured Threshold:** >25 packets / 5.0s
- **Evidence Summary:** Observed 62 packets to identical destination in 5.0s window.
- **Explanation:** Repetitive communication pattern: 2001:4860:4864:6:4000::17 -> 2405:201:402d:e14b:d0b1:730e:60e7:1189:52163 transmitted 62 packets within a 5.0s window.

#### [MEDIUM] ALT-REP-002: Repeated Communication Pattern
- **Target / Scope:** `2405:201:402d:e14b:d0b1:730e:60e7:1189 -> 2001:4860:4864:6:4000::17:3478`
- **Time Window:** 5.0s [1795046184.008 - 1795046184.979]
- **Observed Value:** 79 repeated packets
- **Configured Threshold:** >25 packets / 5.0s
- **Evidence Summary:** Observed 79 packets to identical destination in 5.0s window.
- **Explanation:** Repetitive communication pattern: 2405:201:402d:e14b:d0b1:730e:60e7:1189 -> 2001:4860:4864:6:4000::17:3478 transmitted 79 packets within a 5.0s window.

---

## 7. Active Detection Configuration

```json
{
  "high_packet_rate_threshold": 50,
  "high_packet_rate_window_sec": 1.0,
  "high_packet_rate_policy": "source",
  "port_diversity_threshold": 15,
  "port_diversity_window_sec": 10.0,
  "syn_ratio_threshold": 0.75,
  "syn_min_packets": 10,
  "volume_deviation_zscore": 2.5,
  "volume_deviation_min_intervals": 4,
  "volume_deviation_interval_sec": 2.0,
  "traffic_concentration_threshold": 0.5,
  "traffic_concentration_min_packets": 30,
  "repeated_comm_threshold": 25,
  "repeated_comm_window_sec": 5.0,
  "max_packets_safety_limit": 500000,
  "time_bucket_interval_sec": 1.0
}
```

---

## 8. Defensive Security Scope & Analytical Limitations

- **Metadata vs Payload:** PacketStats inspects packet headers and flow timing. Transport Layer Security (TLS) and application encryption prevent payload inspection; encrypted application content is neither decrypted nor inferred.
- **Flow Grouping vs State Reconstruction:** PacketStats groups packets into bidirectional flows. It does not perform full TCP stack emulation, connection state reconstruction, or retransmission tracking.
- **Explainable Indicators vs Definitive Attribution:** Anomaly rules identify traffic that departs from expected baselines or matches scanning heuristics. High volume, destination port diversity, and high SYN ratios can be caused by legitimate applications, network drops, or asymmetric routing.