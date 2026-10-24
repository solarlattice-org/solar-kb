---
id: param:sma-reconnect-voltage-max
type: Parameter
name: SMA reconnection voltage, maximum
make: sma
product: prod:sma-stp-core1-us
vendor_id: GridGuard.Cntry.VolCtl.ReconMax
display_name: Reconnection voltage max
menu_path: Grid monitoring > Voltage
access_level: role:installer
claims:
  - claim_id: c1
    rel: instance_of
    target: param:ov2-trip-voltage
    cite: [{src: "src:b0-vendor-manual", loc: "sec=1", h: "a1b2c3d4e5f6"}]
    review: drafted
  - claim_id: c2
    rel: configures
    target: func:rapid-shutdown
    cite: [{src: "src:b0-vendor-manual", loc: "sec=1", h: "a1b2c3d4e5f6"}]
    review: drafted
---

Fixture record for schema 0.5.0 (parameters).
