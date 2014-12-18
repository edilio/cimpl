from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {
        # 'settings': settings,
        # 'applications': json.dumps(apps),
        # 'urls': json.dumps(urls),
        # 'organization': json.dumps(request.session.get('real_user:organization', {})),
        }
    )
