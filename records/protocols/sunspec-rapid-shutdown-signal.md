---
id: proto:sunspec-rapid-shutdown-signal
type: Protocol
name: SunSpec rapid shutdown signal
aliases:
- SunSpec RSD signal
- SunSpec Rapid Shutdown
- PLC keep-alive signal
- permission to operate signal
- keep alive signal
- heartbeat signal
- SunSpec communication signal
- PLC Rapid Shutdown Signal
category: Communication
protocol_kind: transport
claims:
- claim_id: c1
  rel: subclass_of
  target: proto:power-line-communication
  note: The signal is sent as power line communication over the PV string conductors to module-level receivers.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: sec=2.11
    h: 1e0cace0bb9d
  - src: src:eq-equip-mlpe-optimizers-tigo-rss-signal-detector
    loc: sec=h2
    h: 3577f98cb205
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-proof-stpcore1-ds-en-32
    loc: tbl=1.r24
    h: 5378fdb8f286
  review: drafted
- claim_id: c2
  rel: part_of
  target: std:sunspec-rapid-shutdown
  note: Defined by the SunSpec Communication Signal for Rapid Shutdown Functional Specification.
  cite:
  - src: src:eq-equip-inverters-sma-stp-core1-us-rss-ti-en-11
    loc: sec=2
    h: 3c1b2a57cad1
  - src: src:kb-sma-sbx1xpus41-configuring-the-rapid-shutdown-function
    loc: tbl=1.r2
    h: 462e78cd6e34
  - src: src:kb-sma-stpxx-us-41-configuring-the-rapid-shutdown-function
    loc: tbl=1.r2
    h: 462e78cd6e34
  review: drafted
---
The SunSpec rapid shutdown signal is a power line keep-alive signal that a transmitter sends over the PV string conductors to module-level rapid shutdown receivers. The receivers let module energy reach the string only while they hear the signal. When it stops, they disconnect the modules so that conductor voltage inside the array falls to the NEC 690.12 limit. SMA Sunny Tripower CORE1 and other SMA US inverters have the transmitter built in and send the permission to operate signal on their DC inputs. Solis 4G-US models and the CPS RSD wirebox also support it, the CPS wirebox for use with APsmart RSD-S-PLC and RSD-D units. APsmart Transmitter-PLC units send the heartbeat to APsmart RSD devices. Switching the transmitter off triggers shutdown, and when the inverter has an integrated SunSpec-certified transmitter, no external transmitter is needed. Opening the AC disconnect, or a grid outage, cuts the signal. The inverter starts transmitting again when grid voltage comes back. SMA event 9034 means the inverter measured more than 30 VDC on an input before it started transmitting. This is often cross-talk from inverters that are already running, and SMA recommends firmware 03.12.23.R or later on CORE1 inverters. During installation, the Tigo RSS Signal Detector checks that the TS4-F receivers are getting the keep-alive signal.

<!-- review notes
- sentence 2: support check: partial - Receivers pass energy only with signal and disconnect without it, but the limit is stated as 80 V per NEC 690.12(B)(2)(2); fine, though array-voltage limit tied to this is stated only for CORE1 context; core is supported.
- sentence 3: support check: partial - CORE1 integrated transmitter on DC inputs, Solis 4G-US and CPS wirebox for APsmart are supported, but 'other SMA US inverters' and the CPS wirebox being a CPS product are not clearly stated.
-->
