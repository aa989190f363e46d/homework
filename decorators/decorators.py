"""
1. Напишите параметрический декоратор, который вызывает оборачиваемую функцию
несколько раз (по умолчанию - 2).

Предусмотрите возможность продолжать повторные вызовы декорируемой функции
при возникновении в ней исключения, в таких случаях выводите сообщения об
ошибке для каждого вызова. Используйте для этого именованный аргумент
continue_on_errors со значением по умолчанию False.


2. Напишите параметрический декоратор, который проверяет количество и типы
позиционных аргументов оборачиваемой функции.

В случае любого несоответствия необходимо сгенерировать исключение TypeError.
"""
from functools import wraps


def type_check(*types):
    def checker_wrapper(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            nonlocal types  # noqa: WPS420
            if len(args) != len(types):
                raise TypeError(
                    f'Wrong arguments count: need {len(types)} but get {len(args)}',
                    )
            err_msgs = []
            for idx, (arg, checked_type) in enumerate(zip(args, types)):
                if not isinstance(arg, checked_type):
                    err_msgs.append(
                        f'arg {idx} need {checked_type} but get {type(arg)}',
                        )
            if err_msgs:
                raise TypeError(
                    f'Wrong arguments types: {";".join(err_msgs)}'
                    )
            return func(*args, **kwargs)
        return wrapped
    return checker_wrapper


def repeat(repeats=2, continue_on_errors=False):
    def repeats_wrapper(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            nonlocal repeats
            nonlocal continue_on_errors
            rep_count = repeats
            while rep_count > 0:
                rep_count -= 1
                try:
                    _ = func(*args, **kwargs)
                except Exception as e:
                    if not continue_on_errors:
                        break
                    continue
        return wrapped
    return repeats_wrapper
