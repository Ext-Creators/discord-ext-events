from typing import Callable, Dict
from . import member_kick

_ALL: Dict[str, Callable] = {
    member_kick.EVENT_NAME: member_kick.EVENT_CALLABLE,
}
