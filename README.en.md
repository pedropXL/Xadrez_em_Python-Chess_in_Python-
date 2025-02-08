# **Chess Game in Python**
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Static Badge](https://img.shields.io/badge/LinkedIn-www.linkedin.com%2Fin%2Fpedropedrazzi-blue)
![Static Badge](https://img.shields.io/badge/License-MIT%20License-red)
![Static Badge](https://img.shields.io/badge/English%20-%20US%20-%20black?style=plastic&labelColor=yellow)

---
### **Click in the badger for acess the text in Portuguese:** [![Static Badge](https://img.shields.io/badge/Portugu%C3%AAs%20-%20BR%20-%20green?style=plastic&labelColor=blue)](README.pt-br.md)

## **Overview**

This is a chess game developed in Python using the Pygame library. The game features a fully functional chessboard with all standard chess pieces, including pawns, rooks, knights, bishops, queens, and kings. Players can take turns moving their pieces, and the game includes features such as capturing pieces, checking the king, and declaring a winner when a king is checkmated. The player can play against the computer, too.

---

## **Table of Contents**

- [Features](#features)
- [Requirements](#requirements)
- [How to install the Requirements libraries](#how-to-install-the-requirements-libraries)
- [Recomendations](#recomendations)
- [Installation](#installation)
- [How to play](#how-to-play)
- [Customization](#customization)
- [Audio](#audio)
- [Language](#language)
- [Code Structure](#code-structure)
- [Key Functions](#key-functions)
- [Assets](#assets)
- [Contributing](#contributing)
- [Licence](#license)
- [Contact and Feedback](#contact-and-feedback)
---

## **Features**
- **One_Player Mode**: Play against the computer.
- **Two-Player Mode**: Play against a friend on the same machine.
- **Customizable Board**: Choose from different board themes and colors.
- **Audio Feedback**: Sound effects for piece movements, captures, and game over.
- **Disable Audio**: It's possible disable the audio if you want.
- **Language Support**: Available in English, Portuguese, and Spanish.
- **Undo Move**: Option to undo the last move (limited to one undo per turn).
- **Game Over Detection**: Automatically detects checkmate and declares the winner.

---

## **Requirements**
- Python 3.x
- Pygame library: For providing the framework to build the game.
- PIL (Pillow) library: For image processing and resizing.
- soundfile library: For handling audio files.

---

## **How to install the Requirements libraries**

- Pygame: `pip install pygame`
- Pillow: `pip install pillow`
- Soudfile: `pip install soundfile`

- Or just type: `pip install pygame pillow soundfile`

---

## **Recomendations**

- Create a Virtual Environment for download the libraries.

---

## **Installation**
1. **Clone the repository**:
   
   Type: `git clone https://github.com/pedropXL/Xadrez_em_Python-Chess_in_Python-.git`

2. **Accessing the cloned repository**:
    Type: `cd Xadrez_em_Python-Chess_in_Python-`

---

## **How to play**

- Mouse Controls: Use the mouse to click in buttons, select and move pieces.
- Turn-Based: Players take turns moving their pieces. White always moves first.
- Capturing Pieces: Move your piece to a square occupied by an opponent's piece to capture it.
- Undo the move: For undo the move click in Undo in the left of the screen on the main game.
- Forfeit: If your want give up and(or) restart the game just click in Forfeit in the left of the screen on the main game.
- Checkmate: The game ends when a player's king is in checkmate.
- Restart the game: For restart the game after the checkmate type Enter.

### **Initial Screen**

![Initial Screen](/README_images/Initial%20screen.png)

### **Main Game**
![Main Game](/README_images/Main%20game.png)
---

## **Customization**

- Board Themes: Customize the board's appearance by selecting different themes in the Custom area.

---

## **Audio**

- Audio: Toggle sound effects on or off in the settings menu.

---

## **Language**

- Language: Change the game's language in the setting menu, you can choose between English, Portuguese, and Spanish.

---

## **Code Structure**

The code is divided into several sections:

- Initialization: Sets up the Pygame environment, loads assets, and initializes game variables.
- Game Logic: Handles piece movements, captures, and game state (check, checkmate, etc.).
- UI Rendering: Draws the board, pieces, and UI elements like the menu and settings.
- Event Handling: Processes user input (mouse clicks, key presses) to control the game.

---

## **Key Functions**

- draw_board(): Renders the chessboard and pieces.
- check_options(): Determines valid moves for each piece.
- draw_valid(): Highlights valid moves for the selected piece.
- draw_captured(): Displays captured pieces on the side of the board.
- draw_game_over(): Displays the game over screen when a player wins.

---

## **Assets**

- Images: All chess piece images are stored in the assets/images directory.
- Audio: Sound effects are stored in the audio directory.

---

## **Contributing**

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request with your changes. Feel free for improve the project, turn the code more efficiently, fix possible bugs and add more features.

---

## **License**
This project is licensed under the MIT License. See the LICENSE file for more details.

---

## **Links**

- [Linkedin](www.linkedin.com/in/pedropedrazzi)
- [Github](https://github.com/pedropXL)

## **Contact and Feedback**

For any questions or feedback, please open an issue on GitHub or contact the project maintainer.

Email for contact: pedroppedrazzi@gmail.com

---