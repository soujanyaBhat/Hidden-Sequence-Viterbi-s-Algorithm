# -*- coding: utf-8 -*-
import sys

def viterbi(input, hot_probability, cold_probability, transition_probability, initial_hot, initial_cold):
    inp=list(input)
    hot=[]
    cold=[]
    sequence=[]
    cold_parent=[]
    hot_parent=[]
    hot.append(initial_hot*hot_probability[(inp[0],"hot")])
    cold.append(initial_cold*cold_probability[(inp[0],"cold")])
    
    for i in range(1,len(inp)):
        #Calculation of probabilities
        hh=hot[i-1]* transition_probability[("hot","hot")]*hot_probability[(inp[i],"hot")]
        hc=hot[i-1]* transition_probability[("hot","cold")]*cold_probability[(inp[i],"cold")]
        ch=cold[i-1]* transition_probability[("cold","hot")]*hot_probability[(inp[i],"hot")]
        cc=cold[i-1]* transition_probability[("cold","cold")]*cold_probability[(inp[i],"cold")]
        
        #Storing the parent for each node
        if hh>ch:
            hot_parent.append("H")
        else:
            hot_parent.append("C")
        if hc >cc:
            cold_parent.append("H")
        else:
            cold_parent.append("C")
            
        #Storing the maximum probability out of the two    
        hot.append(max(hh,ch))
        cold.append(max(cc,hc))
    
    #Backtracking to obtain sequence 
    j=0
    if hot[len(hot)-1]>cold[len(hot)-1]:
        sequence.append("H")
        fin=hot[len(hot)-1]
    else:
        sequence.append("C")
        fin=cold[len(cold)-1]
    for i in range(len(hot_parent)-1,-1,-1):
            if sequence[j]=="H":
                sequence.append(hot_parent[i])
                j+=1
            else:
                sequence.append(cold_parent[i])
                j+=1
    print("Sequence: ", sequence[::-1])
    print("Final Probability:", fin )

if __name__ == '__main__':
    input1 =sys.argv[1] #"331122313"
    
    # Initialization
    initial_hot = 0.8
    initial_cold = 0.2
    hot_probability = {('1', 'hot') : 0.2, ('2', 'hot') : 0.4, ('3', 'hot') : 0.4}
    cold_probability = {('1', 'cold') : 0.5, ('2', 'cold') : 0.4, ('3', 'cold') : 0.1}
    transition_probability = {('hot', 'hot') : 0.7, ('hot', 'cold') : 0.3, ('cold', 'cold') : 0.6, ('cold', 'hot') : 0.4}
    viterbi(input1, hot_probability, cold_probability, transition_probability, initial_hot, initial_cold)

