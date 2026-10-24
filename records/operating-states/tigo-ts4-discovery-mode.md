---
id: state:tigo-ts4-discovery-mode
type: OperatingState
name: TS4 discovery mode
aliases:
- discovery mode
- TS4 detection
category: MLPE
make: tigo
product: prod:tigo-ts4
claims:
- claim_id: c1
  rel: part_of
  target: prod:tigo-ts4
  note: TS4 detection is the commissioning step that finds TS4-R devices through the SMA Gateway Interface
    Board and the rooftop Gateways.
  cite:
  - src: src:sma-kb-commissioning-tigo-ts4-r-devices-using-the-gateway-interface-board-gib-kit
    loc: sec=h1
    h: 96f9eeb90000
  review: drafted
  review_note: 'support check: partial - Passage describes TS4 detection finding TS4-R devices via the
    GIB and Gateways, but nothing about ''discovery mode'' or it being part of the Tigo TS4 platform (prod:tigo-ts4).'
---
Discovery mode, which SMA calls TS4 detection, is the commissioning step in which the SMA inverter uses the Gateway Interface Board and the rooftop Gateways to search for the TS4-R devices installed on the array. You start it by clicking Find and Save in the inverter's Installation Assistant. Run the gateway test first. If the Gateways are not detected within 10-15 minutes, go ahead with TS4 detection anyway. On average, detection takes 10 to 60 minutes. The time depends on how many TS4-R devices are installed and how strong the signal is between the Gateways and each device. While detection is running, the inverter shows Commissioning Status Active, and the green and amber LEDs on the Gateway Interface Board flash alternately. This is normal and needs no action. When detection is finished, Commissioning Status changes to OK and green checkmarks appear. You can then confirm that every TS4-R device is listed and reporting under Instantaneous Values, in the Modular Technology section. The first time devices are detected, they may drop offline for a short time while they update their firmware. This takes about 5-15 minutes and is expected. Once the devices are detected and communicating, check that Rapid Shutdown Mode is set to TS4 Shutdown. That mode does not cover TS4-R-F devices, which need SunSpec Shutdown instead. If devices still do not communicate after detection, check the registered serial numbers against the rooftop map. Make sure every device has a clear line of sight to a Gateway within 25 to 30 ft and that cable connections are secure. Then run detection again.

<!-- review notes
- sentence 1: support check: partial - TS4 detection via Find and Save in the Installation Assistant is stated, but the 'discovery mode' naming equivalence is not in the passage.
- sentence 4: support check: partial - Active status and alternating green/amber GIB LEDs are stated, but that this is normal and needs no action is not explicitly stated.
-->
