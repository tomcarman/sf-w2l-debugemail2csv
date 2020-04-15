# Salesforce W2L fail email -> CSV

This is a script to convert Salesforce Web-to-Lead failure emails (eg. "Salesforce Could Not Create This Lead') into a csv for mass loading.

It's pretty niche, and it's badly written in python. It should only be used when you have no other options.

## Usage

The script expects an `input.txt` of concatenated failure emails eg.

```
Salesforce could not create this lead because of the reason listed below. For more information about this error or help with Web-to-Lead, please contact Customer Support.

Reason: {Stack trace reminding you of your dumb failure}

Lead Capture Page: xxx

Record Information:

    FirstName = Test
    LastName = Lead 
    email = blah@blah.com
    Website = www.oops.com
    city = London
    country = UK
    company = ACME
    LeadSource = Web-to-Lead
    MobilePhone = 1234567
    Some_Custom_Field__c = 'blah'

To incorporate this lead into salesforce.com you can key in the data above.

------------------------------------------------------------------------

Salesforce could not create this lead because of the reason listed below. For more information about this error or help with Web-to-Lead, please contact Customer Support.

Reason: {Stack trace reminding you of your dumb failure}

Lead Capture Page: xxx

Record Information:

    FirstName = Test
    LastName = Lead 
    email = blah@blah.com
    Website = www.oops.com
    city = London
    country = UK
    company = ACME
    LeadSource = Web-to-Lead
    MobilePhone = 1234567
    Some_Custom_Field__c = 'blah'

To incorporate this lead into salesforce.com you can key in the data above.

If you have any questions, please click on Support at the top right of any page within salesforce.com.

Customer Support
salesforce.com

------------------------------------------------------------------------

Salesforce could not create this lead because of the reason listed below. For more information about this error or help with Web-to-Lead, please contact Customer Support.

Reason: {Stack trace reminding you of your dumb failure}

Lead Capture Page: xxx

Record Information:

    FirstName = Test
    LastName = Lead 
    email = blah@blah.com
    Website = www.oops.com
    city = London
    country = UK
    company = ACME
    LeadSource = Web-to-Lead
    MobilePhone = 1234567
    Some_Custom_Field__c = 'blah'

To incorporate this lead into salesforce.com you can key in the data above.

If you have any questions, please click on Support at the top right of any page within salesforce.com.

Customer Support
salesforce.com
