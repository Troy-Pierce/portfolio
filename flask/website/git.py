import datetime
class github:
    _repositories = []
    _expiresAt = datetime.datetime.utcnow()

    def __init__(self):
        self.refreshRepositories()
        self.refreshThread = None
        
        
    
    @classmethod
    def getRepositories(cls):
        return cls._repositories
    
    def refreshRepositories(self):
        repos = []
        import requests
        with requests.get('https://api.github.com/users/Troy-Pierce/repos') as req:
            if req.status_code == 200:
                for x in req.json():
                    if not x['private']:
                        repo = {
                            'name': x['full_name'],
                            'url': x['html_url'],
                            'description': x['description'],
                            'languages': []
                        }
                        with requests.get(f'https://api.github.com/repos/{repo.get("name")}/languages') as rdetail:
                            if rdetail.status_code == 200:
                                languages = []
                                for key in rdetail.json():
                                    languages.append(key)
                                if len(languages) > 0:
                                    repo.update({'languages': languages})
                        repos.append(repo)
                self.__class__._expiresAt = datetime.datetime.now()+datetime.timedelta(days=1)
            else:
                self.__class__._expiresAt = datetime.datetime.now()+datetime.timedelta(hours=1)
        self.__class__._repositories = repos
        from threading import Timer
        self.refreshThread = Timer((self.__class__._expiresAt-datetime.datetime.now()).total_seconds(), self.refreshRepositories).start()
        return self.__class__._repositories

        
