---
id: method:protective-function-field-verification
type: DetectionMethod
name: Protective function field verification
aliases:
- enter service delay verification
- reconnection delay test
- loss of phase test
- LOP test
- trip test
- LOP testing
- loss of phase tests
- field verification of open phase
claims:
- claim_id: c1
  rel: produces
  target: meas:zero-ac-output
  note: During an open phase test, opening the tested phase should make the inverters stop producing power;
    IQ8 Commercial units watch all three phases and react to voltage or phase imbalance at each microinverter.
  cite:
  - src: src:enphase-enphase-verifying-inverter-protective-functions-iq8-commercial
    loc: sec=6.2
    h: 340b96b35ceb
  review: drafted
---
This method checks in the field that a grid-interactive inverter's protective functions work, mainly the enter service (reconnection) delay and the response to loss of a phase. Inverter protective functions are tested in the factory, but many utilities also want the reconnection delay timer checked in the field before the PV system may export power. You can check the enter service delay with a clamp-on ammeter, by watching the meter, or with more accurate power measurement equipment. Which you pick depends on your confidence in the equipment, the test gear you have, and whether there is sunlight. In the open phase test, one phase is opened and the inverters should stop producing power, because they monitor all three phases and trip on voltage or phase imbalance. An open phase can come from a faulty connection, a blown fuse or a damaged wire anywhere between the point of common coupling and the point of connection. Take the loss of phase measurement on the PV side of the PV disconnect at the point of connection, and isolate all other loads from the array first. Loads between the PV system and the open point can change the open phase voltage and mislead the test. The inverters' output filters load the line capacitively, so some stray voltage adaptors may not null the open phase voltage. A correctly sized shunt resistor shows whether power potential is present, but it does not remove it. Follow all standard field safety precautions and use measurement equipment suited to the test.

<!-- review notes
- sentence 1: support check: partial - Passages cover enter service delay verification and open phase verification, but "mainly" and framing as a single method are not stated, and the document title only partly covers it.
- sentence 4: support check: partial - Stopping power due to monitoring three phases and detecting voltage/phase imbalance is stated, but "trip" and the use of such a trip as the mechanism are only loosely implied.
- sentence 5: support check: partial - Faulty connection, blown fuse, damaged wire and location between PCC and POC are stated, though the passage says POC-PCC, and "can come from" is slightly reordered; essentially supported but the passage describes causes as 'typically'.
-->
