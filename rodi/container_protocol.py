from typing import TypeVar, Union, Type

try:
    from typing import Protocol
except ImportError:  # pragma: no cover
    from typing_extensions import Protocol


T = TypeVar("T")


class ContainerProtocol(Protocol):
    """
    Generic interface of DI Container that can register and resolve services,
    and tell if a type is configured.
    """

    def register(self, obj_type: Union[Type, str], *args, **kwargs):
        """Registers a type in the container, with optional arguments."""

    def resolve(self, obj_type: Union[Type[T], str], *args, **kwargs) -> T:
        """Activates an instance of the given type, with optional arguments."""

    def __contains__(self, item) -> bool:
        """
        Returns a value indicating whether a given type is configured in this container.
        """
