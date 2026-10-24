---
id: prod:sma-sunny-sensorbox
type: Product
name: Sunny SensorBox
aliases:
- SensorBox
category: Sensors
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:sma-doc-279088
    loc: sec=h21
    h: 4b99ac37479c
  review: drafted
- claim_id: c2
  rel: compatible_with
  target: prod:sma-sunny-webbox
  note: The SensorBox connects to the Sunny WebBox, which passes its environmental data on for plant monitoring
    and the performance ratio calculation in Sunny Portal.
  cite:
  - src: src:sma-doc-swebbox-ba-en-36
    loc: tbl=7.r1
    h: cd089d8409d4
  - src: src:sma-doc-swebbox-ba-en-36
    loc: tbl=7
    h: 94542036bff8
  - src: src:sma-doc-249641
    loc: sec=h13
    h: 12966e1cf0aa
  - src: src:sma-doc-swebbox-ba-en-36
    loc: sec=2
    h: 326d4f4a98f0
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: prod:sma-sunny-home-manager
  note: When a SensorBox is installed in a Sunny Home Manager system, its measured values appear under
    the Sensors menu and are used to show the performance ratio.
  cite:
  - src: src:sma-doc-246498
    loc: sec=6.7
    h: 3f402b1acb76
  - src: src:sma-doc-246498
    loc: tbl=54.r3
    h: 50b2dfb04be4
  - src: src:sma-doc-246498
    loc: sec=h119
    h: 8c7daf2807e8
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:sma-net
  note: Appears in the Sunny WebBox list of devices that use the SMA-NET protocol.
  cite:
  - src: src:sma-doc-swebbox-ba-en-36
    loc: tbl=25.r1
    h: 493c54ad9641
  - src: src:sma-doc-swebbox-ba-en-36
    loc: tbl=25
    h: 628b7b7a4c10
  review: drafted
---
The Sunny SensorBox is an SMA accessory that records the environmental data needed to monitor how well a PV plant is performing. It has a built-in irradiation sensor and an external module temperature sensor. An ambient temperature sensor and an anemometer can also be connected to it. It works with the Sunny WebBox, which collects its data. In the WebBox settings it is listed as a device that communicates over SMA-NET. For Sunny Portal to calculate the performance ratio automatically, the SensorBox must be connected to a Sunny WebBox that sends the data, its own irradiation sensors must be used, and it must measure at least 60 W/m2 of irradiation per hour at the site. In a Sunny Home Manager system, the SensorBox provides irradiation values from the module location. This enables the Sensors menu and the performance ratio display. If the SensorBox is shaded, dirty or not aligned with the modules, the calculated performance ratio will be wrong and can even go above 100 percent. A difference in cell technology between the sensor and the modules also affects the result.

<!-- review notes
- sentence 3: support check: partial - WebBox collecting SensorBox data and SMA-NET listing are supported, but 'in the WebBox settings' is not stated; the list is only of protocol/device mapping.
- sentence 6: support check: partial - Shading/soiling, orientation, cell technology differences and >100% are supported, but the passages do not say shading or soiling cause values above 100% (only misalignment is tied to that), and 'will be wrong' is stronger than 'can influence'.
-->
