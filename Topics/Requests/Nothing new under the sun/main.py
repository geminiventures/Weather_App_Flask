def database_manipulator():
    if request.method == 'DELETE':
        return "Deleted"
    elif request.method == 'PUT':
        return "Updated"
    return None