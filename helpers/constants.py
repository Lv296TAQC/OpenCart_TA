"""
Contains Return class
"""

# pylint: disable=too-few-public-methods
class Returns:
    """
    Contains constants
    """
    TEXT_DANGER_FIRST_NAME = 'First Name must be between 1 and 32 characters!'
    TEXT_DANGER_LAST_NAME = 'Last Name must be between 1 and 32 characters!'
    TEXT_DANGER_EMAIL = 'E-Mail Address does not appear to be valid!'
    TEXT_DANGER_TELEPHONE = 'Telephone must have 14 characters'
    TEXT_DANGER_ORDER_ID = 'Order ID required!'
    TEXT_DANGER_PRODUCT_NAME = 'Product Name must be greater than 3 and less than 255 characters!'
    TEXT_DANGER_PRODUCT_CODE = 'Product Model must be greater than 3 and less than 64 characters!'

    TEXT_DANGER_FIRST_NAME_INVALID = 'First Name must be between 1 and 32 characters!'
    TEXT_DANGER_LAST_NAME_INVALID = 'Last Name must be between 1 and 32 characters!'
    TEXT_DANGER_EMAIL_INVALID = 'E-Mail Address does not appear to be valid!'
    TEXT_DANGER_TELEPHONE_INVALID = 'Telephone must have 14 characters'
    TEXT_DANGER_ORDER_ID_INVALID = 'Order ID required!'

    DANGER_COLOR = 'rgba(169, 68, 66, 1)'
