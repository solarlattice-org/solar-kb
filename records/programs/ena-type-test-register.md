---
id: prog:ena-type-test-register
type: Program
name: ENA Type Test Register
aliases:
- Type Test Register
- connect-direct device register
- ENA register
- Live Device Register
category: Certification
program_kind: certification
claims:
- claim_id: c1
  rel: issued_by
  target: org:ena
  note: The register now sits on the ENA connect website; the old site is no longer updated.
  cite:
  - src: src:kb-solis-44002591744-how-can-i-find-the-uk-ena-reference-numbers
    loc: sec=h1
    h: 24e5d72a9cff
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: 'support check: partial - The passage says the ENA register moved to the ENA connect website
    and the old site isn''t updated, but it never says the register is issued by the Energy Networks Association.'
- claim_id: c2
  rel: applies_to
  target: region:gb
  note: Gives the UK ENA reference numbers for grid-connected devices.
  cite:
  - src: src:kb-solis-44002591744-how-can-i-find-the-uk-ena-reference-numbers
    loc: sec=h1
    h: 24e5d72a9cff
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
The ENA Type Test Register lists grid-connection devices such as inverters, and gives each one a UK ENA reference number. The register has moved to the Energy Networks Association connect website, and the old site no longer gets updates. To find a device, open the Live Device Register, use the filters to narrow the search, usually by model, and then open a reference to see what it covers. Depending on when a device was registered, it may have a separate reference number for G100, while some newer devices have several certifications under one reference. Any device above 50kW must now go through as Partially Type Tested, whatever the brand. For these larger units, voltage flicker and harmonics are assessed site by site, often through a witness test or an A2-3 form, so the installer should agree the process with the DNO. Older devices stay listed as Fully Type Tested, unchanged from earlier applications, which can confuse DNOs and installers.

<!-- review notes
- sentence 1: support check: partial - The passage covers UK ENA reference numbers and inverters/devices, but it doesn't explicitly say the register lists grid-connection devices.
-->
