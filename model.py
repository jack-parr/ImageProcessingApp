'''
This file contains all the data-related functions, performing logic functions requested by the controller and returning the result.
'''

import ast
import config

class MainModel:

    def _evaluateExpression(expression):
        # this evaluates the given expression (model).
        try:
            node = ast.parse(expression, mode='eval')
            result = str(eval(compile(node, '<string>', 'eval')))
        except Exception:
            result = config.ERROR_MSG
        return result
