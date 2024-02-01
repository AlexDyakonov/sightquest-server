from django.contrib import admin
from django.utils.html import mark_safe

from .models import (
    City,
    Coordinate,
    Game,
    GamePhoto,
    GameQuestTask,
    GameSettings,
    GameUser,
    PlayerTaskCompletion,
    QuestPoint,
    QuestTask,
    Region,
)


class QuestTaskInline(admin.TabularInline):
    model = QuestTask
    extra = 1

class GamePhotoInline(admin.TabularInline):
    model = GamePhoto
    extra = 1


class GameUserInline(admin.TabularInline):
    model = GameUser
    extra = 1


class GameQuestTaskInline(admin.TabularInline): 
    model = GameQuestTask
    extra = 1 


# Админ класс для координат
@admin.register(Coordinate)
class CoordinateAdmin(admin.ModelAdmin):
    list_display = ("latitude", "longitude")
    search_fields = ("latitude", "longitude")


# Админ класс для точек квеста
@admin.register(QuestPoint)
class QuestPointAdmin(admin.ModelAdmin):
    list_display = ("title", "description_short", "location", "product_image")
    search_fields = ("title", "description")
    list_filter = ("location",)
    inlines = [QuestTaskInline]

    def description_short(self, obj):
        return (
            obj.description[:50] + "..."
            if len(obj.description) > 50
            else obj.description
        )

    def product_image(self, obj):
        if obj.image:
            return mark_safe('<img src="%s" width="50" height="50" />' % obj.image.url)
        return "No Image"


# Админ класс для фотографий лобби
@admin.register(GamePhoto)
class GamePhotoAdmin(admin.ModelAdmin):
    list_display = ["id", "game", "image", "upload_time"]


# Админ класс для городов и регионов
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "region"]


@admin.register(QuestTask)
class QuestTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'quest_point')  
    search_fields = ('title', 'description', 'quest_point__title') 
    list_filter = ('quest_point',) 
    ordering = ('title',) 


@admin.register(GameSettings)
class GameSettingsAdmin(admin.ModelAdmin):
    list_display = ('mode', 'duration')
    search_fields = ('mode',) 
    ordering = ('mode',) 


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        'host', 'code', 'created_at', 'started_at', 'ended_at')  
    search_fields = (
        'host__username', 'code', 'created_at', 'started_at', 'ended_at')  
    list_filter = ('host', 'created_at', 'started_at')  
    ordering = ('-created_at',)  
    filter_horizontal = ('players', 'tasks') 
    inlines = [GameUserInline, GameQuestTaskInline] 

@admin.register(PlayerTaskCompletion)
class PlayerTaskCompletionAdmin(admin.ModelAdmin):
    list_display = ('player', 'game_task', 'completed_at')  
    search_fields = (
        'player__username', 'game_task__game__host__username',
        'completed_at') 
    list_filter = ('player', 'game_task__game') 
    ordering = ('-completed_at',)  
