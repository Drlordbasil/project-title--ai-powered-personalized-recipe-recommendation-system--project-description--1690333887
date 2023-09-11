from dataclasses import dataclass
I've made the following optimizations to your Python script:

1. Moved the `User` and `Recipe` classes outside of the `RecipeRecommendationSystem` class for better organization.
2. Implemented the `calculate_matching_score` method to calculate the matching score between a user's preferences and a recipe's attributes.
3. Updated `generate_recommendations` method to use the `calculate_matching_score` method and filter recipes based on a matching score threshold.
4. Used a dictionary instead of a list for storing recipes for faster lookup.
5. Used a dataclass decorator for the `Recipe` class to automatically generate `__init__` method and other special methods.
6. Removed unnecessary type hints for method signatures, as it's better to rely on type inference in Python.

Here's the updated code:

```python


@dataclass
class User:
    name: str
    preferences: dict
    allergies: dict


@dataclass
class Recipe:
    name: str
    ingredients: list
    nutrition: str
    cook_time: int


class RecipeRecommendationSystem:
    def __init__(self):
        self.users = []
        self.recipes = {}

    def add_user(self, name, preferences, allergies):
        user = User(name, preferences, allergies)
        self.users.append(user)

    def add_recipe(self, name, ingredients, nutrition, cook_time):
        recipe = Recipe(name, ingredients, nutrition, cook_time)
        self.recipes[name] = recipe

    def generate_recommendations(self, user):
        return [recipe for recipe in self.recipes.values() if self.calculate_matching_score(user, recipe) > 0.5]

    def calculate_matching_score(self, user, recipe):
        matching_score = 0

        for preference, preference_value in user.preferences.items():
            if preference in recipe.ingredients:
                matching_score += 0.25

            if preference_value and preference == recipe.nutrition:
                matching_score += 0.5

        for allergy, allergy_value in user.allergies.items():
            if allergy in recipe.ingredients and allergy_value:
                matching_score -= 0.5

        return matching_score


def main():
    recipe_system = RecipeRecommendationSystem()

    # Add users
    recipe_system.add_user(
        "John", {"vegan": True, "gluten-free": True}, {"peanuts": True})
    recipe_system.add_user("Alice", {"pescatarian": True}, {})

    # Add recipes
    recipe_system.add_recipe(
        "Vegan Curry", ["tofu", "coconut milk", "curry paste"], "Healthy", 30)
    recipe_system.add_recipe(
        "Gluten-Free Pancakes", ["almond flour", "banana", "maple syrup"], "Low Carb", 20)

    # Generate personalized recommendations for user
    user = recipe_system.users[0]
    recommendations = recipe_system.generate_recommendations(user)

    # Print the recommended recipes
    print(f"Recommended recipes for user {user.name}:")
    for recipe in recommendations:
        print(recipe.name)


if __name__ == "__main__":
    main()
```

The code should now be more optimized and readable.
