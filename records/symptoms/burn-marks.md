---
id: symptom:burn-marks
type: Symptom
name: Burn marks
claims:
- claim_id: c1
  rel: observed_as
  target: meas:visible-burn-marks
  note: Burnt, blackened areas you can see with the naked eye. The encapsulant may bubble or melt, the
    glass may break, or the backsheet may have a hole. Marks on the backsheet may not show from the front.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=31.r1
    h: cb32c9c2f225
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.4
    h: ca1c4ecfbfd5
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=31.r2
    h: cd9064922320
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:ir-hotspot
  note: IR imaging in illuminated or partially shaded conditions shows whether the burnt area is still
    heating or whether current flow there has stopped. A burn mark may not appear in IR if heating has
    stopped.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.4
    h: ca1c4ecfbfd5
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=31.r1
    h: cb32c9c2f225
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=31.r2
    h: cd9064922320
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
---
Burn marks are burnt, blackened areas on a module. They can come with bubbled or melted encapsulant, broken glass or a hole in the backsheet. They are found on the backsheet along cell edges or busbars, along metallic interconnections and ribbons, and above or inside the junction box. Most burn marks can be identified by visual inspection, but marks on the backsheet may not show from the front. If the back of the module cannot be reached, use an IR camera. An IR image taken under illumination or partial shading shows whether the area is still heating or whether current has stopped flowing in that part of the circuit. An area that is no longer heating may not show up in IR. Marks along cell edges in shaded sub-modules point to open-circuited bypass diodes, because reverse current is then driven through cell shunts. Check the diodes of the affected sub-module first, for example with an IV curve under partial shading. Marks along ribbons or solder joints point to solder bond or interconnection failure, where rising resistance heats the joint. Burning together with broken glass can mean cell interconnection failure at an advanced stage. Marks at the junction box or on its housing suggest junction box failure or failed bypass diodes in the box. Other possible causes are cracked cells or shunting defects that force cells into reverse bias. Treat burn marks as a safety risk because arcing and fire can follow. Replacing the module is advised when burn marks are visible.

<!-- review notes
- sentence 5: support check: partial - Cell-edge marks with open-circuit bypass diodes in shaded modules and reverse current through shunts are stated, and IV under partial shading was used to diagnose, but the 'check first' recommendation is not explicitly stated.
- sentence 7: support check: partial - Junction box failure/bypass diode failure causing burn marks near/at the box and cracked cells/shunting causing reverse-bias burn marks are stated, but the diagnostic inference from mark location at the junction box to those causes is only loosely supported.
- sentence 8: support check: partial - Arcing and fire risk are stated and replacement is advised when burn marks are visible, but the latter is in the interconnection-failure context and the explicit 'treat as safety risk' advice is not stated for burn marks generally.
-->
