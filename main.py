import os
import sys
import pygame

from pygame import time
from button import Button
from exercise import Exercise

# https://www.cnet.com/health/fitness/4-hiit-workouts-under-20-minutes-that-are-better-than-an-hour-at-the-gym/

"""
SETUP section - preparing everything before the main loop runs
"""
pygame.init()

# Global constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FRAME_RATE = 30

# Useful colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
LIGHT_GREY = (120, 120, 120)

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

background = pygame.image.load("assets/background.jpg").convert_alpha()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# background music
pygame.mixer.music.load(os.path.join("assets/background.wav"))
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

# sound effects
click_sound = pygame.mixer.Sound("assets/click.wav")
"""
workout images
"""
# lower body
air_squats_image_1 = pygame.image.load("assets/air-squats-1.jpg").convert_alpha()
air_squats_image_1 = pygame.transform.scale(air_squats_image_1, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))
air_squats_image_2 = pygame.image.load("assets/air-squats-2.jpg").convert_alpha()
air_squats_image_2 = pygame.transform.scale(air_squats_image_2, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))

jump_squats_image_1 = pygame.image.load("assets/jump-squats-1.jpg").convert_alpha()
jump_squats_image_1 = pygame.transform.scale(jump_squats_image_1, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))
jump_squats_image_2 = pygame.image.load("assets/jump-squats-2.jpg").convert_alpha() # fix this image
jump_squats_image_2 = pygame.transform.scale(jump_squats_image_2, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))

alternating_lunges_image_1 = pygame.image.load("assets/alternating-lunges-1.jpg").convert_alpha()
alternating_lunges_image_1 = pygame.transform.scale(alternating_lunges_image_1, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))
alternating_lunges_image_2 = pygame.image.load("assets/alternating-lunges-2.jpg").convert_alpha()
alternating_lunges_image_2 = pygame.transform.scale(alternating_lunges_image_2, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))

crossack_squats_image_1 = pygame.image.load("assets/crossack-squats-1.jpg").convert_alpha()
crossack_squats_image_1 = pygame.transform.scale(crossack_squats_image_1, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))
crossack_squats_image_2 = pygame.image.load("assets/crossack-squats-2.jpg").convert_alpha()
crossack_squats_image_2 = pygame.transform.scale(crossack_squats_image_2, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))

tuck_jumps_image_1 = pygame.image.load("assets/tuck-jumps-1.jpg").convert_alpha()
tuck_jumps_image_1 = pygame.transform.scale(tuck_jumps_image_1, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))
tuck_jumps_image_2 = pygame.image.load("assets/tuck-jumps-2.jpg").convert_alpha()
tuck_jumps_image_2 = pygame.transform.scale(tuck_jumps_image_2, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))

# upper body
push_ups_image_1 = pygame.image.load("assets/push-ups-1.jpg").convert_alpha()
push_ups_image_1 = pygame.transform.scale(push_ups_image_1, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))
push_ups_image_2 = pygame.image.load("assets/push-ups-2.jpg").convert_alpha()
push_ups_image_2 = pygame.transform.scale(push_ups_image_2, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))

plank_shoulder_image_1 = pygame.image.load("assets/plank-shoulder-1.jpg").convert_alpha()
plank_shoulder_image_1 = pygame.transform.scale(plank_shoulder_image_1, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))
plank_shoulder_image_2 = pygame.image.load("assets/plank-shoulder-2.jpg").convert_alpha()
plank_shoulder_image_2 = pygame.transform.scale(plank_shoulder_image_2, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))

burpees_image_1 = pygame.image.load("assets/burpees-1.jpg").convert_alpha()
burpees_image_1 = pygame.transform.scale(burpees_image_1, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))
burpees_image_2 = pygame.image.load("assets/burpees-2.jpg").convert_alpha()
burpees_image_2 = pygame.transform.scale(burpees_image_2, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))

sit_ups_image_1 = pygame.image.load("assets/sit-ups-1.jpg").convert_alpha()
sit_ups_image_1 = pygame.transform.scale(sit_ups_image_1, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))
sit_ups_image_2 = pygame.image.load("assets/sit-ups-2.jpg").convert_alpha()
sit_ups_image_2 = pygame.transform.scale(sit_ups_image_2, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))

plank_image_1 = pygame.image.load("assets/plank-1.jpg").convert_alpha()
plank_image_1 = pygame.transform.scale(plank_image_1, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))
plank_image_2 = pygame.image.load("assets/plank-2.jpg").convert_alpha()
plank_image_2 = pygame.transform.scale(plank_image_2, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))

# full body cardio pictures
high_knees_image_1 = pygame.image.load("assets/high-knees-1.jpg").convert_alpha()
high_knees_image_1 = pygame.transform.scale(high_knees_image_1, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))
high_knees_image_2 = pygame.image.load("assets/high-knees-2.jpg").convert_alpha()
high_knees_image_2 = pygame.transform.scale(high_knees_image_2, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))

russian_twist_image_1 = pygame.image.load("assets/russian-twist-1.jpg").convert_alpha()
russian_twist_image_1 = pygame.transform.scale(russian_twist_image_1, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))
russian_twist_image_2 = pygame.image.load("assets/russian-twist-2.jpg").convert_alpha()
russian_twist_image_2 = pygame.transform.scale(russian_twist_image_2, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))

mountain_image_1 = pygame.image.load("assets/mountain-1.jpg").convert_alpha()
mountain_image_1 = pygame.transform.scale(mountain_image_1, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))
mountain_image_2 = pygame.image.load("assets/mountain-2.jpg").convert_alpha()
mountain_image_2 = pygame.transform.scale(mountain_image_2, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))

jump_lunges_image_1 = pygame.image.load("assets/jump-lunges-1.jpg").convert_alpha()
jump_lunges_image_1 = pygame.transform.scale(jump_lunges_image_1, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))
jump_lunges_image_2 = pygame.image.load("assets/jump-lunges-2.jpg").convert_alpha()
jump_lunges_image_2 = pygame.transform.scale(jump_lunges_image_2, (int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)))

# workout sections
lowerBodySession = (
    Exercise("Air Squats", 50, air_squats_image_1, air_squats_image_2), 
    Exercise("Jump Squats", 20, jump_squats_image_1, jump_squats_image_2), 
    Exercise("Alternating Lunges", 50, alternating_lunges_image_1, alternating_lunges_image_2),
    Exercise("Crossack Squats", 50, crossack_squats_image_1, crossack_squats_image_2),
    Exercise("Tuck Jumps", 20, tuck_jumps_image_1, tuck_jumps_image_2)
)

upperBodySession = (
    Exercise("Push Ups", 10, push_ups_image_1, push_ups_image_2), 
    Exercise("Plank Shoulder Taps", 10, plank_shoulder_image_1, plank_shoulder_image_2), 
    Exercise("Burpees", 15, burpees_image_1, burpees_image_2),
    Exercise("Sit Ups", 30, sit_ups_image_1, sit_ups_image_2),
    Exercise("Plank (30 seconds)", 5, plank_image_1, plank_image_2)
)

fullBodySession = (
    Exercise("High Knees", 50, high_knees_image_1, high_knees_image_2), 
    Exercise("Russian Twists", 50, russian_twist_image_1, russian_twist_image_2), 
    Exercise("Tuck Jumps", 50, tuck_jumps_image_1, tuck_jumps_image_2),
    Exercise("Mountain Climbers", 50, mountain_image_1, mountain_image_2),
    Exercise("Jump Lunges", 20, jump_lunges_image_1, jump_lunges_image_2)
)

def intro_menu():
    intro_loop = True
    intro_font = pygame.font.SysFont('microsoftuighur', int(SCREEN_HEIGHT/10))

    # heading text - 1/8
    heading = pygame.font.SysFont('microsoftuighur', int(SCREEN_HEIGHT/6.5)).render("Choose your workout session", True, WHITE)

    # buttons
    lowerBody = Button(WHITE, (SCREEN_WIDTH/3, SCREEN_HEIGHT*(3/8)), intro_font, "Lower body", SCREEN_WIDTH*(1/4))
    lowerBody.active = True
    sessionName = "Lower Body"

    upperBody = Button(WHITE, (SCREEN_WIDTH*(2/3), SCREEN_HEIGHT*(3/8)), intro_font, "Upper Body", SCREEN_WIDTH*(1/4))
    fullCardio = Button(WHITE, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), intro_font, "Full body cardio", SCREEN_WIDTH*(1/3))

    # start button - 4/5
    startButton = Button(WHITE, (SCREEN_WIDTH*(1/2), SCREEN_HEIGHT*(4/5)), pygame.font.SysFont('microsoftuighur', int(SCREEN_HEIGHT/5)), "Start", SCREEN_WIDTH*(2/5))

    # buttons list
    buttons = (lowerBody, upperBody, fullCardio, startButton)

    while intro_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
                intro_loop = False
                pygame.quit()
                sys.exit()
        
        # Mouse events
        mouse_pos = pygame.mouse.get_pos()  # Get position of mouse as a tuple representing the
        # (x, y) coordinate
        mouse_buttons = pygame.mouse.get_pressed() # if clicked

        # hover over buttons
        for button in buttons:
            if button.active:
                button.color = LIGHT_GREY
            else:
                button.color = WHITE
            # if mouse clicked on button
            if button.hover(mouse_pos):
                button.color = GREY
                if mouse_buttons[0]:
                    # click sound
                    click_sound.play()
                    if button == startButton:
                        main(sessionName)

                    if not button.active:
                        button.active = True
                        
                        if button == lowerBody:
                            sessionName = "Lower Body"
                            upperBody.active = False
                            fullCardio.active = False
                        elif button == upperBody:
                            sessionName = "Upper Body"
                            lowerBody.active = False
                            fullCardio.active = False
                        elif button == fullCardio:
                            sessionName = "Full Cardio"
                            lowerBody.active = False
                            upperBody.active = False
                        
                        time.wait(300)

        screen.fill(BLACK)  # Fill the screen with one colour
        screen.blit(background, (0,0))
        
        # heading
        screen.blit(heading, (SCREEN_WIDTH/2 - (heading.get_width()/2), SCREEN_HEIGHT/8))

        # session buttons
        lowerBody.draw(screen, BLACK, 2)
        upperBody.draw(screen, BLACK, 2)
        fullCardio.draw(screen, BLACK, 2)

        #play/prctice button
        startButton.draw(screen, BLACK, 2)

        pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
        clock.tick(int(FRAME_RATE/4))  # Pause the clock to always maintain FRAME_RATE frames per second


def main(sessionName):

    session_text = pygame.font.SysFont('microsoftuighur', int(SCREEN_HEIGHT/7)).render("Current Session: " + sessionName, True, WHITE)

    if sessionName == "Lower Body":
        current_session = lowerBodySession
    elif sessionName == "Upper Body":
        current_session = upperBodySession
    elif sessionName == "Full Cardio":
        current_session = fullBodySession

    current_exercise_index = 0
    current_exercise = current_session[current_exercise_index]

    # menu button
    menuButton = Button(WHITE, (SCREEN_WIDTH/2, SCREEN_HEIGHT/27), pygame.font.SysFont('microsoftuighur', int(SCREEN_HEIGHT/10)), "MENU")

    # next button
    nextButton = Button(WHITE, (SCREEN_WIDTH*(3/4), SCREEN_HEIGHT*(9/10)), pygame.font.SysFont('microsoftuighur', int(SCREEN_HEIGHT/10)), "Next")

    # current exercise
    current_exercise_text = pygame.font.SysFont('microsoftuighur', int(SCREEN_HEIGHT/10)).render("Doing: " + current_exercise.name, True, WHITE)
    exercise_counter_text = pygame.font.SysFont('microsoftuighur', int(SCREEN_HEIGHT/10)).render("Do: " + str(current_exercise.amount), True, WHITE)

    # next exercise
    next_exercise_text = pygame.font.SysFont('microsoftuighur', int(SCREEN_HEIGHT/10)).render("Next: " + current_session[current_exercise_index+1].name, True, WHITE)
    next_exercise_done_text = pygame.font.SysFont('microsoftuighur', int(SCREEN_HEIGHT/10)).render("done!", True, WHITE)

    main_loop = True

    while main_loop:
        """
        EVENTS section - how the code reacts when users do things
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
                main_loop = False
                pygame.quit()
                sys.exit()

        # Mouse events
        mouse_pos = pygame.mouse.get_pos()  # Get position of mouse as a tuple representing the
        # (x, y) coordinate

        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:  # If left mouse pressed
            pass  # Replace this line
        if mouse_buttons[2]:  # If right mouse pressed
            pass  # Replace this line

        menuButton.color = WHITE
        if menuButton.hover(mouse_pos):
            menuButton.color = GREY
            if mouse_buttons[0]:
                click_sound.play()
                time.wait(200)
                main_loop = False
                intro_menu()
        
        nextButton.color = WHITE
        if nextButton.hover(mouse_pos):
            nextButton.color = GREY
            if mouse_buttons[0]:
                click_sound.play()
                time.wait(500)
                # next item
                if current_exercise_index < 4:
                    current_exercise_index += 1
                    current_exercise = current_session[current_exercise_index]
                    current_exercise_text = pygame.font.SysFont('microsoftuighur', int(SCREEN_HEIGHT/10)).render("Doing: " + current_exercise.name, True, WHITE)
                    exercise_counter_text = pygame.font.SysFont('microsoftuighur', int(SCREEN_HEIGHT/10)).render("Do: " + str(current_exercise.amount), True, WHITE)
                else:
                    gameOver(sessionName)
                if current_exercise_index < 4:
                    next_exercise_text = pygame.font.SysFont('microsoftuighur', int(SCREEN_HEIGHT/10)).render("Next: " + current_session[current_exercise_index+1].name, True, WHITE)
                else:
                    next_exercise_text = pygame.font.SysFont('microsoftuighur', int(SCREEN_HEIGHT/10)).render("almost done!", True, WHITE)

        """
        UPDATE section - manipulate everything on the screen
        """

        """
        DRAW section - make everything show up on screen
        """
        screen.fill(BLACK)  # Fill the screen with one colour
        screen.blit(background, (0,0))

        # doing: ...
        screen.blit(current_exercise_text, (SCREEN_WIDTH/30, SCREEN_HEIGHT*(2.5/10)))

        # next exercise text
        if current_exercise_index < 5:
            screen.blit(next_exercise_text, (SCREEN_WIDTH/30, SCREEN_HEIGHT*(9/10)))
        else:
            screen.blit(next_exercise_done_text, (SCREEN_WIDTH/30, SCREEN_HEIGHT*(9/10)))

        # menu button
        menuButton.draw(screen, BLACK, 2)

        # next button
        nextButton.draw(screen, BLACK, 2)

        # session text
        screen.blit(session_text, ((SCREEN_WIDTH/2) - (session_text.get_width()/2), SCREEN_HEIGHT*(1/10)))

        # counter text
        screen.blit(exercise_counter_text, (SCREEN_WIDTH*(2/3), SCREEN_HEIGHT*(2.5/10)))

        # images
        screen.blit(current_exercise.picture1, (SCREEN_WIDTH/10, SCREEN_HEIGHT*(2/5)))
        screen.blit(current_exercise.picture2, (SCREEN_WIDTH*(6/10), SCREEN_HEIGHT*(2/5)))

        pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
        clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second


def gameOver(sessionName):
    over_loop = True
    over_font = pygame.font.SysFont('microsoftuighur', int(SCREEN_HEIGHT/10))

    # heading text
    line_1 = pygame.font.SysFont('microsoftuighur', int(SCREEN_HEIGHT/5)).render("Session over!", True, WHITE)

    # you finished: ...
    line_2 = over_font.render("You completed: " + sessionName + " workout", True, WHITE)

    # menu button
    menuButton = Button(WHITE, (SCREEN_WIDTH/2, SCREEN_HEIGHT*(7/8)), pygame.font.SysFont('microsoftuighur', int(SCREEN_HEIGHT/5)), "Menu")

    while over_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
                over_loop = False
                pygame.quit()
                sys.exit()

        # Mouse events
        mouse_pos = pygame.mouse.get_pos()  # Get position of mouse as a tuple representing the
        # (x, y) coordinate
        mouse_buttons = pygame.mouse.get_pressed()

        menuButton.color = WHITE
        if menuButton.hover(mouse_pos):
            menuButton.color = GREY
            if mouse_buttons[0]:
                click_sound.play()
                time.wait(200)
                over_loop = False
                intro_menu()
        
        screen.fill(BLACK)  # Fill the screen with one colour
        screen.blit(background, (0,0))

        # buttons
        menuButton.draw(screen, BLACK, 2)

        screen.blit(line_1, (SCREEN_WIDTH/2 - (line_1.get_width()/2), SCREEN_HEIGHT/8))
        screen.blit(line_2, (SCREEN_WIDTH/2 - (line_2.get_width()/2), SCREEN_HEIGHT/2))

        pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
        clock.tick(int(FRAME_RATE/4))  # Pause the clock to always maintain FRAME_RATE frames per second

intro_menu()