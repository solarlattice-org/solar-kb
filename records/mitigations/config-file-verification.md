---
id: mit:config-file-verification
type: Mitigation
name: Configuration file verification
---
Configuration file verification means confirming that a configuration file is right for the inverter before you import it. It applies when the inverter rejects an import with event 7347 (Incompatible file) or event 7348 (Incorrect file format). Event 7347 means the selected configuration file does not suit this inverter. The fix is to choose a file that matches the device and then run the import again. Event 7348 means the file is not in the required format or is damaged. Check that the file has the correct format and is intact, then retry the import. To adopt a configuration from a file, you need an inverter configuration that has already been saved to a file. In the user interface, select the option to adopt the configuration from a file, browse to the file and import it. Event 7350 is only a status message. It shows that the configuration file is being transferred. Checking the file does not fix every import problem. If the import fails because of user rights (event 7349), log in as Installer and import the file again.

<!-- review notes
- sentence 1: support check: partial - The passages say events 7347 and 7348 mean the file is unsuitable or in the wrong format and tell you to ensure the file is suitable and retry. They never define 'configuration file verification' as a concept. They also don't say it is done before import or that it applies when the inverter rejects an import.
- sentence 5: support check: partial - Event 7350 is shown as 'Transfer of a configuration file has started', meaning the file is being transferred. The passages never call it a status message or say it is only that.
- sentence 6: support check: partial - Event 7349 is supported: log in as Installer and import the file again. The claim that checking the file does not fix every import problem is an inference, not stated in the passages.
-->
