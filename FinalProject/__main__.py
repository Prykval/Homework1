from Bot import AddBot, ExitBot, SearchBot, EditBot, RemoveBot, SaveBot, LoadBot, CongratulateBot, ViewBot


if __name__ == "__main__":
    app.run(debug=Fulse, host='0.0.0.0')
    choice = {
        "add": AddBot,
        "search": SearchBot,
        "edit": EditBot,
        "remove": RemoveBot,
        "save": SaveBot,
        "load": LoadBot,
        "congratulate": CongratulateBot,
        "view": ViewBot,
        "exit": ExitBot
    }

    action = input("Choose an action: ")

    while True:
        if action in choice:
            choice[action].handle()
        else:
            print("Incorrect action!")