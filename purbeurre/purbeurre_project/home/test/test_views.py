from home import views

# On utilise django test avec rf qui va simuler une requete
# rf c'est la request factory
def test_home_works_correctly(rf):
    request = rf.get('/chemin/vers/home')
    response = views.home(request)
    print("tout est ok")