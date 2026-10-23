---
id: symptom:memory-card-unwritable
type: Symptom
name: Memory card not writable
aliases:
- SD card defective
- SD memory card defective
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: SMA event 7113 means the memory card is full or write-protected.
  quote: The memory card is full or write-protected
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=18.r2
    h: fa5d00a293af
  - src: src:sma-doc-259761
    loc: tbl=65.r11
    h: fa5d00a293af
  - src: src:kb-sma-sbx1xpus41-event-messages
    loc: sec=h41
    h: 603b0e3c0e52
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r8
    h: fa5d00a293af
  - src: src:kb-sma-stpxx-us-41-event-messages
    loc: tbl=1.r23
    h: 3a9d4eb112f2
  - src: src:sma-doc-278742
    loc: tbl=70.r11
    h: fa5d00a293af
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r8
    h: fa5d00a293af
  - src: src:kb-sma-shpxxus20-event-messages
    loc: tbl=1.r26
    h: 3a9d4eb112f2
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r8
    h: fa5d00a293af
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r5
    h: fd0b0630be23
  - src: src:kb-sma-stptl-10-us-event-messages
    loc: tbl=1.r31
    h: 77efe0a4cd25
  - src: src:sma-doc-278742
    loc: tbl=69.r9
    h: 9ab64019d0bd
  - src: src:sma-kb-event-7101
    loc: sec=h1
    h: b034f3e1ecea
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17
    h: 0bf33a33e1f6
  - src: src:sma-doc-259761
    loc: tbl=64.r9
    h: 522661820bfc
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:sd-card-status-message
  note: On Sunny Island, the display can show that the SD card is full, has an invalid file format, is
    incompatible, or is not inserted.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=38
    h: 4b390b4b9557
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=175.r16
    h: 7770ea886fa2
  review: drafted
  review_note: 'support check: partial - Display shows full, invalid format, incompatible, and a ''no
    card inserted'' status exists (CardStt Off), but the passages don''t tie these to ''not writable''
    explicitly, and the Sunny Island display''s ''not inserted'' is from a parameter, not the display
    list.'
---
SMA inverters log event 7113 when the memory card is full or write-protected. On STP-TL-US units, event 7101 reports a defective SD card, and the stated cause is a card that has not been formatted. Other SMA manuals say event 7101 means the micro SD card in the inverter is faulty and should be replaced. SMA describes the 71xx events as faults during an inverter update from the SD card. The fix is to reformat the card, save the files to it again, and replace the card if needed. Don't confuse this with event 7106, a defective update file, or event 7105, where parameters could not be set from the card and the inverter keeps feeding the grid. On Sunny Island units, the display can show that the card is full, has an invalid format or is incompatible. Updates fail on unsupported cards, so use a card of at most 2 GB formatted as FAT-16. Check first whether the card is full or write-protected. Then reformat it, and replace it if the event comes back.

<!-- review notes
- sentence 2: support check: partial - Event 7101 as SD card defective with not-formatted cause is stated, but the passages don't mention STP-TL-US units.
- sentence 5: support check: partial - 7106 defective update file is stated, but 7105 'inverter continues feeding' appears only in the u19 version; the 'don't confuse' framing is not in the passages, though content matches.
- sentence 7: support check: partial - Reformat and replace if necessary appear (for 7101), but the check-first-for-full/write-protected step and 'if event comes back' sequence for 7113 are not stated.
- sentence 7: review: partial - The 7113 meaning and the reformat-then-replace remedy (given for 7101) are stated, but the order of checking full/write-protected first and replacing only if the event comes back is not.
-->
