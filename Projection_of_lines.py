# dimensions of the box
    # main logic
    # for clarity, please go to end of the code for further understanding
    b=abs(x1-x2)
    l=abs(z1-z2)
    h=abs(y1-y2)
        
    alpha = l/((h*h+l*l)**0.5)
    beta = l/((b*b+l*l)**0.5)
    
    # F.V. & T.V. inclination
    ang_alpha = format(degrees(acos(alpha)), '0.2f')
    ang_beta = format(degrees(acos(beta)), '0.2f')
        
    # True Length
    tl=(b**2+h**2+l**2)**0.5
    
    # Inclination with H.P. & V.P.
    theta = format(degrees(asin(h/tl)),'0.2f')
    phi = format(degrees(asin(b/tl)),'0.2f')
    
    # Top view length
    topview_length = format((b**2+l**2)**0.5, '0.2f')
    
    # Front view length
    frontview_length = format((h**2+l**2)**0.5, '0.2f')
    
    fig=plt.figure(figsize=(5,5))
    ax=fig.add_subplot(111,projection="3d")
        
    ax.plot3D([x1,x2], [y1,y2], [z1,z2], 'black')
    ax.plot3D([x1,x2], [0,0], [z1,z2], 'red')
    ax.plot3D([0,0], [y1,y2], [z1,z2], 'blue')
    
    #small one
    ax.plot3D([x1,x1], [y1,0], [z1,z1], 'grey')
    #big one
    ax.plot3D([x2,x2], [y2,0], [z2,z2], 'grey')
    #down top
    ax.plot3D([x2,0], [y2,y2], [z2,z2], 'grey')
    #down bottom
    ax.plot3D([x2,0], [0,0], [z2,z2], 'grey')
    #small one1
    ax.plot3D([0,0], [0,y2], [z2,z2], 'grey')
    # front view to y axis
    ax.plot3D([x1,0], [0,0], [z1,z1], 'grey')
    #front view vertical on y axis
    ax.plot3D([0,0], [0,0], [z1,z2], 'grey') 
    
    ax.plot3D([0,0], [0,y1], [z1,z1], 'grey')
    
    ax.plot3D([x1,0], [y1,y1], [z1,z1], 'grey')
    plt.show()
    
    # creating the Tkinter canvas 
    # containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig, 
                               master = root1)   
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().grid(row=0,column=0,columnspan=10)
  
    # creating the Matplotlib toolbar 
    frame = Frame(root1)
    frame.grid(row=32, column=0)
    toobar = NavigationToolbar2Tk(canvas, frame)
    canvas.get_tk_widget().grid(row=22, column=0)
    
    # Labels of the graph
    label_TL = Label(root1, text = 'True Length of the line (black line): ',)
    label_FV = Label(root1, text = 'Length of Front View (blue line): ')
    label_TV = Label(root1, text = 'Length of Top View (red line): ')
    label_alpha = Label(root1, text = 'Angle made by Front View with HP: ')
    label_beta = Label(root1, text = 'Angle made by Top view with VP: ')
    label_theta = Label(root1, text = 'Angle made by the line with HP: ')
    label_phi = Label(root1, text = 'Angle made by the line with VP: ')
    
    label_TL1 = Label(root1, text = format(tl,'0.2f')+' '+'mm')
    label_FV1 = Label(root1, text = frontview_length+' '+'mm')
    label_TV1 = Label(root1, text = topview_length+' '+'mm')
    label_alpha1 = Label(root1, text = ang_alpha+' '+'degrees')
    label_beta1 = Label(root1, text = ang_beta+' '+'degrees')
    label_theta1 = Label(root1, text = theta+' '+'degrees')
    label_phi1 = Label(root1, text = phi+' '+'degrees')
    

    # Shoving/pushing the labels onto the screen
    label_TL.grid(row=33, column=0, columnspan=8)
    label_FV.grid(row=34, column=0, columnspan=8)
    label_TV.grid(row=35, column=0, columnspan=8)
    label_alpha.grid(row=36, column=0, columnspan=8)
    label_beta.grid(row=37, column=0, columnspan=8)
    label_theta.grid(row=38, column=0, columnspan=8)
    label_phi.grid(row=39, column=0, columnspan=8)
    
    label_TL1.grid(row=33, column=1)
    label_FV1.grid(row=34, column=1)
    label_TV1.grid(row=35, column=1)
    label_alpha1.grid(row=36, column=1)
    label_beta1.grid(row=37, column=1)
    label_theta1.grid(row=38, column=1)
    label_phi1.grid(row=39, column=1)
    
    

# Submit button for the values
sub = Button(root, text='SUBMIT', padx=10, pady=10, command=pl_lines).grid(row=7, column=1, columnspan=2)

root.mainloop()
