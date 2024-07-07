from django.http import HttpResponse,HttpResponseServerError
import json
from tools import tools
from importlib import import_module


def index(request,module,funci):
    if request.method=="POST":
        all_module_and_func=tools.listing_method("./my_modules")
        print(all_module_and_func)
        if not module in all_module_and_func:
            return HttpResponseServerError("Unknown module NAME")
        if not funci in all_module_and_func[module]:
            return HttpResponseServerError("Unknown function NAME")
        my_json = json.loads(request.body)
        print(my_json)
        print(funci)
        imp_module=import_module(module)
        imp_func=getattr(imp_module,funci)
        sorted_json=imp_func(my_json)
        print(sorted_json)
        return HttpResponse(json.dumps(sorted_json), content_type="application/json")
    else:
        return HttpResponseServerError("недопустимый метод")