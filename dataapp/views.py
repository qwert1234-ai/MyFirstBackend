from django.shortcuts import render
from dataapp.models import Enemy

def AllEnemyPage(reguest):
    allEnemies = Enemy.objects.all()

    pageParams = {"enemies": allEnemies}
    return render(reguest, "allEnemies.html", pageParams)


def EnemyPage(request, name):
    allEnemies = Enemy.objects.all()
    print(name)
    currentEnemy = Enemy.objects.all().filter(name=name)

    params = {"enemy": currentEnemy[0]}
    return render(request, "enemy.html", params)

