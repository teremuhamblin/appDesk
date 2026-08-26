from rest_framework.exceptions import APIException

class AppDeskError(APIException):
    status_code = 400
    default_detail = "Une erreur interne est survenue."
