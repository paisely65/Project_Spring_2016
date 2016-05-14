#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Starter data module"""

def cost(arg1, arg2):
    """This function returns the hospital bill.
    Args:
        arg1(float): Bill from the hospital
        arg2)float): Reimbursment from the patient's insurance

    Returns:
        float: The balance due from the patient

    Examples:
        >>> The balance due is $97.66
        >>> The balance due is $348.95
        
    """
    patient_bill = arg1 - arg2
    return patient_bill

balance_due = cost(2359.45, 2010.50)
print 'The balance due is $'+ str(balance_due)
