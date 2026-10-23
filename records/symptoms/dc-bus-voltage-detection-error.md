---
id: symptom:dc-bus-voltage-detection-error
type: Symptom
name: DC bus voltage detection error
aliases:
- UN-BUS02
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Solis hybrid inverters report this condition as message UN-BUS02 (1023 DATA:0002), described as
    abnormal detection of DC bus voltage. The listed first step is to restart the system and check whether
    the fault continues.
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r11
    h: 1fa33bd1dff9
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r11
    h: 1fa33bd1dff9
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=27.r11
    h: 1fa33bd1dff9
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r11
    h: cc0916296066
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
This symptom is an inverter message saying that the DC bus voltage is being detected abnormally. It is not a confirmed high or low bus voltage. On Solis hybrid inverters it shows on the display or event log as UN-BUS02 with data code 1023 DATA:0002. The first step the manufacturer gives is to restart the system and see whether the fault comes back. Keep it separate from the bus overvoltage alarm (OV-BUS) and the bus undervoltage alarm (UN-BUS). Those report a real high or low voltage on the internal bus. Some inverters let you read the positive, negative and total bus voltages over Modbus. Those readings help you check whether the bus reading makes sense.

<!-- review notes
- sentence 1: support check: partial - Passages say 'abnormal detection of DC bus voltage' but do not state that it is not a confirmed high or low voltage; that is an inference.
- sentence 2: support check: partial - Message name and code are stated, but the passages do not say it appears on display or event log specifically, nor mention Solis hybrid explicitly.
- sentence 5: support check: partial - The register table lists positive, negative and total bus voltage as readable, but the passages do not say those readings help check whether the bus reading makes sense, nor name Modbus or 'some inverters'.
- sentence 1: review: partial - The passages state 'Abnormal detection of DC bus voltage', but the claim that this is not a confirmed high or low bus voltage is an inference the passages do not state.
-->
