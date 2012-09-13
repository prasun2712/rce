#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       errors.py
#       
#       This file is part of the RoboEarth Cloud Engine framework.
#       
#       This file was originally created for RoboEearth
#       http://www.roboearth.org/
#       
#       The research leading to these results has received funding from
#       the European Union Seventh Framework Programme FP7/2007-2013 under
#       grant agreement no248942 RoboEarth.
#       
#       Copyright 2012 RoboEarth
#       
#       Licensed under the Apache License, Version 2.0 (the "License");
#       you may not use this file except in compliance with the License.
#       You may obtain a copy of the License at
#       
#       http://www.apache.org/licenses/LICENSE-2.0
#       
#       Unless required by applicable law or agreed to in writing, software
#       distributed under the License is distributed on an "AS IS" BASIS,
#       WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#       See the License for the specific language governing permissions and
#       limitations under the License.
#       
#       \author/s: Dominique Hunziker 
#       
#       

class InternalError(Exception):
    """ This class is used to signal an internal error.
    """
    pass


class InvalidRequest(Exception):
    """ This class is used to signal an invalid request.
    """
    pass


class SerializationError(InternalError):
    """ This error is used for all (de-)serialization errors of
        internal messages.
    """
    pass


class UserConstraintError(Exception):
    """ Error is raised when there are more active users than allowed in a
        manager.
    """
    pass


class AuthenticationError(Exception):
    """ Error is raised when the robot/user could not be authenticated.
    """
    pass

