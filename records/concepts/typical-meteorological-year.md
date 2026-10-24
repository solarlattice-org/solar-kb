---
id: concept:typical-meteorological-year
type: Concept
name: Typical meteorological year
aliases:
- TMY
- TMY3
- 8760 data
- '8760'
- 8760 file
category: Irradiance
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: tool:pvsyst
  note: TMY or 8760 data sets are used as the weather input to PVsyst when predicting performance during
    design.
  cite:
  - src: src:alsoenergy-kb-using-8760-data-with-the-pv-model
    loc: sec=front
    h: ed201c211c7c
  - src: src:test-cx-manuals-sunspec-commissioning-for-pv-performance
    loc: sec=h20
    h: a40e86dc651b
  - src: src:enphase-enphase-iq8-pairing-with-imp-over-12a-modules
    loc: sec=h4
    h: 134a0a82052c
  review: drafted
- claim_id: c2
  rel: related_to
  target: tool:nrel-sam
  note: Performance models such as SAM take weather input in a format such as TMY.
  cite:
  - src: src:test-cx-manuals-sunspec-commissioning-for-pv-performance
    loc: sec=h20
    h: a40e86dc651b
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:expected-energy-model
  note: 8760 files carry expected hourly energy for a full year. They are used to align a monitoring PV
    model with the original design.
  cite:
  - src: src:alsoenergy-kb-using-8760-data-with-the-pv-model
    loc: sec=front
    h: ed201c211c7c
  - src: src:test-cx-manuals-sunspec-commissioning-for-pv-performance
    loc: sec=h20
    h: a40e86dc651b
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:energy-yield-assessment
  note: 8760 values come from modelling software before a project is built and estimate hourly generation
    for the first year.
  cite:
  - src: src:alsoenergy-kb-using-8760-data-with-the-pv-model
    loc: sec=front
    h: ed201c211c7c
  - src: src:alsoenergy-kb-hourly-report-creation
    loc: sec=front
    h: 62ba5b7d5da9
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c5
  rel: related_to
  target: tool:alsoenergy-powertrack
  note: PowerTrack can import a TMY (8760) file as reference data and work out a derate value for each
    inverter.
  cite:
  - src: src:alsoenergy-kb-using-8760-data-with-the-pv-model
    loc: sec=front
    h: ed201c211c7c
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:plane-of-array-irradiance
  note: A TMY file imported into PowerTrack must contain POA irradiance.
  cite:
  - src: src:alsoenergy-kb-using-8760-data-with-the-pv-model
    loc: sec=front
    h: ed201c211c7c
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:global-horizontal-irradiance
  note: An 8760 import can include a global horizontal irradiance column (globhor).
  cite:
  - src: src:alsoenergy-kb-using-8760-data-with-the-pv-model
    loc: sec=front
    h: ed201c211c7c
  review: drafted
- claim_id: c8
  rel: related_to
  target: concept:national-solar-radiation-database
  note: TMY data sets are derived from the NSRDB. NSRDB TMY3 is used as a weather file.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nrel-best-practices-solar
    loc: sec=4.1.1
    h: 9129b8f4a6f2
  - src: src:enphase-enphase-iq8-pairing-with-imp-over-12a-modules
    loc: sec=h4
    h: 134a0a82052c
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - u25 says TMY data sets derive from the NSRDB and u30 uses NSRDB
    TMY3 weather file, but u25 refers specifically to the 1961-1990 NSRDB; the general claim is roughly
    supported.'
---
A typical meteorological year (TMY) is a data set of representative hourly weather for one typical year at a given location. The name 8760 comes from the number of hours in a year, and an 8760 file usually holds both the hourly TMY weather and the expected energy output for a full year. Designers feed TMY data into modelling tools such as PVsyst or SAM to predict site performance before construction. A typical TMY-based file holds plane-of-array irradiance, ambient temperature, wind speed and the expected power or energy under ideal conditions. Module temperature and global horizontal irradiance columns may also be included. Monitoring platforms can import the 8760 file to calibrate their PV model against the original design, for example by working out an inverter derate. TMY3 is a version drawn from the nearest TMY3 station, and TMY data sets in the US are derived from the National Solar Radiation Data Base. For long-term performance checks, the weather actually measured on site can be converted into the TMY input format and run through the original model to get expected energy.
