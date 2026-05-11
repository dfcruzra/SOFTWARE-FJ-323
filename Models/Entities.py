"""
entities.py

Base abstract class for all system entities.

Purpose:
- Define a common structure for all entities
- Enforce implementation of required methods
- Apply inheritance and polymorphism principles
- Promote code reuse
"""

# ABC allows creation of abstract classes
# abstractmethod forces child classes to implement methods
from abc import ABC, abstractmethod


class Entity(ABC):
    """
    Abstract base class for all entities in the system.

    This class cannot be instantiated directly.

    Example:
        entity = Entity(1)   ❌ Not allowed

    Child classes:
        Customer(Entity)     ✅ Allowed
        AnotherEntity(Entity) ✅ Allowed
    """

    def __init__(self, entity_id):
        """
        Initialize common entity attributes.

        Parameters:
            entity_id (int):
                Unique identifier for the entity.
        """

        # Protected attribute
        # Convention: single underscore means
        # "internal use / protected"
        self._id = entity_id

    @property
    def id(self):
        """
        Getter for entity ID.

        Using @property allows controlled access.

        Example:
            customer.id
        """

        return self._id

    @id.setter
    def id(self, new_id):
        """
        Setter with validation.

        Prevents invalid IDs.
        """

        # ID must be integer
        if not isinstance(new_id, int):
            raise ValueError("Entity ID must be an integer.")

        # ID must be positive
        if new_id <= 0:
            raise ValueError("Entity ID must be greater than zero.")

        self._id = new_id

    @abstractmethod
    def show_info(self):
        """
        Abstract method.

        Every child class MUST implement this method.

        Purpose:
            Return readable information about the object.

        Example output:
            "Customer: Daniel | Email: x@gmail.com"
        """

        pass

    def __str__(self):
        """
        String representation of object.

        If object is printed directly,
        this makes output cleaner.
        """

        return f"{self.__class__.__name__}(ID={self._id})"
