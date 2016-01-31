################################
# EvoMan FrameWork - V1.0 2016 
# Author: Karine Miras         #
# karine.smiras@gmail.com      #
################################

# imports framework
import sys
sys.path.insert(0, 'evoman') 
from environment import Environment

env = Environment(playermode="human",enemymode="static",enemies=[8])
env.play()  
 