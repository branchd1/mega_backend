from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from core.models import Feature


# Create your views here.
@login_required
def index(request):
    """ home page for developers """
    _features = request.user.features.all()

    ctx = {
        'features': _features
    }

    return render(request, 'developer/index.html', ctx)


def feature_details(request, feature_id):
    """ feature details page """
    try:
        _feature = Feature.objects.get(pk=feature_id)
    except:
        return redirect('developer:index')

    ctx = {
        'feature': _feature
    }

    return render(request, 'developer/feature_details.html', ctx)


def add_feature(request):
    pass


def edit_feature(request):
    pass
