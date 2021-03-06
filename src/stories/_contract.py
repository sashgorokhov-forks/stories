from .exceptions import ContextContractError


def validate_arguments(arguments, args, kwargs):
    # FIXME: Should be a method of the `Contract` class.
    assert not (args and kwargs)

    if args:
        assert len(arguments) == len(args)
        return [(k, v) for k, v in zip(arguments, args)]

    assert set(arguments) == set(kwargs)
    return [(k, kwargs[k]) for k in arguments]


class Contract(object):
    def check(self, obj, method, ctx, ns):
        tries_to_override = set(ctx) & set(ns)
        if tries_to_override:
            message = variable_override_template.format(
                variables=", ".join(map(repr, sorted(tries_to_override))),
                cls=obj.__class__.__name__,
                method=method.__name__,
            )
            raise ContextContractError(message)


variable_override_template = """
This variables already present in the context: {variables}

Function returned value: {cls}.{method}

Use different names as Success() arguments.
""".strip()
