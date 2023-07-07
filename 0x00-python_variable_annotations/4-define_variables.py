#!/usr/bin/env python3

a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"

print(f"a is a {type(a).__name__} with a value of {a}")
print(f"pi is a {type(pi).__name__} with a value of {pi}")
print(f"i_understand_annotation is a {type(i_understand_annotations).__name__}"
      f"with a value of {i_understand_annotations}")
print(f"school is a {type(school).__name__} with a value of {school}")
