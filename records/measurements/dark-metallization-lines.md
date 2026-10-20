---
id: meas:dark-metallization-lines
type: Measurement
name: Dark metallization discoloration
aliases:
- dark discolouration
claims:
- claim_id: c1
  attr: time_to_onset
  value:
    min: 3
    unit: unit:MO
  conditions: Snail track discoloration of front silver metallization, counted from module installation;
    appears faster in summer and hot climates
  note: Lower end of the reported range; upper end is 1 year.
  quote: The discolouring typically occurs 3 month to 1 year after installation of the PV modules.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.3
    h: 43e35c4c6150
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h7
    h: 8b69da4daaac
  review: drafted
- claim_id: c2
  attr: time_to_onset
  value:
    max: 1
    unit: unit:YR
  conditions: Snail track discoloration of front silver metallization, counted from module installation
  note: Upper end of the reported range; lower end is 3 months.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.3
    h: 43e35c4c6150
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h7
    h: 8b69da4daaac
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
---
This signature is a grey to black discoloration of the silver front-side metallization on screen-printed cells, and you can see it with the naked eye through the front glass. It runs along cell edges and along cell cracks that are normally invisible, which gives the snail track look. Inspection forms record whether fingers, busbars, ribbons and string interconnects look like new, lightly discolored or darkly discolored, and estimate how much of the area is affected. Do not confuse it with photobleaching of browned EVA along cracks, which takes several years to appear. The discoloration itself is reported not to cause a measurable power loss, but the cracks it reveals can reduce module power. Modules with snail tracks tend to show high leakage current in wet leakage testing. Light yellow to dark discoloration of electrical parts often accompanies metallization corrosion, which can lead to cell interconnection failure.
