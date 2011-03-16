# -*- coding: utf-8 -*-
'''
A set of helper functions and helper classes useful tools for all Web2py
projects.

@author: Pierre Thibault (pierre.thibault1 -at- gmail.com)
@organization: Voice of Access (http://voiceofaccess.org)
@license: MIT
@since: 2010-11-09
'''
__docformat__ = "epytext en"

class Web2pyEnum:
    """
    A base class to create enums to work with IS_IN_SET.
    The derived class must have an class iterable member called "ENUM_VALUES"
    containing the values used for the enum in the db. The order of these
    will be used as the default order for presentation. If the derived class
    has member named "FORCE" that is true (based on Python truth) then the
    values will always be translated. 
    @since: 2010-10-29
    """
    def __init__(self):
        raise NotImplementedError("Always abstract.")
        
    @classmethod
    def IS_IN_SET(cls, T, IS_IN_SET):
        """
        @param cls: The derived class.
        @param T: The usual web2py translator.
        @param IS_IN_SET: Web2py IS_IN_SET function.
        @see: The doc of the class itself.
        """
        force = hasattr(cls, "FORCE") and cls.FORCE
        current_languages = T.current_languages
        try:
            if force:
                T.set_current_languages(None)
            in_set_param = []
            for enum_value in cls.ENUM_VALUES:
                in_set_param.append((enum_value, 
                    str(T(enum_value)) if force else T(enum_value)))
            return IS_IN_SET(in_set_param)
        finally:
            if force:
                T.set_current_languages(current_languages)
