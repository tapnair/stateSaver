import adsk.core
import adsk.fusion
import traceback

from .Fusion360CommandBase import Fusion360CommandBase


def unsuppress_all():
    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)

    # Get All components in design
    all_components = design.allComponents
    for comp in all_components:
        
        # Get All features inside the component
        all_features = comp.features
        for feature in all_features:
            
            # Un-suppress feature
            if feature is not None:
                feature.timelineObject.isSuppressed = False


# Fusion 360 Command to Unsuppress all features in the time line
class UnSuppressAllCommand(Fusion360CommandBase):
    
    # Runs when Fusion command would generate a preview after all inputs are valid or changed
    def onPreview(self, command, inputs):
        pass
    
    # Runs when the command is destroyed.  Sometimes useful for cleanup after the fact
    def onDestroy(self, command, inputs, reason_):    
        pass
    
    # Runs when when any input in the command dialog is changed
    def onInputChanged(self, command, inputs, changed_input):
        pass
    
    # Runs when the user presses ok button
    def onExecute(self, command, inputs):
        unsuppress_all()
    
    # Runs when user selects your command from Fusion UI, Build UI here
    def onCreate(self, command, inputs):              
        pass