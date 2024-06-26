from django.shortcuts import render
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, entry):
    item = util.get_entry(entry)
    content = markdown2.markdown(item)
    return render(request, "encyclopedia/wiki.html", {
        "entry": entry,
        "content": content
    })


