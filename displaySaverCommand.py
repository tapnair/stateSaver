import adsk.core, adsk.fusion, traceback

from xml.etree import ElementTree
from xml.etree.ElementTree import SubElement

def write_XML_display_state(root, newState, design):
    
    rootComp = adsk.fusion.Component.cast(design.rootComponent)
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
    
    return xmlstr
    

def read_XML_display_state(root, state):
    
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
