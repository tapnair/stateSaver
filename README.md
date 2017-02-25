# State Saver
Fusion 360 Addin to Save Display,Suppresion and Parameter State

![State Saver Dialog](./resources/configSaverMenu.png)
## Installation:
First see [How to install sample Add-Ins and Scripts](https://rawgit.com/AutodeskFusion360/AutodeskFusion360.github.io/master/Installation.html)


## Usage:
This addin allows you to save and retrieve:
 - The suppresion of features in the timeline 
 - The display of components in the graphics window
 - The values of user defined parameters in the design

See a video here: _TODO_

### Suppression State
* **Save Configuration** will save the current suppression state of all features in the timeline.

* **Switch Configuration** allows you to select a saved configuration from the drop down. The suppression state of features will revert to that previously saved condition.  
- New features added after the state was saved will retain their current state.  
- Selecting Current or cancel will revert to the suppression state of all components when you entered the command.

* **Unsuppress All** will simply unsuppress all features in the timeline.  This can be a useful utility when creating configurations.

### Display State
* **Save Display** will save the current display state (lightbulb on/off) of all _components_ in the timeline.

* **Switch Display** allows you to select a saved display state from the drop down. The display of _components_ will revert to that previously saved condition.  
- New parts added after the state was saved will retain their current state.  
- Selecting Current or cancel will revert to the display state of all components when you entered the command.
- **Note: When selecting objects in the graphics window to "Hide" it is common that you are actually selecting the body NOT the component.  This add-in will only work if you are hiding and showing at the component level.**

### Parmeter State
* **Save Parameters** will save the current value of all _user_ parameters in the design.

* **Switch Parameters** allows you to select a saved set of parameters from the drop down. 
- New paramters added after the state was saved will retain their current value.  
- Selecting Current or cancel will revert to the value of all parameters when you entered the command.
- Addin only saves the values of _User Defined_ parameters, not all model parameters

* **Edit Parameters** allows you to easily modify the values of all user parameters.  See realtime feedback on the changes.

## Limitations
  * Currently no way to delete saved states
  * Seen issues with more complex history trees failing when you unsuppress many features at once.

## License
Samples are licensed under the terms of the [MIT License](http://opensource.org/licenses/MIT). Please see the [LICENSE](LICENSE) file for full details.

## Written by

Created by Patrick Rainsberry <br /> (Autodesk Fusion 360 Business Development)
