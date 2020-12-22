from django.db import models
from django.urls import reverse

from categories.models import Category
from goodsandservices.models import GoodAndService
from measurements.models import Uom
from ingredients.models import Ingredient


class CookingProgram(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        phaseLIst = CookingProgramPhase.objects.filter(program=self)
        strToRet = ''
        for p in phaseLIst:
            strToRet += 'Phase ' + str(p.phaseNumber) + ': ' + str(p.cookTime) + 'min ' + str(
                p.temperature) + '°C ' + str(p.humidity) + '% ' + p.chamber + ' - '
        #  print('p ', p.get_chamber_display())

        return self.name + ': ' + strToRet


class CookingProgramPhase(models.Model):
    Chamber_type = [
        ('op', 'Open'),
        ('cl', 'Closed'),

    ]
    program = models.ForeignKey(CookingProgram, on_delete=models.CASCADE)
    phaseNumber = models.IntegerField(default=1)
    chamber = models.CharField(max_length=20, choices=Chamber_type)
    cookTime = models.IntegerField()
    temperature = models.IntegerField()
    humidity = models.IntegerField()

    def __str__(self):
        return self.program.name + " min " + str(self.cookTime)


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    shortname = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(null=True, blank=True)
    platingimage = models.ImageField(null=True, blank=True)
    servings = models.IntegerField()
    preptime = models.IntegerField(null=True, blank=True)
    #  cooktime = models.IntegerField(null=True, blank=True)
    cookProgram = models.ForeignKey(CookingProgram, on_delete=models.CASCADE, null=True, blank=True)
    # cookingProgram = models.ForeignKey()
    directions = models.TextField()
    origin = models.CharField(max_length=50, null=True, blank=True)
    # nutritional intended for serving
    calories = models.FloatField(null=True, blank=True)
    car = models.FloatField(null=True, blank=True)
    pro = models.FloatField(null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    sta = models.FloatField(null=True, blank=True)

    # TODO default images

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipe-detail",
                       kwargs={"pk": self.pk})  # passing arg through kwargs and call the name of the url

    def save(self, *args, **kwargs):
        # items = self.recipeitem_set.all()
        cal = 0
        car = 0
        pro = 0
        fat = 0
        sta = 0
        peso = 0
        for it in self.recipeitem_set.all():
            # cal value
            cal += it.ingredient.cal * it.quantity / it.recipe.servings / 100
            car += it.ingredient.car * it.quantity / it.recipe.servings / 100
            pro += it.ingredient.pro * it.quantity / it.recipe.servings / 100
            fat += it.ingredient.fat * it.quantity / it.recipe.servings / 100
            sta += it.ingredient.sta * it.quantity / it.recipe.servings / 100
            # cal peso tot ingre
            peso += it.quantity

            self.calories = cal
            self.car = car
            self.pro = pro
            self.fat = fat
            self.sta = sta
            # saving rec
        # for it in items:
        #     it.importance = it.quantity / peso / it.recipe.servings * 100

        super(Recipe, self).save(*args, **kwargs)


class RecipeItem(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    uom = models.ForeignKey(Uom, on_delete=models.CASCADE)
    quantity = models.FloatField()
    destination = models.CharField(max_length=50, null=True, blank=True)

    #  importance = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super(RecipeItem, self).save(*args, **kwargs)
        cal = 0
        car = 0
        pro = 0
        fat = 0
        sta = 0
        # peso = 0  # somma quantita di tutti gli items
        for it in self.recipe.recipeitem_set.all():
            # cal value
            cal += it.ingredient.cal * (it.quantity + self.quantity) / self.recipe.servings / 100
            car += it.ingredient.car * (it.quantity + self.quantity) / self.recipe.servings / 100
            pro += it.ingredient.pro * (it.quantity + self.quantity) / self.recipe.servings / 100
            fat += it.ingredient.fat * (it.quantity + self.quantity) / self.recipe.servings / 100
            sta += it.ingredient.sta * (it.quantity + self.quantity) / self.recipe.servings / 100
        #         peso += it.quantity

        recipets = Recipe.objects.get(pk=self.recipe.id)
        recipets.calories = cal
        recipets.car = car
        recipets.pro = pro
        recipets.fat = fat
        recipets.sta = sta

        recipets.save()
        # TODO USE SIGNALS


class RecipeLine(models.Model):
    position = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    method = models.TextField(null=True, blank=True)
    durationMin = models.IntegerField()

    def __str__(self):
        return self.name


class RecipeLineItem(models.Model):
    recipeLine = models.ForeignKey(RecipeLine, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, null=True)
    uom = models.ForeignKey(Uom, on_delete=models.SET_NULL, null=True)
    quantity = models.FloatField()

    def __str__(self):
        return self.recipeLine.name


class WishToCookRecipe(models.Model):
    recipe = models.OneToOneField(Recipe, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.recipe.title
