// once upon a time a forest...
// no overlapping object packing

var circles = [];
var x; // x origin pos for my circles
var y; // y origin pos for my circles
var r = 0; // radius of my circles
var attempts = 5000; // preventing the risk of ending into an infinite loop

function setup() {
    //createCanvas(640, 360);
    createCanvas(windowWidth, windowHeight);
    colorMode(HSB, 100);  // Use HSB with scale of 0-100
    //frameRate(5);
}

function draw() {
    background(0);
    if (attempts > 0) {
        var myCircle = createCircle();
        attempts --;
        console.log(attempts);
        if (myCircle !== null) {
            circles.push(myCircle);
        }
    } else {
        console.log("I am done!");
        noLoop();
    }

    if (circles.length > 0) {
        for (var i = 0; i < circles.length; i++) {
            for (var j = 0; j < circles.length; j++) {
                if (circles[i] != circles[j]) {
                    circles[i].checkOverlap(circles[j]);
                }
            }
            circles[i].update();
            circles[i].display();
        }
    }
}

function createCircle() {
    x = random(width);
    y = random(height);
    var validC = true;
    circles.forEach(function(c) { //the equivalent of Java's enache for loop
        var d = dist(x, y, c.pos.x, c.pos.y);
        if (d < c.radius) {
            validC = false;
        } else if (d > c.radius) {
            validC = true;
        }
    });

    if (validC) {
        return new Circle(x, y, r);
    } else {
        return null;
    }
}
function Circle(x, y, r) {
    this.pos = createVector(x, y);
    //this.pos = new p5.Vector(x, y, r);
    this.radius = r;
    this.overlapping = false;
    this.growing = true;
    this.offIndex = random(0, 1000);

    this.update = function() {
        if (!this.edges() && this.overlapping === false) {
            this.radius += 0.5;
        } else{
            this.growing = false;
        }
    }

    this.display = function() {
        if (this.growing) {
          //noFill();
          //stroke(255);
          //ellipse(this.pos.x, this.pos.y, this.radius * 2, this.radius * 2);
        } else {
          // build my forest!
          var xoff = this.offIndex;
          var s = map(noise(xoff), 0, 1, 0, 100);
          var h = map(this.radius, 0, 100, 0, 100);
          var b = map(this.radius, 0, 50, 100, 10);
          var c = color(h, 50, b);
          fill(c);
          noStroke();
          push();
          translate(this.pos.x, this.pos.y);
          beginShape();
          for(var a = 0; a < TWO_PI; a += 0.03){
            var offset = map(noise(xoff), 0, 1, -this.radius/4, 0);
            var r = this.radius + offset;
            var x = r * cos(a);
            var y = r * sin(a);
            vertex(x, y);
            xoff += 0.1;
          }
          endShape(CLOSE);
          pop();
        }
    }

    this.edges = function() {
        return (this.pos.x + this.radius > width || this.pos.x - this.radius < 0 || this.pos.y + this.radius > height || this.pos.y - this.radius < 0)
    }

    this.checkOverlap = function(otherC) {
        var d = dist(this.pos.x, this.pos.y, otherC.pos.x, otherC.pos.y);
        if (d < this.radius + otherC.radius) {
            // circles are overlapping
            this.overlapping = true;
        }
    }
}
