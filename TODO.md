
# FVelGame

## TODO

### New features
- Implement achievements
  - 5 stars, the creator choses the score of each star
- Implement a initial screen

#### Game engine

- OST
  - Create a table os equivalent fonts in all systems
  - Select the fonts presente on all systems
- Implement variable tracks
  - Take care of spawning objects outside screen
- Implement blits of track and background images using mask
- Implement function evaluation
- Play crash sound before show game over
- Add transparent option to MetaImage
- Allow creator to make margins kill the player
- Implement horizontal scrolling background
- Take care of background images smaller than screen

#### Games

- Ship on ocean colecting precious stones and chests
  - Vertical scrolling

- student
  - add sounds
  - add background
  - add track image

#### Graphycal Interface

- Implement everything
- Allow creator to define sound volume for each sprite, 1 is the music volume

- Implement a simple image editor 
  - Set size
  - Fill with color
  - Load image
  - Add transparency
  - Rotate
  - Crop
  - Zoom

### Bugs

### Improvements

### Windows

## In progress...

## DONE

2022-12-22
- Events
  - Deal with pygame.ACTIVEEVENT events as the display gains and loses input focus
  - Control the event queue pygame.event.set_allowed()
- Compute elapsed time using pygame function
- racing
  - add sound to treasure catch
  - add oil spill
  - add background
  - add track image

2022-12-21
- Load a scoreboard background image

2022-12-20
- GUI - Implement open game file, to allow selection playing by the interface
- Show game information on help
- Implement scrolling background
- game_world.py: Take scrolling direction in account
- game_world.py: Compute OST size properly
- engine.py:     Take care when the track is smaller than the object
- Sound
  - Reimplement mute do stop music
  - Implement volume control
- Help message must be aware of vertical or horizontal scrolling
- Implement the scoreboard display
- Use a system font that offers unicode support

2022-12-17
- Improve collision boundaries on transparent pngs
- Game: Student running from study
  - Horizontal scrolling
- Volume Control
  - [-] decrease volume - decided to not implement
  - [+] increase volume - decided to not implement
  - [M] toggle mute
- Implement Horizontal scrolling
- Add elapsed time to scoreboard

## GAVE UP
