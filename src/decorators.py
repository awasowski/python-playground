import functools

# == Simple decorator ==
def simple_access_control(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        required_role = 'admin'  # Static specification
        if user.get('role') != required_role:
            raise Exception(f"Unauthorized: This user does not have the {
                            required_role} role.")
        return func(user, *args, **kwargs)
    return wrapper

# Usage
@simple_access_control
def sensitive_function(user, data):
    return f"Sensitive data for {user['name']}"

# This should work
print(sensitive_function({'name': 'admin', 'role': 'admin'}, 'data'))

# This should raise exception
try:
    print(sensitive_function({'name': 'user', 'role': 'user'}, 'data'))
except Exception as e:
    print(e)


# == Parametrized decorator ==
def access_control(required_role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get('role') != required_role:
                raise Exception(f"Unauthorized: This user does not have the {
                                required_role} role.")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@access_control(required_role='admin')
def delete_user(user):
    print(f"User {user['name']} deleted")


# Example Usage
admin_user = {'name': 'Alice', 'role': 'admin'}
regular_user = {'name': 'Bob', 'role': 'user'}

try:
    delete_user(admin_user)  # This should work
except Exception as e:
    print(e)

try:
    delete_user(regular_user)  # This should raise an exception
except Exception as e:
    print(e)
