import adsk.core
import adsk.fusion
import traceback

from .Fusion360CommandBase import Fusion360CommandBase


def update_params(inputs):

    # Get Fusion Objects
    app = adsk.core.Application.get()
    ui = app.userInterface
    design = app.activeProduct
    units_mgr = design.unitsManager

    if inputs.count < 1:
        ui.messageBox('No User Parameters in the model')
        return

        # Set all parameter values based on the input form
    for param in design.userParameters:
        input_expression = inputs.itemById(param.name).value

        # Use Fusion Units Manager to validate user expression
        if units_mgr.isValidExpression(input_expression, units_mgr.defaultLengthUnits):

            # Set parameter value from input form                         
            param.expression = input_expression

        else:
            ui.messageBox("The following expression was invalid: \n" +
                          param.name + '\n' +
                          input_expression)


class ParamEditCommand(Fusion360CommandBase):
    # Runs when Fusion command would generate a preview after all inputs are valid or changed
    def onPreview(self, command, inputs):
        update_params(inputs)

    # Runs when the command is destroyed.  Sometimes useful for cleanup after the fact
    def onDestroy(self, command, inputs, reason_):
        pass

    # Runs when when any input in the command dialog is changed
    def onInputChanged(self, command, inputs, changed_input):
        pass

    # Runs when the user presses ok button
    def onExecute(self, command, inputs):
        update_params(inputs)

    # Runs when user selects your command from Fusion UI, Build UI here
    def onCreate(self, command, inputs):
        app = adsk.core.Application.get()
        design = app.activeProduct

        for param in design.userParameters:
            # if param.name[0] != '_':

            inputs.addStringValueInput(param.name,
                                       param.name,
                                       param.expression)
