"""
This type stub file was generated by pyright.
"""

import re
import imghdr
import zipfile
import sys
from base64 import b64decode
from kivy.event import EventDispatcher
from kivy.core import core_register_libs
from kivy.logger import Logger
from kivy.cache import Cache
from kivy.clock import Clock
from kivy.atlas import Atlas
from kivy.resources import resource_find
from kivy.utils import platform
from kivy.compat import string_types
from kivy.setupconfig import USE_SDL2
from io import BytesIO
from os import environ
from kivy.graphics.texture import Texture, TextureRegion

"""
This type stub file was generated by pyright.
"""
__all__ = ('Image', 'ImageLoader', 'ImageData')
TextureRegion = ...
class ImageData:
    '''Container for images and mipmap images.
    The container will always have at least the mipmap level 0.
    '''
    __slots__ = ...
    _supported_fmts = ...
    def __init__(self, width, height, fmt, data, source=..., flip_vertical=..., source_image=..., rowlength=...) -> None:
        ...
    
    def release_data(self):
        ...
    
    @property
    def width(self):
        '''Image width in pixels.
        (If the image is mipmapped, it will use the level 0)
        '''
        ...
    
    @property
    def height(self):
        '''Image height in pixels.
        (If the image is mipmapped, it will use the level 0)
        '''
        ...
    
    @property
    def data(self):
        '''Image data.
        (If the image is mipmapped, it will use the level 0)
        '''
        ...
    
    @property
    def rowlength(self):
        '''Image rowlength.
        (If the image is mipmapped, it will use the level 0)

        .. versionadded:: 1.9.0
        '''
        ...
    
    @property
    def size(self):
        '''Image (width, height) in pixels.
        (If the image is mipmapped, it will use the level 0)
        '''
        ...
    
    @property
    def have_mipmap(self):
        ...
    
    def __repr__(self):
        ...
    
    def add_mipmap(self, level, width, height, data, rowlength):
        '''Add a image for a specific mipmap level.

        .. versionadded:: 1.0.7
        '''
        ...
    
    def get_mipmap(self, level):
        '''Get the mipmap image at a specific level if it exists

        .. versionadded:: 1.0.7
        '''
        ...
    
    def iterate_mipmaps(self):
        '''Iterate over all mipmap images available.

        .. versionadded:: 1.0.7
        '''
        ...
    


class ImageLoaderBase:
    '''Base to implement an image loader.'''
    __slots__ = ...
    def __init__(self, filename, **kwargs) -> None:
        ...
    
    def load(self, filename):
        '''Load an image'''
        ...
    
    @staticmethod
    def can_save(fmt, is_bytesio=...):
        '''Indicate if the loader can save the Image object

        .. versionchanged:: 1.11.0
            Parameter `fmt` and `is_bytesio` added
        '''
        ...
    
    @staticmethod
    def can_load_memory():
        '''Indicate if the loader can load an image by passing data
        '''
        ...
    
    @staticmethod
    def save(*largs, **kwargs):
        ...
    
    def populate(self):
        ...
    
    @property
    def width(self):
        '''Image width
        '''
        ...
    
    @property
    def height(self):
        '''Image height
        '''
        ...
    
    @property
    def size(self):
        '''Image size (width, height)
        '''
        ...
    
    @property
    def texture(self):
        '''Get the image texture (created on the first call)
        '''
        ...
    
    @property
    def textures(self):
        '''Get the textures list (for mipmapped image or animated image)

        .. versionadded:: 1.0.8
        '''
        ...
    
    @property
    def nocache(self):
        '''Indicate if the texture will not be stored in the cache

        .. versionadded:: 1.6.0
        '''
        ...
    


class ImageLoader:
    loaders = ...
    @staticmethod
    def zip_loader(filename, **kwargs):
        '''Read images from an zip file.

        .. versionadded:: 1.0.8

        Returns an Image with a list of type ImageData stored in Image._data
        '''
        ...
    
    @staticmethod
    def register(defcls):
        ...
    
    @staticmethod
    def load(filename, **kwargs):
        ...
    


class Image(EventDispatcher):
    '''Load an image and store the size and texture.

    .. versionchanged:: 1.0.7

        `mipmap` attribute has been added. The `texture_mipmap` and
        `texture_rectangle` have been deleted.

    .. versionchanged:: 1.0.8

        An Image widget can change its texture. A new event 'on_texture' has
        been introduced. New methods for handling sequenced animation have been
        added.

    :Parameters:
        `arg`: can be a string (str), Texture, BytesIO or Image object
            A string path to the image file or data URI to be loaded; or a
            Texture object, which will be wrapped in an Image object; or a
            BytesIO object containing raw image data; or an already existing
            image object, in which case, a real copy of the given image object
            will be returned.
        `keep_data`: bool, defaults to False
            Keep the image data when the texture is created.
        `mipmap`: bool, defaults to False
            Create mipmap for the texture.
        `anim_delay`: float, defaults to .25
            Delay in seconds between each animation frame. Lower values means
            faster animation.
        `ext`: str, only with BytesIO `arg`
            File extension to use in determining how to load raw image data.
        `filename`: str, only with BytesIO `arg`
            Filename to use in the image cache for raw image data.
    '''
    copy_attributes = ...
    data_uri_re = ...
    _anim_ev = ...
    def __init__(self, arg, **kwargs) -> None:
        ...
    
    def remove_from_cache(self):
        '''Remove the Image from cache. This facilitates re-loading of
        images from disk in case the image content has changed.

        .. versionadded:: 1.3.0

        Usage::

            im = CoreImage('1.jpg')
            # -- do something --
            im.remove_from_cache()
            im = CoreImage('1.jpg')
            # this time image will be re-loaded from disk

        '''
        ...
    
    def anim_reset(self, allow_anim):
        '''Reset an animation if available.

        .. versionadded:: 1.0.8

        :Parameters:
            `allow_anim`: bool
                Indicate whether the animation should restart playing or not.

        Usage::

            # start/reset animation
            image.anim_reset(True)

            # or stop the animation
            image.anim_reset(False)

        You can change the animation speed whilst it is playing::

            # Set to 20 FPS
            image.anim_delay = 1 / 20.

        '''
        ...
    
    anim_delay = ...
    @property
    def anim_available(self):
        '''Return True if this Image instance has animation available.

        .. versionadded:: 1.0.8
        '''
        ...
    
    @property
    def anim_index(self):
        '''Return the index number of the image currently in the texture.

        .. versionadded:: 1.0.8
        '''
        ...
    
    def on_texture(self, *largs):
        '''This event is fired when the texture reference or content has
           changed. It is normally used for sequenced images.

        .. versionadded:: 1.0.8
        '''
        ...
    
    @staticmethod
    def load(filename, **kwargs):
        '''Load an image

        :Parameters:
            `filename`: str
                Filename of the image.
            `keep_data`: bool, defaults to False
                Keep the image data when the texture is created.
        '''
        ...
    
    image = ...
    filename = ...
    def load_memory(self, data, ext, filename=...):
        '''(internal) Method to load an image from raw data.
        '''
        ...
    
    @property
    def size(self):
        '''Image size (width, height)
        '''
        ...
    
    @property
    def width(self):
        '''Image width
        '''
        ...
    
    @property
    def height(self):
        '''Image height
        '''
        ...
    
    @property
    def texture(self):
        '''Texture of the image'''
        ...
    
    @property
    def nocache(self):
        '''Indicate whether the texture will not be stored in the cache or not.

        .. versionadded:: 1.6.0
        '''
        ...
    
    def save(self, filename, flipped=..., fmt=...):
        '''Save image texture to file.

        The filename should have the '.png' extension because the texture data
        read from the GPU is in the RGBA format. '.jpg' might work but has not
        been heavily tested so some providers might break when using it.
        Any other extensions are not officially supported.

        The flipped parameter flips the saved image vertically, and
        defaults to False.

        Example::

            # Save an core image object
            from kivy.core.image import Image
            img = Image('hello.png')
            img.save('hello2.png')

            # Save a texture
            texture = Texture.create(...)
            img = Image(texture)
            img.save('hello3.png')

        .. versionadded:: 1.7.0

        .. versionchanged:: 1.8.0
            Parameter `flipped` added to flip the image before saving, default
            to False.

        .. versionchanged:: 1.11.0
            Parameter `fmt` added to force the output format of the file
            Filename can now be a BytesIO object.

        '''
        ...
    
    def read_pixel(self, x, y):
        '''For a given local x/y position, return the pixel color at that
        position.

        .. warning::
            This function can only be used with images loaded with the
            keep_data=True keyword. For example::

                m = Image.load('image.png', keep_data=True)
                color = m.read_pixel(150, 150)

        :Parameters:
            `x`: int
                Local x coordinate of the pixel in question.
            `y`: int
                Local y coordinate of the pixel in question.
        '''
        ...
    


def load(filename):
    '''Load an image'''
    ...

image_libs = ...
if platform in ('macosx', 'ios'):
    ...
if USE_SDL2:
    ...
else:
    ...
libs_loaded = ...
if 'KIVY_DOC' not in environ and not libs_loaded:
    ...
