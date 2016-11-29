# Importing sample Fusion Command
# Could import multiple Command definitions here
from .configSaverCommand import write_XML_suppressState, read_XML_suppressState
from .displaySaverCommand import write_XML_display_state, read_XML_display_state
from .paramSaverCommand import write_XML_param_state, read_XML_param_state
from .stateSaverCommand import stateSaveCommand, stateSwitchCommand
from .unsuppressAllCommand import unsuppressAllCommand
from .paramEditCommand import paramEditCommand


commands = []
command_defs =[]

#### Define parameters for command #####
cmd = {
        'commandName' : 'Save Configuration',
        'commandDescription' : 'Saves the current State of suppression in the model',
        'commandResources' : './resources/CS',
        'cmdId' : 'CS_CmdId',
        'DC_Resources' : './resources/DC',
        'DC_CmdId' : 'stateSaver',
        'command_in_nav_bar' : True,
        'class' : stateSaveCommand,
        'stateType' : 'config',
        'write_function' : write_XML_suppressState
}
command_defs.append(cmd)

#### Define parameters for command #####
cmd = {
        'commandName' : 'Switch Configuration',
        'commandDescription' : 'Allows you to switch to existing Configurations in the Model',
        'commandResources' : './resources/CS',
        'cmdId' : 'SWC_CmdId',
        'DC_Resources' : './resources/DC',
        'DC_CmdId' : 'stateSaver',
        'command_in_nav_bar' : True,
        'class' : stateSwitchCommand,
        'stateType' : 'config',
        'read_function' : read_XML_suppressState
}
command_defs.append(cmd)

#### Define parameters for command #####
cmd = {
        'commandName' : 'Save Display',
        'commandDescription' : 'Save Current Display State Of Components',
        'commandResources' : './resources/displaySave',
        'cmdId' : 'DisplaySave_CmdId',
        'DC_Resources' : './resources/DC',
        'DC_CmdId' : 'stateSaver',
        'command_in_nav_bar' : True,
        'class' : stateSaveCommand,
        'stateType' : 'display',
        'write_function' : write_XML_display_state
}
command_defs.append(cmd)

#### Define parameters for command #####
cmd = {
        'commandName' : 'Switch Display',
        'commandDescription' : 'Switch Display State Of Components',
        'commandResources' : './resources/displaySave',
        'cmdId' : 'DisplaySwitch_CmdId',
        'DC_Resources' : './resources/DC',
        'DC_CmdId' : 'stateSaver',
        'command_in_nav_bar' : True,
        'class' : stateSwitchCommand,
        'stateType' : 'display',
        'read_function' : read_XML_display_state
}
command_defs.append(cmd)

#### Define parameters for command #####
cmd = {
        'commandName' : 'Unsuppress All',
        'commandDescription' : 'Unsuppresses all features in the timeline',
        'commandResources' : './resources/CS',
        'cmdId' : 'unsuppressAll_CmdId',
        'DC_Resources' : './resources/DC',
        'DC_CmdId' : 'stateSaver',
        'command_in_nav_bar' : True,
        'class' : unsuppressAllCommand
}
command_defs.append(cmd)

#### Define parameters for command #####
cmd = {
        'commandName' : 'Edit Parameters',
        'commandDescription' : 'Quickly Edit User Parameters',
        'commandResources' : './resources/CS',
        'cmdId' : 'EP_CmdId',
        'DC_Resources' : './resources/DC',
        'DC_CmdId' : 'stateSaver',
        'command_in_nav_bar' : True,
        'class' : paramEditCommand
}
command_defs.append(cmd)

#### Define parameters for command #####
cmd = {
        'commandName' : 'Save Parameters',
        'commandDescription' : 'Save the Values of all User Parameters',
        'commandResources' : './resources/CS',
        'cmdId' : 'SP_CmdId',
        'DC_Resources' : './resources/DC',
        'DC_CmdId' : 'stateSaver',
        'command_in_nav_bar' : True,
        'class' : stateSaveCommand,
        'stateType' : 'param',
        'write_function' : write_XML_param_state
}
command_defs.append(cmd)

#### Define parameters for command #####
cmd = {
        'commandName' : 'Switch Parameters',
        'commandDescription' : 'Switch between saved sets of user Parameters',
        'commandResources' : './resources/CS',
        'cmdId' : 'SWP_CmdId',
        'DC_Resources' : './resources/DC',
        'DC_CmdId' : 'stateSaver',
        'command_in_nav_bar' : True,
        'class' : stateSwitchCommand,
        'stateType' : 'param',
        'read_function' : read_XML_param_state
}
command_defs.append(cmd)

# Set to True to display various useful messages when debugging your app
debug = False

for cmd_def in command_defs:
    # Creates the commands for use in the Fusion 360 UI
    command = cmd_def['class'](cmd_def, debug)
    commands.append(command)

def run(context):
    for command in commands:
        command.onRun()


def stop(context):
    for command in commands:
        command.onStop()


