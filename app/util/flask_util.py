from flask import Response, jsonify


def json_response(json_string):
    return Response(json_string, content_type='application/json')


def jsonify_list(lst, list_name, start_point=0):
    return jsonify({
        list_name: lst,
        'scrolling': {
            'start_point': start_point,
            'items': len(lst)
        }
    })
