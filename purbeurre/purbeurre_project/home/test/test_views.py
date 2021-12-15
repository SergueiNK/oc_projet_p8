from home import views

# On utilise django test avec rf qui va simuler une requete
# rf c'est la request factory(une fabrique à requete)
def test_home_works_correctly(rf):
    # On simule une requete http
    request = rf.get('/path/to/home')
    response = views.home(request)
    # permet de tester la condition et d'énclencher une erreur immediatement si la réponse est fausse
    assert response.status_code == 200
    