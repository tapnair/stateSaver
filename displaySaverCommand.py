from xml.etree import ElementTree
from xml.etree.ElementTree import SubElement

import adsk.core
import adsk.fusion
import traceback


def write_xml_display_state(root, new_state, design):
    
    root_comp = adsk.fusion.Component.cast(design.rootComponent)
    all_occurrences = root_comp.allOccurrences
     
    # Create a new State in the xml tree
    state = SubElement(root, 'state', name=new_state)
    
    # Iterate all occurrences and set visibility
    for occurrence in all_occurrences:
            if occurrence.isLightBulbOn:
                SubElement(state, 'occurrence', name=occurrence.fullPathName, hide='show')
            else:
                SubElement(state, 'occurrence', name=occurrence.fullPathName, hide='hide')
    
    xml_string = ElementTree.tostring(root, encoding='unicode', method='xml')
    
    return xml_string
    

def read_xml_display_state(root, state):
    
    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)
    root_comp = adsk.fusion.Component.cast(design.rootComponent)
    all_occurrences = root_comp.allOccurrences

    for occurrence in all_occurrences:
        test = root.find('state[@name="%s"]/occurrence[@name="%s"]' % (state, occurrence.fullPathName))
        if test is not None:
            if test.get('hide') == 'hide':
                occurrence.isLightBulbOn = False
            else:
                occurrence.isLightBulbOn = True
