from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def home(request):
    """
    receives a POST request and return the result
    """
    result = 'está funcionando'
    return Response({'result': f'{result}'})
