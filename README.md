# State Saver
Fusion 360 Addin to Save Display,Suppresion and Parameter State

![State Saver Dialog](./resources/configSaverMenu.png)

# Installation
[Click here to download the Add-in](https://github.com/tapnair/stateSaver/archive/master.zip)


After downloading the zip file follow the [installation instructions here](https://tapnair.github.io/installation.html) for your particular OS version of Fusion 360 


## Usage:
This addin allows you to save and retrieve:
 - The display of components in the graphics window
 - The values of user defined parameters in the design


### Display State
**Save Display** will save the current display state (lightbulb on/off) of all _components_ in the timeline.

**Switch Display** allows you to select a saved display state from the drop down. The display of _components_ will revert to that previously saved condition.  
- New parts added after the state was saved will retain their current state.  
- Selecting Current or cancel will revert to the display state of all components when you entered the command.
- **Note: When selecting objects in the graphics window to "Hide" it is common that you are actually selecting the body NOT the component.  This add-in will only work if you are hiding and showing at the component level.**

### Parameter State
**Save Parameters** will save the current value of all _user_ parameters in the design.

**Switch Parameters** allows you to select a saved set of parameters from the drop down. 
- New parameters added after the state was saved will retain their current value.
- Selecting Current or cancel will revert to the value of all parameters when you entered the command.
- Addin only saves the values of _User Defined_ parameters, not all model parameters

**Edit Parameters** allows you to easily modify the values of all user parameters.  See real time feedback on the changes.

### Delete States

**Select Parameters or Display States** then check the boxes for the states you want to delete.

Note: There is _no undo_ for this action

## License
Samples are licensed under the terms of the [MIT License](http://opensource.org/licenses/MIT). Please see the [LICENSE](LICENSE) file for full details.

## Written by

Written by [Patrick Rainsberry](https://twitter.com/prrainsberry) <br /> (Autodesk Fusion 360 Business Development)

See more useful [Fusion 360 Utilities](https://tapnair.github.io/index.html)

[![Analytics](https://ga-beacon.appspot.com/UA-41076924-3/stateSaver)](https://github.com/igrigorik/ga-beacon)
