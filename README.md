# _MoviePicker
# 🎬 Movie Genre Recommender

This is a simple, interactive Python script that helps users discover movie genres they might enjoy based on their preferences for **action**, **comedy**, and **drama**. It uses basic input handling and conditional logic to suggest a genre and recommend popular films accordingly.

## 💡 How It Works

The script prompts the user with three questions:

```python
Do you like action movies? (yes/no)
Do you like comedy movies? (yes/no)
Do you like drama movies? (yes/no)
Based on the user's responses, it determines a genre combination using boolean logic and prints a curated list of movie recommendations.

🧠 Genre Logic
The genre is determined using a series of if-elif conditions:

✅ Action + ✅ Comedy → Action-Comedy

✅ Action + ✅ Drama → Action-Drama

✅ Comedy + ✅ Drama → Comedy-Drama

✅ All three → Action-Comedy-Drama

✅ Only one → Action, Comedy, or Drama

❌ None → No specific genre

🎥 Sample Output
bash
Do you like action movies? (yes/no): yes
Do you like comedy movies? (yes/no): yes
Do you like drama movies? (yes/no): no

You may like these action-comedy movies: Guardians of the Galaxy, Deadpool