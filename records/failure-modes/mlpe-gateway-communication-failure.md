---
id: fm:mlpe-gateway-communication-failure
type: FailureMode
name: MLPE gateway communication failure
aliases:
- TS4 not responding to detection
- losing communication with the Gateway
- Gateway not detected
- RF signal interference
- EM gateway not found
- IQ Gateway failure
claims:
- claim_id: c1
  rel: affects
  target: comp:mlpe-gateway
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-gateway-interface-board-gib
    loc: sec=h1
    h: 8ea1ca213649
  - src: src:sma-kb-commissioning-tigo-ts4-r-devices-using-the-gateway-interface-board-gib-kit
    loc: sec=h1
    h: 96f9eeb90000
  - src: src:enphase-enphase-power-export-limit-iq8-commercial-tech-brief
    loc: tbl=2.r1
    h: fccccaa15219
  - src: src:enphase-enphase-power-export-limit-iq8-commercial-tech-brief
    loc: tbl=2
    h: e2322ffd7706
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:rapid-shutdown-device
  note: Tigo TS4-R devices that report through the gateway
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-gateway-interface-board-gib
    loc: sec=h1
    h: 8ea1ca213649
  - src: src:sma-kb-troubleshooting-steps-for-tigo-ts4-r-rapid-shutdown-devices
    loc: sec=h1
    h: 93a1d9e35f6f
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:microinverter
  cite:
  - src: src:enphase-enphase-power-export-limit-iq8-commercial-tech-brief
    loc: tbl=2.r1
    h: fccccaa15219
  - src: src:enphase-enphase-power-export-limit-iq8-commercial-tech-brief
    loc: tbl=2
    h: e2322ffd7706
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:weak-wireless-signal
  note: The device may be too far from its gateway, or obstructions may block the RF path between the
    TS4-R and the gateway.
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-ts4-r-rapid-shutdown-devices
    loc: sec=h1
    h: 93a1d9e35f6f
  - src: src:sma-doc-246498
    loc: tbl=85.r2
    h: d81335c68816
  - src: src:sma-doc-246498
    loc: tbl=85
    h: 556b03932f5f
  review: drafted
- claim_id: c5
  rel: caused_by
  target: stressor:signal-cable-emi
  note: Unshielded signal wires run in the same conduit as the DC cables.
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-gateway-interface-board-gib
    loc: sec=h1
    h: 8ea1ca213649
  review: drafted
- claim_id: c6
  rel: caused_by
  target: fm:communication-bus-fault
  note: The termination resistor is misplaced, the RS485 wire order is reversed or cross-connected, or
    terminals are loose.
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-gateway-interface-board-gib
    loc: sec=h1
    h: 8ea1ca213649
  review: drafted
- claim_id: c7
  rel: caused_by
  target: stressor:installation-error
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-gateway-interface-board-gib
    loc: sec=h1
    h: 8ea1ca213649
  - src: src:sma-kb-troubleshooting-steps-for-tigo-ts4-r-rapid-shutdown-devices
    loc: sec=h1
    h: 93a1d9e35f6f
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: 'support check: partial - Wiring, resistor and serial-number errors are implied installation
    faults, but the passages never label them ''installation error''.'
- claim_id: c8
  rel: caused_by
  target: fm:monitoring-network-fault
  note: The gateway is not connected to the local network.
  cite:
  - src: src:sma-doc-246498
    loc: tbl=85
    h: 556b03932f5f
  - src: src:sma-doc-246498
    loc: tbl=85.r4
    h: 184f99b9bd2e
  - src: src:sma-doc-246498
    loc: sec=h480
    h: 4ed1b099ebc5
  review: drafted
  review_note: 'support check: partial - The Home Manager passages say the gateway is not connected to
    the local network, but they concern an EM gateway, not the MLPE gateway.'
- claim_id: c9
  rel: caused_by
  target: stressor:power-supply-interruption
  note: The gateway is unplugged, or there is no gateway supply voltage because no AC on the inverter
    has put the devices into rapid shutdown.
  cite:
  - src: src:sma-doc-246498
    loc: sec=h482
    h: e66c10d81a53
  - src: src:sma-kb-troubleshooting-steps-for-tigo-gateway-interface-board-gib
    loc: sec=h1
    h: 8ea1ca213649
  review: drafted
- claim_id: c10
  rel: presents_as
  target: symptom:communication-loss
  cite:
  - src: src:enphase-enphase-power-export-limit-iq8-commercial-tech-brief
    loc: tbl=2.r1
    h: fccccaa15219
  - src: src:sma-kb-troubleshooting-steps-for-tigo-gateway-interface-board-gib
    loc: sec=h1
    h: 8ea1ca213649
  - src: src:sma-doc-246498
    loc: tbl=85
    h: 556b03932f5f
  - src: src:sma-doc-246498
    loc: tbl=85.r5
    h: fdfe737743e0
  review: drafted
- claim_id: c11
  rel: presents_as
  target: symptom:mlpe-detection-failure
  note: TS4-R devices do not respond to TS4 detection during commissioning.
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-gateway-interface-board-gib
    loc: sec=h1
    h: 8ea1ca213649
  - src: src:sma-kb-troubleshooting-steps-for-tigo-ts4-r-rapid-shutdown-devices
    loc: sec=h1
    h: 93a1d9e35f6f
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c12
  rel: presents_as
  target: symptom:control-fallback-operation
  note: Microinverters cut their output current back to a static safe limit once communication has been
    lost longer than the configured time limit.
  cite:
  - src: src:enphase-enphase-power-export-limit-iq8-commercial-tech-brief
    loc: tbl=2.r1
    h: fccccaa15219
  - src: src:enphase-enphase-power-export-limit-iq8-commercial-tech-brief
    loc: tbl=2
    h: e2322ffd7706
  - src: src:enphase-enphase-power-export-limit-iq8-commercial-tech-brief
    loc: tbl=2.r3
    h: 9af7a5e8c7a7
  review: drafted
- claim_id: c13
  rel: presents_as
  target: symptom:interface-board-red-led
  note: A red LED on the GIB means the termination resistor is installed wrongly or the signal wiring
    polarity is reversed.
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-gateway-interface-board-gib
    loc: sec=h1
    h: 8ea1ca213649
  review: drafted
- claim_id: c14
  rel: detected_by
  target: method:communication-test
  note: The installation assistant's gateway test returns OK or Warning.
  cite:
  - src: src:sma-kb-commissioning-tigo-ts4-r-devices-using-the-gateway-interface-board-gib-kit
    loc: sec=h1
    h: 96f9eeb90000
  - src: src:sma-kb-troubleshooting-steps-for-tigo-gateway-interface-board-gib
    loc: sec=h1
    h: 8ea1ca213649
  review: drafted
- claim_id: c15
  rel: detected_by
  target: method:communication-bus-voltage-test
  note: Measure the supply voltage at the GIB terminal block and at the gateway.
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-gateway-interface-board-gib
    loc: sec=h1
    h: 8ea1ca213649
  review: drafted
- claim_id: c16
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-ts4-r-rapid-shutdown-devices
    loc: sec=h1
    h: 93a1d9e35f6f
  review: drafted
- claim_id: c17
  rel: detected_by
  target: method:known-good-swap-test
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-ts4-r-rapid-shutdown-devices
    loc: sec=h1
    h: 93a1d9e35f6f
  review: drafted
- claim_id: c18
  rel: mitigated_by
  target: mit:communication-bus-termination
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-gateway-interface-board-gib
    loc: sec=h1
    h: 8ea1ca213649
  review: drafted
- claim_id: c19
  rel: mitigated_by
  target: mit:communication-cable-check
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-gateway-interface-board-gib
    loc: sec=h1
    h: 8ea1ca213649
  review: drafted
- claim_id: c20
  rel: mitigated_by
  target: mit:proper-cable-routing
  note: Use shielded, 600 Vdc rated signal cable when it shares conduit with DC cables.
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-gateway-interface-board-gib
    loc: sec=h1
    h: 8ea1ca213649
  review: drafted
- claim_id: c21
  rel: mitigated_by
  target: mit:wireless-range-extension
  note: Add gateways near the suspect TS4-R locations.
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-ts4-r-rapid-shutdown-devices
    loc: sec=h1
    h: 93a1d9e35f6f
  review: drafted
- claim_id: c22
  rel: mitigated_by
  target: mit:gateway-restart
  cite:
  - src: src:sma-doc-246498
    loc: tbl=85
    h: 556b03932f5f
  - src: src:sma-doc-246498
    loc: tbl=85.r5
    h: fdfe737743e0
  review: drafted
- claim_id: c23
  rel: mitigated_by
  target: mit:complete-device-configuration
  note: Configure the device for its gateway, and check that the registered serial numbers match the installed
    devices.
  cite:
  - src: src:sma-doc-246498
    loc: tbl=85
    h: 556b03932f5f
  - src: src:sma-doc-246498
    loc: tbl=85.r3
    h: 369666c4941a
  - src: src:sma-kb-troubleshooting-steps-for-tigo-ts4-r-rapid-shutdown-devices
    loc: sec=h1
    h: 93a1d9e35f6f
  review: drafted
- claim_id: c24
  rel: mitigated_by
  target: mit:network-connection-check
  cite:
  - src: src:sma-doc-246498
    loc: tbl=85.r4
    h: 184f99b9bd2e
  review: drafted
- claim_id: c25
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-gateway-interface-board-gib
    loc: sec=h1
    h: 8ea1ca213649
  - src: src:enphase-enphase-power-export-limit-iq8-commercial-tech-brief
    loc: tbl=2.r3
    h: 9af7a5e8c7a7
  - src: src:sma-kb-troubleshooting-steps-for-tigo-ts4-r-rapid-shutdown-devices
    loc: sec=h1
    h: 93a1d9e35f6f
  review: drafted
---
In this failure, module-level devices such as rapid shutdown units or microinverters stop talking to their communication gateway, or never connect to it at commissioning. It shows up as devices that do not respond to detection or that drop communication, and some microinverter systems fall back to a reduced safe output limit when the link is lost. Common causes are devices out of radio range or behind obstructions, wrong termination resistor placement, reversed or loose RS485 wiring, and signal cables run unshielded beside DC cables. Run the gateway test, look for a red LED on the interface board, and measure the gateway supply voltage at both the interface board and the gateway. If short test wiring makes the gateway work, replace the long run with shielded, color-coded cable in the correct wire order. Check the line of sight to each device, add gateways where the signal is weak, and confirm the registered serial numbers match the installed devices. Also check that the gateway is powered and connected to the network, restart the gateway and device, and contact the manufacturer if the problem persists.
