import adsk.core, adsk.fusion, traceback

from xml.etree import ElementTree
from xml.etree.ElementTree import SubElement

def write_XML_param_state(root, newState, design):
    
    # Create a new State in the xml tree
    state = SubElement( root, 'state', name=newState)

    userParams = design.userParameters
    for param in userParams:
   
        # Record parameter value state
        if param is not None:               
            SubElement( state, 'parameter', value=str(param.value), name=param.name)    
    
    xmlstr = ElementTree.tostring(root, encoding='unicode', method='xml')
    
    return xmlstr
    
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
