#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module updates patient's information."""

# Patient data is entered in this format after initial itake and updated when medication is assigned.
{
  "chart_number": {
    ('patient_name', 'date_of_birth', 'sex'): {
        'diagnosis': 'description',
        'admitted': 'admission_status'}

admit_47283 = {
    ('Loan Peckham', 'May 2 1935', 'F'): {
        'diagnosis': 'hypertension',
        'admitted': 'Y'}
    }
admit_29243 = {
    ('Gay Kilduff', 'June 6 1936', 'F'): {
        'diagnosis': 'bronchitis',
        'admitted': 'Y'}
    }
admit_83362 = {
    ('Clarinda Mcintyre', 'June 27 1936', 'F'): {
        'diagnosis': 'low blood pressure',
        'admitted': 'Y'}
    }
admit_75176 = {
    ('Cristie Hosley', 'January 3 1940', 'F'): {
        'diagnosis': 'kidney disease',
        'admitted': 'N'}
    }
admit_76126 = {
     ('Anneliese Eddinger', 'February 3 1940', 'F'): {
         'diagnosis': 'high blood pressure',
         'admitted': 'N'}
     }
admit_73277 = {
    ('Sandie Hendrickson', 'February 2 1945', 'F'): {
        'diagnosis': 'diabetes',
        'admitted': 'Y'
    }
admit_81823 = {
    ('Norman Konen', 'September 19 1945', 'M'): {
        'diagnosis': 'sprained ankle',
        'admitted': 'N'
    }
admit_56187 = {
    ('Charlie Hartzler', 'November 11 1945', 'M'): {
        'diagnosis': 'hypertension',
        'admitted': 'N'
    }
admit_44204 = {
    ('Bob Byerley', 'April 4 1949', 'M'): {
        'diagnosis': 'infection',
        'admitted': 'Y'
    }
admit_74227 = {
    ('Trang Fairfax', 'July 21 1954', 'M'): {
        'diagnosis':'infection',
        'admitted': 'Y'
    }
admit_78974 = {
    ('Elisha Abler', 'March 3 1955', 'M'): {
        'diagnosis': 'stroke',
        'admitted': 'Y '
    }
admit_64732 = {
    ('Ashlyn Toma', 'July 17 1958', 'F'): {
        'diagnosis': 'diabetes',
        'admitted': 'N'
    }
admit_56547 = {
    ('Magan Bradstreet', 'August 6 1960', 'F'): {
        'diagnosis': 'hypertension',
        'admitted': 'N'
    }
admit_18569 = {
    ('Guy Langlinais', 'September 9 1960', 'M'): {
        'diagnosis': 'diabetes',
        'admitted': 'N'
    }
admit_68171 = {
    ('Cleopatra Cavender', 'March 3 1960', 'F'): {
        'diagnosis': 'lupus',
        'admitted': 'Y'
    }
}

# Support staff can add new medication as dirceted by clinicians
# This information represents a new screen on the user interface

# adding meds template
'chart_number['mediaction'] = ['name', 'strength','dosage']

Examples

>>>
{('Loan Peckham', 'May 2 1935', 'F'): {'admitted': 'Y', 'diagnosis':'hypertension'},
 'mediaction': ['Celexa', '250mg', '1x daily as needed']}

>>>
{('Guy Langlinais', 'September 9 1960', 'M'): {'admitted': 'N', 'diagnosis': 'diabetes'},
 'mediaction': ['Insulin', '100-U', '>= 3x daily as needed']}

>>>
{('Trang Fairfax', 'July 21 1954', 'M'): {'admitted': 'Y', 'diagnosis': 'infection'},
 'mediaction': ['Amikacin', '15 mg', '15 mg/kg/day divided IV/IM q8-12hr']}



#Patient chart is immediatety updated and accessible to clinical staff
