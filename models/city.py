#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
        """Represents a city with its state ID and name attributes.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""

