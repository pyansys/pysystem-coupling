"""
Implementation types for the System Coupling adaptor API.

These comprise: "container" types supporting nesting, basic types
for primitive settings values, and "command" types.

Child containers can be generally accessed/modified using attribute access.
Named child objects can be accessed/modified using the index operator.

Primitive settings are accessed (get/set) as properties.

Calling an object will return its current value as a "state" dictionary.

Example
-------
Given a root object, `setup` say:

interface_name = "interface-1"
interface = setup.coupling_interface.create(interface_name)
interface.side["One"].coupling_participant = "MAPDL-1"

setup.solution_control.time_step_size = "0.1 [s]"
setup.solution_control.print_state()
assert setup.solution_control.time_step_size == "0.1 [s]"
"""
import collections
import keyword
import sys
from typing import Dict, Generic, List, NewType, Tuple, TypeVar, Union
import weakref

from ansys.systemcoupling.core.util import name_util

# Type hints
RealType = NewType("real", Union[float, str])  # constant or expression
RealListType = List[RealType]
RealVectorType = Tuple[RealType, RealType, RealType]
IntListType = List[int]
StringListType = List[str]
BoolListType = List[bool]
PrimitiveStateType = Union[
    str, RealType, int, bool, RealListType, IntListType, StringListType, BoolListType
]
DictStateType = Dict[str, "StateType"]
ListStateType = List["StateType"]
StateType = Union[PrimitiveStateType, DictStateType, ListStateType]

# Special types for specific command arguments
StrFloatPairType = Tuple[str, float]
StrFloatPairListType = List[StrFloatPairType]
StrOrIntType = Union[str, int]
StrOrIntDictType = Dict[str, StrOrIntType]
StrOrIntDictListType = List[StrOrIntDictType]
StrOrIntDictListDictType = Dict[str, StrOrIntDictListType]


def to_python_name(syc_name: str) -> str:
    """Convert a native SyC name string to python variable name.

    Native names are camel case - we convert to snake case.
    """
    if not syc_name:
        return syc_name
    name = name_util.to_python_name(syc_name)
    while name in keyword.kwlist:
        name = name + "_"
    return name


class Base:
    """
    Base class for settings and command objects.


    Attributes
    ----------
    sycproxy
    obj_name
    syc_name

    """

    _initialized = False

    def __init__(self, name: str = None, parent=None):
        """Initializes an instance of the Base class.

        Parameters
        ----------
        name : str
            name of the object if a child of named-object.
        parent: Base
            Object's parent.
        """
        self._parent = weakref.proxy(parent) if parent is not None else None
        if name is not None:
            self._name = name

    _sycproxy = None

    @classmethod
    def set_sycproxy(cls, sycproxy):
        """Set sycproxy object."""
        cls._sycproxy = sycproxy

    @property
    def sycproxy(self):
        """Proxy object.

        This is set at the root level, and accessed via parent for child
        classes.
        """
        if self._sycproxy is None:
            return self._parent.sycproxy
        return self._sycproxy

    _name = None
    syc_name = None
    _syc_pathsep = "/"

    @property
    def obj_name(self) -> str:
        """SystemCoupling name of this object.

        By default, this returns the object's static name. If the object is a
        named-object child, the object's name is returned.
        """
        if self._name is None:
            return self.syc_name
        return self._name

    @property
    def path(self) -> str:
        """Path of this object.

        Constructed from obj_name of self and path of parent.
        """
        if self._parent is None:
            return self.obj_name
        ppath = self._parent.path
        if not ppath:
            return self.obj_name
        return ppath + "/" + self.obj_name

    @property
    def syc_path(self) -> str:
        """Path of this object in native SystemCoupling form."""
        if self._parent is None:
            return "/" + self.syc_name
        ppath = self._parent.syc_path
        return ppath + self._parent._syc_pathsep + self.obj_name


StateT = TypeVar("StateT")


class SettingsBase(Base, Generic[StateT]):
    """
    Base class for settings objects.

    Methods
    -------
    get_state()
        Return the current state of the object

    set_state(state)
        Set the state of the object
    """

    @classmethod
    def to_syc_keys(cls, value: StateT) -> StateT:
        """Convert value to have keys with native System Coupling names.

        This is overridden in ``Container`` and ``NamedContainer`` classes.
        """
        return value

    @classmethod
    def to_python_keys(cls, value: StateT) -> StateT:
        """Convert value to have keys with python names.

        This is overridden in ``Container`` and ``NamedContainer`` classes.
        """
        return value

    @classmethod
    def to_syc_name(cls, name: str) -> str:
        """Convert Python name native System Coupling identifier.

        This is overridden in ``Container`` and ``NamedContainer`` classes.
        """
        return name

    @classmethod
    def to_python_name(cls, name: str) -> str:
        """Convert native System Coupling identifier to Python name.

        This is overridden in ``Container`` and ``NamedContainer`` classes.
        """
        return name

    def __call__(self) -> StateT:
        """Alias for self.get_state."""
        return self.get_state()

    def get_state(self) -> StateT:
        """Get the state of this object."""
        return self.to_python_keys(self.sycproxy.get_state(self.syc_path))

    def set_state(self, state: StateT):
        """Set the state of this object."""
        return self.sycproxy.set_state(self.syc_path, self.to_syc_keys(state))

    def set_property_state(self, prop, value):
        """Set the state of the property ``prop`` to ``value``."""
        self.set_state({prop: value})

    def get_property_state(self, prop):
        """Get the state of the property ``prop``."""
        return self.sycproxy.get_state(self.syc_path + "/" + self.to_syc_name(prop))

    @staticmethod
    def _print_state_helper(state, out, indent=0, indent_factor=2):
        if isinstance(state, dict):
            out.write("\n")
            for key, value in state.items():
                if True:  # value is not None:
                    out.write(f'{indent*indent_factor*" "}{key} :')
                    SettingsBase._print_state_helper(
                        value, out, indent + 1, indent_factor
                    )
        elif isinstance(state, list):
            out.write("\n")
            for index, value in enumerate(state):
                out.write(f'{indent*indent_factor*" "}{index} :')
                SettingsBase._print_state_helper(value, out, indent + 1, indent_factor)
        elif state is None:
            out.write(" <None>\n")
        else:
            out.write(f" {state}\n")

    def print_state(self, out=None, indent_factor=2):
        """Print the state of this object."""
        out = sys.stdout if out is None else out
        self._print_state_helper(self.get_state(), out, indent_factor=indent_factor)
        out.flush()


class Integer(SettingsBase[int]):
    """An Integer object represents an integer value setting."""

    _state_type = int


class Real(SettingsBase[RealType]):
    """A Real object represents a real value setting.

    Some Real objects also accept string arguments representing expression
    values.
    """

    _state_type = RealType


class String(SettingsBase[str]):
    """A String object represents a string value setting."""

    _state_type = str


class Filename(SettingsBase[str]):
    """A Filename object represents a file name."""

    _state_type = str


class Boolean(SettingsBase[bool]):
    """A Boolean object represents a boolean value setting."""

    _state_type = bool


class RealList(SettingsBase[RealListType]):
    """A RealList object represents a real list setting."""

    _state_type = RealListType


class IntegerList(SettingsBase[IntListType]):
    """An Integer object represents a integer list setting."""

    _state_type = IntListType


class RealVector(SettingsBase[RealVectorType]):
    """An object to represent a 3D vector.

    A RealVector object represents a real vector setting consisting of
    3 real values.
    """

    _state_type = RealVectorType


class StringList(SettingsBase[StringListType]):
    """A StringList object represents a string list setting."""

    _state_type = StringListType


class BooleanList(SettingsBase[BoolListType]):
    """A BooleanList object represents a boolean list setting."""

    _state_type = BoolListType


class StrFloatPairList(SettingsBase[StrFloatPairListType]):
    """A StrFloatPairList object represents a list of string-float pairs."""

    _state_type = StrFloatPairListType


class StrOrIntDictList(SettingsBase[StrOrIntDictListType]):
    """A StrOrIntDictList object represents a list of simple dictionary values
    with string keys and string or int values."""

    _state_type = StrOrIntDictListType


class StrOrIntDictListDict(SettingsBase[StrOrIntDictListDictType]):
    """A StrOrIntDictListDict object represents a dictionary of string keys to
    StrOrIntDictList values."""

    _state_type = StrOrIntDictListDictType


class Container(SettingsBase[DictStateType]):
    """Container object for primitive values and other settings objects.

    A ``Container`` may contain child objects which are further objects of
    type ``Container``, objects of type ``NamedContainer``, or various
    types of 'command' object. Child objects are accessed as attributes.

    Concrete instances of ``Container`` will usually provide access to
    primitive settings (e.g., real, string values, etc.) as Python properties.

    Note: the attributes listed below are mainly for implementation purposes.

    Attributes
    ----------
    child_names: list[str]
        Names of the child objects
    command_names: list[str]
        Names of the commands
    property_names_types: List[Tuple[str, str, str]]
        List of tuples, each comprising property name, System Coupling property name,
        type identifier.
    """

    _state_type = DictStateType

    def __init__(self, name: str = None, parent=None):
        """Initializes an instance of the ``Container`` class.

        Parameters
        ----------
        name : str
            name of the object if a child of named-object.
        parent: Base
            Object's parent.
        """
        super().__init__(name, parent)
        for child in self.child_names:
            cls = getattr(self.__class__, child)
            setattr(self, child, cls(None, self))
        for cmd in self.command_names:
            cls = getattr(self.__class__, cmd)
            setattr(self, cmd, cls(None, self))
        self._initialized = True

    @classmethod
    def to_syc_keys(cls, value):
        """Convert value to have keys with System Coupling names."""
        if isinstance(value, collections.abc.Mapping):
            ret = {}
            for k, v in value.items():
                if k in cls.child_names:
                    ccls = getattr(cls, k)
                    ret[ccls.syc_name] = ccls.to_syc_keys(v)
                else:
                    ret[cls.to_syc_name(k)] = v
            return ret
        else:
            return value

    @classmethod
    def _syc_to_py_childmap(cls):
        if not hasattr(cls, "__s2p_childmap"):
            cls.__s2p_childmap = {}
            for pyname in cls.child_names:
                ccls = getattr(cls, pyname)
                cls.__s2p_childmap[ccls.syc_name] = pyname
        return cls.__s2p_childmap

    @classmethod
    def _syc_to_py_propertymap(cls):
        if not hasattr(cls, "__s2p_propertymap"):
            cls.__s2p_propertymap = {
                sycname: pyname for pyname, sycname, _ in cls.property_names_types
            }
        return cls.__s2p_propertymap

    @classmethod
    def to_python_keys(cls, value):
        """Convert value to have keys with python names."""
        if isinstance(value, collections.abc.Mapping):
            # get_state and print_state rely on the value returned from here
            # so we impose the correct datamodel ordering when we build the
            # value. The code below should NOT be simplified unless this is
            # understood! Note that we depend on dict preserving insertion order.

            ret = {}
            # Properties first...
            for pyname, sycname, _ in cls.property_names_types:
                # NB: don't use dict.get() here as we want to preserve
                # any items that are present but unset (None).
                if sycname in value:
                    ret[pyname] = value[sycname]

            # Then children...
            cmap = cls._syc_to_py_childmap()
            for sycname, pyname in cmap.items():
                # NB: we are relying on cmap having been initialised with
                # correct child order here!
                v = value.get(sycname, None)
                if v is not None:
                    ret[pyname] = getattr(cls, pyname).to_python_keys(v)
            return ret
        else:
            return value

    @classmethod
    def to_syc_name(cls, name: str) -> str:
        """Convert Python property name to native System Coupling name.

        This is overridden in ``Container`` and ``NamedContainer`` classes.
        """
        for prop, sycprop, _ in cls.property_names_types:
            if prop == name:
                return sycprop
        raise RuntimeError(f"Key '{name}' is invalid")

    @classmethod
    def to_python_name(cls, name: str) -> str:
        """Convert native System Coupling property name to Python name.

        This is overridden in ``Container`` and ``NamedContainer`` classes.
        """
        return cls._syc_to_py_propertymap()[name]

    child_names = []
    command_names = []
    property_names_types = []

    def get_property_options(self, name: str) -> StringList:
        """Returns the currently available options for the specified property name.

        This function is applicable as follows:

        - May only be called for `String` and `StringList` properties; an
          exception will be thrown otherwise.

        - Should only be called for properties that are known currently to be
          active in the data model. This requirement is not yet enforced or validated
          but, if it is violated, the content of any value returned is unspecified.

        - Should only be called for properties that are known to be constrained
          to a certain list of allowed values. An empty list is returned in other
          cases.
        """
        syc_prop_name, prop_type = self._get_property_name_type(name, self.path)
        if prop_type not in ("str", "StringListType"):
            raise RuntimeError(
                f"Options are not available for non-string type '{name}'."
            )
        return self.sycproxy.get_property_options(self.syc_path, syc_prop_name)

    def __getattribute__(self, name):
        # No "is_active" checks for now.
        # if name in super().__getattribute__("child_names"):
        #     if not self.is_active():
        #         raise RuntimeError(f"'{self.path}' is currently not active")
        return super().__getattribute__(name)

    def __setattr__(self, name: str, value):
        if not self._initialized or name[0] == "_":
            super().__setattr__(name, value)
        elif any(name == n for n, _, __ in self.property_names_types):
            super().__setattr__(name, value)
        else:
            attr = getattr(self, name)
            attr.set_state(value)

    @classmethod
    def _get_property_name_type(cls, name, path):
        for pname, syc_name, prop_type in cls.property_names_types:
            if pname == name:
                return (syc_name, prop_type)
        raise RuntimeError(f"'{name}' does not exist in '{path}'.")


ChildTypeT = TypeVar("ChildTypeT")


class NamedContainer(SettingsBase[DictStateType], Generic[ChildTypeT]):
    """A container for named instances of ``Container`` objects.

    A ``NamedContainer`` is a container object, similar to a Python dict object.
    Generally, many such objects can be created with different names.

    Attributes
    ----------
    command_names: list[str]
                   Names of the commands
    """

    _syc_pathsep = ":"

    # New objects could get inserted by other operations, so we cannot assume
    # that the local cache in self._objects is always up-to-date
    def __init__(self, name: str = None, parent=None):
        """Initializes an instance of the ``NamedContainer`` class.

        Parameters
        ----------
        name : str
            name of the object if a child of named-object.
        parent: Base
            Object's parent.
        """
        super().__init__(name, parent)
        self._objects = {}
        for cmd in self.command_names:
            cls = getattr(self.__class__, cmd)
            setattr(self, cmd, cls(None, self))

    @classmethod
    def to_syc_keys(cls, value):
        """Convert value to have keys with the native System Coupling names."""
        if isinstance(value, collections.abc.Mapping):
            ret = {}
            for k, v in value.items():
                ret[k] = cls.child_object_type.to_syc_keys(v)
            return ret
        else:
            return value

    @classmethod
    def to_python_keys(cls, value):
        """Convert value to have keys with PySystemCoupling names."""
        if isinstance(value, collections.abc.Mapping):
            ret = {}
            for k, v in value.items():
                ret[k] = cls.child_object_type.to_python_keys(v)
            return ret
        else:
            return value

    command_names = []

    def _create_child_object(self, cname: str):
        ret = self._objects.get(cname)
        if not ret:
            # pylint: disable=no-member
            cls = self.__class__.child_object_type
            ret = self._objects[cname] = cls(cname, self)
        return ret

    def _update_objects(self):
        names = self.get_object_names()
        for name in list(self._objects.keys()):
            if name not in names:
                del self._objects[name]
        for name in names:
            if name not in self._objects:
                self._create_child_object(name)

    def __delitem__(self, name: str):
        self.sycproxy.delete(f"{self.syc_path}:{name}")
        if name in self._objects:
            del self._objects[name]

    def __contains__(self, name: str):
        return name in self.get_object_names()

    def __len__(self):
        return len(self.keys())

    def __iter__(self):
        self._update_objects()
        return iter(self._objects)

    def keys(self):
        """Object names."""
        self._update_objects()
        return self._objects.keys()

    def values(self):
        """Object values."""
        self._update_objects()
        return self._objects.values()

    def items(self):
        """Items."""
        self._update_objects()
        return self._objects.items()

    def create(self, name: str):
        """Create a named object with given name.

        Parameters
        ----------
        name: str
              Name of new object

        Returns
        -------
        The object that has been created
        """
        self.sycproxy.create_named_object(self.syc_path, name)
        return self._create_child_object(name)

    def get_object_names(self):
        """Object names."""
        return self.sycproxy.get_object_names(self.syc_path)

    def __getitem__(self, name: str) -> ChildTypeT:
        if name not in self.get_object_names():
            raise KeyError(name)
        obj = self._objects.get(name)
        if not obj:
            obj = self._create_child_object(name)
        return obj

    def __setitem__(self, name: str, value):
        if name not in self.get_object_names():
            self.sycproxy.create_named_object(self.syc_path, name)
        child = self._objects.get(name)
        if not child:
            child = self._create_child_object(name)
        child.set_state(value)


class Command(Base):
    """Command object."""

    _is_path_cmd = False

    def __call__(self, **kwds):
        """Call a command with the specified keyword arguments."""
        newkwds = {}
        if self._is_path_cmd:
            newkwds["ObjectPath"] = self._parent.syc_path

        try:
            missing_args = set(self.essential_arguments)
            if self._is_path_cmd:
                missing_args.discard("object_path")
        except AttributeError:
            missing_args = set()

        for k, v in kwds.items():
            if k in self.argument_names:
                ccls = getattr(self, k)
                newkwds[ccls.syc_name] = ccls.to_syc_keys(v)
                missing_args.discard(k)
            else:
                raise RuntimeError("Argument '" + str(k) + "' is invalid")

        if missing_args:
            raise RuntimeError(
                "At least one essential argument has not been provided.\n"
                f"(Missing: {list(missing_args)})."
            )

        return self.sycproxy.execute_cmd(self._parent.path, self.obj_name, **newkwds)


class InjectedCommand(Base):
    """Call a locally defined function that has been injected into the
    generated API hierarchy to appear alongside the generic commands.

    This can also be used to override an existing API command with a local
    version. In this case the ``syc_name`` will refer to the remote
    System Coupling command name. If the command is not an override the
    ``syc_name`` will be the same as the local function name.

    In all cases, the ``cmd_name`` attribute, that is specific to this class
    will be set and this will be the definitive name to call on the
    proxy interface.

    Attributes
    ----------
    cmd_name
    """

    cmd_name = None

    def __call__(self, **kwds):
        """Call a command with the specified keyword arguments.

        Note that this is a straight "pass-through" call to execute the command
        on the proxy. No argument processing is done as in the ``Command`` case
        because we can make no assumptions about the local function.
        """
        return self.sycproxy.execute_injected_cmd(
            self._parent.path, self.cmd_name, **kwds
        )


class PathCommand(Command):
    """Path-based command object."""

    _is_path_cmd = True
