# An assertion is a sanity-check that you can turn on or turn off when you have finished testing the program.
# An expression is tested, and if the result comes up false, an exception is raised.
# Assertions are carried out through use of the assert statement.

# Утверждение - это проверка правильности кода, её можно включить или выключить по завершению тестирования программы.
# Выражение проверяется, и если оно ложное, вызывается исключение.
# Утверждение создаётся с помощью инструкции assert.

print(1)
assert 2 + 2 == 4
print(2)
# assert 1 + 1 == 3
# print(3)
assert type(5) == int
print(4)
assert type("aqua") == str
print(5)
assert type(2) == str
print(6)

# Result:
"""
1
2
AssertionError
"""
