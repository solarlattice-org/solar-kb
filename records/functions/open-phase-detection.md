---
id: func:open-phase-detection
type: Function
name: Open-phase detection
aliases:
- phase loss detection
- open phase conditions
- Phase failure detection
- OPEN_PH_DETECT
- High-Voltage Open-Phase Detection
- loss-of-phase
category: Protection
function_kind: protection
claims:
- claim_id: c1
  rel: part_of
  target: prod:yaskawa-solectria-xgi-1500-1mw
  note: Raises warning event code 4. It cannot see a high-side open phase behind a floating delta transformer,
    so the user must supply an external three-phase relay.
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=20.r4
    h: 927ff11556c5
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h44
    h: 2ccd9f29467c
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h49
    h: ea8018c6e7f5
  review: drafted
---
Open-phase detection, also called phase failure detection, finds the loss of one or more line conductors of the utility grid. When it detects one, the inverter opens its grid relays. To troubleshoot this warning, check the AC voltage with a CAT III multimeter. If a phase is missing, check all AC fuses and breakers and inspect the AC conductors for damage. If no phase loss is found, contact technical support. If the transformer winding facing the inverter is a floating delta, losing a phase on the high-voltage side can leave a phantom voltage on that phase at the inverter terminals. In that case the XGI 1500-1MW cannot detect the open phase. For that setup, the user must provide a separate three-phase relay or other means that detects loss of phase on the high-voltage side and opens all three phases. Correct protective response to a loss-of-phase event is a required safety function, and it is routinely checked during system acceptance testing.
