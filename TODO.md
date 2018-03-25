To-Do
=====

- Bugs
    - AZERTY doesn't make any sense
- macOS port
    - Replace Dear Imgui's menu with Cocoa menu.
    - Keyboard bindings
- Application
    - GUI
        - nuklear port
        - Color picker inside ImGui window.
        - Image Button
        - Reduce or remove widget rounding
        - Radial menu
    - Features:
        - full-screen option
        - front-to-back rendering
        - alt eye dropper
        - zoom-out toggle for overview and for navigation
        - general, implicitly defined brushes
        - transparent window / background.
        - Select strokes
            - Scale, cut, copy, paste
        - rectangles
        - circles / ellipses
        - merge layers
        - layer color balance
        - select layer by stroke
        - pressure response graph
        - stroke masking?
        - unzoomable&unpannable layer ("pin layer" feature) ?
        - eraser toggle
        - pressure toggle
    - Settings file
        - Default BG
           or
        - Template files - change the default canvas.
        - Key shortcuts
- Polish and/or Debug layer
    - Input recorder for reproducing bugs
    - linux - load dynamic libs at runtime
    - store font data in binary
    - switch to cmake for all platforms
- Milton Library
    - Refactor. Write sample program.