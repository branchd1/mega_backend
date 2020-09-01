from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.urls import reverse

from core.models import Feature

from developer.forms import FeatureForm


# Create your views here.


@login_required
def index(request):
    """ home page for developers """
    _features = request.user.features.all()

    ctx = {
        'features': _features
    }

    return render(request, 'developer/index.html', ctx)


@login_required
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


@login_required
def add_feature(request):
    """ add feature """
    _feature_form = None

    if request.method == 'POST':
        _feature_form = FeatureForm(request.POST)

        if _feature_form.is_valid():
            _feature = _feature_form.save(commit=False)
            _feature.user = request.user
            _feature.save()
            return redirect('developer:index')
    else:
        _feature_form = FeatureForm()

    ctx = {
        'form': _feature_form
    }

    return render(request, 'developer/add_feature.html', ctx)


@login_required
def edit_feature(request, feature_id):
    """ edit feature """
    try:
        _feature = Feature.objects.get(pk=feature_id)
    except:
        return redirect('developer:index')

    _feature_form = None

    if request.method == 'POST':
        _feature_form = FeatureForm(request.POST, instance=_feature)

        if _feature_form.is_valid():
            _feature = _feature_form.save()
            return redirect(reverse('developer:feature_details', kwargs={'feature_id': _feature.id}))
    else:
        _feature_form = FeatureForm(instance=_feature)

    ctx = {
        'form': _feature_form
    }

    return render(request, 'developer/edit_feature.html', ctx)
