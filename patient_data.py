#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module shows how store the inital intake data of patients."""

ADMIT_INFO = 'On {date}, {name}, was admitted to the {department}, ' \
             'complaining of {symptoms}.'
             
print ADMIT_INFO.format(date='5.6.16', name='Sally Vos', \
department='Emergency Department', symptoms=['fever, chills, cough'])

patient_info = '{}, {}, {}, {}, {}'
print patient_info.format('name', 'DOB', 'SS number', 'address', 'insurance information')

