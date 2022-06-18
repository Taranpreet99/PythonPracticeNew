import pygame
import time

#game set-up and main loop
def main():
    pygame.init() #prepare pygame module
    surface_sz = 480 #Desired physical surface size

    #Create surface of (width,height), and its window.
    main_surface = pygame.display.set_mode((surface_sz,surface_sz))

    #Small rectangle and its color
    small_rect = (300,200,150,90)
    some_color = (255,0,0) #RGB

    #load image
    ball = pygame.image.load("ball.jpg")

    #Instantiate 16 point courier font
    my_font = pygame.font.SysFont("Courier",16)
    the_text = my_font.render("Hello, world!", True,(0,0,0))

    frame_count = 0
    frame_rate = 0
    t0 = time.time()

    while True:
        ev = pygame.event.poll() #look for any event
        if ev.type == pygame.QUIT: #Window close button clicked?
            break #leave game loop

        #Game logic
        frame_count += 1
        if frame_count % 500 == 0:
            t1 = time.time()
            frame_rate = 500/(t1-t0)

        #We draw everything from scratch on each frame
        #so first fill everything with the background color
        main_surface.fill((0,200,255))

        #Overpaint a smaller rectangle on the main surface
        main_surface.fill(some_color, small_rect)

        #add image to the surface
        main_surface.blit(ball,(100,200))

        #New surface with image of text
        the_text = my_font.render("Frame = {0}, rate = {1:.2f} fps".format(frame_count, frame_rate), True, (0,0,0))

        #add text to the surface
        main_surface.blit(the_text, (10,10))

        #Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
    
    pygame.quit() #Once we leave the loop, close the window

main()