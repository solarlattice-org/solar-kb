---
id: mit:technology-specific-spectral-response
type: Mitigation
name: Technology-specific spectral response data
---
This action means using spectral response data that matches the specific module technology installed, and not relying on generic assumptions, when you run capacity tests and energy models. Technology-specific data is needed because the same atmospheric spectrum can give different effective irradiance for different module designs. Modules convert some wavelengths better than others, so a broadband irradiance reading alone can overstate the effective irradiance at the cell. Use the response data together with spectral irradiance measurements or validated spectral model inputs, and keep spectral effects separate from temperature, soiling, degradation and irradiance sensor bias. It matters most when comparing technologies or judging tests run during narrow weather windows.

<!-- review notes
- sentence 5: support check: partial - u8 says it can be especially important when comparing technologies or evaluating tests in narrow weather windows, but 'matters most' is stronger than 'can be especially important'.
-->
