"""URL mappings for the recipe app."""
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from recipe.views import RecipeViewSet, TagViewSet, IngredientViewSet

router = DefaultRouter()
router.register("recipes", RecipeViewSet)
router.register("tags", TagViewSet)
router.register("ingredients", IngredientViewSet)
app_name = "recipe"
urlpatterns = [path("", include(router.urls))]
