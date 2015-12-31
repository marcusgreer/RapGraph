# -*- coding: utf-8 -*-

###############################################################################
#
# GetBodyMeasurements
# Gets a summary of a user's body measurements for a specified date.
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

class GetBodyMeasurements(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBodyMeasurements Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetBodyMeasurements, self).__init__(temboo_session, '/Library/Fitbit/Body/GetBodyMeasurements')


    def new_input_set(self):
        return GetBodyMeasurementsInputSet()

    def _make_result_set(self, result, path):
        return GetBodyMeasurementsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBodyMeasurementsChoreographyExecution(session, exec_id, path)

class GetBodyMeasurementsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBodyMeasurements
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(GetBodyMeasurementsInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(GetBodyMeasurementsInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Fitbit.)
        """
        super(GetBodyMeasurementsInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Fitbit.)
        """
        super(GetBodyMeasurementsInputSet, self)._set_input('ConsumerSecret', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((required, date) The date that corresponds with the log entry you want to retrieve (in the format yyyy-MM-dd).)
        """
        super(GetBodyMeasurementsInputSet, self)._set_input('Date', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in: xml or json. Defaults to json.)
        """
        super(GetBodyMeasurementsInputSet, self)._set_input('ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided.)
        """
        super(GetBodyMeasurementsInputSet, self)._set_input('UserID', value)

class GetBodyMeasurementsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBodyMeasurements Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)
    def get_Bicep(self):
        """
        Retrieve the value for the "Bicep" output from this Choreo execution. ((decimal) The bicep measurement.)
        """
        return self._output.get('Bicep', None)
    def get_Calf(self):
        """
        Retrieve the value for the "Calf" output from this Choreo execution. ((decimal) The calf measurement.)
        """
        return self._output.get('Calf', None)
    def get_Chest(self):
        """
        Retrieve the value for the "Chest" output from this Choreo execution. ((decimal) The chest measurement.)
        """
        return self._output.get('Chest', None)
    def get_Fat(self):
        """
        Retrieve the value for the "Fat" output from this Choreo execution. ((decimal) The fat measurement.)
        """
        return self._output.get('Fat', None)
    def get_Forearm(self):
        """
        Retrieve the value for the "Forearm" output from this Choreo execution. ((decimal) The forearm measurement.)
        """
        return self._output.get('Forearm', None)
    def get_Hips(self):
        """
        Retrieve the value for the "Hips" output from this Choreo execution. ((decimal) The hips measurement.)
        """
        return self._output.get('Hips', None)
    def get_Neck(self):
        """
        Retrieve the value for the "Neck" output from this Choreo execution. ((decimal) The neck measurement.)
        """
        return self._output.get('Neck', None)
    def get_Thigh(self):
        """
        Retrieve the value for the "Thigh" output from this Choreo execution. ((decimal) The thigh measurement.)
        """
        return self._output.get('Thigh', None)
    def get_Waist(self):
        """
        Retrieve the value for the "Waist" output from this Choreo execution. ((decimal) The waist measurement.)
        """
        return self._output.get('Waist', None)
    def get_Weight(self):
        """
        Retrieve the value for the "Weight" output from this Choreo execution. ((decimal) The weight measurement.)
        """
        return self._output.get('Weight', None)

class GetBodyMeasurementsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetBodyMeasurementsResultSet(response, path)
