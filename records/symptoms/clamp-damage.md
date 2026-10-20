---
id: symptom:clamp-damage
type: Symptom
name: Clamp damage on module
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ir-hotspot
  note: Applies when clamp damage has broken the module glass; the review states glass breakage causes
    hot spots that overheat the module.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=4.3.1
    h: 1fd87ffa8010
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
---
Clamp damage means the module or its frame has been damaged by a clamp, or the module is not held firmly enough. It is linked to bad module clamping. Look for it with a visual inspection of the clamps and the module edges around them. Common causes are clamp shapes that do not suit the module (for example sharp edges), clamps that are too short or too narrow, clamps placed where the manufacturer's manual does not allow, and screws tightened too hard. Using a clamp that does not match the module type is another known cause. Frameless modules, and glass/glass modules in particular, are more likely to suffer glass breakage at the clamps. Over time, poor clamping can bend the frame, break the glass or crack cells. A loose clamp can also let modules come off the structure in high wind, one after another, because neighbouring modules share the same clamps. Broken glass is a safety risk: insulation can no longer be relied on, especially when the module is wet, and hot spots can appear. Use insulation testing, EL imaging and the operating data to judge how much electrical damage has been done. Replace modules with broken glass if there is a safety or insulation risk, and check whether clamp stress was the root cause.
