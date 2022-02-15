


#Treasure Game replacing treasure with any character
row1=["😂","😂","😂"]
row2=["😂","😂","😂"]
row3=["😂","😂","😂"]


map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Where do you want to put the Treasure ?")



#setting horizontal and vertical positions
horizontal=int(position[0])
vertical=int(position[1])



#setting final steps to print treasured map
selected_row=map[vertical-1][horizontal-1]=input("Enter character")
print(f"{row1}\n{row2}\n{row3}")