# -*- coding: utf-8 -*-
'''
A set of useful tools for all Web2py projects about managing the server
environment.

@author: Pierre Thibault (pierre.thibault1 -at- gmail.com)
@organization: Voice of Access (http://voiceofaccess.org)
@license: MIT
@since: 2010-11-09
'''

__docformat__ = "epytext en"

import os
from gluon.admin import apath

def get_applications(request):
    """
    @param request: The application request.
    Return all the web2py applications running on the server as a list.
    """ 

    return [f for f in os.listdir(apath(r=request)) if f.find('.') < 0]
