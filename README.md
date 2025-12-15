# 🗺️ States Finder Game (Python)

A fun and interactive **States Finder Game** built using **Python Turtle Graphics**.  
Players type the name of a state, and if the answer is correct, the state name appears in the correct position on the map. Incorrect answers are ignored. The game continues until all states are found or the player chooses to exit.

---

## 🎮 How the Game Works

- A map is displayed using Turtle Graphics
- The user types a **state name** into an input box
- ✅ If the state name is correct:
  - The name appears in the correct position on the map
  - The **score increases**
- ❌ If the state name is incorrect:
  - Nothing appears on the map
- Already guessed states are ignored to prevent duplicates
- Typing **`exit`** in the input box ends the game
- When the game ends, a **CSV file containing missing (unguessed) states** is automatically created

---

## 🛠️ Technologies Used

- **Python 3**
- **Turtle Graphics**
- **Pandas** (for handling state data from CSV files)

---



## 🚀 How to Run the Game

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Kalindu-karunarathna/states-finder-game
```

### 2️⃣ Navigate to the Project Folder
```bash
cd states-finder-game
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Game
```bash
python main.py
```

---

## 🧠 Game Rules

- Enter state names **exactly** as they appear in the dataset
- Each correct state can be entered **only once**
- The score increases for every correct answer
- Type **`exit`** at any time to quit the game
- When exiting, a CSV file with all **missing states** will be saved automatically

---

## 📈 Features

- Interactive map-based gameplay
- Real-time user input using Turtle text input
- **Score tracking system**
- Displays correct answers directly on the map
- Prevents duplicate answers
- Generates a **CSV file of missing states** when the user exits
- Uses CSV data for easy scalability


---



## 👤 Author

**Kalindu Karunarathna**  
Python Developer | Software Engineering Undergraduate

---

⭐ If you like this project, consider giving it a star on GitHub!
