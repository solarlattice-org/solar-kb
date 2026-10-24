---
id: tool:sma-sunny-data-control
type: Tool
name: Sunny Data Control
aliases:
- Sunny Data Control 4.0
- Sunny Data Control 3.93
category: Software
tool_kind: software
claims:
- claim_id: c1
  rel: uses_protocol
  target: proto:rs485
  note: A computer running Sunny Data Control can configure PV inverters that communicate over RS485.
    Inverters without an RS485 Piggy-Back or data module also need a USB service cable.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h458
    h: 1f12f5817469
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
Sunny Data Control is SMA software that runs on a computer and is used to set up and read data from SMA inverters. It can configure PV inverters that use RS485, and it is listed with the Sunny WebBox and Sunny Boy Control as tools that can do this job. If an inverter has no RS485 Piggy-Back or RS485 data module, you also need a service cable (the USB Service Interface) to transfer data. To enter an SMA Grid Guard code, log in as installer under Tools > Security level. Then open the Parameters tab, pick the inverter, type your personal code into the Inst.-Code parameter and click Set. If Sunny Explorer shows an inverter with integrated Bluetooth as an unknown device because it has old software, you can use Sunny Data Control to read out that inverter's data. The other fix is to update the inverter software package. SMA says Sunny Data Control 4.0 is out of date and no longer meets current requirements. For inverters with the latest firmware that use Bluetooth, SMA recommends the free Sunny Explorer software, including for resetting inverter errors.

<!-- review notes
- sentence 1: support check: partial - Passages show it's software on a computer used to configure inverters and read out inverter data, but 'SMA software' is implied only via SMA download and 'set up' is loosely supported.
-->
