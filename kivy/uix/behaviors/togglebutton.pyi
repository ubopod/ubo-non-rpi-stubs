"""
This type stub file was generated by pyright.
"""

from kivy.uix.behaviors.button import ButtonBehavior

'''
ToggleButton Behavior
=====================

The :class:`~kivy.uix.behaviors.togglebutton.ToggleButtonBehavior`
`mixin <https://en.wikipedia.org/wiki/Mixin>`_ class provides
:class:`~kivy.uix.togglebutton.ToggleButton` behavior. You can combine this
class with other widgets, such as an :class:`~kivy.uix.image.Image`, to provide
alternative togglebuttons that preserve Kivy togglebutton behavior.

For an overview of behaviors, please refer to the :mod:`~kivy.uix.behaviors`
documentation.

Example
-------

The following example adds togglebutton behavior to an image to make a checkbox
that behaves like a togglebutton::

    from kivy.app import App
    from kivy.uix.image import Image
    from kivy.uix.behaviors import ToggleButtonBehavior


    class MyButton(ToggleButtonBehavior, Image):
        def __init__(self, **kwargs):
            super(MyButton, self).__init__(**kwargs)
            self.source = 'atlas://data/images/defaulttheme/checkbox_off'

        def on_state(self, widget, value):
            if value == 'down':
                self.source = 'atlas://data/images/defaulttheme/checkbox_on'
            else:
                self.source = 'atlas://data/images/defaulttheme/checkbox_off'


    class SampleApp(App):
        def build(self):
            return MyButton()


    SampleApp().run()
'''
__all__ = ('ToggleButtonBehavior', )
class ToggleButtonBehavior(ButtonBehavior):
    '''This `mixin <https://en.wikipedia.org/wiki/Mixin>`_ class provides
    :mod:`~kivy.uix.togglebutton` behavior. Please see the
    :mod:`togglebutton behaviors module <kivy.uix.behaviors.togglebutton>`
    documentation for more information.

    .. versionadded:: 1.8.0
    '''
    __groups = ...
    group = ...
    allow_no_selection = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def on_group(self, *largs): # -> None:
        ...
    
    @staticmethod
    def get_widgets(groupname): # -> list[Any]:
        '''Return a list of the widgets contained in a specific group. If the
        group doesn't exist, an empty list will be returned.

        .. note::

            Always release the result of this method! Holding a reference to
            any of these widgets can prevent them from being garbage collected.
            If in doubt, do::

                l = ToggleButtonBehavior.get_widgets('mygroup')
                # do your job
                del l

        .. warning::

            It's possible that some widgets that you have previously
            deleted are still in the list. The garbage collector might need
            to release other objects before flushing them.
        '''
        ...
    


