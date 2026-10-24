---
id: hazard:disconnecting-under-load
type: Hazard
name: Arc from disconnecting under load
aliases:
- opening connectors under load
- do not disconnect under load
- pulling DC connectors
- disconnecting under load
- switching under load
- opening a fuse under load
category: Electrical
claims:
- claim_id: c1
  rel: controlled_by
  target: mit:low-current-dc-disconnection
  note: Make sure no current is flowing before opening a fuse or disconnecting. Checking that voltage
    is absent is not enough on its own; the absence of current must also be verified.
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  - src: src:yaskawa-solectria-dsp-yellowstone
    loc: sec=h24
    h: adf8a72746bc
  - src: src:yaskawa-solectria-power-supply-board
    loc: sec=h24
    h: adf8a72746bc
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: controlled_by
  target: mit:safety-isolation
  note: Disconnect the supply, prevent reconnection and test for absence of voltage. Open the PV breakers
    and make the equipment inoperable before servicing.
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  - src: src:generac-generac-pwrmicro-installation-manual-a0008718926
    loc: sec=h23
    h: 8c250461e617
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c3
  rel: controlled_by
  target: tool:lockout-tagout-kit
  note: Padlocks and tags on the switched-off isolators prevent reconnection.
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: drafted
  review_note: 'support check: partial - The video describes padlocks and tags on switched-off switches
    to prevent reconnection, but it does not tie lockout/tagout to controlling arcs from disconnecting
    under load.'
- claim_id: c4
  rel: controlled_by
  target: tool:arc-rated-clothing
  scope:
    products:
    - prod:sma-sunny-central-storage
  note: An arc flash protection jacket and flame-resistant, non-synthetic clothing are recommended for
    work on Sunny Central and Sunny Central Storage inverters.
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: drafted
  review_note: 'support check: partial - The video says an arc flash jacket and flame-resistant non-synthetic
    clothing are needed (called mandatory). The statement calls them recommended and scopes them to Sunny
    Central and Storage, which is roughly consistent.'
- claim_id: c5
  rel: controlled_by
  target: tool:face-shield
  scope:
    products:
    - prod:sma-sunny-central-storage
  note: A helmet with a built-in visor gives full face protection against DC-side arc flash. Goggles alone
    are not enough.
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: drafted
---
Opening or switching a circuit while current is flowing can strike an arc flash. The arc turns air into hot plasma and adds a burn risk, and it is especially a concern on the DC side. The classic case is pulling a DC fuse under load. Opening a fuse under load can cause property damage, injury or death, so check that no current is flowing, not just that voltage is absent. Manufacturers advise against unplugging AC or DC connectors under load. The NEC requires PV connectors to be either rated for interrupting current or to need a tool to open and be marked Do Not Disconnect Under Load. Screw-type fuse elements have no load-disconnection properties, and contact erosion can destroy or impair them if they are opened under load. Use a circuit breaker to disconnect an inverter from the grid under load. On a beeping Sunny Tripower TL-10, the electronic string fuse is short-circuiting the PV array. Do not pull the DC connectors or the ESS at that point; wait until the beeping stops after dark. To control the hazard, follow the safety rules: disconnect, lock out and tag out, test for absence of voltage, and open the PV breakers before servicing. Wear an arc flash jacket, flame-resistant clothing and a helmet with a full face visor when working where arcs can occur.
