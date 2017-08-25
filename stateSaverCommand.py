from xml.etree import ElementTree

from .Fusion360CommandBase import Fusion360CommandBase
from .stateSaverFunctions import build_drop_down, process_values, save_values, update_drop_down, get_xml_from_attribute

import adsk.core
import adsk.fusion
import traceback


class StateSaveCommand(Fusion360CommandBase):
    
    def __init__(self, cmd_def, debug):
        
        super().__init__(cmd_def, debug)
        
        self.stateType = cmd_def.get('stateType')
        self.write_function = cmd_def.get('write_function')
        
        self.groupName = 'tapnair-stateSaver'
        self.attribName = self.stateType + 'Saver'
        self.rootName = self.stateType + 'Saves'
    
    # Runs when the user presses ok button
    def onExecute(self, command, inputs):
        
        # Write the Current State as XML data in design parameter                  
        save_values(inputs, self.groupName, self.attribName, self.write_function, self.rootName)
    
    # Runs when user selects your command from Fusion UI, Build UI here
    def onCreate(self, command, inputs):
        
        # Name the new Display State
        inputs.addStringValueInput('newName', 'New' + self.stateType + 'Name:', 'New ' + self.stateType)


class StateSwitchCommand(Fusion360CommandBase):
    
    def __init__(self, cmd_def, debug):
        
        super().__init__(cmd_def, debug)
        
        self.stateType = cmd_def.get('stateType')
        self.read_function = cmd_def.get('read_function')
        
        self.groupName = 'tapnair-stateSaver'
        self.attribName = self.stateType + 'Saver'
        self.rootName = self.stateType + 'Saves'
        
    # Runs when Fusion command would generate a preview after all inputs are valid or changed
    def onPreview(self, command, inputs):
        process_values(inputs, self.groupName, self.attribName, self.read_function, self.rootName)

    # Runs when the user presses ok button
    def onExecute(self, command, inputs):
        process_values(inputs, self.groupName, self.attribName, self.read_function, self.rootName)
    
    # Runs when user selects your command from Fusion UI, Build UI here
    def onCreate(self, command, inputs):
        build_drop_down(inputs, 'Select Saved ' + self.stateType + ':', self.groupName, self.attribName, self.rootName)


class DeleteStates(Fusion360CommandBase):
    def __init__(self, cmd_def, debug):
        super().__init__(cmd_def, debug)

        self.stateType = 'param'

        self.groupName = 'tapnair-stateSaver'
        self.attribName = self.stateType + 'Saver'
        self.rootName = self.stateType + 'Saves'

    # Runs when Fusion command would generate a preview after all inputs are valid or changed
    def onPreview(self, command, inputs):
        pass

    # Runs when the user presses ok button
    def onExecute(self, command, inputs):

        app = adsk.core.Application.get()
        design = adsk.fusion.Design.cast(app.activeProduct)
        ui = app.userInterface

        root = get_xml_from_attribute(self.groupName, self.attribName, self.rootName)

        item_list = inputs.itemById('select_state').listItems

        for item in item_list:
            if item.isSelected:
                test = root.find('state[@name="%s"]' % item.name)
                if test is not None:
                    root.remove(test)

        xml_string = ElementTree.tostring(root, encoding='unicode', method='xml')

        design.attributes.add(self.groupName, self.attribName, xml_string)

    # Runs when when any input in the command dialog is changed
    def onInputChanged(self, command, inputs, changed_input):

            # Update ui based on vent type selected
            if changed_input.id == 'state_type':

                if changed_input.selectedItem.name == 'Parameters':
                    self.stateType = 'param'
                elif changed_input.selectedItem.name == 'Display':
                    self.stateType = 'display'
                # elif changed_input.selectedItem.name == 'Suppression':
                #     self.stateType = 'config'

                self.attribName = self.stateType + 'Saver'
                self.rootName = self.stateType + 'Saves'

                drop_down_items = inputs.itemById('select_state').listItems

                drop_down_items.clear()

                update_drop_down(drop_down_items, self.groupName, self.attribName, self.rootName)

    # Runs when user selects your command from Fusion UI, Build UI here
    def onCreate(self, command, inputs):
        state_type_input = inputs.addDropDownCommandInput('state_type', 'State Type: ',
                                                          adsk.core.DropDownStyles.LabeledIconDropDownStyle)
        state_type_input.listItems.add('Parameters', True)
        state_type_input.listItems.add('Display', False)
        # state_type_input.listItems.add('Suppression', False)

        build_drop_down(inputs, 'Select Saved ' + self.stateType + ' to delete:',
                        self.groupName, self.attribName, self.rootName, True)
