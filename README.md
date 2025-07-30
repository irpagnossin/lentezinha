# Lentezinha

A tiny Lens for Python:

```python
user = {"name": "Ana", "profile": {"age": 20}}

from lentezinha import read
read(user, "profile.age")  # == 20

from lentezinha import update
update(user, "profile.age", lambda a: a + 1)  # Updates age to 21
```

You can use a `Lens` instance if you plan to access nested attributes many times:

```python
from lentezinha import Lens
age = Lens("profile.age")

print(age.get(user))  # == 20

age.set(user, lambda a: a + 1)
print(age.get(user))  # == 21

age.set(user, 27)
print(age.get(user))  # == 27
```
