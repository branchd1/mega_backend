from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.urls import reverse

from core.models import Feature

from developer.forms import FeatureForm


# Create your views here.


@login_required
def index(request):
    """
    Home page view for developers

    Parameters
    ----------
    request

    Returns
    -------
    object
        Http response object

    """
    _features = request.user.features.all()

    ctx = {
        'features': _features
    }

    return render(request, 'developer/index.html', ctx)


@login_required
def feature_details(request, feature_id):
    """
    Feature details page

    Parameters
    ----------
    request
    feature_id : int
        The id of the feature

    Returns
    -------
    object
        Http response object

    """
    try:
        _feature = Feature.objects.get(pk=feature_id)
    except Feature.DoesNotExist:
        return redirect('developer:index')

    ctx = {
        'feature': _feature
    }

    return render(request, 'developer/feature_details.html', ctx)


@login_required
def add_feature(request):
    """
    Add feature

    Parameters
    ----------
    request

    Returns
    -------
    object
        Http response object
    """
    _feature_form = None

    if request.method == 'POST':
        _feature_form = FeatureForm(data=request.POST, files=request.FILES)

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
    """
    Edit feature

    Parameters
    ----------
    request
    feature_id : int
        The id of the feature

    Returns
    -------
    object
        Http response object
    """
    try:
        _feature = Feature.objects.get(pk=feature_id)
    except Feature.DoesNotExist:
        return redirect('developer:index')

    _feature_form = None

    if request.method == 'POST':
        _feature_form = FeatureForm(data=request.POST, files=request.FILES, instance=_feature)

        if _feature_form.is_valid():
            _feature = _feature_form.save()
            return redirect(reverse('developer:feature_details', kwargs={'feature_id': _feature.id}))
    else:
        _feature_form = FeatureForm(instance=_feature)

    ctx = {
        'form': _feature_form
    }

    return render(request, 'developer/edit_feature.html', ctx)


@login_required
def delete_feature(request, feature_id):
    """
    Delete feature

    Parameters
    ----------
    request
    feature_id : int
        The id of the feature

    Returns
    -------
    object
        Http response object
    """

    try:
        _feature = Feature.objects.get(pk=feature_id)
    except Feature.DoesNotExist:
        return redirect('developer:index')
    _feature.delete()
    return redirect(reverse('developer:index'))
