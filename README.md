# Battleship Game

#### Video Demo:  https://www.youtube.com/watch?v=th8OmPmfEr4&t=48s&ab_channel=OmarHamid

### Description:
This is my final project for CS50p: https://www.edx.org/course/cs50s-introduction-to-programming-with-python
The program is a single player battleship game in terminal. You have to sink enemy fleet but be careful because enemy left some mines on battlefield!

# Functionality
## Rules:
After running code with `python project.py` program will show you game rules. If you are familiar with them - type 'y' to start the game,
or type 'n' if you want to exit
<br/><br/> 
## Game 
When game started you see a 
<br/><br/> 
### **Battlefield:**

<img width="172" alt="Screenshot 2022-12-27 at 15 36 49" src="https://user-images.githubusercontent.com/105215745/209719993-1f1a09dc-3339-47fd-a923-56d866e8dfea.png">  


### **Lives:**  

<img width="114" alt="Screenshot 2022-12-27 at 15 40 32" src="https://user-images.githubusercontent.com/105215745/209720087-4e02f62c-695b-4c59-a9f8-0fc751d0ea53.png">  

Every time when you hit a mine '💣' you lose one life. If you hit a mine 3 times - game will be over
<br/><br/> 

# **Coordinates:**

You have to input coordinates to check a cell. Input is checked with regular expression, any invalid input will pe rejected and you will be prompted for coordinates again
<br/><br/> 

# **End of the game**
* You win if you sink enemy fleet 💥  
* You lose if you hit 3 mines 💣  
<br/><br/> 

# Future development

Now the game have only one level and ships and mines are always in the same positions.  
In future good improvement would be to add algorithm to randomly generate ship's and mine's positions before every game