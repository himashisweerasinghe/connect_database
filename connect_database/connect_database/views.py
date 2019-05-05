from django.shortcuts import render
import pyrebase
from django.contrib import auth
config = {
    'apiKey': "AIzaSyADhVy78N1ac12IzrhSmaeY10uFmgFaTj4",
    'authDomain': "dinelabs-35998.firebaseapp.com",
    'databaseURL': "https://dinelabs-35998.firebaseio.com",
    'projectId': "dinelabs-35998",
    'storageBucket': "dinelabs-35998.appspot.com",
    'messagingSenderId': "938931808055"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def signIn(request):
    return render(request, "signIn.js")


def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get('password')
    try:
        user = authe.sign_in_with_email_and_password(email,passw)

    except:
        message="Invalid Credentials"
        return render(request,"signIn.js",{"messg":message})
    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request, "welcome.js",{"e":email})

def logout(request):
    auth.logout(request)
    return render(request, 'signIn.js')

def signUp(request):
    return render(request,'signUp.js')

def postsignup(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    passw=request.POST.get('password')

    user=authe.create_user_with_email_and_password(email,passw)

def order(request):

    details = database.child('dinelabs-35998').child('0').child('price').shallow().get().val()
    print(details)

    return render(request,'order.js')