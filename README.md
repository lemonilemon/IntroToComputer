IntroToComputer Project - DoggoWorld
---


#### ABOUT

DoggoWorld is a (very) simple 2D horizontal tower defense game. It is an attempt to recreate the experience 
of Battle Cats on the Hack computer, whose many
limitations have necessitated several compromises.

#### OBJECT OF THE GAME

The object of the game is to destroy the enemy's tower and defend your tower. You can achieve the goal by summoning cute doggos, but the enemy's doggos will try to stop you at the same time.

#### GAME PLAYING INSTRUCTIONS

See **How to play** in the game.

RUNNING THE GAME

* Download the .vm files into a single directory. 
* Download the Hack VM Emulator from the NAND2tetris website: http://nand2tetris.org.
* Run the VMEmulator from a shell.
* Select 'File > Load' Program from the menu and point to the directory containing the .vm files
* Select 'View > Animate > No Animation' and set the slider to 'Fast'
* Finally press the '>>' button or F5 to run the game.

ABOUT THE PLATFORM

DoggoWorld runs in conjunction with the Hack OS services on the Jack virtual machine which is designed to be compatable with the specifications of the Hack computer, it was programmed in the Jack programming language.

The *Hack Computer* is a specification for a microcomputer with a very simple 16-bit CPU and 64K of built-in RAM (half of which is set aside for IO memory maps). The CPU has no built-in facility for multiply, divide, bit-shift or floating point. The Hack computer's design and implementation are detailed in the book 'Elements of Computing Systems' by Noam Nissan and Shimon Schoken and in the Coursera courses 'NAND2Tetris Part1 and Part2'. The website for the book and course is: http://nand2tetris.org

The *Hack Operating System* conforms to an API specified in the book and course and provides functionality for text output, graphical output, simple maths functions, strings and memory management.

The *Jack Virtual Machine* is a stack-based virtual machine whose specifications are also described in the book and course. The virtual machine assumes that it is running on a Hack-compatible architecture and memory map and has available the services of the Hack Operating System. In practice, virtual machine programs are run on the VM Emulator supplied by the course authors and which can be downloaded from the course website. Other (faster) implementations are also available from students who have completed the course.

The *Jack Programming language* is a simple Java-like language whose specification and implementation are also described in the book and course. It's only built-in types are 16-bit integers and 16-bit Array (pointer offset) references. It supports user-defined classes, but lacks inheritance. A Jack compiler that produces virtual machine intermediate code is available from the website.

ABOUT THE DESIGN


**Linked-list**  

Jack doesn't support Linked-list, so let's carve one.

**image display**
	Controls user interaction and manages the game mechanics
	The main() function handles initialisation,
	user interaction, scores, initiating movement, and initiating
	rendering.

**Player.jack**
	Manages movement, prevents walking through walls, and caches
	some of the trigonometric calculations related to player orientation.
	Player is not an object class. It is a singleton module which
	operates using statics and functions. This is not ideal OOP, but
	it avoids unnecessary indirection that would clog the stack and
	slow down the game.

**Walls.jack**
	Performs the ray casting to identify what walls are visible,
	what they look like and how far away they are.
	It also keeps the details of the maze in a series of arrays.
	Again it is a singleton module, not an object class.
	It frequently abuses the weak typing of the Jack language
	to cast integers to Arrays and back in a way similar to what
	is possible in C, with all the same dangers.

**Display.jack**
	Performs the screen rendering of the walls using texture maps. 
	It also takes responsibility for rendering text (scores, splash screens and load screen),
	as well as drawing bitmap graphics to the screen for the gun and sights.
	All graphics are rendered by writing whole 16-bit words to
	the screen at a time, and the code goes out of its way in both the bitmap rendering
	and the wall rendering to avoid multiple writes
	to the same memory location. The render resolution is only 256 x 64 (quarter of that
	of the screen itself), which means each pixel to be rendered involves writing 4 bits
	to the screen.

//credit