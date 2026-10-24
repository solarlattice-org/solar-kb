---
id: concept:permit-plan-set
type: Concept
name: Permit plan set
aliases:
- plan set
- permit package
- permit set
category: Design
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:authority-having-jurisdiction
  note: The AHJ reviews and approves the drawings and inspects the installation to confirm it matches
    the permit set.
  cite:
  - src: src:trn-training-very-basics-of-pv-lesson-1
    loc: sec=h42
    h: 219057bc5789
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=3.1
    h: ce068f1c7779
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:single-line-diagram
  note: A detailed electrical diagram showing array configuration, overcurrent protection, disconnects
    and conductor details is a core item of the permit package.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=3.1
    h: ce068f1c7779
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: tbl=29
    h: 8684060f2b9b
  review: drafted
- claim_id: c3
  rel: related_to
  target: arch:string-inverter-system
  note: SolarABCs expedited permit templates include standard plans for string inverter systems.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=2.10
    h: 99e939b1a312
  review: drafted
- claim_id: c4
  rel: related_to
  target: arch:microinverter-system
  note: SolarABCs expedited permit templates include standard plans for micro-inverter and ac module systems.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=2.10
    h: 99e939b1a312
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
A permit plan set is the package of drawings and documents an installer submits so the local jurisdiction can approve a PV system before it is built. A good package has a title page, the forms the jurisdiction requires, a site plan with the array layout, access pathways and setbacks, and a detailed electrical diagram. The electrical diagram must show how the array is configured, where the overcurrent protection and disconnects are and how they are rated, and the conduit and wire sizes, types and ratings, plus the content of the required labels. The package also includes mounting structure details and spec sheets for major equipment such as modules, inverters and combiner boxes. More complex projects need more detailed plan sets, which can include structural drawings and fuller electrical drawings. Simple residential systems can use fill-in templates for string inverter, microinverter and AC module designs. The authority having jurisdiction reviews the drawings and then inspects the installation during construction to check that it matches the permit set. Information that is relevant and well organized makes plan review faster, and talking with the building department early helps you learn what it expects the package to contain.

<!-- review notes
- sentence 1: support check: partial - Passages describe the permit package and its contents and the jurisdiction's approval, but do not explicitly define it as what the installer submits to get approval before the system is built.
-->
