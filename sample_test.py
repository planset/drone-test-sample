import sample

def pytest_funcarg__sample(request):
    return sample.Sample()

def test_sample_get_name(sample):
    assert sample.get_name() == 'planset'
