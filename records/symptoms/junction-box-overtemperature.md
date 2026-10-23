---
id: symptom:junction-box-overtemperature
type: Symptom
name: Junction box overtemperature
aliases:
- Junction Box Over-Temperature Fault
- Fault6000
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ir-hot-junction-box
  note: On modules, a junction box that runs hotter than its neighbours can point to resistive heating
    from a loose connection or a cold solder joint. In one failure mode, this heating shows only under
    shading or during a bypass diode test.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
First, watch the inverter for about five minutes to see whether the alarm clears by itself. If it keeps coming back, contact the manufacturer's after-sales service. The same register uses separate codes for a junction box temperature sensor fault and for an abnormal junction box temperature, so check which code is actually active before assuming real overheating. On PV modules, bad contacts, corrosion or unreliable soldered joints raise the resistance inside the junction box and make it heat up, which points to junction box failure. An infrared camera can show a junction box running hotter than the others, which may indicate a loose connection or a cold solder joint. Some joint faults only heat up under shading or during a bypass diode test. A failed bypass diode can also overheat the box until it deforms or burns, and internal arcing can leave burn marks around it. Inspect suspect boxes by eye and with IR, check how the bypass diodes behave, and add IV tracing and insulation checks if you find damage. Replace the module rather than repairing the box, because repairs can easily lead to new fires.

<!-- review notes
- sentence 5: support check: partial - u3 supports bypass diode failures deforming or burning the box, but burn marks around the box from internal arcing is not stated (burn marks are tied to encapsulant degradation, arcing separately).
-->
