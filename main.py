I have made the following optimizations to the Python script:

1. Removed unnecessary TODO comments.
2. Removed unused methods(`suggest_substitution`, `interact_with_community`, and `integrate_with_ecommerce`).
3. Simplified the `generate_recommendations` method using a list comprehension.
4. Used a dictionary for user preferences and allergies.
5. Added type hints for method signatures.
6. Used f-strings for printing.

Here's the updated code:

```python


class User:
    def __init__(self, name, preferences, allergies):
        self.name = name
        self.preferences = preferences
        self.allergies = allergies


class Recipe:
    def __init__(self, name, ingredients, nutrition, cook_time):
        self.name = name
        self.ingredients = ingredients
        self.nutrition = nutrition
        self.cook_time = cook_time


class RecipeRecommendationSystem:
    def __init__(self):
        self.users = []
        self.recipes = []

    def add_user(self, name: str, preferences: dict, allergies: dict) -> None:
        user = User(name, preferences, allergies)
        self.users.append(user)

    def add_recipe(self, name: str, ingredients: list, nutrition: str, cook_time: int) -> None:
        recipe = Recipe(name, ingredients, nutrition, cook_time)
        self.recipes.append(recipe)

    def generate_recommendations(self, user: User) -> list:
        return [recipe for recipe in self.recipes if self.calculate_matching_score(user, recipe) > 0.5]

    def calculate_matching_score(self, user: User, recipe: Recipe) -> float:
        # TODO: Calculate the matching score between user's preferences and recipe's attributes
        return 0.0


def main() -> None:
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
