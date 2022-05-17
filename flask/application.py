from website import create_app
def isMain():
    return __name__ == "__main__"

application = create_app()

if isMain():
    application.run(port=4998, debug=True)