# configSaver
Fusion 360 Addin to Save Suppresion State

![Config Saver Dialog](./resources/configSaverUI.png)
## Usage:
First see [How to install sample Add-Ins and Scripts](https://rawgit.com/AutodeskFusion360/AutodeskFusion360.github.io/master/Installation.html)

This addin allows you to save and retrieve the suppresion of components and the user parameters in the graphics window.

See a video here: TODO

If you select a saved config from the drop down it will revert the suppression of features and/or user parameters to that condition.  New parts will retain their current state.  Selecting Current or cancel will revert to the suppression state of all components and user parameters when you entered the command.

If you select the check box you can create a new state based on the suppresion state of the components when you entered the command.

It stores the saved suppression information in a folder called configSaver in your user directory.  

Alternatively you can select "Unsuppress All"  and it will simply unsuppress all features in the timeline.  

If you select Modify Configuration then you can select an existing configuration to modify/update.  Once you select it you will get a dialog box in which you can update the values of the user parameters for that configuration.

![Modify Configuration Dialog](./resources/MC_1.png)
![Modify Configuration Dialog](./resources/MC_2.png)

## Limitations
  * Since the config information is stored locally it will only be available on the computer it was created.  Looking to add some kind of cloud support in the future.
  * If you have two models of the same name they are not distinguished. Potentially will add project directory to file names.
  * Currently no way to delete saved configs
  * Seen issues with more complex history trees failing when you unsuppress many features at once.

## License
Samples are licensed under the terms of the [MIT License](http://opensource.org/licenses/MIT). Please see the [LICENSE](LICENSE) file for full details.

## Written by

Created by Patrick Rainsberry <br /> (Autodesk Fusion 360 Business Development)
