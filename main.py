
from flask import Flask
import random
_NUMBER_OF_MODIFIERS_ = 2



app = Flask(__name__)

def roll(max_num_to_roll):
    pick = random.randrange(1,max_num_to_roll)
    return pick


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    output = 'This app is designed to generate a selection of random challenges for different games'
    output += '<br>'
    output += '<b>Challenges</b> can be made up of two separate parts: <b>Challenges</b> and <b>Modifiers</b>. There can be up to 2 <b>Modifiers</b> but there must be 1 <b>Challenges</b>'
    output += '<br>'
    output += '<b>Challenges</b> are problems or restrictions large enough that they have to be dealt with all game or can severly effect gameplay'
    output += '<br>'
    output += '<b>Modifiers</b> are problems or restrictions that arent big on their own or can be ignored for most of the game'
    output += '<br><br>'
    output += 'There are a few games I plan to implement this for, but for now I only have Black ops 2 with Apex legends coming soon'
    output += '<br>'
    output += 'You can access the different games by modifying the URL above and adding one of the games listed in the brackets: [ <a href="https://stratroulette-377821.ue.r.appspot.com/blackops2"> blackops2 </a> ] after the "/" or by clicking one of their links'
    output += '<br>'
    output += 'For example, you would put "https://stratroulette-377821.ue.r.appspot.com/blackops2" in the URL for COD: Black Ops 2'
    return output

@app.route('/apex')
def apex_roulette():
    output = ""
    NumMods = 0
    # Challenge Initialization Section
    chall = [("Put a Sock on it","Your team must play with socks over their hands like gloves")]
    
    
    
    # Modifier Initialization Section
    mods = [("Leg Injury","Your team cannot sprint")]
    
    
    
    # Only 2 Modifiers Allowed
    while NumMods < _NUMBER_OF_MODIFIERS_:
        pick = roll(1,len(chall)+len(mods))
        if pick < len(chall):
            # Pop instead of access to prevent duplicate Modifiers/Challenges
            temp = chall.pop(pick-1)
            output += "<b>Title: </b>"+temp[0] +"<br>"
            output += "<b>Description: </b>"+temp[1] +"<br>"
            return output
        else:
            # Pop instead of access to prevent duplicate Modifiers/Challenges
            temp = mods.pop(pick-len(chall)-1)
            output += "<b>Title: </b>[Modifier] "+temp[0] +"<br>"
            output += "<b>Description: </b>"+temp[1] +"<br>"
            output += "<br>"
            NumMods += 1
    pick = random.randrange(1,len(chall))
    # Pop instead of access to prevent duplicate Modifiers/Challenges
    temp = chall.pop(pick-1)
    output += "<b>Title: </b>"+temp[0] +"<br>"
    output += "<b>Description: </b>"+temp[1] +"<br>"
    return output
    
@app.route('/blackops2')
def black_ops():
    output = ""
    NumMods = 0
    # Challenge Initialization Section
    chall = [("Put a Sock on it","Your team must play with socks over their hands like gloves")]
    chall.append(("Sabotage","The last team that lost gets to change 2 settings for each winner without their knowledge"))
    chall.append(("Wild West","Your team cannot Aim Down Sights and must hipfire or melee only"))
    chall.append(("Oh, like chatGPT!", "Add a veteran bot to the opposing team, if any member of your team ends the game with fewer kills than the bot, they must take a shot"))
    chall.append(("Team Building Exercise", "Every callout or sentence MUST include a compliment to your teammate. Failure to compliment means you must take a shot or put down your controller"))
    chall.append(("Buck Wild","Shotguns only"))
    chall.append(("Seven Shots, Maybe One Kill", "Snipers only"))
    chall.append(("Runnin Dry","Once you see an enemy, you must start shooting immediately and cannot stop until the mag is empty"))
    chall.append(("Slow & Steady","Someone on your team must use Minimum sensitivity"))
    chall.append(("Fast & Ready", "Someone on your team must use Maximum Sensitivity"))
    chall.append(("Low & Slow", "Your team can only kill people while prone or dolphin diving"))
    chall.append(("Reaction Testing","The opposing team may call out 'Marco' at any time and all members of your team must respond with 'Polo' or else their next kill has to be a melee kill"))
    chall.append(("Gun Game on a Budget","You can only get 1 kill with a weapon before you must swap it for one on the ground or swap loadout if you die"))
    chall.append(("Human Centipede", "All members of your team must remain crouched and touching for the entire game, IRL or ingame"))
    chall.append(("Big game","LMG's only"))
    chall.append(("Speed Kills","You must use a weapon that has the rapid fire attachment equipped"))
    chall.append(("Pick a member of your team to be the VIP, they may only use a pistol and every time they die, you must take a shot or set your controller down for 15 seconds"))
    chall.append(("Quite the view","The opposing team gets to pick where your team stands to play the match. Your portion of the screen must be visible in some way shape or form from where you are standing e.g reflection"))
    chall.append(("Red Light, Green light","Someone who is not playing the game gains the ability to call Red Light and Green Light. Your team must stop moving on a Red light and may only continue on a green light"))
    chall.append(("Primitive Player","One member on your team is only allowed to use special weapons e.g Riot Shield, Rocket Launcher, etc"))
    chall.append(("Let's change it up","Set the gamemode to Kill Confirmed instead of Team Deathmatch"))
    chall.append(("Sharpshooter","Set the Gamemode to Sharpshooter"))
    chall.append(("Localized Chaos","Set the gamemode to Hardpoint"))
    
    
    # Modifier Initialization Section
    mods = [("Leg Injury","Your team cannot sprint")]
    mods.append(("Claim Your Voice","Nobody on your team can speak until they personally have gotten a Melee Kill. ALL Team members take a shot if this rule is violated"))
    mods.append(("I thought we were friends","Every callout or sentence MUST include an insult to your teammate. Failure to insult means you must take a shot or put down your controller for 15 seconds"))
    mods.append(("Fashion Over Form","Your weapon MUST use a sight with a custom and unorothodox dot e.g Smiley Face"))
    mods.append(("Perk 1 famine", "You cannot have anything in perk slot 1"))
    mods.append(("Perk 2 famine", "You cannot have anything in perk slot 2"))
    mods.append(("Perk 3 famine", "You cannot have anything in perk slot 3"))
    mods.append(("The Taj Special","Someone on your team must use Taj's controller"))
    mods.append(("Hypersensitive","Increase your sensitivity by four"))
    mods.append(("Dulled senses","Decrease your sensitivity by two"))
    mods.append(("Compulsive Reloader","You must reload immediately after every kill, failure to do so is a shot or 15 second timeout"))
    mods.append(("Vanilla","No attachements unless specified by a challenge or modifier"))
    mods.append(("Double the Trouble", "Double any punishments from challenges or modifiers"))
    mods.append(("Sore Losers", "If your team loses this game, Your team must take 3 shots collectively, divided however you want"))
    mods.append(("Rags to Riches","Each member of your team must get a kill with a melee THEN a pistol before they may play normally"))
    mods.append(("Dead weight", "The best player on your team must use the Legacy Southpaw controller layout"))
    mods.append(("Heavy is the Head that Wears the Crown","Whoever has the most kills on your team at the end of the game, must take a shot"))
    mods.append(("Sugar Rush","Your team must be moving at all times, standing still for longer than 1s for any reason is a shot"))
    mods.append(("Wasted space","Your loadout must include the maximum amount of tactical and lethal equipment possible"))
    mods.append(("WW1","Your team must use bolt action or semi automatic weapons"))
    mods.append(("Blue on Blue","Enable hardcore mode"))
    mods.append(("Up is Down","All players on your team must invert their look inversion setting"))
    
    
    # Only 2 Modifiers Allowed
    while NumMods < _NUMBER_OF_MODIFIERS_:
        pick = roll(1,len(chall)+len(mods))
        if pick < len(chall):
            # Pop instead of access to prevent duplicate Modifiers/Challenges
            temp = chall.pop(pick-1)
            output += "<b>Title: </b>"+temp[0] +"<br>"
            output += "<b>Description: </b>"+temp[1] +"<br>"
            return output
        else:
            # Pop instead of access to prevent duplicate Modifiers/Challenges
            temp = mods.pop(pick-len(chall)-1)
            output += "<b>Title: </b>[Modifier] "+temp[0] +"<br>"
            output += "<b>Description: </b>"+temp[1] +"<br>"
            output += "<br>"
            NumMods += 1
    pick = random.randrange(1,len(chall))
    # Pop instead of access to prevent duplicate Modifiers/Challenges
    temp = chall.pop(pick-1)
    output += "<b>Title: </b>"+temp[0] +"<br>"
    output += "<b>Description: </b>"+temp[1] +"<br>"
    return output


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
