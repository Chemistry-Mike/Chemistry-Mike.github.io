/* Image comparisons work with a mouse, keyboard, and touch. */
document.querySelectorAll('.hover-swap-container').forEach(function (container) {
  var image = container.querySelector('.hover-image');
  if (!image) return;
  var button = document.createElement('button');
  button.type = 'button';
  button.className = 'comparison-toggle';
  button.textContent = 'Compare images';
  button.setAttribute('aria-pressed', 'false');
  button.setAttribute('aria-label', 'Compare images: ' + (image.alt || 'molecular visualization'));
  button.addEventListener('click', function () {
    var active = container.classList.toggle('is-compared');
    button.setAttribute('aria-pressed', String(active));
    button.textContent = active ? 'Show original' : 'Compare images';
  });
  container.appendChild(button);
});

/* Progressive enhancement: first image works without JavaScript. */
document.querySelectorAll('.hero-slideshow').forEach(function (carousel) {
  var slides = Array.from(carousel.querySelectorAll('.hero-slide'));
  var controls = carousel.querySelector('.hero-slide-controls');
  if (slides.length < 2 || !controls) return;
  var pauseButton = controls.querySelector('[data-slide="pause"]');
  var motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');
  var paused = motionPreference.matches;
  var current = 0;
  var timer = null;
  function show(direction) {
    for (var step = 1; step < slides.length; step++) {
      var next = (current + direction * step + slides.length) % slides.length;
      // Keep the current figure while another image loads, or if its file failed.
      if (!slides[next].complete || slides[next].naturalWidth === 0) continue;
      slides[current].classList.remove('is-active');
      slides[current].setAttribute('aria-hidden', 'true');
      slides[next].classList.add('is-active');
      slides[next].removeAttribute('aria-hidden');
      current = next;
      break;
    }
  }
  function schedule() {
    window.clearInterval(timer);
    timer = null;
    if (!paused && !document.hidden) timer = window.setInterval(function () { show(1); }, 6000);
    pauseButton.textContent = paused ? 'Play slideshow' : 'Pause slideshow';
  }
  controls.hidden = false;
  controls.querySelector('[data-slide="previous"]').addEventListener('click', function () { show(-1); schedule(); });
  controls.querySelector('[data-slide="next"]').addEventListener('click', function () { show(1); schedule(); });
  pauseButton.addEventListener('click', function () { paused = !paused; schedule(); });
  document.addEventListener('visibilitychange', schedule);
  function updateMotionPreference() { paused = motionPreference.matches; schedule(); }
  if (motionPreference.addEventListener) motionPreference.addEventListener('change', updateMotionPreference);
  else motionPreference.addListener(updateMotionPreference);
  schedule();
});
