import adsk.core, adsk.fusion, traceback

from xml.etree import ElementTree

# Reads XML data from attribute 
def get_XML_from_attribute(groupName, attributeName, rootName):
    app = adsk.core.Application.get()
    design_ = adsk.fusion.Design.cast(app.activeProduct)

    attrib = design_.attributes.itemByName(groupName, attributeName)
    
    # Get XML Root node
    if attrib is not None:
        root = ElementTree.fromstring(attrib.value)
        
    else:
        root = ElementTree.Element(rootName)

    return root

# Builds a dropdown menu for all states of the given type
def build_drop_down(inputs, title, groupName, attribName, rootName):
    dropDown = inputs.addDropDownCommandInput('currentState', title, adsk.core.DropDownStyles.TextListDropDownStyle)
    dropDownItems = dropDown.listItems
    dropDownItems.add('Current', True)
    
    root = get_XML_from_attribute(groupName, attribName, rootName)
    if root:
        for state in root.findall('state'):
            dropDownItems.add(state.get('name'), False,)

# Processes values from a state if a new one is selected
def process_values(inputs, groupName, attribName, xml_read_function, rootName):
    state = inputs.itemById('currentState').selectedItem.name
    if state != 'Current':
        root = get_XML_from_attribute(groupName, attribName, rootName)
        if root:
            xml_read_function(root, state)

# Saves values for the given state type into proper attribute XML          
def save_values(inputs, groupName, attribName, xml_write_function, rootName):
    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)
    
    root = get_XML_from_attribute(groupName, attribName, rootName)
    
    xmlstr = xml_write_function(root, inputs.itemById('newName').value, design)
    
    design.attributes.add(groupName, attribName, xmlstr)    
    
    
    
    
    