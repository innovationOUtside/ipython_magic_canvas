# ipython_magic_canvas
Simple IPython magic for working with HTML / Javascript Canvas.

To install:

`pip install git+https://github.com/innovationOUtside/ipython_magic_canvas.git`

To upgrade a current installation to the latest repo version without updating dependencies:

`pip install --upgrade --no-deps git+https://github.com/innovationOUtside/ipython_magic_canvas.git`

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/innovationOUtside/ipython_magic_canvas/master)

To load the magic in a Jupyter notebook:

`%load_ext canvas_magic`

Then call as block magic: `%%canvas`

The magic automatically creates a canvas element with a  random HTML tag `id`. Specify the `id` using the `--id` argument: `%%canvas --id mytag` or `%%canvas -I mytag`


## Examples

Prefix canvas code with a reference to the canvas 2D context:

```
%%canvas -c ctx
ctx.beginPath(); 

ctx.fillStyle = "#F9A520";
ctx.moveTo(0, 0);
ctx.lineTo(200, 0); 
ctx.lineTo(100, 200); 
ctx.fill(); 

// triangle 2, top center
ctx.moveTo(300, 0); // pick up "pen," reposition at 300 (horiz), 0 (vert)
ctx.lineTo(300, 200); // draw straight down (from 300,0) to 200px
ctx.lineTo(500, 100); // draw up toward right (100 half of 200)
ctx.fill(); // connect and fill
```

Automatically generate a canvas element and 2D context and write to that:

```
%%canvas
beginPath(); 

fillStyle = "#F9A520";
moveTo(0, 0);
lineTo(200, 0); 
lineTo(100, 200); 
fill(); 

beginPath(); 
fillStyle = "#F00";
moveTo(300, 200); 
lineTo(300, 400); // draw straight down by 200px (200 + 200)
lineTo(100, 300); // draw up toward left (100 less than 300, so left)
fill(); // connect and fill
```

We can also pass the script in via a (python) variable. For example, using the following script:

```
txt='''
    ctx.beginPath(); // note usage below 

    // triangle 1, at left
    ctx.fillStyle = "#F9A520";
    ctx.moveTo(0, 0); // start at top left corner of canvas
    ctx.lineTo(200, 0); // go 200px to right (x), straight line from 0 to 0
    ctx.lineTo(100, 200); // go to horizontal 100 (x) and vertical 200 (y)
    ctx.fill(); // connect and fill

    // triangle 2, top center
    ctx.moveTo(300, 0); // pick up "pen," reposition at 300 (horiz), 0 (vert)
    ctx.lineTo(300, 200); // draw straight down (from 300,0) to 200px
    ctx.lineTo(500, 100); // draw up toward right (100 half of 200)
    ctx.fill(); // connect and fill

    // triangle 3, bottom center
    ctx.beginPath(); // note: w/o this, color does not work as expected 
    ctx.fillStyle = "#F00";
    ctx.moveTo(300, 200); // pick up "pen," reposition at 300 (horiz), 200 (vert)
    ctx.lineTo(300, 400); // draw straight down by 200px (200 + 200)
    ctx.lineTo(100, 300); // draw up toward left (100 less than 300, so left)
    ctx.fill(); // connect and fill
'''
```

and then pass it into the magic:

```
%canvas -v txt --context ctx
```

The `--wrap` switch also requires a default context element (`ctx`) to be referenced in the script:
```
%canvas -v txt --wrap
```

We can also pass in scripts that *do not* require a context t be explicitly defined - the canvas element and an associated context will be generated automatically:

```
txt2='''
    beginPath(); // note usage below 

    // triangle 1, at left
    fillStyle = "#F9A520";
    moveTo(0, 0); // start at top left corner of canvas
    lineTo(200, 0); // go 200px to right (x), straight line from 0 to 0
    lineTo(100, 200); // go to horizontal 100 (x) and vertical 200 (y)
    fill(); // connect and fill
    
   // triangle 3, bottom center
    beginPath(); // note: w/o this, color does not work as expected 
    fillStyle = "#F00";
    moveTo(300, 200); // pick up "pen," reposition at 300 (horiz), 200 (vert)
    lineTo(300, 400); // draw straight down by 200px (200 + 200)
    lineTo(100, 300); // draw up toward left (100 less than 300, so left)
    fill(); // connect and fill

'''
```

Pass it into the script using the `-v` argument as before:

```
%canvas -v txt2
```
