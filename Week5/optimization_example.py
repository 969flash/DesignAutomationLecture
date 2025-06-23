"""Placeholder script for Week 5 optimization exercises."""
import rhinoscriptsyntax as rs

def adjust_height(orientation):
    base_height = 10
    if orientation == 'north':
        return base_height * 1.2
    return base_height

# Additional optimization logic would be implemented here
