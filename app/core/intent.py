from enum import Enum


class Intent(str, Enum):
    VIEW = "VIEW"
    EDIT = "EDIT"
    CREATE = "CREATE"
    SEARCH = "SEARCH"
    HELP = "HELP"
    LIST = "LIST"
    UNKNOWN = "UNKNOWN"
