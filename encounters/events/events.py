from encounters.events.event_class import Event, EventOption
from items.weapons import Longsword_plus1
from tools.enums import AbilityScore, Skill

SwordInStone = Event(
    name = "The Sword in the Stone",
    description = "In the center of this room, you see a longsword with its blade stuck into a stone pedestal.\n" \
    "As you investigate, you notice some runes carved around the top of the pedestal.",
    options = [
        EventOption(
            name = "Pull out the sword",
            ability_check = AbilityScore.STR,
            difficulty_class = 15,
            rewards = [Longsword_plus1],
            success_text = "{} wrenches the sword from the stone. It gleams in your faint torchlight.",
            failure_text = "{} pulls at the sword with all their might, but it won't budge.",
        ),
        EventOption(
            name = "Examine the runes etched into the rock",
            ability_check = Skill.arcana,
            difficulty_class = 15,
            rewards = [],
                # I think this should be a control spell, which would make this decision more meaningful- big damage or control?
            success_text = "{} studies the runes and recognizes them as the incantation for a powerful spell.",
            failure_text = "{} examines the runes, but is unable to decipher them.",
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