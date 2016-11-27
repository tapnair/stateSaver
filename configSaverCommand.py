import adsk.core, adsk.fusion, traceback

from .stateSaverFunctions import build_drop_down, process_values, save_values

from xml.etree import ElementTree
from xml.etree.ElementTree import SubElement

from .Fusion360CommandBase import Fusion360CommandBase

groupName = 'tapnair-stateSaver'
attribName = 'configSaver'
rootName = 'configSaves'

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
                        feature.timelineObject.isSuppressed = True
                    else:
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




############# Create your Actions Here #################################################
class configSaveCommand(Fusion360CommandBase):
    
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
        save_values(inputs, groupName, attribName, write_XML_suppressState, rootName)
    
    # Runs when user selects your command from Fusion UI, Build UI here
    def onCreate(self, command, inputs):
        
        # Create a few inputs in the UI
        inputs.addStringValueInput('newName', 'New Config Name:', 'New Config')  
        
############# Create your Actions Here #################################################
class configSwitchCommand(Fusion360CommandBase):
    
    # Runs when Fusion command would generate a preview after all inputs are valid or changed
    def onPreview(self, command, inputs):
        process_values(inputs, groupName, attribName, read_XML_suppressState, rootName)
    
    # Runs when the command is destroyed.  Sometimes useful for cleanup after the fact
    def onDestroy(self, command, inputs, reason_):    
        pass
    
    # Runs when when any input in the command dialog is changed
    def onInputChanged(self, command, inputs, changedInput):
        pass
    
    # Runs when the user presses ok button
    def onExecute(self, command, inputs):
        process_values(inputs, groupName, attribName, read_XML_suppressState, rootName)

    # Runs when user selects your command from Fusion UI, Build UI here
    def onCreate(self, command, inputs):
        build_drop_down(inputs, 'Select Saved Config:', groupName, attribName, rootName)

############# Create your Actions Here #################################################
class unsuppressAllCommand(Fusion360CommandBase):
    
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