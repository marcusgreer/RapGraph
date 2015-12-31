# -*- coding: utf-8 -*-

###############################################################################
#
# ForumHasViews
# Determines if the specified forum has one or more views.
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

class ForumHasViews(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ForumHasViews Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ForumHasViews, self).__init__(temboo_session, '/Library/Disqus/Forums/ForumHasViews')


    def new_input_set(self):
        return ForumHasViewsInputSet()

    def _make_result_set(self, result, path):
        return ForumHasViewsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ForumHasViewsChoreographyExecution(session, exec_id, path)

class ForumHasViewsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ForumHasViews
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth 2.0 access token.)
        """
        super(ForumHasViewsInputSet, self)._set_input('AccessToken', value)
    def set_Forum(self, value):
        """
        Set the value of the Forum input for this Choreo. ((required, string) Forum Short Name (i.e., the subdomain of the Disqus Site URL).  )
        """
        super(ForumHasViewsInputSet, self)._set_input('Forum', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        super(ForumHasViewsInputSet, self)._set_input('PublicKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default), jsonp, or rss.)
        """
        super(ForumHasViewsInputSet, self)._set_input('ResponseFormat', value)

class ForumHasViewsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ForumHasViews Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Disqus.)
        """
        return self._output.get('Response', None)

class ForumHasViewsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ForumHasViewsResultSet(response, path)
