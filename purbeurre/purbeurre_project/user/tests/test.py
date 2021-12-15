from user import views

def test_user_works_correctly(rf):
    # On simule une requete http
    request = rf.get('/path/to/user')
    response = views.user(request)
    # permet de tester la condition et d'énclencher une erreur immediatement si la réponse est fausse
    assert response.status_code == 200
    
def test_register_user_works_correctly(rf):
    request = rf.get('/path/to/user/register')
    response = views.registerPage(request)
    # permet de tester la condition et d'énclencher une erreur immediatement si la réponse est fausse
    assert response.status_code == 200    

def test_login_user_works_correctly(rf):
    request = rf.get('/path/to/user/login')
    response = views.loginPage(request)
    # permet de tester la condition et d'énclencher une erreur immediatement si la réponse est fausse
    assert response.status_code == 200  