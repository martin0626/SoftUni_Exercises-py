def age_assignment(*args, **kwargs):
    result = {}
    for k, v in kwargs.items():
        for name in args:
            if name.startswith(k):
                result[name] = v
    return result


print(age_assignment("Peter", "George", G=26, P=19))
