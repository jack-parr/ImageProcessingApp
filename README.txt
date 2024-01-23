Project aim: make a useful image pre-processing app that allows you to experiment with pre-processing methods.
Goals: tree like structure, easy to move and modify each step. Ability to apply filter to mass of images and save the results.

Built using the MVC design pattern. 
Note: all functions that modify the view must be in the view class. More complicated functions can be put in the model, but ultimately call the view functions to actually modify the view.

To-Do:
- Create frame for the app.
- Add ability to import an image into the image display.
- Add ability to clear image from the image display.
- Add ability to add a new stage to the tree.
- Add ability to remove a stage from the tree.
- Add ability to change order of stages in the tree.

Plan:
menuBtn1: Image (dropdown of options: import, export, clear).
menuBtn2: Add new stage to tree (dropdown of stage types).
menuBtn3: Apply tree to image.
menuBtn4: Export tree as function (saves a file).

Have tree of stages on the left, make it scrollable.
Have image displayed in a square box in top right.
Have a parameter modiying screen below the box. Scrollable if needed.