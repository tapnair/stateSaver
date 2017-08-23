from xml.etree import ElementTree

import adsk.core
import adsk.fusion
import traceback


# Reads XML data from attribute returns element tree root element
def get_xml_from_attribute(group_name, attribute_name, root_name):
    app = adsk.core.Application.get()
    design_ = adsk.fusion.Design.cast(app.activeProduct)

    attrib = design_.attributes.itemByName(group_name, attribute_name)
    
    # Get XML Root node
    if attrib is not None:
        root = ElementTree.fromstring(attrib.value)
        
    else:
        root = ElementTree.Element(root_name)

    return root


# Builds a drop down menu for all states of the given type
def build_drop_down(inputs, title, group_name, attrib_name, root_name, is_check_box=False):

    if is_check_box:
        drop_down = inputs.addDropDownCommandInput('select_state', title,
                                                   adsk.core.DropDownStyles.CheckBoxDropDownStyle)
        drop_down_items = drop_down.listItems

    else:
        drop_down = inputs.addDropDownCommandInput('currentState', title,
                                                   adsk.core.DropDownStyles.TextListDropDownStyle)
        drop_down_items = drop_down.listItems
        drop_down_items.add('Current', True)

    update_drop_down(drop_down_items, group_name, attrib_name, root_name)


def update_drop_down(drop_down_items, group_name, attrib_name, root_name):

    root = get_xml_from_attribute(group_name, attrib_name, root_name)

    if root:
        for state in root.findall('state'):
            drop_down_items.add(state.get('name'), False, )


# Processes values from a state if a new one is selected
def process_values(inputs, group_name, attrib_name, xml_read_function, root_name):

    state = inputs.itemById('currentState').selectedItem.name

    if state != 'Current':
        root = get_xml_from_attribute(group_name, attrib_name, root_name)

        if root:
            xml_read_function(root, state)


# Saves values for the given state type into proper attribute XML          
def save_values(inputs, group_name, attrib_name, xml_write_function, root_name):

    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)
    
    root = get_xml_from_attribute(group_name, attrib_name, root_name)
    
    xml_string = xml_write_function(root, inputs.itemById('newName').value, design)
    
    design.attributes.add(group_name, attrib_name, xml_string)

