import adsk.core, adsk.fusion, traceback

from xml.etree import ElementTree
from xml.etree.ElementTree import SubElement

from .Fusion360CommandBase import Fusion360NavCommandBase

groupName = 'tapnair-stateSaver'
attribName = 'displaySaver'

def writeXML_DisplayState(root, newState):
    app = adsk.core.Application.get()
    design_ = adsk.fusion.Design.cast(app.activeProduct)
    rootComp = adsk.fusion.Component.cast(design_.rootComponent)
    allOccurences = rootComp.allOccurrences
     
    # Create a new State in the xml tree
    state = SubElement( root, 'state', name=newState )
    
    # Iteraate all occurances and set visibility
    for occurence in allOccurences:
            if occurence.isLightBulbOn:                               
                SubElement( state, 'occurance', name=occurence.fullPathName, hide = 'show')
            else:
                SubElement( state, 'occurance', name=occurence.fullPathName, hide = 'hide')
    
    xmlstr = ElementTree.tostring(root, encoding='unicode', method='xml')
    
    design_.attributes.add(groupName, attribName, xmlstr)
    


def getXML_from_Attribute(groupName, attributeName):
    app = adsk.core.Application.get()
    design_ = adsk.fusion.Design.cast(app.activeProduct)

    attrib = design_.attributes.itemByName(groupName, attributeName)
    
    # Get XML Root node
    if attrib is not None:
        root = ElementTree.fromstring(attrib.value)
        
    else:
        root = ElementTree.Element('displaySaves')

    return root

def read_XML_displayState(root, state):
    
    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)
    rootComp = adsk.fusion.Component.cast(design.rootComponent)
    allOccurences = rootComp.allOccurrences

    for occurence in allOccurences:
        test = root.find('state[@name="%s"]/occurance[@name="%s"]' % (state, occurence.fullPathName))
        if test is not None:
            if test.get('hide') == 'hide':
                occurence.isLightBulbOn = False
            else:
                occurence.isLightBulbOn = True
            
            
############# Create your Actions Here #################################################
class displaySaveCommand(Fusion360NavCommandBase):
    
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
        
        # Write the Current State of Display to file                   
        root = getXML_from_Attribute(groupName, attribName)
        writeXML_DisplayState(root, inputs.itemById('newName').value)
    
    # Runs when user selects your command from Fusion UI, Build UI here
    def onCreate(self, command, inputs):
        
        # Name the new Display State
        inputs.addStringValueInput('newName', 'New Display Name:', 'New Display') 

############# Create your Actions Here #################################################
class displaySwitchCommand(Fusion360NavCommandBase):
    
    # Runs when Fusion command would generate a preview after all inputs are valid or changed
    def onPreview(self, command, inputs):
        state = inputs.itemById('currentState').selectedItem.name
        if state != 'Current':
            root = getXML_from_Attribute(groupName, attribName)
            if root:
                read_XML_displayState(root, state)
    
    # Runs when the command is destroyed.  Sometimes useful for cleanup after the fact
    def onDestroy(self, command, inputs, reason_):    
        pass
    
    # Runs when when any input in the command dialog is changed
    def onInputChanged(self, command, inputs, changedInput):
        pass
    
    # Runs when the user presses ok button
    def onExecute(self, command, inputs):
        state = inputs.itemById('currentState').selectedItem.name
        root = getXML_from_Attribute(groupName, attribName)
        if root:
            read_XML_displayState(root, state)
    
    # Runs when user selects your command from Fusion UI, Build UI here
    def onCreate(self, command, inputs):
        
        dropDown = inputs.addDropDownCommandInput('currentState', 'Select Saved Display:', adsk.core.DropDownStyles.TextListDropDownStyle)
        dropDownItems = dropDown.listItems
        
        dropDownItems.add('Current', True)
        
        root = getXML_from_Attribute(groupName, attribName)
        if root:
            for state in root.findall('state'):
                dropDownItems.add(state.get('name'), False,)