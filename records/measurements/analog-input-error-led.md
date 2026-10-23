---
id: meas:analog-input-error-led
type: Measurement
name: Analog input error LED
aliases:
- Error AI 1
- Error AI 2
- Error AI 3
- Error AI 4
---
Each channel of the 4-channel analog input terminal has its own error LED, designated Error AI 1 through Error AI 4. An unlit error LED means the channel is working normally. A red error LED means a wire break on that channel, or a measured value outside the permitted measurement range. On another analog input terminal in the same document, a red channel LED means the range was violated (values too high or too low), a short circuit, or a wire break. On that terminal, an unlit LED means no error. Note which channel's LED is red, then check that input's sensor wiring for breaks or shorts and confirm the signal is within range.

<!-- review notes
- sentence 6: support check: partial - The passages give the red-LED meanings (wire break, short circuit, out of range), which support the checks. They give no troubleshooting steps, and the short-circuit check applies only to the second terminal.
-->
