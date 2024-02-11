#!/usr/bin/python3

from models import storage
import uuid
import datetime

class BaseModel:
    """
    BaseModel class for storing common attributes/methods for other models.
    
    Attributes:
        id (str): Unique identifier for the BaseModel instance.
        created_at (datetime.datetime): Date and time when the instance was created.
        updated_at (datetime.datetime): Date and time when the instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments. If provided, the attributes of
                the instance will be set according to these key-value pairs.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def save(self):
        """
        Updates the updated_at attribute and saves the instance to the storage.
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
            dict: A dictionary containing all attributes of the BaseModel instance.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A string containing the class name and the instance id.
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

