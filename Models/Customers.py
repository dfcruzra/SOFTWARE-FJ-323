"""
customers.py

Contains the Customer class.

Purpose:
- Represent customers inside the system
- Store customer information safely
- Apply inheritance from Entity
- Apply encapsulation using properties
- Validate data before saving
"""

# Regular expressions module
# Used for stronger email validation
import re

# Base abstract class
from models.entities import Entity # type: ignore

# Custom exception
from exceptions.errors import CustomerError # type: ignore


class Customer(Entity):
    """
    Represents a customer in the system.

    Inherits:
        Entity

    Features:
    - Unique ID
    - Name
    - Email
    - Data validation
    - Encapsulation
    """

    # Basic email validation pattern
    EMAIL_PATTERN = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    def __init__(self, entity_id, name, email):
        """
        Customer constructor.

        Parameters:
            entity_id (int):
                Unique customer ID

            name (str):
                Customer name

            email (str):
                Customer email
        """

        # Initialize parent class
        super().__init__(entity_id)

        # Internal protected attributes
        # Start empty and assign through setters
        # to force validation
        self._name = ""
        self._email = ""

        # Assign values through validated properties
        self.name = name
        self.email = email

    # ==================================================
    # NAME PROPERTY
    # ==================================================
    @property
    def name(self):
        """
        Get customer name.
        """

        return self._name

    @name.setter
    def name(self, new_name):
        """
        Set customer name with validation.
        """

        # Must be string
        if not isinstance(new_name, str):
            raise CustomerError("Customer name must be text.")

        # Remove leading/trailing spaces
        cleaned_name = new_name.strip()

        # Cannot be empty
        if not cleaned_name:
            raise CustomerError("Customer name cannot be empty.")

        # Minimum reasonable length
        if len(cleaned_name) < 2:
            raise CustomerError("Customer name is too short.")

        self._name = cleaned_name

    # ==================================================
    # EMAIL PROPERTY
    # ==================================================
    @property
    def email(self):
        """
        Get customer email.
        """

        return self._email

    @email.setter
    def email(self, new_email):
        """
        Set customer email with validation.
        """

        # Must be string
        if not isinstance(new_email, str):
            raise CustomerError("Email must be text.")

        # Clean spaces
        cleaned_email = new_email.strip().lower()

        # Cannot be empty
        if not cleaned_email:
            raise CustomerError("Email cannot be empty.")

        # Validate format
        if not re.match(self.EMAIL_PATTERN, cleaned_email):
            raise CustomerError("Invalid email format.")

        self._email = cleaned_email

    # ==================================================
    # INFORMATION METHOD
    # ==================================================
    def show_info(self):
        """
        Required implementation from Entity.

        Returns:
            str
        """

        return f"Customer: {self.name} | Email: {self.email}"

    # ==================================================
    # STRING REPRESENTATION
    # ==================================================
    def __str__(self):
        """
        Human-readable representation.
        """

        return self.show_info()

    def __repr__(self):
        """
        Developer-friendly representation.
        Useful for debugging lists/objects.
        """

        return (
            f"Customer("
            f"id={self.id}, "
            f"name='{self.name}', "
            f"email='{self.email}')"
        )
