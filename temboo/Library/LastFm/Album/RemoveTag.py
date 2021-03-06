# -*- coding: utf-8 -*-

###############################################################################
#
# RemoveTag
# Removes a user's tag from a specified album.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RemoveTag(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RemoveTag Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RemoveTag, self).__init__(temboo_session, '/Library/LastFm/Album/RemoveTag')


    def new_input_set(self):
        return RemoveTagInputSet()

    def _make_result_set(self, result, path):
        return RemoveTagResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RemoveTagChoreographyExecution(session, exec_id, path)

class RemoveTagInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RemoveTag
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((string) Your Last.fm API Key.)
        """
        super(RemoveTagInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((string) Your Last.fm API Secret.)
        """
        super(RemoveTagInputSet, self)._set_input('APISecret', value)
    def set_Album(self, value):
        """
        Set the value of the Album input for this Choreo. ((string) The album name.)
        """
        super(RemoveTagInputSet, self)._set_input('Album', value)
    def set_Artist(self, value):
        """
        Set the value of the Artist input for this Choreo. ((string) The artist name.)
        """
        super(RemoveTagInputSet, self)._set_input('Artist', value)
    def set_SessionKey(self, value):
        """
        Set the value of the SessionKey input for this Choreo. ((string) The session key retrieved in the last step of the authorization process.)
        """
        super(RemoveTagInputSet, self)._set_input('SessionKey', value)
    def set_Tag(self, value):
        """
        Set the value of the Tag input for this Choreo. ((string) A single user tag to remove from this album.)
        """
        super(RemoveTagInputSet, self)._set_input('Tag', value)

class RemoveTagResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RemoveTag Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class RemoveTagChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RemoveTagResultSet(response, path)
