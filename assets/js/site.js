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
