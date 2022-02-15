age: int
name: str
height: float
is_human: bool


def police_check(age: int) -> bool:  # age: int is to forecast any errors that are not a int,
    # and -> bool to let python know the next one will be a boolean. Pycharm will show highlights of errors
    # by doing this, Type hints
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(12):
    print("You may pass")
else:
    print("Pay a fine.")