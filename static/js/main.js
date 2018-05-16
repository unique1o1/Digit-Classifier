(function() {
  var canvas = document.getElementById("canvas");
  var context = canvas.getContext("2d");
  canvas.width = 280;
  canvas.height = 280;

  var Mouse = { x: 0, y: 0 };
  var lastMouse = { x: 0, y: 0 };
  context.fillStyle = "black";
  context.fillRect(0, 0, canvas.width, canvas.height);
  context.color = "white";
  context.lineWidth = 15;
  context.lineJoin = context.lineCap = "round";

  canvas.addEventListener(
    "mousemove",
    function(e) {
      lastMouse.x = Mouse.x;
      lastMouse.y = Mouse.y;
      console.log(e.pageX, e.pageY);
      Mouse.x = e.pageX - this.offsetLeft;
      Mouse.y = e.pageY - this.offsetTop;
    },
    false
  );

  canvas.addEventListener(
    "mousedown",
    function(e) {
      console.log("down");
      canvas.addEventListener("mousemove", onPaint, false);
    },
    false
  );

  canvas.addEventListener(
    "mouseup",
    function() {
      console.log("up");
      canvas.removeEventListener("mousemove", onPaint, false);
    },
    false
  );

  var onPaint = function() {
    context.lineWidth = context.lineWidth;
    context.lineJoin = "round";
    context.lineCap = "round";
    context.strokeStyle = context.color;
    console.log("paint");
    context.beginPath();
    context.moveTo(lastMouse.x, lastMouse.y);
    context.lineTo(Mouse.x, Mouse.y);
    context.closePath();
    context.stroke();
  };

  var clearButton = $("#clearButton");

  clearButton.on("click", function() {
    context.clearRect(0, 0, 280, 280);
    context.fillStyle = "black";
    context.fillRect(0, 0, canvas.width, canvas.height);
  });

  var slider = document.getElementById("myRange");
  var output = document.getElementById("sliderValue");
  output.innerHTML = slider.value;

  slider.oninput = function() {
    output.innerHTML = this.value;
    context.lineWidth = this.value;
  };
})();
