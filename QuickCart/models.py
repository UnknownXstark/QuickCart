from enum import Enum
from datetime import datetime

class Role(Enum):
    ADMIN = "Admin"
    USER = "User"
    RIDER = "Rider"