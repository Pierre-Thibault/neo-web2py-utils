# -*- coding: utf-8 -*-
'''
A set of useful tools for all Web2py projects about internalization.

@author: Pierre Thibault (pierre.thibault1 -at- gmail.com)
@organization: Voice of Access (http://voiceofaccess.org)
@license: MIT
@since: 2010-11-09
'''
__docformat__ = "epytext en"

def fr_en_language_set(T):
    """
    A ready to use French/English sequence to use with IS_IN_SET to create a
    language menu.
    @param T: The web2py translator.
    """
    return (("fr", T("French")), ("en", T("English")))

def expand_abbreviation(abbreviation, language, T):
    """
    Expand an abbreviation based on the abbreviation file for the language
    found the application "languages" translation folder.
    @param abbreviation: The abbreviation string to exand.
    @param language: The language used by the translator. The suffix
    "-abbreviations" is added after the language to form the name of the file
    to use.
    @param T: The usual "T" translator.
    @return: The word or the expression related to the abbreviation.
    """
    return translate(abbreviation, language + "-abbreviations", T)
        
def translate(word, language, T):
    """
    Force the translation of "word" in "language".
    Restore the state of T before returning.
    @param word: Word or text translate.
    @param language: The language used by the translator.
    @param T: The usual "T" translator.
    @return: The text translated in the requested language.
    """
    accepted_language = T.accepted_language 
    try:
        if language == None:
            language = "en"
        T.force(language)
        return str(T(word))
    finally:
        T.force(accepted_language)

def always_translate(word, T):
    """
    Always translate like there is no default language.
    Restore the state of T before returning.
    @param word: Word or text translate.
    @param T: The usual "T" translator.
    @return: The text translated.
    """
    current_languages = T.current_languages
    try:
        T.set_current_languages(None)
        return str(T(word))
    finally:
        T.set_current_languages(current_languages)

def format_phone(phone):
    """
    Format a string as a phone number.
    """
    if len(phone) == 10:
        return "(" + phone[:3] + ") " + phone[3:6] + "-" + phone[-4:]
    else:
        return phone
    
def format_postal_code(postal_code):
    """
    Format a postal.
    """
    if len(postal_code) == 6:
        return postal_code[:3] + " " + postal_code[-3:]
    else:
        return postal_code

