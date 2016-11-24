# Importing sample Fusion Command
# Could import multiple Command definitions here
from .configSaverCommand import configSaveCommand, configSwitchCommand, unsuppressAllCommand
from .displaySaverCommand import displaySaveCommand, displaySwitchCommand

#### Define parameters for 2nd command #####
commandName1 = 'Save Configuration'
commandDescription1 = 'Saves the current State of suppression in the model'
commandResources1 = './resources/CS'
cmdId1 = 'CS_CmdId'

#### Define parameters for 2nd command #####
commandName2 = 'Switch Configuration'
commandDescription2 = 'Allows you to switch to existing Configurations in the Model'
commandResources2 = './resources/CS'
cmdId2 = 'SWC_CmdId'

#### Define parameters for 3rd command #####
commandName3 = 'Display Save'
commandDescription3 = 'Manage Display Of Components and Bodies'
commandResources3 = './resources/displaySave'
cmdId3 = 'DisplaySave_CmdId'

#### Define parameters for 3rd command #####
commandName4 = 'Display Switch'
commandDescription4 = 'Switch Display Of Components'
commandResources4 = './resources/displaySave'
cmdId4 = 'DisplaySwitch_CmdId'

#### Define parameters for 3rd command #####
commandName5 = 'Unsuppress All'
commandDescription5 = 'Unsuppresses all features in the timeline'
commandResources5 = './resources/CS'
cmdId5 = 'unsuppressAll_CmdId'

#### Define parameters for Drop Down Command #####
DC_Resources = './resources/DC'
DC_CmdId = 'stateSaver'

# Set to True to display various useful messages when debugging your app
debug = False

# Creates the commands for use in the Fusion 360 UI
newCommand1 = configSaveCommand(commandName1, commandDescription1, commandResources1, cmdId1, DC_CmdId, DC_Resources, debug)
newCommand2 = configSwitchCommand(commandName2, commandDescription2, commandResources2, cmdId2, DC_CmdId, DC_Resources, debug)
newCommand3 = displaySaveCommand(commandName3, commandDescription3, commandResources3, cmdId3, DC_CmdId, DC_Resources, debug)
newCommand4 = displaySwitchCommand(commandName4, commandDescription4, commandResources4, cmdId4, DC_CmdId, DC_Resources, debug)
newCommand5 = unsuppressAllCommand(commandName5, commandDescription5, commandResources5, cmdId5, DC_CmdId, DC_Resources, debug)

def run(context):
    newCommand1.onRun()
    newCommand2.onRun()
    newCommand3.onRun()
    newCommand4.onRun()
    newCommand5.onRun()

def stop(context):
    newCommand1.onStop()
    newCommand2.onStop()
    newCommand3.onStop()
    newCommand4.onStop()
    newCommand5.onStop()

