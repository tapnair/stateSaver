import adsk.core, adsk.fusion, traceback

from xml.etree import ElementTree
from xml.etree.ElementTree import SubElement

from .Fusion360CommandBase import Fusion360CommandBase
from .stateSaverFunctions import build_drop_down, process_values, save_values


groupName = 'tapnair-stateSaver'
attribName = 'paramSaver'
rootName = 'paramSaves'

def write_XML_param_state(root, newState):
    
    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)
    
    # Create a new State in the xml tree
    state = SubElement( root, 'state', name=newState)

    userParams = design.userParameters
    for param in userParams:
   
        # Record parameter value state
        if param is not None:               
            SubElement( state, 'parameter', value=str(param.value), name=param.name)    
    
    xmlstr = ElementTree.tostring(root, encoding='unicode', method='xml')
    
    design.attributes.add(groupName, attribName, xmlstr)

def read_XML_param_state(root, state):
    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)

    # Get All parameters in design
    allParams = design.allParameters
    for param in allParams:

        # Apply Saved dimension info
        if param is not None:                       
            test = root.find("state[@name='%s']/parameter[@name='%s']" % (state, param.name))
            if test is not None:
                param.value = float(test.get('value'))

def updateParams(inputs):
    
    # Get Fusion Objects
    app = adsk.core.Application.get()
    ui  = app.userInterface
    design = app.activeProduct
    unitsMgr = design.unitsManager
    
    if inputs.count < 1:
        ui.messageBox('No User Parameters in the model')
        return          
    
    # Set all parameter values based on the input form                            
    for param in design.userParameters:
        inputExpresion = inputs.itemById(param.name).value
        
        # Use Fusion Units Manager to validate user expresion                        
        if unitsMgr.isValidExpression(inputExpresion, unitsMgr.defaultLengthUnits):
            
            # Set parameter value from input form                         
            param.expression = inputExpresion
        
        else:
            ui.messageBox("The following expresion was invalid: \n" +
                            param.name + '\n' +
                            inputExpresion)

############# Create your Actions Here #################################################
class paramSaveCommand(Fusion360CommandBase):
    
    # Runs when Fusion command would generate a preview after all inputs are valid or changed
    def onPreview(self, command, inputs):
        pass
    
    # Runs when the command is destroyed.  Sometimes useful for cleanup after the fact
    def onDestroy(self, command, inputs, reason_):    
        pass
    
    # Runs when when any input in the command dialog is changed
    def onInputChanged(self, command, inputs, changedInput):
        pass
    
    # Runs when the user presses ok button
    def onExecute(self, command, inputs):
        save_values(inputs, groupName, attribName, write_XML_param_state, rootName)
    
    # Runs when user selects your command from Fusion UI, Build UI here
    def onCreate(self, command, inputs):
        
        # Create a few inputs in the UI
        inputs.addStringValueInput('newName', 'New Parameter Set Name:', 'New Params')  
        
############# Create your Actions Here #################################################
class paramSwitchCommand(Fusion360CommandBase):
    
    # Runs when Fusion command would generate a preview after all inputs are valid or changed
    def onPreview(self, command, inputs):
        process_values(inputs, groupName, attribName, read_XML_param_state, rootName)
    
    # Runs when the command is destroyed.  Sometimes useful for cleanup after the fact
    def onDestroy(self, command, inputs, reason_):    
        pass
    
    # Runs when when any input in the command dialog is changed
    def onInputChanged(self, command, inputs, changedInput):
        pass
    
    # Runs when the user presses ok button
    def onExecute(self, command, inputs):

        process_values(inputs, groupName, attribName, read_XML_param_state, rootName)

    # Runs when user selects your command from Fusion UI, Build UI here
    def onCreate(self, command, inputs):
        
        build_drop_down(inputs, 'Select Saved Parameter Set:', groupName, attribName, rootName)

############# Create your Actions Here #################################################
class paramEditCommand(Fusion360CommandBase):
    
    # Runs when Fusion command would generate a preview after all inputs are valid or changed
    def onPreview(self, command, inputs):
        updateParams(inputs)
    
    # Runs when the command is destroyed.  Sometimes useful for cleanup after the fact
    def onDestroy(self, command, inputs, reason_):    
        pass
    
    # Runs when when any input in the command dialog is changed
    def onInputChanged(self, command, inputs, changedInput):
        pass
    
    # Runs when the user presses ok button
    def onExecute(self, command, inputs):
        updateParams(inputs)
    
    # Runs when user selects your command from Fusion UI, Build UI here
    def onCreate(self, command, inputs):              
        app = adsk.core.Application.get()
        design = app.activeProduct
        for param in design.userParameters:                                         
            #if param.name[0] != '_':
            inputs.addStringValueInput(param.name,
                                       param.name,
                                       param.expression)