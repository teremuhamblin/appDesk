from rest_framework.views import APIView
from rest_framework.response import Response
from plugins.kernel import kernel
from plugins.marketplace.installer import install_from_zip
from plugins.registry import registry

class PluginList(APIView):
    def get(self, request):
        plugins = [
            {"name": p.name, "version": p.version, "description": p.description}
            for p in registry.all()
        ]
        return Response(plugins)


class PluginRun(APIView):
    def post(self, request, name):
        result = kernel.run_plugin(name, data=request.data)
        return Response(result)


class PluginInstall(APIView):
    def post(self, request):
        url = request.data.get("url")
        result = install_from_zip(url)
        return Response(result)
