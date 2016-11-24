import adsk.core, adsk.fusion, traceback

from xml.etree import ElementTree
from xml.etree.ElementTree import SubElement

from .Fusion360CommandBase import Fusion360NavCommandBase

groupName = 'tapnair-stateSaver'
attribName = 'configSaver'
def write_XML_suppressState(root, newState):
    
    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)
    
    # Create a new State in the xml tree
    state = SubElement( root, 'state', name=newState)

    # Get All components in design and itterate
    allComponents = design.allComponents
    for comp in allComponents:
        
        # Get All features inside the component
        allFeatures = comp.features
        for feature in allFeatures:
            
            # Record feature suppression state
            if feature is not None:               
                if feature.timelineObject.isSuppressed:                               
                    # ui.messageBox(str(feature.name) + " Is Suppressed")
                    SubElement( state, 'feature', component=comp.name, name=feature.name, suppress = 'suppressed')
                else:
                    # ui.messageBox(str(feature.name) + " Is Unsuppressed")
                    SubElement( state, 'feature', component=comp.name, name=feature.name, suppress = 'unSuppressed')
    
    xmlstr = ElementTree.tostring(root, encoding='unicode', method='xml')
    
    design.attributes.add(groupName, attribName, xmlstr)

def read_XML_suppressState(root, state):
    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)

    # Get All components in design
    allComponents = design.allComponents
    for comp in allComponents:
        
        # Get All features inside the component
        allFeatures = comp.features
        for feature in allFeatures:
            
            # Find feature saved state and set value
            if feature is not None:
                test = root.find("state[@name='%s']/feature[@name='%s'][@component='%s']" % (state, feature.name, comp.name))
                if test is not None:
                    if test.get('suppress') == 'suppressed':
                        # ui.messageBox(str(feature.name) + " Is Suppressed")
                        feature.timelineObject.isSuppressed = True
                    else:
                        # ui.messageBox(str(feature.name) + " Is Unsuppressed")
                        feature.timelineObject.isSuppressed = False

def unsuppressAll():

    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)

    # Get All components in design
    allComponents = design.allComponents
    for comp in allComponents:
        
        # Get All features inside the component
        allFeatures = comp.features
        for feature in allFeatures:
            
            # Unsuppress feature
            if feature is not None:
                feature.timelineObject.isSuppressed = False

def getXML_from_Attribute(groupName, attributeName):
    app = adsk.core.Application.get()
    design_ = adsk.fusion.Design.cast(app.activeProduct)

    attrib = design_.attributes.itemByName(groupName, attributeName)
    
    # Get XML Root node
    if attrib is not None:
        root = ElementTree.fromstring(attrib.value)
        
    else:
        root = ElementTree.Element('configSaves')

    return root


############# Create your Actions Here #################################################
class configSaveCommand(Fusion360NavCommandBase):
    
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
        root = getXML_from_Attribute(groupName, attribName)
        write_XML_suppressState(root, inputs.itemById('newName').value)
    
    # Runs when user selects your command from Fusion UI, Build UI here
    def onCreate(self, command, inputs):
        
        # Create a few inputs in the UI
        inputs.addStringValueInput('newName', 'New Config Name:', 'New Config')  
        
############# Create your Actions Here #################################################
class configSwitchCommand(Fusion360NavCommandBase):
    
    # Runs when Fusion command would generate a preview after all inputs are valid or changed
    def onPreview(self, command, inputs):
        state = inputs.itemById('currentState').selectedItem.name
        if state != 'Current':
            root = getXML_from_Attribute(groupName, attribName)
            if root:
                read_XML_suppressState(root, state)
    
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
            read_XML_suppressState(root, state)

    # Runs when user selects your command from Fusion UI, Build UI here
    def onCreate(self, command, inputs):
        
        dropDown = inputs.addDropDownCommandInput('currentState', 'Select Saved Config:', adsk.core.DropDownStyles.TextListDropDownStyle)
        dropDownItems = dropDown.listItems
        dropDownItems.add('Current', True)
        
        root = getXML_from_Attribute(groupName, attribName)
        if root:
            for state in root.findall('state'):
                dropDownItems.add(state.get('name'), False,)

############# Create your Actions Here #################################################
class unsuppressAllCommand(Fusion360NavCommandBase):
    
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
        unsuppressAll()
    
    # Runs when user selects your command from Fusion UI, Build UI here
    def onCreate(self, command, inputs):              
        pass