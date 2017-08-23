from xml.etree import ElementTree
from xml.etree.ElementTree import SubElement

import adsk.core
import adsk.fusion
import traceback


# TODO rewrite to simply walk the timeline.  Not components features.
def write_xml_suppress_state(root, new_state, design):
   
    # Create a new State in the xml tree
    state = SubElement(root, 'state', name=new_state)

    # Get All components in design and iterate
    all_components = design.allComponents
    for comp in all_components:
        
        # Get All features inside the component
        all_features = comp.features
        for feature in all_features:
            
            # Record feature suppression state
            if feature is not None:               
                if feature.timelineObject.isSuppressed:                               
                    # ui.messageBox(str(feature.name) + " Is Suppressed")
                    SubElement(state, 'feature', component=comp.name, name=feature.name, suppress = 'suppressed')
                else:
                    # ui.messageBox(str(feature.name) + " Is Unsuppressed")
                    SubElement(state, 'feature', component=comp.name, name=feature.name, suppress = 'unSuppressed')
    
    xml_string = ElementTree.tostring(root, encoding='unicode', method='xml')
    
    return xml_string


def read_xml_suppress_state(root, state):
    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)

    # Get All components in design
    all_components = design.allComponents
    for comp in all_components:
        
        # Get All features inside the component
        all_features = comp.features
        for feature in all_features:
            
            # Find feature saved state and set value
            if feature is not None:
                test = root.find("state[@name='%s']/feature[@name='%s'][@component='%s']" % (state, feature.name, comp.name))
                if test is not None:
                    if test.get('suppress') == 'suppressed':
                        feature.timelineObject.isSuppressed = True
                    else:
                        feature.timelineObject.isSuppressed = False
