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

def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if (not util.get_entry(title)):
            util.save_entry(title, request.POST.get('content'))
            return redirect('wiki', entry=title)
        else: 
            return render(request, "encyclopedia/new.html", {
                "error": "Entry already exists, try another title"
            })
    return render(request, "encyclopedia/new.html")
