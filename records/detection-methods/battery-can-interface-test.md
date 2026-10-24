---
id: method:battery-can-interface-test
type: DetectionMethod
name: Battery CAN interface functional test
aliases:
- CAN test mode
- CAN bus functional test
- Functional test of CAN interface
- CAN interface test cable
- 'success rate: 100'
- battery interface module test
- Battery CAN interface loopback test
claims:
- claim_id: c1
  rel: produces
  target: meas:can-test-success-rate-zero
  note: Events menu reports a success rate of 0 instead of 100 after the CAN test mode value is saved,
    meaning one of the tested CAN inputs on the battery interface module is defective; a service request
    is needed and the module must be replaced.
  quote: 'the Events menu shows "success rate: 0" instead of 100, one of the CAN inputs are defective'
  cite:
  - src: src:sma-kb-functional-test-of-can-interface-of-the-sunny-boy-storage
    loc: sec=h1
    h: b20d3ee6952a
  - src: src:sma-doc-sbsx-x-10-can-sg-en-10
    loc: sec=h37
    h: c71b18b1a656
  review: drafted
- claim_id: c2
  rel: produces
  target: meas:can-test-success-rate-full
  note: A success rate of 100 in the Events menu means the tested pair of CAN interfaces (BAT1/BAT2 or
    BAT3/BAT4) has no fault. Battery communication error events may still be listed because the battery
    cable is removed during the test.
  cite:
  - src: src:sma-kb-functional-test-of-can-interface-of-the-sunny-boy-storage
    loc: sec=h1
    h: b20d3ee6952a
  - src: src:sma-doc-sbsx-x-10-can-sg-en-10
    loc: sec=h35
    h: 5e6fa2ee8481
  - src: src:sma-doc-sbsx-x-10-can-sg-en-10
    loc: sec=7
    h: edeb28b371f9
  review: drafted
---
This is a built-in check of the inverter's battery CAN inputs. It is used when the inverter fails to detect connected batteries or the backup box during commissioning, to rule out a defect in the inverter's CAN interface. The test needs no connection to the battery. Instead, a test cable with CAN L, CAN H and GND wired on two terminal blocks links two battery inputs on the battery interface module. Before any work inside the inverter, isolate it from the AC and DC sources in the order the manual gives. Do this again before moving the test cable or putting the original wiring back. With the test cable in place, switch on the AC supply, log in as Installer and make sure the firmware is at least version 3.11.49.R. Then set CAN test mode under the battery parameters and save it, once for the BAT1/BAT2 pair and once for the BAT3/BAT4 pair. A success rate of 100 in the Events menu means the tested inputs work. A success rate of 0 means a CAN input is defective, and the battery interface module must be replaced through a service request. Battery communication error events may show up during the test only because the battery cable is unplugged, so they do not mean the interface is faulty. The test only rules out an inverter defect with reasonable certainty and is not a full check of the CAN bus. If the communication error remains after a passed test and re-running the installation assistant, look for the cause elsewhere, such as cable termination, cabling, cable type, grounding or software version.

<!-- review notes
- sentence 3: support check: partial - Passages require disconnecting from voltage sources in the prescribed sequence before work and again between BAT pairs and before restoring wiring, but they don't say 'AC and DC' for each repeat or a 'before moving' rule beyond the described steps.
- sentence 7: support check: partial - Passages support the limited-purpose test and that a persisting error originates elsewhere, with possible causes listed, but they don't state this as a causal check after re-running the installation assistant; mapping the listed causes to the follow-up is an inference.
-->
