from django.shortcuts import render, redirect
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

def results(request):
    title = request.GET.get('q', None)
    if util.get_entry(title):
        return redirect('wiki', entry=title)
    entries = util.list_entries()
    return render(request, "encyclopedia/results.html", {
        "items": [i for i in entries if title in i]
    })