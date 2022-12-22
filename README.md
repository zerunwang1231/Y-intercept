# Y-intercept

## Overview: 

This porject contains a trading startegy based on bollinger bands and volume oscillator. Backtesting is conducted using the provided dataset. A demonstration using stock "1332 JT" is provided.

## Documents:

### .py files:


#### main.py: 
main function 


#### utils.py:
  1. vo() is to calculate the volume oscillator for a single stock. The short and the long time windows are user-defined. For simplicity, I set long window to be the same as the window used in bollinger bands. 
  2. bb() is the function for bollinger bands. Note that the scale parameter m is user-defined and a typical choice is 2 (default).
  3. signal() ia the function that combine the results of vo and bb into buying or selling signals. We utilize vo to confirm the signals generated from bb to ensure the robustness of our signal prediction. 


#### testing.py: 
  1. execution_pl() records the log of daily transaction (action), daily cumulative position, and daily cumulative profit and loss. Note that one the final date, we clean up all of our positions to obtain final P&L (i.e., buy or sell all positions based on the close price of the last day)
  2. get_plot(): visulize price, volume and our actions on daily basis of a single plot. We selected 1332 JT for demonstration. 
  
### Other files:

#### 1332JT.png: 
saved grapgh of the visulization of buy-sell signals of stock 1332 JT

#### log_book1332JT.csv: 
log book of positions. P&L of 1332 JT

#### P_and_L.txt: 
final profits and loss of all avaliable stocks based on our strategy.



  
  
 
