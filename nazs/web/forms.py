from achilles.forms import *  # noqa


# Override forms template
FormBlock.template_name = 'web/form.html'

#: Show a save button by default
FormBlock.save_button = True
