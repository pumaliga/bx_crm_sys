from app.auth import auth


@auth.route('login/', methods=['GET', 'POST'])
def login():
    return 'Login'

@auth.route('/signup')
def signup():
    return 'Signup'

@auth.route('/logout')
def logout():
    return 'Logout'


