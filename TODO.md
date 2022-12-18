
# FVelGame

## TODO

### New features

#### Game engine

- Deal with pygame.ACTIVEEVENT events as the display gains and loses input focus
- Use a system font that offers unicode support
  - Create a table os equivalent fonts in all systems
  - Select the fonts presente on all systems
- Implement the scoreboard display
  - Load a scoreboard background image
- Implement a initial screen
- Show game information on help
- Implement scrolling background
- Implement variable tracks
  - Take care of spawning objects outside screen
- Implement blits of track and background images using mask
- Implement function evaluation
- Implement achievements
  - 5 stars, the creator choses the score of each star
- Help message must be aware of vertical or horizontal scrolling
- Play crash sound before show game over
- Add elapsed time to scoreboard
- Add transparent option to MetaImage
- Allow creator to make margins kill the player
- Compute elapsed time using pygame function

#### Games

- Ship on ocean colecting precious stones and chests
  - Vertical scrolling
- racing
  - add sound to treasure catch
  - add oil spill
  - add background
  - add track image
- student
  - add sounds
  - add background
  - add track image

#### Graphycal Interface

- Implement open game file, to allow selection playing by the interface
- Implement a simple image editor 
  - Set size
  - Fill with color
  - Load image
  - Add transparency
  - Rotate
  - Crop
  - Zoom

- Implement everything

### Bugs

- game_world.py: Take scrolling direction in account
- game_world.py: Compute OST size properly
- engine.py:     Take care when the track is smaller than the object

### Improvements

### Windows

## In progress...

## DONE

2022-12-17
- Improve collision boundaries on transparent pngs
- Game: Student running from study
  - Horizontal scrolling
- Volume Control
  - [-] decrease volume - decided to not implement
  - [+] increase volume - decided to not implement
  - [M] toggle mute
- Implement Horizontal scrolling

## GAVE UP
