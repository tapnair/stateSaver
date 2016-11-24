# State Saver
Fusion 360 Addin to Save Display and Suppresion State

![State Saver Dialog](./resources/configSaverMenu.png)
## Usage:
First see [How to install sample Add-Ins and Scripts](https://rawgit.com/AutodeskFusion360/AutodeskFusion360.github.io/master/Installation.html)

This addin allows you to save and retrieve the suppresion of features and display of components in the graphics window.

See a video here: _TODO_

Select **Save Configuration** to save the current suppression state of all features in the timeline.

Select **Switch Configuration** and select a saved configuration from the drop down. The suppression state of features will revert to that previously saved condition.  
- New features added after the state was saved will retain their current state.  
- Selecting Current or cancel will revert to the suppression state of all components when you entered the command.

Select **Save Display** to save the current display state (lightbulb on/off) of all _components_ in the timeline.

Select **Switch Display** and select a saved display state from the drop down. The display of _components_ will revert to that previously saved condition.  
- New parts added after the state was saved will retain their current state.  
- Selecting Current or cancel will revert to the display state of all components when you entered the command.
- **Note: When selecting objects in the graphics window to "Hide" it is common that you are actually selecting the body NOT the component.  This add-in will only work if you are hiding and showing at the component level.**

Select **Unsuppress All** to simply unsuppress all features in the timeline.  This can be a useful utility when creating configurations.

## Limitations
  * Currently no way to delete saved states
  * Seen issues with more complex history trees failing when you unsuppress many features at once.

## License
Samples are licensed under the terms of the [MIT License](http://opensource.org/licenses/MIT). Please see the [LICENSE](LICENSE) file for full details.

## Written by

Created by Patrick Rainsberry <br /> (Autodesk Fusion 360 Business Development)
