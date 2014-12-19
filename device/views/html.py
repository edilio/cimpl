from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {
        # 'settings': settings,
        # 'applications': json.dumps(apps),
        # 'urls': json.dumps(urls),
        # 'organization': json.dumps(request.session.get('real_user:organization', {})),
        }
    )


def devices(request):
    return render(request, 'device.html', {})


def account(request):
    return render(request, 'account.html', {})


def angular(request):
    return render(request, 'test_angular.html', {})