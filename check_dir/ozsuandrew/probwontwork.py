def fantasy():

    import nflgame

    x=int(input("What year?: "))
    y=int(input("What week?: "))
    z=int(input("How many players?: "))
    print()
    if x>=2009:
        if x<2020:
            if y>0:
                if y<=17:
                    games = nflgame.games(x, week=y)
                    players = nflgame.combine_game_stats(games)

                    for p in players.rushing().sort('rushing_yds').limit(z):
                        msg = '{}: {} carries for {} yards and {} TDs'
                        print( msg.format(p, p.rushing_att, p.rushing_yds, p.rushing_tds))

                    print()

                    for p in players.passing().sort('passing_yds').limit(z):
                        msg = '{}: {} passes for {} yards and {} TDs'
                        print( msg.format(p, p.passing_att, p.passing_yds, p.passing_tds))

                    print()

                    for p in players.receiving().sort('receiving_yds').limit(z):
                        msg = '{}: {} receptions for {} yards and {} TDs'
                        print( msg.format(p, p.receiving_rec, p.receiving_yds, p.receiving_tds))

                    print()

                    for p in players.kicking().sort('kicking_fgm').limit(z):
                        msg = '{}: {} out of {} field goals made'
                        print( msg.format(p, p.kicking_fgm, p.kicking_fga))
                else:
                    print("Invalid input")
            else:
                print("Invalid input")
        else:
            print("Invalid input")

    else:
        print("Invalid input")
    





   
