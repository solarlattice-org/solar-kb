---
id: state:sma-mpp-peak
type: OperatingState
name: MPP-Peak
aliases:
- peak load operation
category: Inverters
make: sma
claims:
- claim_id: c1
  rel: subclass_of
  target: state:mpp-operation
  note: SMA groups MPP-Peak with its MPP status messages (MPP, MPP-Search, MPP-Tracking). It shows when
    feed-in power is above the inverter's nominal power.
  cite:
  - src: src:sma-kb-inverter-status-messages-mpp-mpp-peak-mpp-such-and-mpp-tracking
    loc: sec=h1
    h: 375082c6d044
  review: drafted
---
MPP-Peak is an SMA inverter status message. It means the inverter is feeding in more power than its nominal power, which SMA calls peak load operation. It can appear when solar radiation is very strong and the modules are cold, or when the PV generator is oversized for the inverter. How often you see this message depends on the system design. As an example, SMA says the SB2500 shows MPP-Peak at about 2150 watts. MPP-Peak is only a display message. It does not cost any yield and does not damage the inverter, even if it appears often. No corrective action is needed. Under normal irradiation the display shows the standard MPP message instead.
