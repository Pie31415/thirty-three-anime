from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse


from .services import get_search


def anime_view(request):
    # context = {
    #     'aniresults': get_search,
    # }
    title_param = request.GET.get('q')

    anime_results = []
    if title_param:
        anime_results = get_search(title_param)

    ctx = {
        "aniresults": anime_results
    }

    if request.is_ajax():
        html = render_to_string(
            template_name='recsys/results.html',
            context=ctx
        )
        data = {"html_view": html}
        return JsonResponse(data, safe=False)

    return render(request, 'recsys/search.html', context=ctx)