from django.http import JsonResponse


def success_response(response=None, message=None, meta=None, response_status=200):
    if response_status >= 400:
        raise Exception("invalid status code: %d for success response" % response_status)

    final_response = {
        'data': response if response is not None else {},
    }

    if message is not None:
        final_response["message"] = message

    if meta is not None:
        final_response["meta"] = meta

    if isinstance(response, list):
        final_response["count"] = len(response)
    else:
        final_response["count"] = 1

    return JsonResponse(final_response, status=response_status)