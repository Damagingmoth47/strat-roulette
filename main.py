
from flask import Flask
import random
_NUMBER_OF_MODIFIERS_ = 2



app = Flask(__name__)

def roll(max_num_to_roll):
    pick = random.randrange(1,max_num_to_roll)
    return pick

def weapon_type():
    weapon_types = ["Heavy","Light","Energy","Shotgun","Sniper"]
    pick = roll(len(weapon_types))
    return weapon_types[pick-1]

def forbidden():
    words = ""
    apex_words = ["Battle","Royale","Bloodhound","Gibraltar","Gibby","Lifeline","Pathfinder","Path","Wraith",
                  "Bangalore","Caustic","Mirage","Octane","Wattson","Crypto","Revenant","Loba","Rampart","Horizon",
                  "Fuse","Valkyrie","Seer","Ash","Maggie","Newcastle","Scan","Ping","Dome","Ult","Barrage","Drone",
                  "Heal","Supply","Drop","Grapple","Zipline","Phase","Portal","Passive","Smoke","Oscar","Mike","Squad",
                  "Enemy","Gas","Trap","Trap","Grenade","Clone","Stim","Jumppad","Fence","EMP","Silence","Totem",
                  "Bracelet","Teleport","Wall","Minigun","Sheila","Lift","Knuckle","Cluster","Jets","Rockets","Drill",
                  "Barrier","Rez","Revive","Lava","Havoc","Flatline","Hemlok","301","Alternator","Prowler","99","Volt",
                  "CAR","Devotion","L-Star","Spitfire","Rampage","G7","Triple","Take","Snake","30-30","Bow","Charge",
                  "Rifle","Longbow","Kraber","Sentinel","Eva","Mastiff","Mozambique","Peacekeeper","RE-45","P2020",
                  "Wingman","Light","Heavy","Energy","Sniper","Shotgun","Ammo","White","Blue","Purple","Gold","Red",
                  "Cracked","Cell","Medkit","Battery","Syringe","One","Fuck","Shit","Damnit"]
    w1 = roll(len(apex_words))
    w2 = roll(len(apex_words))
    w3 = roll(len(apex_words))
    w4 = roll(len(apex_words))
    w5 = roll(len(apex_words))
    words += w1 + ","+w2+","+w3+","+w4+","+w5
    return words


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
    output += 'You can access the different games by modifying the URL above and adding one of the games listed in the brackets: [ <a href="https://stratroulette-377821.ue.r.appspot.com/blackops2"> blackops2 </a> - <a href="https://stratroulette-377821.ue.r.appspot.com/apex"> Apex </a> ] after the "/" or by clicking one of their links'
    output += '<br>'
    output += 'For example, you would put "https://stratroulette-377821.ue.r.appspot.com/blackops2" in the URL for COD: Black Ops 2'
    return output

@app.route('/apex')
def apex_roulette():
    output = ""
    NumMods = 0
    # Challenge Initialization Section
    chall = [("Put a Sock on it","Your team must play with socks over their hands like gloves")]
    chall.append(("Taj's Keeper", "Taj may only use pistols, If he dies then we wipe"))
    chall.append(("Josh's Keeper", "Josh may only use pistols, If he dies then we wipe"))
    chall.append(("Amrinder's Keeper", "Amrinder may only use pistols, If he dies then we wipe"))
    chall.append(("Lord Rep","Only Taj may shoot, we must throw grenades and carry stuff for Taj. If the Lord dies, the serfs are free"))
    chall.append(("Lord Moth","Only Josh may shoot, we must throw grenades and carry stuff for Josh. If the Lord dies, the serfs are free"))
    chall.append(("Lord Gunde","Only Amrinder may shoot, we must throw grenades and carry stuff for Amrinder. If the Lord dies, the serfs are free"))
    chall.append(("Bargain Bin","Only White equipment may be used, anything of a higher rarity must be thrown away, including shields"))
    chall.append(("What's yours is mine"," You may only grab 2 items off the ground, everything else must come from a deathbox"))
    chall.append(("Slow and Steady","You may not use shield cells or syringes"))
    chall.append(("Shroud Special","You must land at the most popular spot and cannot leave until everyone there is dead or gone"))
    chall.append(("Best Part of Me","You can only use weapons that can fit a hopup"))
    chall.append(("Armed and (not) Dangerous","Shotguns and Snipers only"))
    chall.append(("Clean Hands","Someone else must reload your guns"))
    chall.append(("Used Goods","You must drop both guns and look for new ones after killing someone"))
    chall.append(("Taj is gonna hate this","If you CAN do a finisher, you MUST do a finisher"))
    chall.append(("Tower of Babel","Nobody is allowed to speak english, Abandon all your loot if you do"))
    chall.append(("Never Liked you Anyway","Every callout must include an insult, no insult or poor quality insult is a loot wipe"))
    chall.append(("Pray to RNGesus","Pick a weapon type and Loot tier, you may only use that weapon type and loot tier"))
    chall.append(("Illicit Goods","Pick a Lifeline and a Loba, you may only collect loot through their ultimates"))
    chall.append(("Rent and Spent","You may not pick up ammo boxes"))
    chall.append(("On cooldown","You must use your abilities whenever they are available"))
    chall.append(("Reunited and it feels so good","Everyone must land separately, regroup"))
    chall.append(("Misclick!","You must swap your control scheme to the option two below your current"))
    chall.append(("Sneaky Beaky Like","You must pick and follow a squad for the entire game, if they spot you, you must die. If they die, you must abandon all of your loot and take theirs"))
    chall.append(("One hit wonder","You must reload after every shot"))
    chall.append(("Rules of the road","You must walk only on roads, paths and streets. Valk and Pathfinder ults count as paths"))
    chall.append(("Numb Feeling","Set your sensitivity to half its current value"))
    chall.append(("Late to the party","You may only loot once there are 10 or fewer squads left"))
    chall.append(("Red Light, Green Light","You may only move during fights or when the zone is moving"))
    chall.append(("Amrinders bullshit","Can only move during a movement speed buff or via movement abilities"))
    chall.append(("Robbin Hood","Bows only"))
    chall.append(("In Honor of that one Octane","Pick a squad to annoy, your goal is to make sure they stay alive but constantly damage or annoy them while you stay alive. You cannot kill this squad"))
    chall.append(("Forbidden words","?You cannot say 5 randomly selected, apex related words. If you say them, you must drop all of your loot. The words are: "))
    chall.append(("Stalker Pro","You must ADS whenever possible in a fight"))
    chall.append(("Forgot my headset","Turn off all audio in settings"))
    chall.append(("WW1 Simulation","You may only use Semi-automatic or Bolt action weapons that fire bullets (No lasers or energy weapons)"))
    chall.append(("Sharing is Caring","!No Loba's allowed, All players can only use one ammo type, that type is: "))
    chall.append(("We're all friends right?","Every callout must include a compliment, loot reset if you don't"))
    chall.append(("Tag","Jumpmaster is it. Whoever is it may only use Melee or abilities. If whoever is it melees another squadmate, they become it. If the player who is it dies or gets a kill, the player with the lowest damage other than who is it becomes it"))
    chall.append(("Broken Telephone","Mute the squadmate with the username that is next in the alphabet from yours"))
    chall.append(("Open Door Policy","All doors must be smashed or opened if they cannot be smashed, you may not close any doors"))
    chall.append(("A Michael bay Production","One inventory slot can be whatever you want, every other slot must be ONLY grenades. You cannot start shooting in a fight until you have THROWN all your grenades"))
    chall.append(("Where the hell are my teammates","Squad members are sorted alphabetically by username, the first player has no restrictions. Other players cannot shoot until the player before them has gone down"))
    
    # Modifier Initialization Section
    mods = [("Leg Injury","Your team cannot sprint")]
    mods.append(("Survival of the Fittest","Dying with less than 2 kills means you cannot use your character next game"))
    mods.append(("An Acquired Taste","You must use your least favourite legend available"))
    mods.append(("The Best Motivator is Fear","The zone now counts as an insta kill"))
    mods.append(("Wild West","You cannot ADS and must hipfire"))
    mods.append(("The Marie Kondo Special","No backpacks"))
    mods.append(("Dirty Boxing","Last squad can only be damaged by melee or abilities"))
    mods.append(("Took too much","You cannot stop moving except to loot a deathbox"))
    mods.append(("Premature Ejection","You must drop from the ship immediately"))
    mods.append(("Social Distancing","You cannot be in the same room as a teammate and must remain 2m apart at all times"))
    mods.append(("BFF's","The first two weapons you pickup cannot be swapped for others"))
    mods.append(("Earn your Keep","You cannot speak until you have a kill"))
    mods.append(("Blind faith","The Jumpmaster is blind until landing, they may not ping to assist in being guided"))
    mods.append(("High NRG","Energy Weapons only"))
    mods.append(("Rich get Richer","The kill leader within our squad at the end of the game can choose to ignore the next challenge or add a second challenge onto the other squad members in the next game"))
    mods.append(("Christian Server","You cannot swear or get angry, Loot reset if you do"))
    mods.append(("Rookie numbers","Damage leader within our squad at the end of the game may choose to ignore the next challenge or add another challenge for other squad members in the next game"))
    mods.append(("He's One!","Turn off damage numbers and feedback in settings"))
    mods.append(("Quenched","No Thirsting allowed"))
    mods.append(("Deer in Headlights","You cannot move while scanned by any ability"))
    mods.append(("My Insurance Doesnt cover that","You cannot use ziplines or zipline related items"))
 
    
    # Only 2 Modifiers Allowed
    while NumMods < _NUMBER_OF_MODIFIERS_:
        pick = roll(len(chall)+len(mods))
        if pick < len(chall):
            # Pop instead of access to prevent duplicate Modifiers/Challenges
            temp = chall.pop(pick-1)
            output += "<b>Title: </b>"+temp[0] +"<br>"
            
            # Check for Special challenges section begin
            # Check the first character of the challenge description to see if we rolled the sharing is caring challenge. If we did, remove the special marker character and roll for a weapon type
            if str(temp[1][0]) == "!":
                output += "<b>Description: </b>"+temp[1][1:] + weapon_type()
            # Check the first character of the challenge description to see if we rolled the forbidden words challenge. If we did, remove the special marker character and roll for a weapon type
            if str(temp[1][0]) == "?":
                output += "<b>Description: </b>"+temp[1][1:] + forbidden()
            # Check for Special challenges section end
            if not str(temp[1][0]) == "!" and not str(temp[1][0]) == "?":
                output += "<b>Description: </b>"+temp[1] +"<br>"
            return output
        else:
            # Pop instead of access to prevent duplicate Modifiers/Challenges
            temp = mods.pop(pick-len(chall)-1)         
            output += "<b>Title: </b>[Modifier] "+temp[0] +"<br>"
            output += "<b>Description: </b>"+temp[1] +"<br>"
            output += "<br>"
            NumMods += 1
    pick = roll(len(chall))
    # Pop instead of access to prevent duplicate Modifiers/Challenges
    temp = chall.pop(pick-1)
    output += "<b>Title: </b>"+temp[0] +"<br>"
    
    # Check for Special challenges section begin
    # Check the first character of the challenge description to see if we rolled the sharing is caring challenge. If we did, remove the special marker character and roll for a weapon type
    if str(temp[1][0]) == "!":
        output += "<b>Description: </b>"+temp[1][1:] + weapon_type()
    # Check the first character of the challenge description to see if we rolled the forbidden words challenge. If we did, remove the special marker character and roll for a weapon type
    if str(temp[1][0]) == "?":
        output += "<b>Description: </b>"+temp[1][1:] + forbidden()
    # Check for Special challenges section end   
    if not str(temp[1][0]) == "!" and not str(temp[1][0]) == "?":
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
        pick = roll(len(chall)+len(mods))
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
    pick = roll(len(chall))
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
