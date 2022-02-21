# kicad-zone-manager
This is a KiCad Python plugin that manages the zone fills' priority levels in one place.
If you have many zone fills needs to be adjusted then this plugin is probably what you want to have.

This plugin is tested working with KiCad 6.0.

## Windows compatibility
Due to a mysterious bug of wxMSW, the behavior of tree component is different between Windows and Linux, and broke Windows compatibility.
On Linux, the selected zone items kept selected after their priority has been changed. However it is impossible to do on Windows and it is disabled in the code.

# Installation
Clone this repository and drop the top level folder into the plugins folder.
