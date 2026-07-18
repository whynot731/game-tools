from django.db import models
from django.forms import IntegerField

# Create your models here.

class Resonators(models.Model):
    resonator_id = models.AutoField(primary_key = True)
    character_name = models.TextField(unique=True, null=False)
    is_counted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Resonators"

    def __str__(self):
        return self.character_name

class Materials(models.Model):
    class MATERIAL_TYPE(models.IntegerChoices):
        WEEKLY = 1, "Weekly Boss"
        FORGERY = 2, "Forgery"
    class RARITY(models.IntegerChoices):
        GREEN = 1, "Green"
        BLUE = 2, "Blue"
        PURPLE = 3, "Purple"
        GOLD = 4, "Gold"

    material_id = models.AutoField(primary_key = True)
    material_name = models.TextField(unique=True)
    material_type = models.IntegerField(choices=MATERIAL_TYPE)
    rarity = models.IntegerField(choices=RARITY) #1 = Green, 2 = Blue, 3 = Purple, 4 = Gold

    class Meta:
        verbose_name_plural = "Materials"

    def __str__(self):
        return self.material_name

class Forte_Costs(models.Model):
    class FORTE_NODES(models.IntegerChoices):
        BASIC_ATTACK = 1, "Basic Attack"
        RESONANCE_SKILL = 2, "Resonance Skill"
        FORTE_CIRCUIT = 3, "Forte Circuit"
        RESONANCE_LIBERATION = 4, "Resonance Liberation"
        INTRO_SKILL = 5, "Intro Skill"
        INHERENT_SKILL = 6, "Inherent Skill"
        STAT_BONUS = 7, "Stat Bonus"
    class STAT_BRANCH(models.IntegerChoices):
        BRANCH_1 = 1, "Stat Bonus 1"
        BRANCH_2 = 2, "Stat Bonus 2"
        BRANCH_3 = 3, "Stat Bonus 3"
        BRANCH_4 = 4, "Stat Bonus 4"
    
    cost_id = models.AutoField(primary_key=True)
    resonators = models.ForeignKey(Resonators, on_delete=models.CASCADE)
    materials = models.ForeignKey(Materials, on_delete=models.CASCADE)
    target_level = models.IntegerField()
    forte_node = models.IntegerField(choices=FORTE_NODES)
    stat_branch = models.IntegerField(choices=STAT_BRANCH, null=True, blank=True)   #4 Branches for Stat Bonuses
    node_cost = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Forte Costs"

    def __str__(self):
        return str(self.node_cost) #Figure out what to return later. Likely need most of the columns
