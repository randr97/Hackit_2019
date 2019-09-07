from dao.user_dao import UserDatabase

class UserJob:

    def __init__(self, name, accountId, avatarUrls, displayName, github_id, **kwargs):
        self.data ={
            "name": name,
            "accountId": accountId,
            "avatarUrls": avatarUrls,
            "displayName": displayName,
            "github_id": github_id,
        }
    
    def save(self):
        user_database = UserDatabase()
        response = user_database.write_user(self.data)
        return response

dhruva_data = {
    "name" : "dhruvapatil98",
    "accountId" : "5d71ffa995fbcc0c341dc287",
    "avatarUrls": {
        "48x48" : "https://secure.gravatar.com/avatar/0b4082963c84d71802886cf59d5aad3e?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FDP-3.png&size=48&s=48",
        "24x24" : "https://secure.gravatar.com/avatar/0b4082963c84d71802886cf59d5aad3e?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FDP-3.png&size=24&s=24",
        "16x16" : "https://secure.gravatar.com/avatar/0b4082963c84d71802886cf59d5aad3e?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FDP-3.png&size=16&s=16",
        "32x32" : "https://secure.gravatar.com/avatar/0b4082963c84d71802886cf59d5aad3e?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FDP-3.png&size=32&s=32",
        },
    "displayName": "Dhruva Patil",
    "github_id": "DhruvaPatil98",
}
rohit_data = {
    "name": "admin",
    "accountId": "5c6e8a3acfbc206be9098219", 
    "avatarUrls": {
        "16x16": "https://secure.gravatar.com/avatar/e41b551f404194c47f1af8e809934243?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FRS-3.png&size=16&s=16", 
        "24x24": "https://secure.gravatar.com/avatar/e41b551f404194c47f1af8e809934243?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FRS-3.png&size=24&s=24", 
        "32x32": "https://secure.gravatar.com/avatar/e41b551f404194c47f1af8e809934243?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FRS-3.png&size=32&s=32", 
        "48x48": "https://secure.gravatar.com/avatar/e41b551f404194c47f1af8e809934243?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FRS-3.png&size=48&s=48"
        }, 
    "displayName": "Rohit Shrothrium", 
    "github_id": "randr97",
}
nausheen_data = {
    "name": "nausheen.sultana0212", 
    "accountId": "5d53d144400d9d0d9f53c55b", 
    "avatarUrls": {
        "16x16": "https://secure.gravatar.com/avatar/1f2ba8b8e5429ce1d4e1c881537ffcc4?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FNS-0.png&size=16&s=16", 
        "24x24": "https://secure.gravatar.com/avatar/1f2ba8b8e5429ce1d4e1c881537ffcc4?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FNS-0.png&size=24&s=24", 
        "32x32": "https://secure.gravatar.com/avatar/1f2ba8b8e5429ce1d4e1c881537ffcc4?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FNS-0.png&size=32&s=32", 
        "48x48": "https://secure.gravatar.com/avatar/1f2ba8b8e5429ce1d4e1c881537ffcc4?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FNS-0.png&size=48&s=48"
        }, 
    "displayName": "Nausheen Sultana", 
    "github_id": "NausheenSultana",
}
UserDatabase().delete_all_users()
UserJob(**dhruva_data).save()
UserJob(**rohit_data).save()
UserJob(**nausheen_data).save()