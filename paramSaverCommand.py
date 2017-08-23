from xml.etree import ElementTree
from xml.etree.ElementTree import SubElement

import adsk.core
import adsk.fusion
import traceback


def write_xml_param_state(root, new_state, design):
    
    # Create a new State in the xml tree
    state = SubElement(root, 'state', name=new_state)

    user_params = design.userParameters
    for param in user_params:
   
        # Record parameter value state
        if param is not None:               
            SubElement(state, 'parameter', value=str(param.value), name=param.name)
    
    xml_string = ElementTree.tostring(root, encoding='unicode', method='xml')
    
    return xml_string


def read_xml_param_state(root, state):
    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)

    # Get All parameters in design
    all_params = design.allParameters
    for param in all_params:

        # Apply Saved dimension info
        if param is not None:                       
            test = root.find("state[@name='%s']/parameter[@name='%s']" % (state, param.name))
            if test is not None:
                param.value = float(test.get('value'))
