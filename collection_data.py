import requests
import json

ACCESS_TOKEN = "EAAPeqq4WIiQBPsZAShZAnWGJ0tx8sF9q3erm8lZB7lagOcLVKED1paHElmy1RCgn4fgqQHSO3PQQgaufYu30ZCECuYAIYRk7q8huJPyHxX5usfsDYglSvBtWJAvTWoBLQE5yYKr3G5w40jB79AZByWQZAXVqil6WkY4bHfIAoXskA7928w9qclZAV7GpdYVxtgjgPjeA39qFz4DGVJ7uw27jly4x64ZAa7fmeWsoB1USbgZDZD"

def collect_all_facebook_data(access_token):
    """Collecte toutes les données disponibles avec le token"""
    
    print("🔄 Collecte des données en cours...")
    
    # 1. PROFIL DE BASE
    print("📊 Récupération du profil...")
    profile_data = get_basic_profile(access_token)
    
    # 2. PAGES AIMÉES (LIKES)
    print("❤️ Récupération des pages aimées...")
    likes_data = get_user_likes(access_token)
    
    # 3. CENTRES D'INTÉRÊT
    print("🎯 Récupération des centres d'intérêt...")
    interests_data = get_user_interests(access_token)
    
    # 4. ÉVÉNEMENTS
    print("📅 Récupération des événements...")
    events_data = get_user_events(access_token)
    
    # 5. PHOTO DE PROFIL
    print("🖼️ Récupération de la photo de profil...")
    picture_data = get_profile_picture(access_token)
    
    return {
        'profile': profile_data,
        'likes': likes_data,
        'interests': interests_data,
        'events': events_data,
        'picture': picture_data
    }

def get_basic_profile(token):
    """Récupère le profil de base"""
    url = "https://graph.facebook.com/me"
    params = {
        'fields': 'id,name,first_name,last_name,email,gender,age_range',
        'access_token': token
    }
    response = requests.get(url, params=params)
    return response.json()

def get_user_likes(token):
    """Récupère les pages aimées"""
    url = "https://graph.facebook.com/me/likes"
    params = {
        'fields': 'name,category,created_time',
        'limit': 100,
        'access_token': token
    }
    response = requests.get(url, params=params)
    return response.json().get('data', [])

def get_user_interests(token):
    """Récupère les centres d'intérêt"""
    url = "https://graph.facebook.com/me/interests"
    params = {
        'access_token': token,
        'limit': 50
    }
    response = requests.get(url, params=params)
    return response.json().get('data', [])

def get_user_events(token):
    """Récupère les événements"""
    url = "https://graph.facebook.com/me/events"
    params = {
        'fields': 'name,description,start_time',
        'access_token': token,
        'limit': 20
    }
    response = requests.get(url, params=params)
    return response.json().get('data', [])

def get_profile_picture(token):
    """Récupère la photo de profil"""
    url = "https://graph.facebook.com/me/picture"
    params = {
        'redirect': 'false',
        'type': 'large',
        'access_token': token
    }
    response = requests.get(url, params=params)
    return response.json()

# 🎯 EXÉCUTION PRINCIPALE
if __name__ == "__main__":
    try:
        # Collecter toutes les données
        user_data = collect_all_facebook_data(ACCESS_TOKEN)
        
        # Sauvegarder dans un fichier
        with open('user_profile.json', 'w', encoding='utf-8') as f:
            json.dump(user_data, f, ensure_ascii=False, indent=2)
        
        print("\n" + "="*50)
        print("✅ DONNÉES COLLECTÉES AVEC SUCCÈS !")
        print("="*50)
        
        # Afficher un résumé
        profile = user_data['profile']
        print(f"👤 PROFIL UTILISATEUR:")
        print(f"   Nom: {profile.get('name', 'N/A')}")
        print(f"   ID: {profile.get('id', 'N/A')}")
        print(f"   Email: {profile.get('email', 'N/A')}")
        print(f"   Genre: {profile.get('gender', 'N/A')}")
        
        print(f"\n📊 STATISTIQUES:")
        print(f"   ❤️  Pages aimées: {len(user_data['likes'])}")
        print(f"   🎯 Centres d'intérêt: {len(user_data['interests'])}")
        print(f"   📅 Événements: {len(user_data['events'])}")
        
        # Afficher quelques pages aimées
        if user_data['likes']:
            print(f"\n📌 5 PAGES AIMÉES:")
            for i, like in enumerate(user_data['likes'][:5]):
                print(f"   {i+1}. {like['name']} ({like.get('category', 'N/A')})")
        
        print(f"\n💾 Fichier sauvegardé: user_profile.json")
        
    except Exception as e:
        print(f"❌ ERREUR: {e}")
        print("🔧 Vérifiez que le token est valide et a les bonnes permissions")