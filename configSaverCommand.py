import adsk.core, adsk.fusion, traceback

from xml.etree import ElementTree
from xml.etree.ElementTree import SubElement

def write_XML_suppressState(root, newState, design):
   
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
    
    return xmlstr

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
