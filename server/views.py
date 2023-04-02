from django.views import View

# Create your views here.
from server.status import get_user_status, mark_user_online
from server.utilities import success_response


class Status(View):
    def get(self, request, user_id=None):
        return success_response(get_user_status(user_id), response_status=200)

    def put(self, request, user_id=None):
        return success_response(mark_user_online(user_id), response_status=204)

