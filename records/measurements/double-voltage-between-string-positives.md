---
id: meas:double-voltage-between-string-positives
type: Measurement
name: Double voltage between string positives
---
This signature comes from a combiner box test. It is done before the string fuses or connectors are inserted for the first time. All negative fuses are inserted so the strings share a common negative bus, and the positive fuses are left out. First confirm that the open-circuit voltage of one string is as expected. Then keep one meter lead on that string's positive pole and move the other lead across the positive poles of the other strings. Correctly wired strings read close to zero between their positive poles because they share the same negative reference. If a string is connected in reverse polarity, the reading between positives is about twice the system voltage. This is much easier to spot than the small minus sign on a digital multimeter. Use a voltmeter rated for at least twice the maximum system voltage so it can safely show the doubled reading. The failure behind this signature is a string wired with reversed polarity. Inverters may also raise a reverse-connection alarm for it. Do the polarity check before closing switches or inserting string protection devices. If a reversed string is found on a system that was already connected, check the modules and bypass diodes for damage.

<!-- review notes
- sentence 5: support check: partial - Meter range at least twice max system voltage is stated, but the reason (to safely show the doubled reading) is implied, not stated.
-->
