"""
Dunder methods:

__init__
__str__
__repr__
__dict__
__call__
__dir__
__bool__
__float__

__len__
__getitem__
w

__add__
__sub__
__mul__
__truediv__
__pow__

all of them with like: __iadd__
"""

"""
Object Initialization and Representation
    __init__(self, ...): Object constructor, called when a new instance is created.
    __new__(cls, ...): Responsible for creating a new instance. Called before __init__.
    __del__(self): Object destructor, called when an object is about to be destroyed.
    __repr__(self): Provides an "official" string representation of the object.
    __str__(self): Provides a "nice" string representation of the object.
    __bytes__(self): Converts the object to a byte string.
    __format__(self, format_spec): Defines how an object is formatted using format() or f-strings.

Attribute Access
    __getattr__(self, name): Called when an attribute is not found in the usual places.
    __getattribute__(self, name): Called unconditionally to access an attribute.
    __setattr__(self, name, value): Called when an attribute assignment is attempted.
    __delattr__(self, name): Called when an attribute deletion is attempted.

Container Emulation
    __len__(self): Returns the length of the container.
    __getitem__(self, key): Retrieves an item from the container.
    __setitem__(self, key, value): Sets an item in the container.
    __delitem__(self, key): Deletes an item from the container.
    __iter__(self): Returns an iterator object.
    __next__(self): Returns the next item from the iterator.
    __reversed__(self): Returns a reverse iterator.
    __contains__(self, item): Checks if an item is in the container.

Numeric Operations
    __add__(self, other): Addition (+).
    __sub__(self, other): Subtraction (-).
    __mul__(self, other): Multiplication (*).
    __matmul__(self, other): Matrix multiplication (@).
    __truediv__(self, other): True division (/).
    __floordiv__(self, other): Floor division (//).
    __mod__(self, other): Modulus (%).
    __divmod__(self, other): Divmod (divmod()).
    __pow__(self, other[, mod]): Exponentiation (** or pow()).
    __lshift__(self, other): Left bitwise shift (<<).
    __rshift__(self, other): Right bitwise shift (>>).
    __and__(self, other): Bitwise AND (&).
    __xor__(self, other): Bitwise XOR (^).
    __or__(self, other): Bitwise OR (|).

Reflected (Reversed) Numeric Operations
    __radd__(self, other): Addition (+).
    __rsub__(self, other): Subtraction (-).
    __rmul__(self, other): Multiplication (*).
    __rmatmul__(self, other): Matrix multiplication (@).
    __rtruediv__(self, other): True division (/).
    __rfloordiv__(self, other): Floor division (//).
    __rmod__(self, other): Modulus (%).
    __rdivmod__(self, other): Divmod (divmod()).
    __rpow__(self, other[, mod]): Exponentiation (** or pow()).
    __rlshift__(self, other): Left bitwise shift (<<).
    __rrshift__(self, other): Right bitwise shift (>>).
    __rand__(self, other): Bitwise AND (&).
    __rxor__(self, other): Bitwise XOR (^).
    __ror__(self, other): Bitwise OR (|).

In-Place Numeric Operations
    __iadd__(self, other): In-place addition (+=).
    __isub__(self, other): In-place subtraction (-=).
    __imul__(self, other): In-place multiplication (*=).
    __imatmul__(self, other): In-place matrix multiplication (@=).
    __itruediv__(self, other): In-place true division (/=).
    __ifloordiv__(self, other): In-place floor division (//=).
    __imod__(self, other): In-place modulus (%=).
    __ipow__(self, other[, mod]): In-place exponentiation (**= or pow()).
    __ilshift__(self, other): In-place left bitwise shift (<<=).
    __irshift__(self, other): In-place right bitwise shift (>>=).
    __iand__(self, other): In-place bitwise AND (&=).
    __ixor__(self, other): In-place bitwise XOR (^=).
    __ior__(self, other): In-place bitwise OR (|=).

Unary Operations
    __neg__(self): Negation (-self).
    __pos__(self): Unary plus (+self).
    __abs__(self): Absolute value (abs(self)).
    __invert__(self): Bitwise inversion (~self).

Type Conversion
    __complex__(self): Conversion to complex (complex(self)).
    __int__(self): Conversion to int (int(self)).
    __float__(self): Conversion to float (float(self)).
    __bool__(self): Conversion to bool (bool(self)).
    __index__(self): Conversion to an integer for slicing (self[1:2:3]).

Comparison Operations
    __lt__(self, other): Less than (<).
    __le__(self, other): Less than or equal to (<=).
    __eq__(self, other): Equal to (==).
    __ne__(self, other): Not equal to (!=).
    __gt__(self, other): Greater than (>).
    __ge__(self, other): Greater than or equal to (>=).

Context Management
    __enter__(self): Called when entering a with statement.
    __exit__(self, exc_type, exc_value, traceback): Called when exiting a with statement.

Callable Objects
    __call__(self, ...): Called when the object is called as a function.

Descriptor Protocol
    __get__(self, instance, owner): Defines behavior for when an attribute is accessed.
    __set__(self, instance, value): Defines behavior for when an attribute is set.
    __delete__(self, instance): Defines behavior for when an attribute is deleted.

Pickling
    __getstate__(self): Returns the state of the object for pickling.
    __setstate__(self, state): Restores the state of the object from the pickle.
"""

