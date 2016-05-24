
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides guidelines for creating a budget"""

def projected_funding(estimated_costs, approved_budget):
    """This function guides creation of the budget.

    Args:
        estimated_costs(int): The estimated cost of the budget in US Dollars
        approved_budget(int): The budget approved for the project in US Dollars

    Returns:
        The final budget for the project
        
    Examles:
        >>> projected_approval(96000, 60000)
        -36000
        
        >>> projected_approval(75000, 90000)
        15000
        
        >>> projected_approval(102000, 96000)
        -6000
    """
    budget_slack = approved_budget - estimated_costs 
    return budget_slack

def project_approval(budget_slack):
    """This functions determines project approval status.

    Args:
         budget_slack: Extra financing created for potential unexpected costs
 
    Returns:
        The approval status of the project

    Examples:
        >>> project_approval(20000)
        'Schedule meetings with stakeholders.'
        
        >>> project_approval(30000)
        'Budget approved!'
    """
    if budget_slack >= 27000:    
        return "Budget approved!"
    else:
        return "Schedule meetings with stakeholders."
    
    

