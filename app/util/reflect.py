def set_attribute_safely(subject, field, value):
    try:
        setattr(subject, field, value)

    except Exception as ex:
        print('An error occurs while trying to set attribute .{}: {}'.format(field, ex))
