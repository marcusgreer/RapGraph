# -*- coding: utf-8 -*-

###############################################################################
#
# InsertRecords
# Inserts records into your Zoho CRM account.
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

class InsertRecords(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the InsertRecords Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(InsertRecords, self).__init__(temboo_session, '/Library/Zoho/CRM/InsertRecords')


    def new_input_set(self):
        return InsertRecordsInputSet()

    def _make_result_set(self, result, path):
        return InsertRecordsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return InsertRecordsChoreographyExecution(session, exec_id, path)

class InsertRecordsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the InsertRecords
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AnnualRevenue(self, value):
        """
        Set the value of the AnnualRevenue input for this Choreo. ((optional, string) Corresponds to the Annual Revenue field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('AnnualRevenue', value)
    def set_AuthenticationToken(self, value):
        """
        Set the value of the AuthenticationToken input for this Choreo. ((required, string) A valid authentication token. Permanent authentication tokens can be generated by the GenerateAuthToken Choreo.)
        """
        super(InsertRecordsInputSet, self)._set_input('AuthenticationToken', value)
    def set_CampaignSource(self, value):
        """
        Set the value of the CampaignSource input for this Choreo. ((optional, string) Corresponds to the Campaign Source field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('CampaignSource', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((optional, string) Corresponds to the City field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('City', value)
    def set_Company(self, value):
        """
        Set the value of the Company input for this Choreo. ((optional, string) Corresponds to the Company field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('Company', value)
    def set_Country(self, value):
        """
        Set the value of the Country input for this Choreo. ((optional, string) Corresponds to the Country field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('Country', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) Corresponds to the Description field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('Description', value)
    def set_EmailOptOut(self, value):
        """
        Set the value of the EmailOptOut input for this Choreo. ((optional, boolean) Corresponds to the Email Opt Out field in Zoho. Defaults to 0 for false.)
        """
        super(InsertRecordsInputSet, self)._set_input('EmailOptOut', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((optional, string) Corresponds to the Email field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('Email', value)
    def set_Fax(self, value):
        """
        Set the value of the Fax input for this Choreo. ((optional, string) Corresponds to the Fax field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('Fax', value)
    def set_FirstName(self, value):
        """
        Set the value of the FirstName input for this Choreo. ((optional, string) Corresponds to the First Name field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('FirstName', value)
    def set_Industry(self, value):
        """
        Set the value of the Industry input for this Choreo. ((optional, string) Corresponds to the Industry field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('Industry', value)
    def set_LastName(self, value):
        """
        Set the value of the LastName input for this Choreo. ((required, string) Corresponds to the Last Name field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('LastName', value)
    def set_LeadOwner(self, value):
        """
        Set the value of the LeadOwner input for this Choreo. ((optional, string) Corresponds to the Lead Owner field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('LeadOwner', value)
    def set_LeadSource(self, value):
        """
        Set the value of the LeadSource input for this Choreo. ((optional, string) Corresponds to the Lead Source field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('LeadSource', value)
    def set_LeadStatus(self, value):
        """
        Set the value of the LeadStatus input for this Choreo. ((optional, string) Corresponds to the Lead Status field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('LeadStatus', value)
    def set_Mobile(self, value):
        """
        Set the value of the Mobile input for this Choreo. ((optional, string) Corresponds to the Mobile field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('Mobile', value)
    def set_Module(self, value):
        """
        Set the value of the Module input for this Choreo. ((optional, string) The Zoho module you want to access. Defaults to 'Leads'.)
        """
        super(InsertRecordsInputSet, self)._set_input('Module', value)
    def set_NumOfEmployees(self, value):
        """
        Set the value of the NumOfEmployees input for this Choreo. ((optional, string) Corresponds to the Num Of Employees field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('NumOfEmployees', value)
    def set_Phone(self, value):
        """
        Set the value of the Phone input for this Choreo. ((optional, string) Corresponds to the Phone field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('Phone', value)
    def set_Rating(self, value):
        """
        Set the value of the Rating input for this Choreo. ((optional, string) Corresponds to the Rating field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('Rating', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid formats are: json and xml (the default).)
        """
        super(InsertRecordsInputSet, self)._set_input('ResponseFormat', value)
    def set_Salutation(self, value):
        """
        Set the value of the Salutation input for this Choreo. ((optional, string) Corresponds to the Salutation field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('Salutation', value)
    def set_SkypeID(self, value):
        """
        Set the value of the SkypeID input for this Choreo. ((optional, string) Corresponds to the Skype ID field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('SkypeID', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) Corresponds to the State field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('State', value)
    def set_Street(self, value):
        """
        Set the value of the Street input for this Choreo. ((optional, string) Corresponds to the Street field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('Street', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((optional, string) Corresponds to the Title field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('Title', value)
    def set_Website(self, value):
        """
        Set the value of the Website input for this Choreo. ((optional, string) Corresponds to the Website field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('Website', value)
    def set_ZipCode(self, value):
        """
        Set the value of the ZipCode input for this Choreo. ((optional, integer) Corresponds to the Zip Code field in Zoho)
        """
        super(InsertRecordsInputSet, self)._set_input('ZipCode', value)

class InsertRecordsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the InsertRecords Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Zoho. Format corresponds to the ResponseFormat input. Defaults to xml.)
        """
        return self._output.get('Response', None)

class InsertRecordsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return InsertRecordsResultSet(response, path)
