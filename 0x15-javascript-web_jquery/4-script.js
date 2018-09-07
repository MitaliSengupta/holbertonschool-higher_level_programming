$("#toggle_header").click(function () {
  $("HEADER").addClass(function (color) {
    if (color === 'red') {
      $("HEADER").removeClass('red').addClass('green');
    } else {
      $("HEADER").removeClass('green').addClass('red');
    }
  });
});
