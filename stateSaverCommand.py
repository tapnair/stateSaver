import adsk.core, adsk.fusion, traceback

from .Fusion360CommandBase import Fusion360CommandBase
from .stateSaverFunctions import build_drop_down, process_values, save_values

############# Create your Actions Here #################################################
class stateSaveCommand(Fusion360CommandBase):
    
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
        inputs.addStringValueInput('newName', 'New' + self.stateType + 'Name:', 'New '+ self.stateType) 

############# Create your Actions Here #################################################
class stateSwitchCommand(Fusion360CommandBase):
    
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