# Lentezinha

A tiny Lens for Python:

```python
from lentezinha import Lens
user = {"name": "Ana", "profile": {"age": 20}}
age = Lens("profile.age")

# Getter
print(age.get(user))  # == 20

# Setter
age.set(user, lambda a: a + 1)
print(age.get(user))  # == 21

age.set(user, 27)
print(age.get(user))  # == 27
```

## Bugs

- `Lens.set` with lambda requires **one** parameter: `age.set(lambda _: 10)`
