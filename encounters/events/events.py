from encounters.events.event_class import Event, EventOption
from encounters.combat.combats import MurderHoboFight, InjuredAdventurerFight
from items.weapons import Longsword_plus1
from characters.companions import Bard
from tools.enums import AbilityScore, Skill

SwordInStone = Event(
    name = "The Sword in the Stone",
    description = "In the center of this room, you see a longsword with its blade stuck into a stone pedestal.\n" \
    "As you investigate, you notice some runes carved around the top of the pedestal.",
    options = [
        EventOption(
            name = "Pull out the sword",
            ability_check = AbilityScore.STR,
            difficulty_class = 12,
            rewards = [Longsword_plus1],
            success_text = "{} wrenches the sword from the stone. It gleams in your faint torchlight.",
            failure_text = "{} pulls at the sword with all their might, but it won't budge.",
        ),
        EventOption(
            name = "Examine the runes etched into the rock",
            ability_check = Skill.arcana,
            difficulty_class = 14,
            rewards = [],
                # I think this should be a control spell, which would make this decision more meaningful- big damage or control?
            success_text = "{} studies the runes and recognizes them as the incantation for a powerful spell.",
            failure_text = "{} examines the runes, but is unable to decipher them.",
        ),
    ],
)
TheInjuredAdventurer = Event(
    name = "The Injured Adventurer",
    description = "You come across a rogue who appears to have just come off worse in a fight. " \
    "On the ground beside him is a backpack and an unconscious bard with a large bruise on his forehead. " \
    "The rogue clutches a bloody wound at his side and scowls at you. ",
    options = [
        EventOption(
            name = "Fight him",
            success_text = "You squash the last vestiges of life from the bloodied rogue.",
            failure_text = "In spite of the rogue's wounds, you are no match for him.",
            rewards = [], # Nothing
            combat = InjuredAdventurerFight,
        ),
        EventOption(
            name = "Scare him off",
            success_text = "{} stares down the bloodied rogue, who realizes you mean business and dashes off into the the darkness. " \
            "Left behind, you see the rogue's backpack and the unconscious bard. ",
            failure_text = "The rogue isn't scared of {} and readies his dagger.",
            ability_check = Skill.intimidation,
            difficulty_class = 12,
            combat = InjuredAdventurerFight,
            combat_on_failure = True,
            combat_success_text="You squash the last vestiges of life from the bloodied rogue.",
            combat_failure_text="In spite of the rogue's wounds, you are no match for him.",
            rewards = [], # He leaves behind some rations.
        ),
        EventOption(
            name = "Offer to heal his wounds",
            success_text = "You see a flicker in the rogue's eye before he lets his guard down. " \
            "\n\n" \
            "You sit together for an hour as {} tends to his wounds. " \
            "The rogue reveals his name is |NAME|, and all he wants is to escape this dungeon. " \
            "He leaves you with |ITEM| before slipping away into the shadows.",
            failure_text = "The rogue isn't intersted in {}'s help and readies his dagger.",
            ability_check = Skill.medicine,
            difficulty_class = 12,
            combat = InjuredAdventurerFight,
            combat_on_failure = True,
            combat_success_text="You squash the last vestiges of life from the bloodied rogue.",
            combat_failure_text="In spite of the rogue's wounds, you are no match for him.",
            rewards = [], # He gives you maybe a wondrous item? I'd have to raise the DC. Maybe he gives you a map that would be too blood-soaked if you killed him
        ),
        # Depending on what you do, I think it would be cool to see the rogue again. 
        # If they die in combat, they could be resurrected by the necromancer. 
        # If they run away, they could get killed anyway or get captured by the goblins. 
        # If they get healed, maybe they just escape or maybe they show up later to help you.

        # I think this project is way too ambitious
    ],
    rewards = [Bard,]
)
TheMurderHobo = Event(
    name = "The Murder Hobo",
    description = 
        "As you travel, you notice a trail of blood and bits of bone and viscera. " \
        "Eventually, you happen upon a blood-splattered figure in armor made of skulls and other bones bound together with guts and tendons. " \
        "They're surrounded by piles of gore you realize were once living goblins. " \
        "\n\n" \
        "As the figure carves the skin off one of the goblins' skulls, you accidentally kick a pebble that skitters across the ground. " \
        "The figure turns to you, panting. You can just barely see their eyes through their mask, made of a shattered skull. ",
    options = [
        EventOption(
            name = "Fight them",
            combat = MurderHoboFight,
            rewards = [], # Boon from DM. Not included here: the Murder Hobo's equipped bone armor and greatsword
            success_text = 
                "The figure collapses, their blood pooling around them, mixing with that of the rotting goblins." \
                "\n\n" \
                "Your party lets out a sigh, and you sense a feeling of immense relief from some great being beyond your comprehension. " \
                "It is grateful that this one will no longer disturb its plans. ", 
                # I thought it would be funny if the DM was relieved the murder hobo was dead
            failure_text = "The figure holds you by your chin as the life leaves your body. " \
            "As he stares into your eyes, you know your body will soon be just another part of their armor. ",
        ),
        EventOption(
            name = "Join them in desecrating these bodies",
            ability_check = Skill.investigation,
            difficulty_class = 16, # I think this can be a relatively hard check with a big reward.
            options = [
                EventOption(
                    name = "Shortsword",
                    rewards = [],
                    success_text="You create a shortsword from bone.",
                    failure_text="If you're seeing this, there is a bug.",
                ),
                EventOption(
                    name = "Longbow",
                    rewards = [],
                    success_text="You create a longbow from bone.",
                    failure_text="If you're seeing this, there is a bug.",
                ),
                EventOption(
                    name = "Magic item",
                    rewards = [],
                    success_text="You create a magic item from bone.",
                    failure_text="If you're seeing this, there is a bug.",
                )
            ],
            success_text = "{} picks through the bodies and finds a bones sturdy enough to make something.",
            failure_text = "After an hour, {} is unable to make anything out of the goblins' bodies.",
        ),
    ],
)
# Mimic event:
# - Open the chest or whatever it is
# - Take something small and ignore the chest
# Other idea
# - Look into a chest, pick one of several items, but a random one of them is a mimic and leads to a fight
#   - Could also have an item that is a mimic and hurts you

# Gelatinous cube event

# Talk with a beholder?

# Door puzzle


if __name__ == "__main__":
    from characters.companions import Brains, Brawn
    SwordInStone.begin([Brawn, Brains])